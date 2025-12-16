# Pandas Data Cleaning

import pandas as pd
import numpy as np

print("=" * 50)
print("HANDLING MISSING DATA")
print("=" * 50)

# Create DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eve'],
    'Age': [25, 30, np.nan, 28, 35],
    'City': ['Mumbai', None, 'Bangalore', 'Delhi', 'Mumbai'],
    'Salary': [50000, 60000, 55000, np.nan, 70000]
}
df = pd.DataFrame(data)
print("DataFrame with missing values:")
print(df)

print("\n" + "=" * 50)
print("DETECTING MISSING VALUES")
print("=" * 50)

# Check for null values
print("Is null:")
print(df.isnull())

print("\nNull count per column:")
print(df.isnull().sum())

print("\nTotal null values:")
print(df.isnull().sum().sum())

# Check for non-null values
print("\nNot null:")
print(df.notnull())

print("\n" + "=" * 50)
print("REMOVING MISSING VALUES")
print("=" * 50)

# Drop rows with any null values
df_dropped = df.dropna()
print("After dropna() - any null:")
print(df_dropped)

# Drop rows only if all values are null
df_all_null = df.dropna(how='all')
print("\nAfter dropna(how='all'):")
print(df_all_null)

# Drop columns with null values
df_drop_cols = df.dropna(axis=1)
print("\nAfter dropping columns with null:")
print(df_drop_cols)

# Drop rows with null in specific columns
df_subset = df.dropna(subset=['Name', 'City'])
print("\nDrop rows with null in Name or City:")
print(df_subset)

print("\n" + "=" * 50)
print("FILLING MISSING VALUES")
print("=" * 50)

# Fill with specific value
df_filled = df.fillna(0)
print("Fill NaN with 0:")
print(df_filled)

# Fill with different values for each column
df_filled_dict = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),
    'City': 'Unknown',
    'Salary': df['Salary'].median()
})
print("\nFill with different values:")
print(df_filled_dict)

# Forward fill (use previous value)
df_ffill = df.fillna(method='ffill')
print("\nForward fill:")
print(df_ffill)

# Backward fill (use next value)
df_bfill = df.fillna(method='bfill')
print("\nBackward fill:")
print(df_bfill)

print("\n" + "=" * 50)
print("HANDLING DUPLICATES")
print("=" * 50)

# Create DataFrame with duplicates
data_dup = {
    'Name': ['Alice', 'Bob', 'Alice', 'David', 'Bob'],
    'Age': [25, 30, 25, 28, 30],
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi']
}
df_dup = pd.DataFrame(data_dup)
print("DataFrame with duplicates:")
print(df_dup)

# Check for duplicates
print(f"\nDuplicated rows:\n{df_dup.duplicated()}")
print(f"\nNumber of duplicates: {df_dup.duplicated().sum()}")

# Show duplicate rows
print("\nActual duplicate rows:")
print(df_dup[df_dup.duplicated()])

# Drop duplicates
df_unique = df_dup.drop_duplicates()
print("\nAfter dropping duplicates:")
print(df_unique)

# Drop duplicates based on specific columns
df_unique_name = df_dup.drop_duplicates(subset=['Name'])
print("\nDrop duplicates based on Name:")
print(df_unique_name)

# Keep last occurrence instead of first
df_keep_last = df_dup.drop_duplicates(keep='last')
print("\nKeep last occurrence:")
print(df_keep_last)

print("\n" + "=" * 50)
print("DATA TYPE CONVERSION")
print("=" * 50)

data_types = {
    'Numbers': ['100', '200', '300'],
    'Prices': ['10.5', '20.3', '15.8'],
    'Active': ['True', 'False', 'True']
}
df_types = pd.DataFrame(data_types)
print("Original DataFrame:")
print(df_types)
print(f"\nData types:\n{df_types.dtypes}")

# Convert to numeric
df_types['Numbers'] = pd.to_numeric(df_types['Numbers'])
df_types['Prices'] = pd.to_numeric(df_types['Prices'])
print("\nAfter conversion:")
print(f"Data types:\n{df_types.dtypes}")

# Convert to boolean
df_types['Active'] = df_types['Active'].map({'True': True, 'False': False})
print(f"\nActive column:\n{df_types['Active']}")

print("\n" + "=" * 50)
print("REPLACING VALUES")
print("=" * 50)

data_replace = {
    'Product': ['A', 'B', 'C', 'A', 'B'],
    'Status': ['pending', 'complete', 'pending', 'failed', 'complete']
}
df_replace = pd.DataFrame(data_replace)
print("Original:")
print(df_replace)

# Replace single value
df_replaced = df_replace.copy()
df_replaced['Status'] = df_replaced['Status'].replace('pending', 'in_progress')
print("\nReplace 'pending' with 'in_progress':")
print(df_replaced)

# Replace multiple values
df_multi = df_replace.copy()
df_multi['Status'] = df_multi['Status'].replace({
    'pending': 'waiting',
    'complete': 'done',
    'failed': 'error'
})
print("\nReplace multiple values:")
print(df_multi)

print("\n" + "=" * 50)
print("REMOVING WHITESPACE")
print("=" * 50)

data_space = {
    'Name': ['  Alice', 'Bob  ', '  Charlie  '],
    'City': ['Mumbai  ', '  Delhi', 'Bangalore']
}
df_space = pd.DataFrame(data_space)
print("With whitespace:")
print(df_space)

# Strip whitespace
df_stripped = df_space.copy()
df_stripped['Name'] = df_stripped['Name'].str.strip()
df_stripped['City'] = df_stripped['City'].str.strip()
print("\nAfter strip:")
print(df_stripped)

print("\n" + "=" * 50)
print("RENAMING COLUMNS")
print("=" * 50)

df_rename = pd.DataFrame({
    'old_name': [1, 2, 3],
    'OLD_AGE': [25, 30, 35],
    'CiTy': ['A', 'B', 'C']
})
print("Original columns:")
print(df_rename.columns.tolist())

# Rename specific columns
df_renamed = df_rename.rename(columns={
    'old_name': 'Name',
    'OLD_AGE': 'Age',
    'CiTy': 'City'
})
print("\nRenamed columns:")
print(df_renamed.columns.tolist())

# Rename all columns to lowercase
df_lower = df_rename.copy()
df_lower.columns = df_lower.columns.str.lower()
print("\nAll lowercase:")
print(df_lower.columns.tolist())
