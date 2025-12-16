# Pandas DataFrame Basics

import pandas as pd
import numpy as np

print("=" * 50)
print("CREATING DATAFRAMES")
print("=" * 50)

# From dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai']
}
df1 = pd.DataFrame(data_dict)
print("DataFrame from dictionary:")
print(df1)

# From list of lists
data_list = [
    ['Alice', 25, 'Mumbai'],
    ['Bob', 30, 'Delhi'],
    ['Charlie', 35, 'Bangalore']
]
df2 = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print("\nDataFrame from list:")
print(df2)

# From NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print("\nDataFrame from NumPy array:")
print(df3)

print("\n" + "=" * 50)
print("DATAFRAME ATTRIBUTES")
print("=" * 50)

students = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [20, 21, 22, 20, 23],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [85, 78, 92, 70, 88]
})

print("Students DataFrame:")
print(students)

print(f"\nShape: {students.shape}")
print(f"Size: {students.size}")
print(f"Columns: {students.columns.tolist()}")
print(f"Index: {students.index.tolist()}")
print(f"\nData types:\n{students.dtypes}")

print("\n" + "=" * 50)
print("VIEWING DATA")
print("=" * 50)

print("First 3 rows:")
print(students.head(3))

print("\nLast 2 rows:")
print(students.tail(2))

print("\nInfo:")
print(students.info())

print("\nDescribe (statistics):")
print(students.describe())

print("\n" + "=" * 50)
print("SELECTING COLUMNS")
print("=" * 50)

# Single column (returns Series)
names = students['Name']
print("Name column (Series):")
print(names)
print(f"Type: {type(names)}")

# Single column (returns DataFrame)
names_df = students[['Name']]
print("\nName column (DataFrame):")
print(names_df)
print(f"Type: {type(names_df)}")

# Multiple columns
subset = students[['Name', 'Marks']]
print("\nName and Marks:")
print(subset)

print("\n" + "=" * 50)
print("SELECTING ROWS")
print("=" * 50)

# By position using iloc
print("First row:")
print(students.iloc[0])

print("\nFirst 3 rows:")
print(students.iloc[:3])

print("\nRows 1 to 3:")
print(students.iloc[1:4])

# By label using loc
students_indexed = students.set_index('Name')
print("\nDataFrame with Name as index:")
print(students_indexed)

print("\nAccess 'Bob' row:")
print(students_indexed.loc['Bob'])

print("\n" + "=" * 50)
print("SELECTING ROWS AND COLUMNS")
print("=" * 50)

# iloc[rows, columns]
print("First 2 rows, first 2 columns:")
print(students.iloc[:2, :2])

print("\nRows 1-3, columns 'Name' and 'Marks':")
print(students.loc[1:3, ['Name', 'Marks']])

print("\n" + "=" * 50)
print("FILTERING ROWS")
print("=" * 50)

print("Students with marks > 80:")
high_marks = students[students['Marks'] > 80]
print(high_marks)

print("\nStudents with grade 'A':")
grade_a = students[students['Grade'] == 'A']
print(grade_a)

print("\nStudents age 20 or marks > 85:")
filtered = students[(students['Age'] == 20) | (students['Marks'] > 85)]
print(filtered)

print("\n" + "=" * 50)
print("ADDING/MODIFYING COLUMNS")
print("=" * 50)

# Add new column
students['Passed'] = students['Marks'] >= 75
print("Added 'Passed' column:")
print(students)

# Modify column
students['Marks'] = students['Marks'] + 5
print("\nAdded 5 marks to everyone:")
print(students[['Name', 'Marks']])

# Add calculated column
students['Grade_Points'] = students['Marks'] / 10
print("\nAdded Grade_Points:")
print(students[['Name', 'Marks', 'Grade_Points']])

print("\n" + "=" * 50)
print("DELETING COLUMNS/ROWS")
print("=" * 50)

# Drop column
df_copy = students.copy()
df_dropped = df_copy.drop('Grade_Points', axis=1)
print("After dropping 'Grade_Points':")
print(df_dropped.columns.tolist())

# Drop multiple columns
df_dropped2 = students.drop(['Passed', 'Grade_Points'], axis=1)
print("\nAfter dropping multiple columns:")
print(df_dropped2.columns.tolist())

# Drop row by index
df_no_first = students.drop(0, axis=0)
print("\nAfter dropping first row:")
print(df_no_first)

print("\n" + "=" * 50)
print("SORTING")
print("=" * 50)

# Sort by column
sorted_marks = students.sort_values('Marks')
print("Sorted by Marks (ascending):")
print(sorted_marks[['Name', 'Marks']])

sorted_marks_desc = students.sort_values('Marks', ascending=False)
print("\nSorted by Marks (descending):")
print(sorted_marks_desc[['Name', 'Marks']])

# Sort by multiple columns
sorted_multi = students.sort_values(['Age', 'Marks'])
print("\nSorted by Age, then Marks:")
print(sorted_multi[['Name', 'Age', 'Marks']])

print("\n" + "=" * 50)
print("RESET INDEX")
print("=" * 50)

sorted_df = students.sort_values('Marks', ascending=False)
print("Before reset:")
print(sorted_df)

reset_df = sorted_df.reset_index(drop=True)
print("\nAfter reset_index:")
print(reset_df)
