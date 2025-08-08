import pandas as pd

# Load the previously cleaned version
df = pd.read_pickle("freelancers_clean_gender.pkl")

# Analyze original values (optional)
print("\n--- Original values in \"hourly_rate (USD)\" ---")
print(df["hourly_rate (USD)"].dropna().unique()[:15])

# Remove "$", "USD", spaces, etc. - keep only digits and decimal point
df["hourly_rate (USD)"] = (
    df["hourly_rate (USD)"]
    .astype(str)
    .str.replace(r"[^\d.]", "", regex=True)
)

# Convert to float (invalid values become NaN)
df["hourly_rate (USD)"] = pd.to_numeric(df["hourly_rate (USD)"], errors="coerce")

# Check the result
print("\n--- Cleaned hourly rates (float) ---")
print(df["hourly_rate (USD)"].describe())

# Show sample rows
print("\n--- Sample rows with cleaned hourly rates ---")
print(df[["name", "hourly_rate (USD)"]].head(10))

# Save for next step
df.to_pickle("freelancers_clean_hourly.pkl")

