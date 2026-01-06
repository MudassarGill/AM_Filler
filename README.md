# AM_filler

> **Automatic Missing Value Filler** - Fill missing values in datasets intelligently with one line of code.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Overview

AM_filler is a Python library that **automatically detects column types** and fills missing values using the **best strategy** — without any user configuration. It saves time and prepares datasets for ML/DL tasks in one line of code.

### Why AM_filler?

| Feature | sklearn/PyCaret | AM_filler |
|---------|-----------------|-----------|
| Choose imputation strategy | Manual | **Automatic** |
| Handle text columns | Limited | **Built-in** |
| Configuration required | Yes | **None** |
| One-line usage | No | **Yes** |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/AM_filler.git
cd AM_filler

# Install in development mode (recommended)
pip install -e .

# Or install with optional dependencies
pip install -e ".[dev]"      # Includes pytest for testing
pip install -e ".[ml]"       # Includes scikit-learn for ML imputation

# Build for PyPI distribution
pip install build
python -m build              # Creates wheel and sdist in dist/
```

### From PyPI (coming soon)
```bash
pip install am_filler
```

---

## ⚡ Quick Start

```python
from am_filler import AMFiller
import pandas as pd

# Your DataFrame with missing values
df = pd.read_csv("your_data.csv")

# One line to fill all missing values!
df_clean = AMFiller().fit_transform(df)
```

That's it! AM_filler automatically:
- Detects column types (numeric, categorical, text)
- Chooses the best imputation strategy
- Fills all missing values
- Logs what was done

---

## 🧠 How It Works

### Automatic Column Detection

| Column Type | Detection Method |
|-------------|------------------|
| **Numeric** | int, float dtypes |
| **Categorical** | object dtype with short values |
| **Text** | object dtype with sentence-like content |

### Smart Imputation Strategies

#### Numeric Columns
- **Skewness check**: Uses scipy to detect skewed distributions
- **Outlier detection**: IQR method to find outliers
- Uses **median** if skewed or has outliers (more robust)
- Uses **mean** if approximately normal

#### Categorical Columns
- Fills with **mode** (most frequent value)
- Falls back to random choice if no clear mode

#### Text Columns
- Detects sentence-like content
- Fills with **predefined meaningful sentences**
- Context-aware templates based on column name

---

## 📖 API Reference

### AMFiller Class

```python
from am_filler import AMFiller

# Initialize
filler = AMFiller(verbose=True)  # verbose=False to disable logging

# Fit and transform (one step)
df_clean = filler.fit_transform(df)

# Or separate steps
filler.fit(df)
df_clean = filler.transform(df)

# Get imputation strategies used
strategies = filler.get_strategies()
```

### Individual Functions

```python
from am_filler import detect_column_type, fill_numeric, fill_categorical, fill_text

# Detect column type
col_type = detect_column_type(df["column"])  # Returns: "numeric", "categorical", or "text"

# Fill specific column types
filled_series, strategy, value = fill_numeric(df["age"])
filled_series, strategy, value = fill_categorical(df["city"])
filled_series, strategy, sample = fill_text(df["description"])
```

---

## 📁 Project Structure

```
AM_filler/
├── am_filler/
│   ├── __init__.py      # Public API exports
│   ├── core.py          # Main AMFiller class
│   ├── numeric.py       # Numeric imputation (mean/median)
│   ├── categorical.py   # Categorical imputation (mode)
│   ├── text.py          # Text imputation (sentences)
│   └── utils.py         # Helper functions
├── examples/
│   └── basic_usage.py   # Demo script
├── tests/
│   └── test_am_filler.py
├── README.md
├── pyproject.toml       # Modern packaging config (PEP 517/518)
├── setup.py             # Legacy packaging support
├── requirements.txt
└── LICENSE
```

---

## 🧪 Running Tests

```bash
# Install test dependencies
pip install pytest

# Run all tests
pytest tests/ -v

# Run with coverage
pip install pytest-cov
pytest tests/ --cov=am_filler --cov-report=html
```

---

## 📊 Example Output

```
============================================================
AM_FILLER IMPUTATION SUMMARY
============================================================

📊 Column: 'age'
   Type: numeric
   Strategy: mean (approximately normal distribution)
   Fill Value: 29.6250

📊 Column: 'income'
   Type: numeric
   Strategy: median (skewed distribution with outliers)
   Fill Value: 52000.0000

📊 Column: 'city'
   Type: categorical
   Strategy: mode
   Fill Value: London

📊 Column: 'description'
   Type: text
   Strategy: predefined sentences (10 templates)
   Sample Fill: "Information not available."

============================================================
✅ Successfully filled 4 column(s)
============================================================
```

---

## 🔮 Future Enhancements

- [ ] ML-based imputation using scikit-learn (KNNImputer, IterativeImputer)
- [ ] Time series aware imputation
- [ ] Custom strategy configuration
- [ ] Integration with popular ML pipelines

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request