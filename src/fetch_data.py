import yfinance as yf
import pandas as pd
from datetime import datetime

tickers = ["ACN", "PLTR", "GLOB"]
start = "2023-01-01"
end = datetime.today().strftime('%Y-%m-%d')

final_df = pd.DataFrame()

for t in tickers:
    s = yf.Ticker(t)
    h = s.history(start=start, end=end)

    info = s.info
    pe = info.get("trailingPE")

    if not h.empty:
        h = h.reset_index()
        h["Company"] = t
        h["PE_Ratio"] = pe
        h["Valuation"] = "Overvalued" if pe and pe > 25 else "Undervalued"

        final_df = pd.concat([final_df, h], ignore_index=True)
        final_df = final_df[[
    "Date", "Company", "Open", "High", "Low", "Close", "Volume",
    "PE_Ratio", "Valuation"
]]

final_df["Date"] = pd.to_datetime(final_df["Date"]).dt.date

final_df.to_csv("data/stock_data.csv", index=False)

print(final_df.head())