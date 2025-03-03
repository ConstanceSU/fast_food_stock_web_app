# Fast-Food Stock Performance Web App Documentation

## Overview

The Fast-Food Stock Performance Web App is an interactive Streamlit application designed to analyze and visualize the stock performance of major fast-food companies, including Berkshire Hathaway Inc. (BRK-A), Krispy Kreme, Inc. (DNUT), Domino’s Pizza, Inc. (DPZ), Luckin Coffee Inc. (LKNCY), McDonald’s Corporation (MCD), Papa John’s International, Inc. (PZZA), Restaurant Brands International, Inc. (QSR), Starbucks Corporation (SBUX), The Wendy’s Corporation (WEN), and Yum! Brands, Inc. (YUM). The app provides key financial insights by leveraging historical stock market data and integrates advanced interactive visualizations to enhance user experience.

*The datasets come from the final project of Python in the 1st term

### Key Features

1. Stock Data Exploration
   Users can compare multiple fast-food companies from a preloaded list, making trend analysis straightforward.

2. Stock Price Visualization

The app features candlestick charts with a red-green color scheme for intuitive tracking of stock movements. A moving average line smooths fluctuations and highlights trends, while the responsive design ensures a seamless experience across all devices.

3. Trading Volume Analysis

A gradient-style bar chart visually represents trading volume trends at a glance. Hovering over individual bars reveals detailed trading activity, making it easy to identify periods of high and low volume.

4. Market Summary Dashboard

This dashboard offers a quick snapshot of key financial metrics, including the latest closing price, highest and lowest stock values within the selected range, and total trading volume. Users can instantly gain insights without sifting through raw data.

5. Interactive Controls

Users can customize their analysis with a range of intuitive tools: a dropdown for company selection, a date picker to refine the timeframe, a toggle to switch between adjusted and raw closing prices, and a slider for moving average adjustments. A search bar allows quick lookups, and a file uploader enables the addition of new stock data.

### Main difficuties

I met a lot of difficuties. Please read this file to see how I failed my initial idea: https://github.com/ConstanceSU/fast_food_stock_web_app/blob/main/failed_attempt.md 

### How to run the app?

- Run the command in my terminal: streamlit run streamlit_web_app.py
<img width="500" alt="Screenshot 2025-03-03 at 14 45 32" src="https://github.com/user-attachments/assets/eca09d6d-d8c5-4e32-b637-6739a4410280" />

- The web app will be display automatically in your default browser
<img width="1200" alt="Screenshot 2025-03-03 at 14 46 49" src="https://github.com/user-attachments/assets/7fb645e1-d9f0-472a-8023-d230621451bc" />

- You can filter/choose the stock data as you like to discover/comapre different ones
<img width="300" alt="Screenshot 2025-03-03 at 14 47 31" src="https://github.com/user-attachments/assets/039097f6-35b6-41e9-8c8b-9be9817aa36a" />

<img width="400" alt="Screenshot 2025-03-03 at 14 49 31" src="https://github.com/user-attachments/assets/376a0a82-d7f8-4050-87eb-469df8bd0ec8" />

- You can set up the date range as you like in the side bar
<img width="257" alt="Screenshot 2025-03-03 at 14 49 54" src="https://github.com/user-attachments/assets/dc4e32b8-7b0e-4657-b75a-c0ac8dd00b5e" />

- You can search a company's name to view the stock price in detail
<img width="500" alt="Screenshot 2025-03-03 at 14 50 37" src="https://github.com/user-attachments/assets/48e09cb4-7d12-4363-9bf0-6ed737cfea7a" />

- The web app enables you to upload a new dataset regarding stock price
<img width="500" alt="Screenshot 2025-03-03 at 14 52 13" src="https://github.com/user-attachments/assets/f9966205-d178-418a-ae98-106ee30e62e6" />







