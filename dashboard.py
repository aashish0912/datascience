import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Trader Performance Dashboard")
st.write("Exploratory analysis of trader behavior vs Market Sentiment.")

# Load Data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/trader_data.csv')
        sent = pd.read_csv('data/bitcoin_sentiment.csv')
        # Basic prep
        sent['date'] = pd.to_datetime(sent['date'], format='mixed', dayfirst=True, errors='coerce')
        df['datetime'] = pd.to_datetime(df['Timestamp'], unit='ms')
        df['date'] = df['datetime'].dt.normalize()
        # Merge
        merged = pd.merge(df, sent, on='date', how='left')
        return merged
    except Exception as e:
        return None

df = load_data()

if df is not None:
    st.sidebar.header("Filters")
    sentiment_filter = st.sidebar.multiselect(
        "Select Sentiment:",
        options=df['classification'].dropna().unique(),
        default=df['classification'].dropna().unique()
    )

    filtered_df = df[df['classification'].isin(sentiment_filter)]

    # Metrics
    total_pnl = filtered_df['Closed PnL'].sum()
    total_vol = filtered_df['Size USD'].sum()
    
    col1, col2 = st.columns(2)
    col1.metric("Total PnL", f"${total_pnl:,.2f}")
    col2.metric("Total Volume", f"${total_vol:,.2f}")

    # Charts
    st.subheader("PnL Distribution")
    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_df, x='classification', y='Closed PnL', showfliers=False, ax=ax)
    st.pyplot(fig)
    
    st.subheader("Raw Data")
    st.dataframe(filtered_df.head(50))
    
else:
    st.error("Could not load data. Please ensure 'data/' folder contains 'trader_data.csv' and 'bitcoin_sentiment.csv'")
