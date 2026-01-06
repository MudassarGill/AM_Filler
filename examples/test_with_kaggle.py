"""
Test AM_Filler with Your Kaggle Dataset

HOW TO USE:
1. Download any CSV file from Kaggle (with missing values)
2. Put the CSV file in the 'examples' folder (or anywhere you like)
3. Update the CSV_PATH below to point to your file
4. Run: python examples/test_with_kaggle.py
"""

import pandas as pd
from am_filler import AMFiller

# ===============================================
# CHANGE THIS PATH TO YOUR KAGGLE CSV FILE
# ===============================================
CSV_PATH = "your_kaggle_file.csv"  # <-- Put your file path here!

# Example paths:
# CSV_PATH = "titanic.csv"
# CSV_PATH = "C:/Users/LAPTOPS HUB/Downloads/house-prices.csv"


def test_with_kaggle_data():
    print("=" * 70)
    print("AM_FILLER - Testing with Your Kaggle Dataset")
    print("=" * 70)
    
    # Load your CSV
    print(f"\n[1] Loading data from: {CSV_PATH}")
    try:
        df = pd.read_csv(CSV_PATH)
    except FileNotFoundError:
        print(f"\n❌ ERROR: File not found!")
        print(f"   Please update CSV_PATH in this script to point to your Kaggle file.")
        print(f"\n   Steps:")
        print(f"   1. Download a CSV from Kaggle")
        print(f"   2. Edit line 17 in this file: CSV_PATH = 'your_file.csv'")
        return
    
    print(f"    ✓ Loaded {len(df)} rows, {len(df.columns)} columns")
    
    # Show original data info
    print(f"\n[2] Dataset Overview:")
    print("-" * 70)
    print(f"    Columns: {list(df.columns)}")
    print(f"\n    First 5 rows:")
    print(df.head().to_string())
    
    # Show missing values
    print(f"\n[3] Missing Values BEFORE:")
    print("-" * 70)
    missing = df.isnull().sum()
    missing_cols = missing[missing > 0]
    if len(missing_cols) == 0:
        print("    No missing values found! Your dataset is already complete.")
        return
    
    print(missing_cols)
    print(f"\n    Total missing: {df.isnull().sum().sum()} values")
    
    # Apply AM_Filler
    print(f"\n[4] Applying AM_Filler...")
    print("-" * 70)
    filler = AMFiller(verbose=True)
    df_clean = filler.fit_transform(df)
    
    # Show results
    print(f"\n[5] Missing Values AFTER:")
    print("-" * 70)
    print(df_clean.isnull().sum()[df_clean.isnull().sum() >= 0])
    print(f"\n    Total missing: {df_clean.isnull().sum().sum()} values")
    
    # Show cleaned data
    print(f"\n[6] Cleaned Data (First 5 rows):")
    print("-" * 70)
    print(df_clean.head().to_string())
    
    # Save cleaned data
    output_path = CSV_PATH.replace(".csv", "_cleaned.csv")
    df_clean.to_csv(output_path, index=False)
    print(f"\n[7] ✓ Saved cleaned data to: {output_path}")
    
    print("\n" + "=" * 70)
    print("SUCCESS! Your data has been cleaned with AM_Filler!")
    print("=" * 70)


if __name__ == "__main__":
    test_with_kaggle_data()
