from ast import main

import streamlit as st
from pymongo import MongoClient

from session_state import SessionState
import Login
import add_transaction
import view_transactions

import streamlit as st


def main():
    Login.configure ()
    session_state = st.session_state

    if not Login.display_login_form ():
        pass
    else:
        st.title ("Cashflow Master")
        st.write ("Welcome user", session_state["username"] + "!!")

        if "username" not in session_state:
            session_state.username = st.session_state["username"]

        menu = ["Add Transaction", "View Transactions"]
        choice = st.sidebar.selectbox ("Menu", menu)
        if choice == "Add Transaction":
            session_state.username = st.session_state["username"]
            add_transaction.add_transaction_form (session_state.username)

        elif choice == "View Transactions":
            # if "username" not in session_state:
            #     session_state.username = st.session_state["username"]
            view_transactions.view_transactions (session_state.username)
            session_state.username = st.session_state["username"]


if __name__ == '__main__':
    main ()

# demo
# TbhJ0l1wDdZwfgBk
