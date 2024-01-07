import streamlit as st
from Login import records


def add_transaction_form(username):
    st.subheader ("Transaction Form")

    # Input fields for transaction details
    with st.form (key='transaction_form'):
        st.write ("Enter the details of the transaction:")
        name = st.text_input ("Description", max_chars=50)
        amount = st.number_input ("Amount", min_value=0.01, format="%.2f")
        category = st.selectbox ("Category", ("Income", "Expense"))
        datevalue = st.text_input ("Date posted", max_chars=50)
        remarks = st.text_area ("Remarks", max_chars=200)

        # Submit button
        submitted = st.form_submit_button ("Register")

        if submitted:
            # Save the record to the database
            record = {
                'user': username,
                'name': name,
                'amount': amount,
                'category': category,
                'date': datevalue,
                'remarks': remarks
            }
            records.insert_one (record)
            st.success ("Record saved successfully!")

            # Clear the input fields after successful submission
          #  st.rerun()

    # Additional instructions
    st.markdown ("---")
    st.write ("Please fill in the details and click 'Register' to save the transaction.")

# import streamlit as st
#
# from Login import records
#
#
# def add_transaction_form(username):
#     st.subheader("Transaction")
#     name = st.text_input("Description")
#     amount = st.number_input("Amount")
#     category = st.selectbox("Category", ("Income", "Expense"))
#     datevalue = st.text_input("Date posted")
#     remarks = st.text_area("Remarks")
#   #  st.write(username)
#     if st.button("Register"):
#         record = {
#             'name': name,
#             'amount': amount,
#             'category': category,
#             'date': datevalue,
#             'remarks': remarks
#         }
#         records.insert_one(record)
#         st.success("Record saved successfully!")
