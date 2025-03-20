import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set up the page layout
st.set_page_config(page_title="Credit Card Fraud Dashboard", layout="wide")

# Project Context Description
st.title("Credit Card Fraud Detection Analysis 💳")
st.markdown("""
    ## Project Context 📋
    In this project, the goal is to analyze credit card transactions to identify fraudulent activities. The dataset consists of transactions made by credit cards, with labels marking whether the transaction was fraudulent or not. The aim is to apply data analysis techniques to understand patterns, detect anomalies, and gain insights into fraud detection systems.

""")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("creditcard.csv")

data = load_data()

# Sidebar Filters
st.sidebar.header("Filters 🛠️")
time_range = st.sidebar.slider("Transaction Time Range", int(data.Time.min()), int(data.Time.max()), (int(data.Time.min()), int(data.Time.max())))
amount_range = st.sidebar.slider("Transaction Amount Range", float(data.Amount.min()), float(data.Amount.max()), (float(data.Amount.min()), float(data.Amount.max())))
selected_class = st.sidebar.radio("Select Transaction Class", ["Both", "Non-Fraud", "Fraud"])

# Data Filtering
filtered_data = data[(data["Time"] >= time_range[0]) & (data["Time"] <= time_range[1]) &
                     (data["Amount"] >= amount_range[0]) & (data["Amount"] <= amount_range[1])]
if selected_class == "Non-Fraud":
    filtered_data = filtered_data[filtered_data["Class"] == 0]
elif selected_class == "Fraud":
    filtered_data = filtered_data[filtered_data["Class"] == 1]

# Metrics Calculation
total_transactions = filtered_data.shape[0]
fraud_transactions = filtered_data[filtered_data["Class"] == 1].shape[0]
nonfraud_transactions = filtered_data[filtered_data["Class"] == 0].shape[0]
fraud_ratio = (fraud_transactions / total_transactions * 100) if total_transactions > 0 else 0

# Dashboard Layout
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Total Transactions 🧾", value=f"{total_transactions:,}")
with col2:
    st.metric(label="Fraudulent Transactions 🚨", value=f"{fraud_transactions:,}", delta_color="inverse")
with col3:
    st.metric(label="Non-Fraudulent Transactions ✅", value=f"{nonfraud_transactions:,}")
with col4:
    st.metric(label="Fraud Ratio (%) 📊", value=f"{fraud_ratio:.2f}%")

# Data Overview
st.subheader("Data Overview 📑")
st.dataframe(filtered_data.head(), use_container_width=True)

# Graphs Layout
col1, col2 = st.columns(2)
with col1:
    fig_amount = px.histogram(filtered_data, x="Amount", color="Class", nbins=50, title="Transaction Amount Distribution 💵", color_discrete_map={0: "#1f77b4", 1: "#d62728"})
    st.plotly_chart(fig_amount, use_container_width=True)
with col2:
    fig_time = px.histogram(filtered_data, x="Time", color="Class", nbins=50, title="Transaction Time Distribution ⏰", color_discrete_map={0: "#1f77b4", 1: "#d62728"})
    st.plotly_chart(fig_time, use_container_width=True)

# Correlation Matrix
st.subheader("Correlation Analysis 🔍")
corr_matrix = filtered_data.corr()
fig_corr = px.imshow(corr_matrix, text_auto=True, aspect="auto", title="Correlation Matrix 🧠", color_continuous_scale='Blues')
st.plotly_chart(fig_corr, use_container_width=True)

# Author References and Additional Information
st.markdown("""
    ---
    ## References 📚
    This dashboard was created by **Fofana Ibrahim Seloh**.
    
    For more insights, tutorials, and to connect with me, feel free to visit my LinkedIn profile:

    - [Fofana Ibrahim Seloh](https://www.linkedin.com/in/ibrahim-seloh-fofana-6073b4291/)

    I look forward to connecting with you and sharing knowledge!
""")

