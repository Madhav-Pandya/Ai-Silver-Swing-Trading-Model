import pandas as pd
import xgboost as xgb
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


def create_labels(df, lookahead=5, move=0.03):
    labels=[]
    for i in range(len(df)):
        future = df['high'].iloc[i+1:i+lookahead+1].max()
        now = df['close'].iloc[i]
        labels.append(1 if future >= now*(1+move) else 0)
    return labels


# Load data
df = pd.read_csv("data/silver_swing_clean.csv")

df = add_features(df)
df.dropna(inplace=True)

df['y'] = create_labels(df)

X = df[['ema20','ema50','ema200','rsi','atr','bb_width']]
y = df['y']

model = xgb.XGBClassifier(
    max_depth=4,
    n_estimators=200,
    learning_rate=0.05
)

model.fit(X,y)

joblib.dump(model,"models/swing_model.pkl")

print("Swing AI model trained successfully")
