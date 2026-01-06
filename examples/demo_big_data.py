"""
AM_Filler Big Data Performance Demo
Tests the library on a larger dataset (50,000 rows) to verify performance and logging.
"""

import pandas as pd
import numpy as np
import logging
import time
import sys
import os

# Ensure we can import the local package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from am_filler import AMFiller

# Configuration
LOG_FILE = "am_filler_big_data.log"
N_ROWS = 50000

# Configure logging
logger = logging.getLogger("am_filler")
logger.setLevel(logging.INFO)
# Remove existing handlers to avoid duplicate logs if run multiple times
if logger.handlers:
    logger.handlers.clear()
    
file_handler = logging.FileHandler(LOG_FILE, mode='w')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# Add stream handler to verify output in console too
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def generate_big_data(n_rows):
    print(f"Generating {n_rows:,} rows of synthetic data...")
    np.random.seed(42)
    
    # 1. Normal Distribution (Age)
    age = np.random.normal(35, 10, n_rows)
    # Add 5% missing
    mask_age = np.random.random(n_rows) < 0.05
    age[mask_age] = np.nan
    
    # 2. Skewed Distribution (Income)
    income = np.random.exponential(50000, n_rows) + 20000
    # Add outliers
    outlier_indices = np.random.choice(n_rows, size=int(n_rows * 0.01), replace=False)
    income[outlier_indices] = income[outlier_indices] * 10
    # Add 10% missing
    mask_income = np.random.random(n_rows) < 0.10
    income[mask_income] = np.nan
    
    # 3. Categorical (City)
    cities = ["New York", "London", "Paris", "Tokyo", "Berlin", "Sydney"]
    city = np.random.choice(cities, n_rows, p=[0.3, 0.2, 0.15, 0.15, 0.1, 0.1])
    # Add 8% missing
    mask_city = np.random.random(n_rows) < 0.08
    # Pandas handles None/NaN in object arrays better if we use a loop or conversion, 
    # but for speed we'll construct DataFrame then replace
    
    # 4. Text (Feedback)
    templates = [
        "Great service", "Fast delivery", "Poor quality", "Will buy again",
        "Not satisfied", "Excellent support", "Average experience", "Highly recommended"
    ]
    feedback = np.random.choice(templates, n_rows)
    # Add 15% missing
    mask_feedback = np.random.random(n_rows) < 0.15
    
    df = pd.DataFrame({
        "Age": age,
        "Income": income,
        "City": city,
        "Feedback": feedback
    })
    
    # Apply missing values to object columns
    df.loc[mask_city, "City"] = np.nan
    df.loc[mask_feedback, "Feedback"] = np.nan
    
    return df

def main():
    print("=" * 80)
    print(f"AM_FILLER BIG DATA DEMO ({N_ROWS:,} Rows)")
    print("=" * 80)
    
    # 1. Generate Data
    start_gen = time.time()
    df = generate_big_data(N_ROWS)
    print(f"Data Generation Time: {time.time() - start_gen:.4f} seconds")
    
    print("\n[DATASET SUMMARY]")
    print(df.info())
    print("\nMissing Values Count:")
    print(df.isnull().sum())
    
    # 2. Run AM_Filler
    print("\n" + "=" * 40)
    print("STARTING IMPUTATION...")
    print("=" * 40)
    
    start_time = time.time()
    
    filler = AMFiller(verbose=True)
    df_clean = filler.fit_transform(df)
    
    end_time = time.time()
    duration = end_time - start_time
    
    # 3. Validation
    print("\n" + "=" * 40)
    print(f"IMPUTATION COMPLETE in {duration:.4f} seconds")
    print("=" * 40)
    
    remaining = df_clean.isnull().sum().sum()
    if remaining == 0:
        print("\n[OK] SUCCESS: 0 missing values remain.")
    else:
        print(f"\n[!] FAILURE: {remaining} missing values remain.")
        
    print(f"\nLogs have been written to: {os.path.abspath(LOG_FILE)}")

if __name__ == "__main__":
    main()
