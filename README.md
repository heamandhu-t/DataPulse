# Customer Behavior Analytics and Churn Prediction Using Python

A data science and analytics project that analyzes customer purchasing behavior, segments customers using RFM analysis and K-Means clustering, and predicts customer churn using a Random Forest classifier.

## Project Overview

This project uses the UCI Online Retail II dataset to understand customer purchasing patterns, identify different customer segments, and predict customers who may be at risk of churn.

The project follows a complete data science workflow:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Customer behavior analysis
- RFM analysis
- Customer segmentation using K-Means clustering
- Churn definition and prediction
- Random Forest classification
- Model evaluation
- Feature importance analysis
- Interactive Streamlit dashboard

## Dataset

**Dataset:** UCI Online Retail II

The dataset contains online retail transaction records from December 2009 to December 2011.

Main transaction fields include:

- Invoice
- StockCode
- Description
- Quantity
- InvoiceDate
- Price
- Customer ID
- Country

## Data Processing

The raw transaction data was cleaned by:

- Removing duplicate transactions
- Removing cancelled invoices
- Removing invalid quantities
- Removing invalid prices
- Removing transactions without Customer IDs
- Creating a Revenue feature

After cleaning, the project contains:

- **5,878 customers**
- **36,969 orders**
- **£17.37M total revenue**

## Customer Segmentation

RFM analysis was used to calculate:

- **Recency** — how recently a customer purchased
- **Frequency** — how often a customer purchased
- **Monetary** — how much a customer spent

The RFM values were log-transformed and standardized before applying K-Means clustering.

Four customer segments were identified:

- High-Value Loyal Customers
- Inactive Customers
- Occasional Customers
- Recent Low-Value Customers

## Churn Prediction

A customer was classified as churned when:

```text
Recency > 180 days
```

Customer behavior features used for machine learning:

- Total Quantity
- Unique Products
- Total Orders
- Total Spending
- Average Order Value

A **Random Forest Classifier** was trained to predict customer churn.

### Model Performance

Test-set accuracy:

```text
68.11%
```

Churn class F1-score:

```text
0.62
```

The trained model was saved using Joblib and integrated into the Streamlit dashboard.

## Dashboard

The interactive Streamlit dashboard provides:

- Total customer count
- Total revenue
- Total orders
- Churn rate
- Customer segment distribution
- Active vs churned customer analysis
- Revenue contribution by customer segment
- Customer segment filtering
- Customer-level analysis table
- Interactive churn prediction

Users can enter customer behavior information into the dashboard and receive a churn prediction from the trained Random Forest model.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook
- VS Code

## Project Structure

```text
Customer_Intelligence/
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── online_retail_II.xlsx
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── outputs/
│   └── customer_analysis.csv
│
├── src/
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Customer_Intelligence
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open at:

```text
http://localhost:8501
```

## Key Skills Demonstrated

- Python for Data Science
- Data Cleaning
- Exploratory Data Analysis
- Statistical Analysis
- Customer Analytics
- RFM Analysis
- Feature Engineering
- K-Means Clustering
- Supervised Machine Learning
- Random Forest Classification
- Model Evaluation
- Feature Importance Analysis
- Data Visualization
- Streamlit Dashboard Development
- Git and GitHub