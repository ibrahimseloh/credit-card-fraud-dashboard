# Credit Card Fraud Detection Dashboard

## 📌 Project Overview
This project is a **Streamlit-based interactive dashboard** designed to analyze and visualize credit card transactions, specifically focusing on fraud detection. The dataset used contains real-world credit card transaction data labeled as either fraudulent or non-fraudulent.

## 🚀 Features
- **Dynamic Filtering**: Adjust transaction time, amount, and fraud class to explore data.
- **Key Metrics Display**: Get insights on total transactions, fraud counts, and fraud ratios.
- **Visualizations**:
  - Transaction amount and time distributions
  - Fraud vs. Non-Fraud transaction comparisons
  - Correlation matrix for feature relationships
- **User-Friendly UI**: Built with **Streamlit** and **Plotly** for an intuitive and interactive experience.

## 📂 Dataset
The dataset used is `creditcard.csv`, which contains:
- `Time`: Time elapsed since the first transaction
- `Amount`: Transaction value
- `Class`: 0 (Non-Fraud) or 1 (Fraud)
- Several anonymized features (`V1` to `V28`)

## 🔧 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/credit-card-fraud-dashboard.git
   cd credit-card-fraud-dashboard
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run app.py
   ```

## 🖥️ Usage
- Adjust the **filters** in the sidebar to explore different transaction patterns.
- Analyze **fraudulent vs. non-fraudulent transactions** through visualizations.
- Observe **correlations** between features using the correlation matrix.

## 📚 References
Created by **Fofana Ibrahim Seloh**. Connect with me on LinkedIn:
- [Fofana Ibrahim Seloh](https://www.linkedin.com/in/ibrahim-seloh-fofana-6073b4291/)

## 🏗️ Future Improvements
- Implement a **machine learning model** for fraud prediction.
- Add a **real-time detection system** with live transaction feeds.
- Enhance the UI with more advanced **interactive visualizations**.

---
🛠 Built with **Python, Streamlit, Pandas, and Plotly**.

