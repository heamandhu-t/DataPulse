import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(
    page_title="Customer Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Behavior Analytics and Churn Prediction")
st.write(
    "Analyze customer behavior, segmentation, spending patterns, and churn risk."
)
# Load customer analysis data
data = pd.read_csv("outputs/customer_analysis.csv", index_col=0)

st.success("Customer data loaded successfully!")

st.write("Dataset shape:", data.shape)
# Load trained churn prediction model
model = joblib.load("models/churn_model.pkl")

st.success("Churn model loaded successfully!")
# Key Performance Indicators

total_customers = data.shape[0]
total_revenue = data["Monetary"].sum()
total_orders = data["Total_Orders"].sum()
churn_rate = data["Churn"].mean() * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Total Revenue", f"£{total_revenue:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Churn Rate", f"{churn_rate:.2f}%")
# Customer Segment Distribution

st.subheader("Customer Segmentation")

segment_counts = data["Segment"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    x=segment_counts.values,
    y=segment_counts.index,
    ax=ax
)

ax.set_xlabel("Number of Customers")
ax.set_ylabel("Customer Segment")
ax.set_title("Customer Distribution by Segment")

plt.tight_layout()

st.pyplot(fig)
# Churn Overview

st.subheader("Customer Churn Overview")

churn_counts = data["Churn"].value_counts().sort_index()

churn_labels = ["Active Customers", "Churned Customers"]

fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    x=churn_labels,
    y=churn_counts.values,
    ax=ax
)

ax.set_xlabel("Customer Status")
ax.set_ylabel("Number of Customers")
ax.set_title("Active vs Churned Customers")

plt.tight_layout()

st.pyplot(fig)
# Revenue by Customer Segment

st.subheader("Revenue by Customer Segment")

segment_revenue = (
    data.groupby("Segment")["Monetary"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    x=segment_revenue.values,
    y=segment_revenue.index,
    ax=ax
)

ax.set_xlabel("Total Revenue (£)")
ax.set_ylabel("Customer Segment")
ax.set_title("Revenue Contribution by Customer Segment")

plt.tight_layout()

# Customer Segment Summary

st.subheader("Customer Segment Summary")

segment_summary = (
    data.groupby("Segment")
    .agg(
        Customers=("Segment", "size"),
        Avg_Recency=("Recency", "mean"),
        Avg_Frequency=("Frequency", "mean"),
        Avg_Monetary=("Monetary", "mean"),
        Total_Revenue=("Monetary", "sum")
    )
    .reset_index()
)

segment_summary["Avg_Recency"] = segment_summary["Avg_Recency"].round(1)
segment_summary["Avg_Frequency"] = segment_summary["Avg_Frequency"].round(1)
segment_summary["Avg_Monetary"] = segment_summary["Avg_Monetary"].round(2)
segment_summary["Total_Revenue"] = segment_summary["Total_Revenue"].round(2)

st.dataframe(
    segment_summary,
    use_container_width=True
)

st.pyplot(fig)
# Segment Filter

st.subheader("Explore Customers")

segments = ["All Segments"] + sorted(data["Segment"].unique().tolist())

selected_segment = st.selectbox(
    "Select Customer Segment",
    segments
)

if selected_segment == "All Segments":
    filtered_data = data
else:
    filtered_data = data[data["Segment"] == selected_segment]

st.write(
    f"Customers in selected segment: **{len(filtered_data):,}**"
)

st.dataframe(
    filtered_data[
        [
            "Recency",
            "Frequency",
            "Monetary",
            "Segment",
            "Churn",
            "Total_Quantity",
            "Unique_Products",
            "Total_Orders",
            "Total_Spending",
            "Avg_Order_Value"
        ]
    ],
    use_container_width=True
)

# Churn Prediction Tool

st.subheader("Churn Prediction Tool")

st.write(
    "Enter customer behavior details to predict churn."
)

col1, col2, col3 = st.columns(3)

with col1:
    total_quantity = st.number_input(
        "Total Quantity",
        min_value=1,
        value=100
    )

with col2:
    unique_products = st.number_input(
        "Unique Products",
        min_value=1,
        value=10
    )

with col3:
    total_orders = st.number_input(
        "Total Orders",
        min_value=1,
        value=3
    )

col4, col5 = st.columns(2)

with col4:
    total_spending = st.number_input(
        "Total Spending (£)",
        min_value=0.0,
        value=500.0
    )

with col5:
    avg_order_value = st.number_input(
        "Average Order Value (£)",
        min_value=0.0,
        value=50.0
    )

if st.button("Predict Churn"):

    input_data = pd.DataFrame({
        "Total_Quantity": [total_quantity],
        "Unique_Products": [unique_products],
        "Total_Orders": [total_orders],
        "Total_Spending": [total_spending],
        "Avg_Order_Value": [avg_order_value]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Prediction: Customer is likely to churn.")
    else:
        st.success("Prediction: Customer is likely to remain active.")