import requests
import pandas as pd
from datetime import datetime

# SBI Silver ETF token (Groww)
TOKEN = "SBI_SILVER_ETF"

url = "https://groww.in/v1/api/charting_service/v2/chart/exchange/NSE/segment/CASH/token/{}"

params = {
    "interval": "60minute",   # 1 Hour
    "from": 1577836800,       # Jan 2020
    "to": int(datetime.now().timestamp())
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url.format(TOKEN), params=params, headers=headers)
data = res.json()["candles"]

df = pd.DataFrame(data, columns=[
    "timestamp","open","high","low","close","volume"
])

df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")
df = df[["datetime","open","high","low","close","volume"]]

df.to_csv("data/silver_swing.csv", index=False)

print("Download complete")
print(df.head())
