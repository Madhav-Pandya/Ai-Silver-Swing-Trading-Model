import joblib
import pandas as pd
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

def evaluate(model_path, df):
    model = joblib.load(model_path)
    df = add_features(df)
    df.dropna(inplace=True)

    equity = 100000

    for i in range(len(df)-5):
        row = df.iloc[i:i+1]
        X = row[['ema20','ema50','ema200','rsi','atr','bb_width']]
        prob = model.predict_proba(X)[0][1]

        price = row['close'].values[0]
        rsi = row['rsi'].values[0]
        trend = row['ema50'].values[0] > row['ema200'].values[0]

        if trend and 35 < rsi < 50 and prob > 0.55:
            sl = price - 1.5 * row['atr'].values[0]
            tgt = price + 3 * row['atr'].values[0]

            future = df.iloc[i+1:i+6]
            if (future['high'] >= tgt).any():
                equity *= 1.02
            elif (future['low'] <= sl).any():
                equity *= 0.99

    return equity
