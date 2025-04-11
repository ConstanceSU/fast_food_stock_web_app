import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import yfinance as yf

@st.cache_data
def get_live_stock_data(ticker, start, end):
    # Remove group_by="ticker" or, if you prefer to keep it, extract the single ticker's data.
    stock = yf.download(ticker, start=start, end=end, group_by="ticker", auto_adjust=False)
    # Extract the data for the single ticker so that the columns become standard strings.
    stock = stock[ticker]
    stock.reset_index(inplace=True)
    return stock


DATA_FOLDER = "./Cleaned_Fast_Food_Stocks"

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400;700&display=swap');
    
    body, .stApp, .stMarkdown, .stSidebar, .stTextInput, .stSelectbox, .stButton > button, .stDataFrame, .stTable, .stMetric, .stSlider, .stToggle, .stSubheader {
        font-family: 'Roboto Mono', monospace !important;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    all_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]
    df_list = []
    
    for file in all_files:
        file_path = os.path.join(DATA_FOLDER, file)
        temp_df = pd.read_csv(file_path)
        temp_df["Company"] = file.replace("_cleaned.csv", "")
        temp_df["Date"] = pd.to_datetime(temp_df["Date"]) 
        df_list.append(temp_df)
    
    df = pd.concat(df_list, ignore_index=True)
    return df

df = load_data()

# Sidebar for stock selection
st.sidebar.title("🔎 Filters")
st.sidebar.markdown("<span style='color: black;'>Select companies:</span>", unsafe_allow_html=True)
companies = df["Company"].unique()
selected_companies = st.sidebar.multiselect(" ", companies, default=[companies[0]])
use_live_data = st.sidebar.checkbox("🔄 Use live data from Yahoo Finance")

# Date range selection
st.sidebar.markdown("<span style='color: black;'>Select Date Range:</span>", unsafe_allow_html=True)
start_date, end_date = st.sidebar.date_input(" ", [df["Date"].min(), df["Date"].max()],
                                     min_value=df["Date"].min(), max_value=df["Date"].max())
start_date, end_date = pd.to_datetime(start_date), pd.to_datetime(end_date)

# Toggle adjusted vs. raw prices
st.sidebar.markdown("<span style='color: black;'>Use Adjusted Closing Price:</span>", unsafe_allow_html=True)
use_adjusted = st.sidebar.toggle(" ")

# Moving average slider
st.sidebar.markdown("<span style='color: black;'>Select Moving Average Window:</span>", unsafe_allow_html=True)
ma_window = st.sidebar.slider(" ", min_value=3, max_value=50, value=10, step=1)

# Filter data
if use_live_data:
    live_data_list = []
    # Map company names to stock tickers manually
    ticker_map = {
        "BRK-A": "BRK-A",       
        "DNUT": "DNUT",         
        "DPZ": "DPZ",           
        "LKNCY": "LKNCY",       
        "MCD": "MCD",           
        "PZZA": "PZZA",         
        "QSR": "QSR",           
        "SBUX": "SBUX",         
        "WEN": "WEN",           
        "YUM": "YUM"            
    }
    for company in selected_companies:
        ticker = ticker_map.get(company)
        if ticker:
            df_live = get_live_stock_data(ticker, start_date, end_date)
            if not df_live.empty:
                df_live["Company"] = company
                live_data_list.append(df_live)
    if live_data_list:
        df_live_all = pd.concat(live_data_list, ignore_index=True)
        # Set adjusted close key as returned by yfinance (note the space)
        adj_close_key = "Adj Close"
        df_live_all.loc[:, "Moving_Avg"] = df_live_all[adj_close_key if use_adjusted else "Close"].rolling(ma_window).mean()
        filtered_df = df_live_all
    else:
        st.warning("⚠️ No live data found. Check tickers or internet connection.")
        st.stop()
else:
    # For CSV data, the adjusted close column is "Adj_Close"
    adj_close_key = "Adj_Close"
    filtered_df = df[
        (df["Company"].isin(selected_companies)) & 
        (df["Date"] >= start_date) & 
        (df["Date"] <= end_date)
    ]
    filtered_df.loc[:, "Moving_Avg"] = filtered_df[adj_close_key if use_adjusted else "Close"].rolling(ma_window).mean()

import numpy as np

# Flatten the Volume column to make sure it's 1D
filtered_df["Volume"] = filtered_df["Volume"].apply(
    lambda x: x[0] if isinstance(x, (list, np.ndarray)) else x
)
# Market Summary
st.sidebar.header("📊 Market Summary")
if not filtered_df.empty and len(selected_companies) == 1:
    company = selected_companies[0]
    company_df = filtered_df[filtered_df["Company"] == company]

    # (Market summary code...)

    # Debug prints (if you specifically need to see single-company data)
    st.write("company_df shape:", company_df.shape)
    st.write("Last row in company_df:", company_df.iloc[-1])
    st.write("Close column, last row:", company_df["Close"].iloc[-1])

elif len(selected_companies) > 1:
    st.sidebar.info("ℹ️ Market summary available when one company is selected.")




# Candlestick Chart with Red/Green Theme
st.subheader("📈 Stock Price Trends", help="Stock price movements with candlestick visualization")
fig = go.Figure()
for company in selected_companies:
    temp_df = filtered_df[filtered_df["Company"] == company]
    fig.add_trace(go.Candlestick(
        x=temp_df["Date"],
        open=temp_df["Open"],
        high=temp_df["High"],
        low=temp_df["Low"],
        close=temp_df[adj_close_key if use_adjusted else "Close"],
        increasing_line_color='green', decreasing_line_color='red',
        name=f"{company} Price"
    ))
    fig.add_trace(go.Scatter(
        x=temp_df["Date"],
        y=temp_df["Moving_Avg"],
        mode='lines',
        line=dict(color='black', dash='dash', width=1.5),
        name=f"{company} {ma_window}-day MA"
    ))


fig.update_layout(template="plotly_white", xaxis_rangeslider_visible=False, plot_bgcolor="white", paper_bgcolor="white")
st.plotly_chart(fig, use_container_width=True)

# Display stock volume
st.subheader("📊 Trading Volume", help="Historical trading volume")
import plotly.express as px

fig_vol = px.bar(
    filtered_df,
    x='Date',
    y='Volume',
    title='Trading Volume',
    color='Volume',
    color_continuous_scale='Greens'
)

fig_vol.update_traces(marker=dict(line=dict(width=0), opacity=0.7))
fig_vol.update_layout(template='plotly_white', xaxis_title='Date', yaxis_title='Volume')
st.plotly_chart(fig_vol, use_container_width=True)

# Search function
st.markdown("<span style='color: black;'>Search for a company:</span>", unsafe_allow_html=True)
search_term = st.text_input(" ")
if search_term:
    search_results = df[df["Company"].str.contains(search_term, case=False)]
    st.dataframe(search_results)

# Upload new dataset
st.markdown("<span style='color: black;'>Upload a new CSV file:</span>", unsafe_allow_html=True)
uploaded_file = st.file_uploader(" ", type=["csv"])
if uploaded_file:
    df_uploaded = pd.read_csv(uploaded_file)
    st.dataframe(df_uploaded.head())
