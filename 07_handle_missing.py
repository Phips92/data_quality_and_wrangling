import pandas as pd

# Load the most recently cleaned dataset
df = pd.read_pickle("freelancers_clean_satisfaction.pkl")

# Check missing values again
print("\n--- Missing values before handling ---")
print(df.isna().sum())

# =============================
# STRATEGY 1: Drop rows with too many missing values
# =============================
# Drop rows with more than 3 missing fields

df = df[df.isnull().sum(axis=1) <= 3]

# =============================
# STRATEGY 2: Fill numerical columns with median or mean
# =============================

# Fill missing 'age' with median

df["age"] = df["age"].fillna(df["age"].median())

# Fill missing 'years_of_experience' with median
df["years_of_experience"] = df["years_of_experience"].fillna(df["years_of_experience"].median())

# Fill missing 'hourly_rate (USD)' with mean
df["hourly_rate (USD)"] = df["hourly_rate (USD)"].fillna(df["hourly_rate (USD)"].mean())

# Fill missing 'rating' with 0 (assume unrated)
df["rating"] = df["rating"].fillna(0)

# =============================
# STRATEGY 3: Leave 'client_satisfaction' and 'is_active' as NaN
# =============================

# Reason: NaN can represent unknown or inactive state, depending on later analysis.

# Final check
print("\n--- Missing values after cleaning ---")
print(df.isna().sum())

# Save final cleaned dataset
df.to_pickle("freelancers_final_clean.pkl")
df.to_csv("freelancers_final_clean.csv", index=False)

