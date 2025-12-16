# NumPy Array Indexing and Slicing

import numpy as np

print("=" * 50)
print("1D ARRAY INDEXING")
print("=" * 50)

arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(f"Array: {arr}")

# Positive indexing
print(f"\nFirst element (index 0): {arr[0]}")
print(f"Third element (index 2): {arr[2]}")
print(f"Last element (index -1): {arr[-1]}")

# Negative indexing
print(f"\nSecond last element: {arr[-2]}")

print("\n" + "=" * 50)
print("1D ARRAY SLICING")
print("=" * 50)

print(f"Array: {arr}")

# Basic slicing
print(f"\nElements from index 1 to 4: {arr[1:5]}")
print(f"First 3 elements: {arr[:3]}")
print(f"From index 3 to end: {arr[3:]}")
print(f"Every 2nd element: {arr[::2]}")
print(f"Reverse array: {arr[::-1]}")

# Step slicing
print(f"\nElements from 1 to 6 with step 2: {arr[1:6:2]}")

print("\n" + "=" * 50)
print("2D ARRAY INDEXING")
print("=" * 50)

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print(f"Matrix:\n{matrix}")

# Access specific element
print(f"\nElement at (0, 0): {matrix[0, 0]}")
print(f"Element at (1, 2): {matrix[1, 2]}")
print(f"Element at (2, 3): {matrix[2, 3]}")

# Access entire row
print(f"\nFirst row: {matrix[0]}")
print(f"Second row: {matrix[1]}")

# Access entire column
print(f"\nFirst column: {matrix[:, 0]}")
print(f"Third column: {matrix[:, 2]}")

print("\n" + "=" * 50)
print("2D ARRAY SLICING")
print("=" * 50)

print(f"Matrix:\n{matrix}")

# Slice rows and columns
print(f"\nFirst 2 rows:\n{matrix[:2]}")
print(f"\nFirst 2 rows, first 2 columns:\n{matrix[:2, :2]}")
print(f"\nAll rows, columns 1-3:\n{matrix[:, 1:4]}")
print(f"\nRows 1-2, columns 2-3:\n{matrix[1:3, 2:4]}")

# Every other element
print(f"\nEvery other row:\n{matrix[::2]}")
print(f"\nEvery other column:\n{matrix[:, ::2]}")

print("\n" + "=" * 50)
print("BOOLEAN INDEXING")
print("=" * 50)

arr = np.array([10, 25, 30, 15, 45, 20])
print(f"Array: {arr}")

# Create boolean mask
mask = arr > 20
print(f"\nMask (arr > 20): {mask}")
print(f"Filtered values: {arr[mask]}")

# Direct boolean indexing
print(f"\nValues > 20: {arr[arr > 20]}")
print(f"Values <= 25: {arr[arr <= 25]}")

# Multiple conditions
print(f"\nValues between 15 and 35: {arr[(arr > 15) & (arr < 35)]}")
print(f"Values < 15 or > 40: {arr[(arr < 15) | (arr > 40)]}")

print("\n" + "=" * 50)
print("FANCY INDEXING (Index Arrays)")
print("=" * 50)

arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(f"Array: {arr}")

# Using array of indices
indices = [0, 2, 4]
print(f"\nElements at indices {indices}: {arr[indices]}")

# Multiple fancy indexing
indices = [6, 1, 3, 1]
print(f"Elements at indices {indices}: {arr[indices]}")

# 2D fancy indexing
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"\nMatrix:\n{matrix}")

rows = [0, 1, 2]
cols = [2, 1, 0]
print(f"Elements at (0,2), (1,1), (2,0): {matrix[rows, cols]}")

print("\n" + "=" * 50)
print("MODIFYING ARRAYS USING INDEXING")
print("=" * 50)

arr = np.array([10, 20, 30, 40, 50])
print(f"Original: {arr}")

# Modify single element
arr[0] = 100
print(f"After arr[0] = 100: {arr}")

# Modify slice
arr[1:4] = 0
print(f"After arr[1:4] = 0: {arr}")

# Modify using boolean indexing
arr = np.array([10, 20, 30, 40, 50])
arr[arr > 25] = 99
print(f"After setting values > 25 to 99: {arr}")

print("\n" + "=" * 50)
print("3D ARRAY INDEXING")
print("=" * 50)

arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])

print(f"3D Array:\n{arr_3d}")
print(f"Shape: {arr_3d.shape}")

# Access elements
print(f"\nElement at [0, 0, 0]: {arr_3d[0, 0, 0]}")
print(f"Element at [1, 1, 1]: {arr_3d[1, 1, 1]}")

# Access sub-arrays
print(f"\nFirst 2D array:\n{arr_3d[0]}")
print(f"Last row of second 2D array: {arr_3d[1, 1]}")

print("\n" + "=" * 50)
print("CONDITIONAL REPLACEMENT")
print("=" * 50)

arr = np.array([10, 25, 30, 15, 45, 20])
print(f"Original: {arr}")

# Replace all values > 20 with 100
arr_copy = arr.copy()
arr_copy[arr_copy > 20] = 100
print(f"Replace > 20 with 100: {arr_copy}")

# np.where
arr = np.array([10, 25, 30, 15, 45, 20])
result = np.where(arr > 20, "High", "Low")
print(f"\nUsing np.where: {result}")

# Numerical where
result_num = np.where(arr > 20, arr, 0)
print(f"Keep if > 20, else 0: {result_num}")

print("\n" + "=" * 50)
print("EXTRACTING DIAGONAL")
print("=" * 50)

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"Matrix:\n{matrix}")

diagonal = np.diag(matrix)
print(f"\nMain diagonal: {diagonal}")

# Upper and lower triangles
print(f"\nUpper triangle:\n{np.triu(matrix)}")
print(f"\nLower triangle:\n{np.tril(matrix)}")
