"""
AM_Filler Skewed Data Verification
Tests if the library correctly switches to Median strategy for skewed data.
"""

import pandas as pd
import numpy as np
import sys
import os

# Ensure we can import the local package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from am_filler import AMFiller

def test_distribution_handling():
    print("=" * 80)
    print("TEST: DISTRIBUTION HANDLING (NORMAL vs SKEWED)")
    print("=" * 80)
    
    np.random.seed(42)
    
    # 1. Create Data
    # Normal Distribution (e.g. Height in cm)
    normal_data = np.random.normal(170, 10, 1000)
    
    # Skewed Distribution (e.g. House Prices - lots of cheap, few super expensive)
    # Using Lognormal distribution to simulate heavy skew
    skewed_data = np.random.lognormal(mean=10.0, sigma=1.0, size=1000)
    
    # Add outliers to make it extra skewed
    skewed_data[0] = 100000000  # Huge outlier
    
    df = pd.DataFrame({
        "Height_Normal": normal_data,
        "Price_Skewed": skewed_data
    })
    
    # Add missing values
    df.loc[0:4, "Height_Normal"] = np.nan
    df.loc[0:4, "Price_Skewed"] = np.nan
    
    # Calculate expected values manually
    mean_height = df["Height_Normal"].mean()
    median_price = df["Price_Skewed"].median()
    mean_price = df["Price_Skewed"].mean()
    
    print("\n[DATA STATISTICS]")
    print(f"Height (Normal) -> Mean: {mean_height:.2f}, Median: {df['Height_Normal'].median():.2f}")
    print(f"Price  (Skewed) -> Mean: {mean_price:.2f}, Median: {median_price:.2f}")
    print(f"Difference in Price Mean vs Median: {abs(mean_price - median_price):.2f}")
    
    # 2. Run AM_Filler
    print("\n[RUNNING AM_FILLER]")
    filler = AMFiller(verbose=True)
    df_clean = filler.fit_transform(df)
    
    # 3. Verify Strategy
    print("\n[VERIFYING RESULTS]")
    print("-" * 50)
    
    # Check Height (Should use Mean)
    filled_height = df_clean.loc[0, "Height_Normal"]
    print(f"Column 'Height_Normal':")
    print(f"  - Filled Value: {filled_height:.4f}")
    print(f"  - Expected Mean: {mean_height:.4f}")
    if abs(filled_height - mean_height) < 0.01:
        print("  ✅ CORRECT: Used Mean strategy (Normal Distribution)")
    else:
        print("  ❌ INCORRECT: Did not use Mean")
        
    print("-" * 50)
        
    # Check Price (Should use Median)
    filled_price = df_clean.loc[0, "Price_Skewed"]
    print(f"Column 'Price_Skewed':")
    print(f"  - Filled Value: {filled_price:.4f}")
    print(f"  - Expected Median: {median_price:.4f}")
    print(f"  - (Mean would be: {mean_price:.4f})")
    
    if abs(filled_price - median_price) < 0.01:
        print("  ✅ CORRECT: Used Median strategy (Skewed Distribution)")
    elif abs(filled_price - mean_price) < 0.01:
        print("  ❌ INCORRECT: Used Mean implementation (Failed to detect skewness)")
    else:
         print("  ❌ INCORRECT: Used unknown value")
         
    print("=" * 80)

if __name__ == "__main__":
    test_distribution_handling()
