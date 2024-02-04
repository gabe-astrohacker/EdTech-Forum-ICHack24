from functools import reduce

import pyrebase
from flask import *

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


# Example Usage
# for_all_table(["users", "adamwatson1234", "posts", postID], print)
def for_all_table(path, func):
    elems = list_to_children(path).get()
    for elem in elems.each():
        func(elem)


def to_composite_key(keys):
    return reduce(lambda x, y: str(x) + "_" + str(y), keys)

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
