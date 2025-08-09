import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


df_raw = pd.read_pickle("freelancers_raw.pkl")
df_clean_adv = pd.read_pickle("advanced_final_dataset.pkl") 

features_raw = [
    "gender", "age", "country", "language", "primary_skill",
    "years_of_experience", "rating", "is_active", "client_satisfaction"
]

features_advanced = [
    "gender", "age", "country", "language", "primary_skill",
    "years_of_experience", "rating", "is_active", "client_satisfaction",
    "experience_level", "continent", "hourly_rate_capped",
    "satisfaction_bucket", "experience_per_age", "is_senior",
    "has_rating", "language_group", "rate_vs_continent_median"
]

target = "hourly_rate (USD)"

def prepare_data_keep_feature_nans(df, feature_list):
    """Konvertiert Ziel zu float, entfernt nur Zeilen mit ungültigem Zielwert."""
    data = df[feature_list + [target]].copy()
    
    # target col to float
    data[target] = pd.to_numeric(data[target], errors="coerce")
    
    before = len(data)
    data = data.dropna(subset=[target])
    after = len(data)
    dropped = before - after
    
    X = data[feature_list]
    y = data[target]
    return X, y, dropped

def train_and_evaluate(X, y, label, dropped_rows):
    X_enc = pd.get_dummies(X, dummy_na=True)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_enc, y, test_size=0.1, random_state=42
    )
    
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)
    
    print(f"\n--- {label} ---")
    print(f"Dropped rows (invalid target): {dropped_rows}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²:   {r2:.3f}")


# RAW DATA 
X_raw, y_raw, dropped_raw = prepare_data_keep_feature_nans(df_raw, features_raw)
train_and_evaluate(X_raw, y_raw, "RAW DATA", dropped_raw)

# CLEAN DATA 
X_clean_adv, y_clean_adv, dropped_clean_adv = prepare_data_keep_feature_nans(df_clean_adv, features_advanced)
train_and_evaluate(X_clean_adv, y_clean_adv, "CLEAN DATA (Advanced Features)", dropped_clean_adv)





