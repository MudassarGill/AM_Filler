"""
Test AM_Filler with User Data
This script simulates testing on a user's dataset to demonstrate the package capabilities.
"""

import pandas as pd
import numpy as np
import logging
import sys
import os

# Ensure we can import the local package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from am_filler import AMFiller

# Configure logging to file
logger = logging.getLogger("am_filler")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("am_filler_demo.log", mode='w')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def create_demo_dataset():
    """Create a rich dataset with various types of missing values."""
    np.random.seed(42)  # For reproducible results
    
    n_rows = 20
    
    data = {
        # Numeric (Normal) - Age
        "Age": [25, 30, np.nan, 34, 28, 45, np.nan, 23, 31, 29, 
                33, 50, np.nan, 27, 35, 41, 22, 38, np.nan, 46],
                
        # Numeric (Skewed/Outliers) - Salary
        "Salary": [50000, 55000, np.nan, 52000, 48000, 120000, 51000, 53000, np.nan, 
                   54000, 49000, 250000, 51500, 52500, np.nan, 1500000, 47000, 56000, 50500, np.nan],
                   
        # Categorical - Department
        "Department": ["Sales", "IT", "HR", "Sales", "IT", np.nan, "HR", "Sales", "Marketing", "IT",
                      "Sales", np.nan, "IT", "Sales", "Marketing", "IT", np.nan, "HR", "Sales", "IT"],
                      
        # Text - Feedback
        "Customer_Feedback": [
            "Great service!", 
            np.nan, 
            "Product quality is amazing.", 
            "Fast delivery.", 
            np.nan, 
            "Customer support was helpful.", 
            "Will buy again.", 
            np.nan, 
            "Not satisfied with packaging.", 
            "Excellent experience.",
            "Good value for money.", 
            np.nan, 
            "User interface is intuitive.", 
            np.nan, 
            "Highly recommended.", 
            "Needs improvement.", 
            np.nan, 
            "Quick response time.", 
            "Loved the design.", 
            np.nan
        ]
    }
    
    return pd.DataFrame(data)

def main():
    print("=" * 80)
    print("                      AM_FILLER LIBRARY LIVE DEMO")
    print("=" * 80)
    
    # 1. Load Data
    print("\n[STEP 1] Loading Dataset...")
    df = create_demo_dataset()
    print(f"Data Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # 2. Show Original Data (First 10 rows)
    print("\n[STEP 2] Original Data (First 10 rows with missing values):")
    print("-" * 80)
    print(df.head(10).to_string())
    print("-" * 80)
    
    # 3. Show Missing Values Summary BEFORE
    print("\n[STEP 3] Missing Values Count (Before Imputation):")
    print("-" * 40)
    print(df.isnull().sum())
    print("-" * 40)
    
    # 4. Initialize and Apply AM_Filler
    print("\n[STEP 4] Applying AM_Filler Library...")
    print("Running: AMFiller().fit_transform(df)")
    
    filler = AMFiller(verbose=True)
    df_clean = filler.fit_transform(df)
    
    # 5. Show Cleaned Data (First 10 rows)
    print("\n[STEP 5] Cleaned Data (First 10 rows):")
    print("-" * 80)
    print(df_clean.head(10).to_string())
    print("-" * 80)
    
    # 6. Show Final Verification
    print("\n[STEP 6] Final Verification:")
    remaining_missing = df_clean.isnull().sum().sum()
    if remaining_missing == 0:
        print("\n[OK] SUCCESS: All missing values have been filled!")
    else:
        print(f"\n[!] WARNING: {remaining_missing} missing values remain.")
        
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
