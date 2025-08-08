import pandas as pd

# Load the latest cleaned version (with gender and hourly rate cleaned)
df = pd.read_pickle("freelancers_clean_hourly.pkl")

# Preview original values
print("\n--- Original values in \"is_active\" ---")
print(df["is_active"].value_counts(dropna=False))

# Define a mapping to unify all to True / False
is_active_map = {
    "1": True, 1: True, "yes": True, "Y": True, "True": True, True: True,
    "0": False, 0: False, "no": False, "N": False, "False": False, False: False
}

# Convert to string first, then map
df["is_active"] = df["is_active"].astype(str).str.strip().map(is_active_map)

# Check results
print("\n--- Cleaned boolean values in \"is_active\" ---")
print(df["is_active"].value_counts(dropna=False))

# Rows where mapping failed (still NaN)
print("\n--- Unmapped or missing \"is_active\" values ---")
print(df[df["is_active"].isna()][["name", "is_active"]].head())

# Save cleaned version
df.to_pickle("freelancers_clean_active.pkl")

