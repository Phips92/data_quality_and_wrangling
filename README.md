# Data Quality and Data Wrangling

This project was created as part of the IU course **DLBDSDQDW01 - Data Quality and Data Wrangling**. It includes scripts for profiling, cleaning, and transforming a real-world dataset of global freelancers.

---

## Project Structure

- `01_load_data.py` - Load raw CSV data and convert to pickle
- `02_data_profile.py` - Basic profiling: missing values, data types, etc.
- `03_clean_gender.py` - Standardize gender values
- `04_clean_hourly_rate.py` - Clean and convert hourly rate values
- `05_clean_active.py` - Normalize active/inactive status
- `06_clean_satisfaction.py` - Convert client satisfaction to numeric
- `07_handle_missing.py` - Handle missing values using custom strategies
- `08_advanced techniques.py` - Advanced wrangling techniques (e.g., outlier handling, transformations)
- `model_comparison.py` - Compare and evaluate alternative cleaning/imputation strategies

---

## Dataset

- **Name:** Global Freelancers
- **Source:** Kaggle  
- **Note:** The dataset is not included in this repository for copyright reasons.

You can download the dataset from [Kaggle](https://www.kaggle.com/) and place it in the `/data/` folder before running the scripts.

---

## Tasks Covered

- Data profiling and exploration
- Data cleaning (standardization, conversion, imputation)
- Missing value handling
- Pipeline design for real-world data wrangling
- Advanced techniques and strategy comparison

---

## Requirements

- Python 3.8+
- pandas
- numpy

---

## License & Author

**Author**: \[Philipp Mc Guire]

**License**: \This project is licensed under the GNU General Public License v3.0
