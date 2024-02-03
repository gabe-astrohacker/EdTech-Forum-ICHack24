# Import the functions you need from the SDKs you need
# import initializeApp from "firebase/app"
# import getAnalytics from "firebase/analytics"
# TODO: Add SDKs for Firebase products that you want to use
# https://firebase.google.com/docs/web/setup#available-libraries

import pyrebase
from flask import *

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
def list_to_children(children):
    x = db
    for child in children:
        x = db.child(child)
    return x

# Example Usage
# data = {"name": "Adam Watson", "age": "20"}
# set_data(["users", "adamwatson1234"], data2)
def set_data(children, data):
    list_to_children(children).set(data)

# Example Usage
# delete_data(["users", "adamwatson1234", "posts", postID])
def delete_data(children):
    list_to_children(children).remove()

# Example Usage
# upvotes = get_val(["users", "adamwatson1234", "posts", "upvotes"])
def get_val(children):
    return list_to_children(children).get().val()

# AUTHENTICATION

# Example Usage
# create_user("1.aniketgupta@gmail.com", "password1234")
def create_user(email, password):
    auth.create_user_with_email_and_password(email, password)



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