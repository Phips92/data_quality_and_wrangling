import pandas as pd

# Load the CSV file
df = pd.read_csv("data/global_freelancers_raw.csv")

# Overview
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nSample rows:\n", df.head())

# Save for later use
df.to_pickle("freelancers_raw.pkl")
