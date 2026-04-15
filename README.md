# Stock Market Data Pipeline and Dashboard

## Overview
This project is a simple end-to-end data pipeline that collects stock market data using Python and displays it in Power BI.

The goal is to automate data collection and build a dashboard that changes by every refresh.


## What this project does
- Fetches stock data using Python (yfinance)
- Stores the data in a CSV file
- Runs using a pipeline script
- Displays insights in Power BI



## Tools used
- Python (pandas, yfinance)
- Power BI
- Windows Task Scheduler
- GitHub




## Dashboard features
- Average stock price per company
- Stock price trend over time
- Comparison between companies
- Filters for company and date



## How to run
Run:
python pipeline.py
or
open Task scheduler,
Select the created task and run, then open Power BI and click refresh.



## Automation
The pipeline can be scheduled using Task Scheduler to run daily.  
Power BI reads the updated CSV file and refreshing it changes the dashboard.
