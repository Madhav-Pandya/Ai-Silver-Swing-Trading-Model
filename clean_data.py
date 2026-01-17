import pandas as pd

df = pd.read_csv("data/silver_swing.csv")

# Remove non-date rows
df = df[pd.to_datetime(df["datetime"], errors="coerce").notna()]

df.to_csv("data/silver_swing_clean.csv", index=False)

print("Cleaned successfully")
print(df.head())
