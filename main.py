import requests

BOT_TOKEN = "8351738232:AAGQEQwFTyApRcWsPK8Z7rPmuTh-Don0mWg"
CHAT_ID = "591297901"



import pandas as pd
import joblib
import yfinance as yf

from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange, BollingerBands


def load_live_data():
    df = yf.download(
        "SBISILVER.NS",
        interval="1h",
        period="60d"
    )

    # Fix multi-index columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    df = df.rename(columns={
        "Datetime": "datetime",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    })

    return df

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)


def add_features(df):
    df['ema20'] = EMAIndicator(df['close'], 20).ema_indicator()
    df['ema50'] = EMAIndicator(df['close'], 50).ema_indicator()
    df['ema200'] = EMAIndicator(df['close'], 200).ema_indicator()

    df['rsi'] = RSIIndicator(df['close'], 14).rsi()

    atr = AverageTrueRange(df['high'], df['low'], df['close'], 14)
    df['atr'] = atr.average_true_range()

    bb = BollingerBands(df['close'], 20)
    df['bb_width'] = bb.bollinger_hband() - bb.bollinger_lband()

    return df


# ---------------- MAIN ---------------- #

df = load_live_data()

df = add_features(df)
df.dropna(inplace=True)

model = joblib.load("models/swing_model.pkl")

row = df.iloc[-1:]

X = row[['ema20','ema50','ema200','rsi','atr','bb_width']]
prob = model.predict_proba(X)[0][1]

price = row['close'].values[0]
rsi = row['rsi'].values[0]

trend_up = row['ema50'].values[0] > row['ema200'].values[0]

print("Current price:", price)
print("AI probability:", round(prob, 2))

risk = 1.5 * row['atr'].values[0]
reward = 3 * row['atr'].values[0]

# BUY SETUP
if trend_up and 38 < rsi < 45 and prob > 0.65:

    sl = round(price - risk, 2)
    target = round(price + reward, 2)

    msg = (
        f"🚀 BUY SIGNAL\n"
        f"Price: {price:.2f}\n"
        f"Stoploss: {sl}\n"
        f"Target: {target}\n"
        f"AI Confidence: {prob*100:.1f}%"
    )

    print(msg)
    send_telegram(msg)

# SELL SETUP
elif rsi > 68 and prob > 0.65:

    sl = round(price + risk, 2)
    target = round(price - reward, 2)

    msg = (
        f"🔴 SELL SIGNAL\n"
        f"Price: {price:.2f}\n"
        f"Stoploss: {sl}\n"
        f"Target: {target}\n"
        f"AI Confidence: {prob*100:.1f}%"
    )

    print(msg)
    send_telegram(msg)

# NO TRADE
else:

    msg = (
        f"⚪ NO TRADE\n"
        f"Price: {price:.2f}\n"
        f"AI Confidence: {prob*100:.1f}%"
    )

    print(msg)
    send_telegram(msg)
