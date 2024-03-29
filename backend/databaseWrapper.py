from databaseAPI import *
from datetime import datetime
import uuid
import time
from math import log


# Authentication

# Example Usage
# create_user("user@example.com", "password1234", "Jane", "Doe)
def create_user(email, password):
    auth.create_user_with_email_and_password(email, password)
    cur_user = sign_in_user(email, password)
    set_data(["users", cur_user],
             {"uid": str(cur_user), "reputation": "0"})


def get_user_token(email, password):
    cur_user = sign_in_user(email, password)
    if cur_user != 0:
        user = auth.sign_in_with_email_and_password(email, password)
        # before the 1-hour expiry:
        user = auth.refresh(user['refreshToken'])
        # now we have a fresh token
        token = user['idToken']
        return token
    else:
        print("Error: User not logged in")


# Example Usage
# sign_in_user("user@example.com", "password1234")
def sign_in_user(email, password):
    auth.sign_in_with_email_and_password(email, password)
    token = get_user_token(email, password)
    user = auth.sign_in_with_custom_token(token)
    cur_user = auth.get_account_info(user['idToken'])
    return cur_user


def sign_out_user():
    auth.current_user = None


# Example Usage
# verify_email(emailFromTextfield, passwordFromTextfield)
def verify_email(email, password):
    token = get_user_token(email, password)
    user = auth.sign_in_with_custom_token(token)
    auth.send_email_verification(user['idToken'])


# Database retrieval

# RETURNS: Dict
def get_user_info(token):
    return get_val(["users", token])


# RETURNS: teacherid
def get_class_teacher(token):
    return get_val(["classrooms", token])


# RETURNS: [ classid ]
def get_students_classes(token):
    return [value for key, value in get_val(["students"]).items() if key.startswith(token + "_")]


# RETURNS: [ studentid ]
def get_students_in_class(token):
    return [value for key, value in get_val(["students"]).items() if key.endswith("_" + token)]


# return:
#         {
#           link: { count: int, description: String, up_score: int , down_score: int },
#           link2...
#         }
def filter_by_keywords(keywords):
    table = get_val(["resources"])

    link_to_info = {}

    for rid in table:
        count = 0
        resource_keywords = table[rid]["keywords"].values()

        for keyword in keywords:
            if keyword in resource_keywords:
                count += 1

        if count > 0:
            up_score, down_score = get_resource_scores(rid)

            link_to_info.update({
                get_resource_link(rid):
                    {"count": count,
                     "description": get_resource_description(rid),
                     "up_score": up_score,
                     "down_score": down_score
                     }
            })

    return link_to_info


# RETURNS: Hyperlink
def get_resource_link(token):
    entry = get_val(["resources", token])
    if entry is None:
        return None
    return entry["link"]


# RETURNS: Hyperlink
def get_resource_description(token):
    entry = get_val(["resources", token])
    if entry is None:
        return None
    return entry["description"]


# RETURNS: (up_score, down_score)
def get_resource_scores(token):
    entry = get_val(["resources", token])
    if entry is None:
        return None
    return int(entry["up_score"]), int(entry["down_score"])


# RETURNS: [ rid ]
def get_student_searches(token):
    return [value for key, value in get_val(["searches"]).items() if key.startswith(token + "_")]


# Database updating

def add_resource(link, description, keywords):
    rid = hash(link)
    try_val = get_val(["resources", str(rid)])

    # Check if resource is already added
    if try_val is None:
        set_data(["resources", str(rid)],
                 {"link": str(link),
                  "description": str(description),
                  "up_score": "0",
                  "down_score": "0"})
        add_keywords(keywords)
        # TODO: If already added then increase reputation but do not add to database again


def add_discussion(link, question):
    rid = hash(link)
    discussion_id = uuid.uuid4()
    owner_id = auth.current_user['localId']
    timestamp = datetime.timestamp(datetime.now())
    update_data(["discussions", str(discussion_id)],
                {"owner_id": str(owner_id), "question": str(question), "timestamp": str(timestamp), "rid": str(rid)})


def add_reply(discussion_id, reply):
    reply_id = uuid.uuid4()
    timestamp = datetime.timestamp(datetime.now())
    owner_id = auth.current_user['localId']
    update_data(["replies", str(reply_id)],
                {"owner_id": str(owner_id), "reply": reply, "discussion_id": str(discussion_id),
                 "timestamp": str(timestamp)})


def add_classroom(teacherid):
    classid = uuid.uuid4()
    set_data(["classrooms", str(classid)], {"teacherid": str(teacherid)})


def add_student(studentid, classid):
    student_class_id = to_composite_key([studentid, classid])
    set_data(["students", str(student_class_id)], {"studentid": studentid, "classid": classid})


def add_search_result(studentid, rid):
    epoch_time = round(time.time() * 1000)
    student_time_id = to_composite_key([studentid, epoch_time])
    set_data(["searches", str(student_time_id)], {"rid": str(rid)})


def add_keywords(link, keywords):
    rid = hash(link)

    keyword_num = 0
    for key in keywords:
        keyword_num += 1
        update_data(["resources", rid, "keywords"], {str(keyword_num): key})


auth.sign_in_with_email_and_password("1.aniketgupta@gmail.com", "password1234")


# Reputation misc

def scale_rep(rep, func):
    if func == 'i':
        return round(rep + rep * log(rep))
    elif func == 'd':
        return round(rep - rep * log(rep))
    else:
        return None


def inc_rep(link, func):
    rid = hash(link)
    cur_user = auth.current_user['localId']
    if cur_user is not None:
        up_score = get_val(["resources", str(rid), "up_score"])
        cur_user_rep = get_val(["users", str(cur_user), "reputation"])
        up_score += 1 if func == 'i' else - 1
        cur_user_rep = scale_rep(cur_user_rep, func)
        update_data(["resources", str(rid)], {"up_score": str(up_score)})
        update_data(["users", str(cur_user)], {"reputation": str(cur_user_rep)})


def dec_rep(link, func):
    rid = hash(link)
    cur_user = auth.current_user['localId']
    if cur_user is not None:
        down_score = get_val(["resources", str(rid), "down_score"])
        cur_user_rep = get_val(["users", str(cur_user), "reputation"])
        down_score += 1 if func == 'i' else -1
        cur_user_rep = scale_rep(cur_user_rep, func)
        update_data(["resources", str(rid)], {"down_score": str(down_score)})
        update_data(["users", str(cur_user)], {"reputation": str(cur_user_rep)})
