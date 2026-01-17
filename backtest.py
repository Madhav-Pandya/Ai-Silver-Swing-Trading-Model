import pandas as pd
import joblib
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange, BollingerBands

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

df = pd.read_csv("data/silver_swing_clean.csv")
df = add_features(df)
df.dropna(inplace=True)

model = joblib.load("models/swing_model.pkl")

capital = 100000
risk_pct = 0.01
equity = capital
wins = losses = 0

for i in range(len(df)-5):
    row = df.iloc[i:i+1]
    X = row[['ema20','ema50','ema200','rsi','atr','bb_width']]
    prob = model.predict_proba(X)[0][1]

    price = row['close'].values[0]
    rsi = row['rsi'].values[0]
    trend = row['ema50'].values[0] > row['ema200'].values[0]

    if trend and 38 < rsi < 45 and prob > 0.65:

        sl = price - 1.5 * row['atr'].values[0]
        tgt = price + 3 * row['atr'].values[0]

        future = df.iloc[i+1:i+6]

        hit_sl = (future['low'] <= sl).any()
        hit_tgt = (future['high'] >= tgt).any()

        risk_amt = equity * risk_pct

        if hit_tgt:
            equity += risk_amt * 2
            wins += 1
        elif hit_sl:
            equity -= risk_amt
            losses += 1

print("\nBACKTEST REPORT")
print("----------------")
print("Starting capital:", capital)
print("Ending capital:", round(equity,2))
print("Total trades:", wins+losses)
print("Wins:", wins)
print("Losses:", losses)
