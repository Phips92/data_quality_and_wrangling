import pandas as pd

# Load the previously cleaned dataset
df = pd.read_pickle("freelancers_clean_active.pkl")

# Preview original values
print("\n--- Original values in \"client_satisfaction\" ---")
print(df["client_satisfaction"].dropna().unique()[:15])

# Remove % symbol and convert to float safely
df["client_satisfaction"] = (df["client_satisfaction"].astype(str).str.replace("%", "", regex=False))

# Use pd.to_numeric to handle invalid or missing entries
df["client_satisfaction"] = pd.to_numeric(df["client_satisfaction"], errors="coerce")

# Check result
print("\n--- Cleaned \"client_satisfaction\" as float ---")
print(df["client_satisfaction"].describe())

# Show some sample rows
print("\n--- Sample rows with cleaned \"client_satisfaction\" ---")
print(df[["name", "client_satisfaction"]].head(10))

# Save for the next step
df.to_pickle("freelancers_clean_satisfaction.pkl")

