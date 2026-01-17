import yfinance as yf

# SBI Silver ETF NSE ticker
ticker = "SBISILVER.NS"   # works on Yahoo

data = yf.download(
    ticker,
    interval="1h",
    period="2y"
)

data = data.reset_index()
data = data.rename(columns={
    "Datetime":"datetime",
    "Open":"open",
    "High":"high",
    "Low":"low",
    "Close":"close",
    "Volume":"volume"
})

data = data[["datetime","open","high","low","close","volume"]]
data.to_csv("data/silver_swing.csv", index=False)

print("Download complete")
print(data.head())
