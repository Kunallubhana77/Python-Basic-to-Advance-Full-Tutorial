# Pandas Introduction and Series

import pandas as pd
import numpy as np

print("=" * 50)
print("WHAT IS PANDAS?")
print("=" * 50)

print("Pandas is a library for:")
print("  - Data manipulation and analysis")
print("  - Working with structured data (tables)")
print("  - Reading/writing various file formats (CSV, Excel, JSON)")
print("  - Data cleaning and preparation")

print("\n" + "=" * 50)
print("PANDAS SERIES - 1D Labeled Array")
print("=" * 50)

# Create Series from list
series1 = pd.Series([10, 20, 30, 40, 50])
print("Series from list:")
print(series1)

# Series with custom index
series2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("\nSeries with custom index:")
print(series2)

# Series from dictionary
data_dict = {'apple': 10, 'banana': 15, 'cherry': 8}
series3 = pd.Series(data_dict)
print("\nSeries from dictionary:")
print(series3)

# Series with name
series4 = pd.Series([100, 200, 300], name='Sales')
print("\nSeries with name:")
print(series4)

print("\n" + "=" * 50)
print("ACCESSING SERIES ELEMENTS")
print("=" * 50)

fruits = pd.Series([10, 15, 8, 20], index=['apple', 'banana', 'cherry', 'mango'])
print("Fruits series:")
print(fruits)

# Access by index
print(f"\nAccess 'apple': {fruits['apple']}")
print(f"Access 'mango': {fruits['mango']}")

# Access by position
print(f"\nFirst element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")

# Multiple elements
print(f"\nFirst 2 elements:\n{fruits[:2]}")
print(f"\nElements at 'apple' and 'mango':\n{fruits[['apple', 'mango']]}")

print("\n" + "=" * 50)
print("SERIES OPERATIONS")
print("=" * 50)

prices = pd.Series([100, 200, 300, 400], index=['A', 'B', 'C', 'D'])
print("Prices:")
print(prices)

# Arithmetic operations
print(f"\nPrices + 50:\n{prices + 50}")
print(f"\nPrices * 1.1:\n{prices * 1.1}")

# Statistical operations
print(f"\nSum: {prices.sum()}")
print(f"Mean: {prices.mean()}")
print(f"Max: {prices.max()}")
print(f"Min: {prices.min()}")
print(f"Standard Deviation: {prices.std()}")

print("\n" + "=" * 50)
print("FILTERING SERIES")
print("=" * 50)

scores = pd.Series([85, 92, 78, 95, 88], index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
print("Scores:")
print(scores)

# Boolean filtering
high_scores = scores[scores > 85]
print(f"\nScores > 85:\n{high_scores}")

low_scores = scores[scores < 90]
print(f"\nScores < 90:\n{low_scores}")

# Range filtering
mid_range = scores[(scores >= 80) & (scores <= 90)]
print(f"\nScores between 80 and 90:\n{mid_range}")

print("\n" + "=" * 50)
print("SERIES METHODS")
print("=" * 50)

data = pd.Series([10, 20, 30, 20, 10, 40])
print("Data:")
print(data)

# Unique values
print(f"\nUnique values: {data.unique()}")
print(f"Number of unique: {data.nunique()}")

# Value counts
print(f"\nValue counts:\n{data.value_counts()}")

# Check for duplicates
print(f"\nHas duplicates: {data.duplicated().any()}")

# Sort values
print(f"\nSorted ascending:\n{data.sort_values()}")
print(f"\nSorted descending:\n{data.sort_values(ascending=False)}")

print("\n" + "=" * 50)
print("HANDLING MISSING VALUES")
print("=" * 50)

data_with_nan = pd.Series([10, np.nan, 30, np.nan, 50])
print("Data with NaN:")
print(data_with_nan)

# Check for null values
print(f"\nIs null:\n{data_with_nan.isnull()}")
print(f"Not null:\n{data_with_nan.notnull()}")

# Drop null values
cleaned = data_with_nan.dropna()
print(f"\nAfter dropna:\n{cleaned}")

# Fill null values
filled = data_with_nan.fillna(0)
print(f"\nFill NaN with 0:\n{filled}")

filled_mean = data_with_nan.fillna(data_with_nan.mean())
print(f"\nFill NaN with mean:\n{filled_mean}")

print("\n" + "=" * 50)
print("SERIES ATTRIBUTES")
print("=" * 50)

series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Series:")
print(series)

print(f"\nIndex: {series.index}")
print(f"Values: {series.values}")
print(f"Shape: {series.shape}")
print(f"Size: {series.size}")
print(f"Data type: {series.dtype}")
print(f"Name: {series.name}")

print("\n" + "=" * 50)
print("SERIES STRING OPERATIONS")
print("=" * 50)

names = pd.Series(['alice', 'bob', 'charlie', 'david'])
print("Names:")
print(names)

print(f"\nUppercase:\n{names.str.upper()}")
print(f"\nCapitalize:\n{names.str.capitalize()}")
print(f"\nLength:\n{names.str.len()}")
print(f"\nContains 'a':\n{names.str.contains('a')}")
print(f"\nStarts with 'b':\n{names.str.startswith('b')}")
