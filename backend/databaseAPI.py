from functools import reduce

import pyrebase
import uuid
from flask import *
import time

# https://firebase.google.com/docs/web/setup#available-libraries
# Initialize Firebase
app = Flask(__name__)
config = {
    "apiKey": "AIzaSyDlc7YC8u0lpV_bh0XsSHmkVQXGo5wRnos",
    "authDomain": "edtech-forum-ichack24.firebaseapp.com",
    "databaseURL": "https://edtech-forum-ichack24-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "edtech-forum-ichack24",
    "storageBucket": "edtech-forum-ichack24.appspot.com",
    "messagingSenderId": "302199976942"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the database service
db = firebase.database()

# Get a reference to the authentication service
auth = firebase.auth()


# Login 1:1 User

# DATABASE FUNCTIONS

# Helper function for converting set of children to editable database child
def list_to_children(path):
    x = db
    for child in path:
        x = db.child(child)
    return x


# Example Usage
# data = {"name": "Adam Watson", "age": "20"}
# push_data(["users", "adamwatson1234"], data2)
def push_data(path, data):
    list_to_children(path).push(data)


# Example Usage
# data = {"name": "Adam Watson", "age": "20"}
# set_data(["users", "adamwatson1234"], data2)
def set_data(path, data):
    list_to_children(path).set(data)


# Example Usage
# There is already a user called adamwatson1234 with a name and age defined
# data = {"name": "Adam Watson", "age": "20"}
# update_data(["users", "adamwatson1234"], data2)
def update_data(path, data):
    list_to_children(path).update(data)


# Example Usage
# delete_data(["users", "adamwatson1234", "posts", postID])
def delete_data(path):
    list_to_children(path).remove()


# Example Usage
# upvotes = get_val(["users", "adamwatson1234", "posts", postID, "upvotes"])
def get_val(path):
    return list_to_children(path).get().val()


# AUTHENTICATION

cur_user = 0


# Example Usage
# create_user("user@example.com", "password1234", "Jane", "Doe)
def create_user(email, password, first_name, surname):
    auth.create_user_with_email_and_password(email, password)
    token = get_user_token(email, password)
    user = auth.sign_in_with_custom_token(token)
    global cur_user
    cur_user = auth.get_account_info(user['idToken'])
    set_data(["users", cur_user],
             {"uid": str(cur_user), "firstname": str(first_name), "surname": str(surname), "reputation": "0"})


def get_user_token(email, password):
    global cur_user
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


# Example Usage
# verify_email(emailFromTextfield, passwordFromTextfield)
def verify_email(email, password):
    token = get_user_token(email, password)
    user = auth.sign_in_with_custom_token(token)
    auth.send_email_verification(user['idToken'])


# Example Usage
# for_all_table(["users", "adamwatson1234", "posts", postID], print)
def for_all_table(path, func):
    elems = list_to_children(path).get()
    for elem in elems.each():
        func(elem)


def scale_rep(rep):
    return rep


def inc_rep(rid):
    global cur_user
    if cur_user != 0:
        upscore = get_val(["resources", str(rid), "upscore"])
        cur_user_rep = get_val(["users", str(cur_user), "reputation"])
        upscore += scale_rep(cur_user_rep)
        update_data(["resources", str(rid)], {"upscore": str(upscore)})


def dec_rep(rid):
    global cur_user
    if cur_user != 0:
        downscore = get_val(["resources", str(rid), "downscore"])
        cur_user_rep = get_val(["users", str(cur_user), "reputation"])
        downscore += scale_rep(cur_user_rep)
        set_data(["resources", str(rid)], {"downscore": str(downscore)})


def add_resource(link):
    rid = hash(link)
    try_val = get_val(["resources", str(rid)])

    # Check if resource is already added
    if try_val is None:
        set_data(["resources", str(rid)], {"link": str(link), "upscore": "0", "downscore": "0"})
        return True
    else:
        # TODO: If already added then increase reputation but do not add to database again
        return False


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


def to_composite_key(keys):
    return reduce(lambda x, y: x + "_" + y, keys)

# # Your web app's Firebase configuration
# # For Firebase JS SDK v7.20.0 and later, measurementId is optional
# const firebaseConfig = {
#   apiKey: "AIzaSyDlc7YC8u0lpV_bh0XsSHmkVQXGo5wRnos",
#   authDomain: "edtech-forum-ichack24.firebaseapp.com",
#   projectId: "edtech-forum-ichack24",
#   storageBucket: "edtech-forum-ichack24.appspot.com",
#   messagingSenderId: "302199976942",
#   appId: "1:302199976942:web:4c8355896074da8e2594ff",
#   measurementId: "G-SRE344N90Z"
# };
#
