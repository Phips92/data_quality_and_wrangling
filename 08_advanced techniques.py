import pandas as pd
import numpy as np

# -------------------
# 1. Load cleaned dataset
# -------------------
df = pd.read_pickle("freelancers_final_clean.pkl")

# -------------------
# 2. Feature Engineering
# -------------------
# Experience level
def categorize_experience(years):
    if pd.isna(years):
        return "unknown"
    elif years < 3:
        return "junior"
    elif years < 8:
        return "mid"
    else:
        return "senior"

df["experience_level"] = df["years_of_experience"].apply(categorize_experience)

# Country -> Continent mapping
continent_map = {
    "Germany": "Europe", "France": "Europe", "Netherlands": "Europe", "Italy": "Europe", "Spain": "Europe", "United Kingdom": "Europe",
    "United States": "North America", "Canada": "North America", "Mexico": "North America",
    "Brazil": "South America", "Argentina": "South America",
    "India": "Asia", "China": "Asia", "Japan": "Asia", "South Korea": "Asia", "Indonesia": "Asia", "Russia": "Asia", "Turkey": "Asia",
    "South Africa": "Africa", "Egypt": "Africa"
}
df["continent"] = df["country"].map(continent_map).fillna("Other")

# Log transformation of hourly rate
df["log_hourly_rate"] = np.log1p(df["hourly_rate (USD)"])

# Outlier capping (99th percentile)
upper_cap = df["hourly_rate (USD)"].quantile(0.99)
df["hourly_rate_capped"] = np.where(df["hourly_rate (USD)"] > upper_cap, upper_cap, df["hourly_rate (USD)"])

# Client satisfaction bucket
def satisfaction_bucket(val):
    if pd.isna(val):
        return "unknown"
    elif val < 70:
        return "low"
    elif val < 85:
        return "medium"
    else:
        return "high"

df["satisfaction_bucket"] = df["client_satisfaction"].apply(satisfaction_bucket)

# Experience per age ratio
df["experience_per_age"] = df["years_of_experience"] / df["age"]

# Is senior (binary)
df["is_senior"] = (df["years_of_experience"] >= 8).astype(int)

# Has rating (binary)
df["has_rating"] = df["rating"].notna().astype(int)

# Language group mapping
language_group_map = {
    "English": "Indo-European", "Spanish": "Indo-European", "French": "Indo-European",
    "German": "Indo-European", "Dutch": "Indo-European", "Italian": "Indo-European",
    "Portuguese": "Indo-European", "Hindi": "Indo-European", "Russian": "Indo-European",
    "Arabic": "Afro-Asiatic", "Afrikaans": "Indo-European",
    "Mandarin": "Sino-Tibetan", "Japanese": "Japonic", "Korean": "Koreanic",
    "Turkish": "Turkic", "Indonesian": "Austronesian"
}
df["language_group"] = df["language"].map(language_group_map).fillna("Other")

# Hourly rate deviation from continent median
continent_median = df.groupby("continent")["hourly_rate (USD)"].transform("median")
df["rate_vs_continent_median"] = df["hourly_rate (USD)"] - continent_median

# -------------------
# 3. Save as advanced dataset
# -------------------
df.to_pickle("advanced_final_dataset.pkl")
print("Advanced dataset saved as advanced_final_dataset.pkl")




