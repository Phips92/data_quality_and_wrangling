import pandas as pd

# Load the original raw dataset
df = pd.read_pickle("freelancers_raw.pkl")

# Mapping to standardize gender values
gender_map = {
    "male": "male", "MALE": "male", "Male": "male", "m": "male", "M": "male",
    "female": "female", "FEMALE": "female", "Female": "female", "f": "female", "F": "female"
}

# Apply the mapping
df["gender"] = df["gender"].map(gender_map)

# Show result
print("\n--- Standardized gender values ---")
print(df["gender"].value_counts(dropna=False))

# Show rows with unmapped gender values
print("\n--- Unmapped gender values (if any) ---")
print(df[df["gender"].isna()][["name", "gender"]])

# Save cleaned version for the next step
df.to_pickle("freelancers_clean_gender.pkl")

