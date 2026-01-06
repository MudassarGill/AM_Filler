"""
AM_filler Basic Usage Example

This script demonstrates how to use AM_filler to automatically
fill missing values in a dataset with one line of code.
"""

import pandas as pd
import numpy as np

# Import AM_filler
from am_filler import AMFiller


def create_sample_dataframe():
    """Create a sample DataFrame with various missing values."""
    np.random.seed(42)
    
    # Create sample data
    data = {
        # Numeric column - approximately normal (should use mean)
        "age": [25, 30, np.nan, 35, 28, 32, np.nan, 29, 31, 27],
        
        # Numeric column - skewed with outliers (should use median)  
        "income": [50000, 55000, np.nan, 150000, 52000, np.nan, 48000, 500000, 51000, 53000],
        
        # Categorical column (should use mode)
        "city": ["New York", "London", np.nan, "Paris", "London", "London", np.nan, "Paris", "New York", np.nan],
        
        # Text/description column (should use predefined sentences)
        "description": [
            "Experienced professional in tech.",
            np.nan,
            "Entry-level candidate seeking opportunities.",
            "Senior manager with leadership skills.",
            np.nan,
            "Data scientist passionate about ML.",
            np.nan,
            "Software engineer with 5 years experience.",
            "Product manager focused on user needs.",
            np.nan,
        ],
        
        # Another numeric - normal distribution
        "score": [85.5, np.nan, 78.2, 92.1, 88.0, np.nan, 79.5, 84.3, 90.0, 86.7],
        
        # Categorical with unique mode
        "status": ["active", "active", "inactive", np.nan, "active", "pending", np.nan, "active", "active", "inactive"],
    }
    
    return pd.DataFrame(data)


def main():
    print("=" * 70)
    print("AM_FILLER DEMO - Automatic Missing Value Imputation")
    print("=" * 70)
    
    # Create sample data
    df = create_sample_dataframe()
    
    print("\n[ORIGINAL DATAFRAME]")
    print("-" * 70)
    print(df.to_string())
    
    print("\n\n[MISSING VALUES COUNT]")
    print("-" * 70)
    print(df.isnull().sum())
    
    # ========================================
    # ONE-LINE USAGE - The main API
    # ========================================
    print("\n\n[APPLYING AM_FILLER...]")
    df_clean = AMFiller().fit_transform(df)
    
    print("\n[CLEANED DATAFRAME]")
    print("-" * 70)
    print(df_clean.to_string())
    
    print("\n\n[MISSING VALUES AFTER CLEANING]")
    print("-" * 70)
    print(df_clean.isnull().sum())
    
    print("\n\n[SUCCESS] All missing values have been automatically filled!")
    print("=" * 70)


if __name__ == "__main__":
    main()
