import streamlit as st
from pymongo import MongoClient
import bcrypt

from pymongo.mongo_client import MongoClient

from pymongo.server_api import ServerApi
import bcrypt
from dotenv import load_dotenv
import os


def configure():
    load_dotenv ()
configure()

uri = os.getenv ('URI_DB')


# db_login = os.environ.get ('USER_NAME')
# db_login_ps = os.environ.get ('PASS_WORD')

# ibH6UtJrHuK1ylfc


# "mongodb+srv://subramaniann435SS:RgJa07YguYoePSob@cluster0.md9bnwg.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient (uri)
# print(client.list_database_names())
db = client.income_expense_register
# print(client.list_collection)
records = db['records']
users_collection = db["users"]
records_collection = db["records"]


def creds_entered():
    user = users_collection.find_one ({"username": st.session_state['username']})
    if user and bcrypt.checkpw (st.session_state['password'].encode ('utf-8'), user['password']):
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False


def display_login_form():
    if "authenticated" not in st.session_state:
        # Login form
        st.text_input ("Username:", value="", key="username", on_change=creds_entered)
        st.text_input ("Password:", key="password", type="password", on_change=creds_entered)
        if st.button ("Login", on_click=creds_entered):
            creds_entered ()

        # Signup form
        st.markdown ("---")
        st.subheader ("Sign Up")
        if st.button ("Show Sign Up Form"):
            st.text_input ("New Username:", key="new_username")
            st.text_input ("New Password:", key="new_password", type="password")
            if st.button ("Sign Up"):
                signup ()

    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input ("Username:", value="", key="username")
            st.text_input ("Password:", key="password", type="password")
        if st.button ("Login", on_click=creds_entered):
            return False


def signup():
    st.text_input ("Username:", key="new_username")
    st.text_input ("Password:", key="new_password", type="password")
    if st.button ("Sign Up"):
        username = st.session_state["new_username"]
        password = st.session_state["new_password"]
        hashed_password = bcrypt.hashpw (password.encode ("utf-8"), bcrypt.gensalt ())
        user = {"username": username, "password": hashed_password}
        users_collection.insert_one (user)
        st.info ("Sign up successful! Please login with your new account.")
