import pandas as pd

# Load data
df = pd.read_pickle("freelancers_raw.pkl")

# Missing values per column
print("\n--- Missing values per column ---")
print(df.isna().sum())

# Data types
print("\n--- Data types ---")
print(df.dtypes)

# Distribution of 'gender' values
print("\n--- Values in \"gender\" ---")
print(df["gender"].value_counts(dropna=False))

# Sample values for 'hourly_rate (USD)'
print("\n--- Sample values in \"hourly_rate (USD)\" ---")
print(df["hourly_rate (USD)"].dropna().unique()[:15])  # first 15 unique values

# Sample values for 'client_satisfaction'
print("\n--- Sample values in \"client_satisfaction\" ---")
print(df["client_satisfaction"].dropna().unique()[:15])

# Distribution of 'is_active'
print("\n--- Values in \"is_active\" ---")
print(df["is_active"].value_counts(dropna=False))

# Save problematic columns
problematic_columns = df[["gender", "hourly_rate (USD)", "client_satisfaction", "is_active"]]
problematic_columns.to_csv("profiling_output.csv", index=False)

