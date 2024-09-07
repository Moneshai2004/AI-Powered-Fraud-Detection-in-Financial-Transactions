import streamlit as st
import json
import requests as re

# Title of the app
st.title("AI-Powered Fraud Detection in Financial Transactions - YAR TECH PROJECT")

# Displaying the image with increased size
st.markdown("""
    <style>
        .image-container img {
            width: 150%;  /* Increase the size by 50% */
        }
    </style>
    <div class="image-container">
        <img src="image.png">
    </div>
    """, unsafe_allow_html=True)

# Project Description
st.write("""
Monesh Yar Tech project
""")

# Sidebar for input features
st.sidebar.header('Input Features of The Transaction')

sender_name = st.sidebar.text_input("Input Sender ID")
receiver_name = st.sidebar.text_input("Input Receiver ID")
step = st.sidebar.slider("Number of Hours it took the Transaction to complete:")
types = st.sidebar.selectbox("Enter Type of Transfer Made:", (0, 1, 2, 3, 4))
x = ''
if types == 0:
    x = 'Cash In'
elif types == 1:
    x = 'Cash Out'
elif types == 2:
    x = 'Debit'
elif types == 3:
    x = 'Payment'
elif types == 4:
    x = 'Transfer'

amount = st.sidebar.number_input("Amount in $", min_value=0, max_value=110000)
oldbalanceorg = st.sidebar.number_input("Original Balance Before Transaction was made", min_value=0, max_value=110000)
newbalanceorg = st.sidebar.number_input("New Balance After Transaction was made", min_value=0, max_value=110000)
oldbalancedest = st.sidebar.number_input("Old Balance", min_value=0, max_value=110000)
newbalancedest = st.sidebar.number_input("New Balance", min_value=0, max_value=110000)
isflaggedfraud = st.sidebar.selectbox("Specify if this was flagged as Fraud by your System:", (0, 1))

if st.button("Detection Result"):
    values = {
        "step": step,
        "types": types,
        "amount": amount,
        "oldbalanceorig": oldbalanceorg,
        "newbalanceorig": newbalanceorg,
        "oldbalancedest": oldbalancedest,
        "newbalancedest": newbalancedest,
        "isflaggedfraud": isflaggedfraud
    }

    st.write(f"""### These are the transaction details:
    - Sender ID: {sender_name}
    - Receiver ID: {receiver_name}
    - Number of Hours it took to complete: {step}
    - Type of Transaction: {x}
    - Amount Sent: {amount}
    - Sender Previous Balance Before Transaction: {oldbalanceorg}
    - Sender New Balance After Transaction: {newbalanceorg}
    - Recipient Balance Before Transaction: {oldbalancedest}
    - Recipient Balance After Transaction: {newbalancedest}
    - System Flag Fraud Status: {isflaggedfraud}
    """)

    res = re.post(f"http://backend.docker:8000/predict/", json=values)
    json_str = json.dumps(res.json())
    resp = json.loads(json_str)
    
    if sender_name == '' or receiver_name == '':
        st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
    else:
        st.write(f"### The '{x}' transaction that took place between {sender_name} and {receiver_name} is {resp[0]}.")
