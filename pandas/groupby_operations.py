# Pandas GroupBy Operations

import pandas as pd
import numpy as np

print("=" * 50)
print("WHAT IS GROUPBY?")
print("=" * 50)

print("GroupBy allows you to:")
print("  - Split data into groups based on criteria")
print("  - Apply a function to each group")
print("  - Combine results into a data structure")

print("\n" + "=" * 50)
print("BASIC GROUPBY")
print("=" * 50)

# Sample sales data
sales = pd.DataFrame({
    'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C'],
    'Region': ['North', 'North', 'South', 'South', 'North', 'South', 'North', 'South'],
    'Sales': [100, 150, 120, 180, 110, 160, 90, 95],
    'Quantity': [10, 15, 12, 18, 11, 16, 9, 10]
})

print("Sales data:")
print(sales)

# Group by single column
grouped = sales.groupby('Product')
print("\nGrouped by Product:")
print(grouped.sum())

print("\n" + "=" * 50)
print("AGGREGATE FUNCTIONS")
print("=" * 50)

# Different aggregations
print("Sum by Product:")
print(sales.groupby('Product')['Sales'].sum())

print("\nMean by Product:")
print(sales.groupby('Product')['Sales'].mean())

print("\nCount by Product:")
print(sales.groupby('Product').size())

print("\nMax sales by Product:")
print(sales.groupby('Product')['Sales'].max())

print("\nMin sales by Product:")
print(sales.groupby('Product')['Sales'].min())

print("\n" + "=" * 50)
print("MULTIPLE COLUMN GROUPING")
print("=" * 50)

# Group by multiple columns
multi_group = sales.groupby(['Product', 'Region'])['Sales'].sum()
print("Sum of Sales by Product and Region:")
print(multi_group)

# Convert to DataFrame
print("\nAs DataFrame:")
print(multi_group.reset_index())

print("\n" + "=" * 50)
print("MULTIPLE AGGREGATIONS")
print("=" * 50)

# Apply multiple functions
agg_multiple = sales.groupby('Product').agg({
    'Sales': ['sum', 'mean', 'max'],
    'Quantity': ['sum', 'mean']
})
print("Multiple aggregations:")
print(agg_multiple)

# Custom aggregations with agg()
custom_agg = sales.groupby('Region').agg({
    'Sales': ['sum', 'mean', lambda x: x.max() - x.min()],
    'Quantity': 'sum'
})
print("\nCustom aggregations:")
print(custom_agg)

print("\n" + "=" * 50)
print("FILTERING GROUPS")
print("=" * 50)

# Filter groups where total sales > 200
filtered = sales.groupby('Product').filter(lambda x: x['Sales'].sum() > 200)
print("Products with total sales > 200:")
print(filtered)

print("\n" + "=" * 50)
print("TRANSFORM")
print("=" * 50)

# Add group statistics as new columns
sales['Total_by_Product'] = sales.groupby('Product')['Sales'].transform('sum')
sales['Mean_by_Product'] = sales.groupby('Product')['Sales'].transform('mean')

print("With group statistics:")
print(sales[['Product', 'Sales', 'Total_by_Product', 'Mean_by_Product']])

print("\n" + "=" * 50)
print("ITERATING THROUGH GROUPS")
print("=" * 50)

for name, group in sales.groupby('Product'):
    print(f"\nProduct: {name}")
    print(group[['Region', 'Sales']])

print("\n" + "=" * 50)
print("PIVOT TABLE")
print("=" * 50)

# Create pivot table
pivot = sales.pivot_table(
    values='Sales',
    index='Product',
    columns='Region',
    aggfunc='sum',
    fill_value=0
)
print("Pivot table (Sales by Product and Region):")
print(pivot)

# Multiple aggregations in pivot
pivot_multi = sales.pivot_table(
    values='Sales',
    index='Product',
    columns='Region',
    aggfunc=['sum', 'mean'],
    fill_value=0
)
print("\nPivot with multiple aggregations:")
print(pivot_multi)

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: Employee Data")
print("=" * 50)

employees = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [70000, 50000, 75000, 80000, 55000, 72000],
    'Experience': [5, 3, 6, 8, 4, 5]
})

print("Employee data:")
print(employees)

# Department-wise statistics
dept_stats = employees.groupby('Department').agg({
    'Salary': ['mean', 'min', 'max'],
    'Experience': 'mean',
    'Name': 'count'
})
dept_stats.columns = ['Avg_Salary', 'Min_Salary', 'Max_Salary', 'Avg_Experience', 'Employee_Count']

print("\nDepartment-wise statistics:")
print(dept_stats)

# Find highest paid employee per department
highest_paid = employees.loc[employees.groupby('Department')['Salary'].idxmax()]
print("\nHighest paid employee per department:")
print(highest_paid[['Name', 'Department', 'Salary']])

print("\n" + "=" * 50)
print("CUMULATIVE OPERATIONS")
print("=" * 50)

# Add cumulative sum within each group
sales['Cumulative_Sales'] = sales.groupby('Product')['Sales'].cumsum()
print("With cumulative sales:")
print(sales[['Product', 'Sales', 'Cumulative_Sales']])

# Rank within groups
sales['Sales_Rank'] = sales.groupby('Product')['Sales'].rank(ascending=False)
print("\nWith sales rank:")
print(sales[['Product', 'Sales', 'Sales_Rank']])
