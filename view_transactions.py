import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Import Matplotlib for creating the pie chart
import Login
from Login import records
from session_state import SessionState


def view_transactions(username):
    st.subheader ("View Records")
    st.write ("Welcome user", st.session_state['username'])
    categories = [category['_id'] for category in records.aggregate ([{"$group": {"_id": "$category"}}])]
    selected_category = st.selectbox ("Filter by Category", ["All"] + categories)

    if selected_category == "All":
        filtered_records = records.find ()
    else:
        filtered_records = records.find ({"category": selected_category})

    # Create a DataFrame to display the records
    records_df = pd.DataFrame (filtered_records)

    if not records_df.empty:
        if 'user' not in records_df:
            records_df['user'] = username  # Add a 'user' column with the logged-in username

        # Hide the ID column and display the modified DataFrame
        st.write ("List of Records:")
        st.write (records_df.drop ('_id', axis=1))

        # Add update option
        if st.button ("Update Selected Record"):
            # Logic for updating the selected record
            pass

        if st.button ("Delete Selected Record"):
            # Logic for deleting the selected record
            pass

        # Data Analysis
        st.subheader ("Data Analysis")
        st.write ("Summary Statistics:")
        st.write (records_df.describe ())

        st.write ("Total Amount by Category:")
        total_amount_by_category = records_df.groupby ('category')['amount'].sum ().reset_index ()
        st.write (total_amount_by_category)

        # Visualization - Pie chart for total amount by category
        st.write ("Total Amount by Category (Pie Chart):")
        chart_data = total_amount_by_category.set_index ('category')

        fig, ax = plt.subplots ()
        chart_data['amount'].plot (kind='pie', autopct='%1.1f%%', ax=ax)
        st.pyplot (fig)

        st.write ("Total Transactions by Category:")
        total_transactions_by_category = records_df['category'].value_counts ().reset_index ()
        total_transactions_by_category.columns = ['category', 'count']
        st.write (total_transactions_by_category)

    else:
        st.write ("No records found.")
# import streamlit as st
#
# import Login
# from Login import records
# from session_state import SessionState
#
#
# def view_transactions(username):
#
#    # st.write ("Welcome user", st.session_state["username"] + "!!")
#
#     st.subheader("View Records")
#     st.write ("Welcome user", st.session_state['username'])
#     categories = [category['_id'] for category in records.aggregate([{"$group": {"_id": "$category"}}])]
#     selected_category = st.selectbox("Filter by Category", ["All"] + categories)
#
#     if selected_category == "All":
#         filtered_records = records.find()
#     else:
#         filtered_records = records.find({"category": selected_category})
#
#     # Create a simple table to display the records
#     records_list = []
#     for record in filtered_records:
#         records_list.append(record)
#
#     if len(records_list) > 0:
#         st.write("List of Records:")
#         for i, record in enumerate(records_list):
#             st.write(
#                 f"{i + 1}. Name: {record['name']}, Amount: {record['amount']}, Category: {record['category']}, Date: {record['date']}, Remarks: {record['remarks']}")
#
#             # Add delete and update options
#             delete_checkbox = st.checkbox(f"Delete Record {i + 1}")
#             if delete_checkbox:
#                 records.delete_one({"_id": record["_id"]})
#                 st.write(f"Record {i + 1} deleted successfully!")
#
#             # Add update option
#             update_checkbox = st.checkbox(f"Update Record {i + 1}")
#             if update_checkbox:
#                 new_name = st.text_input("New Name", value=record['name'])
#                 new_amount = st.number_input("New Amount", value=record['amount'])
#                 new_category = st.selectbox("New Category", ["Income", "Expense"],
#                                             index=0 if record['category'] == "Income" else 1)
#                 new_date = st.text_input("New Date", value=record['date'])
#                 new_remarks = st.text_area("New Remarks", value=record['remarks'])
#
#                 # Update the record
#                 if st.button("Update"):
#                     new_values = {
#                         "$set": {
#                             "name": new_name,
#                             "amount": new_amount,
#                             "category": new_category,
#                             "date": new_date,
#                             "remarks": new_remarks
#                         }
#                     }
#                     records.update_one({"_id": record["_id"]}, new_values)
#                     st.write(f"Record {i + 1} updated successfully!")
#
#     else:
#         st.write("No records found.")

# if st.button ("Delete Selected Record"):
#     selected_index = st.session_state['selected_index']
#     if selected_index is not None:
#         records.delete_one({'_id': records_df.loc[selected_index, '_id']})
#         st.write ("Record deleted successfully.")
#         st.session_state['selected_index'] = None
#     else:
#         st.write ("No record selected.")
#
# # Display the DataFrame with a button for each record
# for i, row in records_df.iterrows():
#     # Display the record details
#     st.write(row)
#
#     # Add a button to delete the record
#     if st.button(f"Delete Record {i}"):
#         st.session_state['selected_index'] = i


# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from pymongo import MongoClient
# import Login
# from Login import records
# from session_state import SessionState
#
#
# state = SessionState.get(username='')
#
# def view_transactions(username):
#     st.subheader("View Records")
#     st.write("Welcome user", st.session_state['username'])
#     categories = [category['_id'] for category in records.aggregate ([{"$group": {"_id": "$category"}}])]
#     selected_category = st.selectbox("Filter by Category", ["All"] + categories)
#
#     if selected_category == "All":
#         filtered_records = records.find()
#     else:
#         filtered_records = records.find({"category": selected_category})
#
#     # Create a DataFrame to display the records
#     records_df = pd.DataFrame(filtered_records)
#
#     if not records_df.empty:
#         if 'user' not in records_df:
#             records_df['user'] = username
#
#         # Hide the ID column and display the modified DataFrame
#         st.write("List of Records:")
#         st.write(records_df.drop('_id', axis=1))
#
#         # Add delete option
#         st.write("Delete Selected Record:")
#         if 'selected_id' not in state:
#             state.selected_id = None
#         selected_id = st.selectbox("Select a record to delete:", [None] + list(records_df['_id']))
#         if selected_id is not None:
#             if st.button("Delete"):
#                 records.delete_one({'_id': selected_id})
#                 st.write("Record deleted successfully.")
#                 state.selected_id = None
#         else:
#             st.write("No record selected.")
#
#         # Data Analysis
#         st.subheader("Data Analysis")
#         st.write("Summary Statistics:")
#         st.write(records_df.describe())
#
#         st.write("Total Amount by Category:")
#         total_amount_by_category = records_df.groupby('category')['amount'].sum().reset_index()
#         st.write(total_amount_by_category)
#
#         # Visualization - Pie chart for total amount by category
#         st.write("Total Amount by Category (Pie Chart):")
#         chart_data = total_amount_by_category.set_index('category')
#
#         fig, ax = plt.subplots()
#         chart_data['amount'].plot(kind='pie', autopct='%1.1f%%', ax=ax)
#         st.pyplot(fig)
#
#         st.write("Total Transactions by Category:")
#         total_transactions_by_category = records_df['category'].value_counts().reset_index()
#         total_transactions_by_category.columns = ['category', 'count']
#         st.write(total_transactions_by_category)
#
#     else:
#         st.write("No records found.")
#
# view_transactions("username")
