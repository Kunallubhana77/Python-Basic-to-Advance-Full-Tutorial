# NumPy Array Reshaping

import numpy as np

print("=" * 50)
print("RESHAPE() - Change Array Shape")
print("=" * 50)

# 1D to 2D
arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Original 1D array: {arr}")
print(f"Shape: {arr.shape}")

reshaped = arr.reshape(2, 3)
print(f"\nReshaped to (2, 3):\n{reshaped}")

reshaped2 = arr.reshape(3, 2)
print(f"\nReshaped to (3, 2):\n{reshaped2}")

# 1D to 3D
arr = np.arange(24)
reshaped_3d = arr.reshape(2, 3, 4)
print(f"\n1D array reshaped to (2, 3, 4):")
print(reshaped_3d)

print("\n" + "=" * 50)
print("RESHAPE WITH -1 (Auto-calculate)")
print("=" * 50)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f"Array: {arr}")

# Auto-calculate columns
reshaped = arr.reshape(2, -1)  # -1 means "figure out this dimension"
print(f"\nReshape (2, -1) → Shape: {reshaped.shape}")
print(reshaped)

# Auto-calculate rows
reshaped = arr.reshape(-1, 4)
print(f"\nReshape (-1, 4) → Shape: {reshaped.shape}")
print(reshaped)

print("\n" + "=" * 50)
print("FLATTEN() vs RAVEL() - Convert to 1D")
print("=" * 50)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Matrix:\n{matrix}")

# flatten() - returns copy
flat1 = matrix.flatten()
print(f"\nFlatten: {flat1}")
flat1[0] = 999
print(f"Modified flatten: {flat1}")
print(f"Original matrix:\n{matrix}")  # Unchanged

# ravel() - returns view (if possible)
flat2 = matrix.ravel()
print(f"\nRavel: {flat2}")
flat2[0] = 888
print(f"Modified ravel: {flat2}")
print(f"Original matrix:\n{matrix}")  # Changed!

print("\n" + "=" * 50)
print("TRANSPOSE - Swap Rows and Columns")
print("=" * 50)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original (2x3):\n{matrix}")

transposed = matrix.T
print(f"\nTransposed (3x2):\n{transposed}")

# Or use transpose()
transposed2 = np.transpose(matrix)
print(f"\nUsing transpose():\n{transposed2}")

print("\n" + "=" * 50)
print("ADDING/REMOVING DIMENSIONS")
print("=" * 50)

arr = np.array([1, 2, 3, 4])
print(f"Original: {arr}, Shape: {arr.shape}")

# Add dimension using reshape
arr_2d = arr.reshape(1, -1)
print(f"\nRow vector: {arr_2d}, Shape: {arr_2d.shape}")

arr_2d = arr.reshape(-1, 1)
print(f"\nColumn vector:\n{arr_2d}")
print(f"Shape: {arr_2d.shape}")

# Using newaxis
row = arr[np.newaxis, :]
print(f"\nUsing newaxis (row): {row}, Shape: {row.shape}")

col = arr[:, np.newaxis]
print(f"\nUsing newaxis (column):\n{col}")
print(f"Shape: {col.shape}")

# expand_dims
expanded = np.expand_dims(arr, axis=0)
print(f"\nExpand dims (axis=0): {expanded}, Shape: {expanded.shape}")

expanded = np.expand_dims(arr, axis=1)
print(f"\nExpand dims (axis=1):\n{expanded}")
print(f"Shape: {expanded.shape}")

print("\n" + "=" * 50)
print("SQUEEZE - Remove Single-Dimensional Entries")
print("=" * 50)

arr = np.array([[[1], [2], [3]]])
print(f"Original shape: {arr.shape}")
print(f"Array:\n{arr}")

squeezed = np.squeeze(arr)
print(f"\nAfter squeeze: {squeezed}")
print(f"Shape: {squeezed.shape}")

print("\n" + "=" * 50)
print("CONCATENATE - Join Arrays")
print("=" * 50)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate 1D arrays
concat = np.concatenate([arr1, arr2])
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")
print(f"Concatenated: {concat}")

# Concatenate 2D arrays
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

print(f"\nmat1:\n{mat1}")
print(f"mat2:\n{mat2}")

# Along rows (axis=0)
concat_rows = np.concatenate([mat1, mat2], axis=0)
print(f"\nConcatenate along rows:\n{concat_rows}")

# Along columns (axis=1)
concat_cols = np.concatenate([mat1, mat2], axis=1)
print(f"\nConcatenate along columns:\n{concat_cols}")

print("\n" + "=" * 50)
print("STACK - Join Arrays Along New Axis")
print("=" * 50)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# vstack (vertical stack)
vstacked = np.vstack([arr1, arr2])
print(f"vstack:\n{vstacked}")

# hstack (horizontal stack)
hstacked = np.hstack([arr1, arr2])
print(f"\nhstack: {hstacked}")

# dstack (depth stack)
dstacked = np.dstack([arr1, arr2])
print(f"\ndstack shape: {dstacked.shape}")

# Generic stack
stacked = np.stack([arr1, arr2])
print(f"\nstack (axis=0):\n{stacked}")

stacked_axis1 = np.stack([arr1, arr2], axis=1)
print(f"\nstack (axis=1):\n{stacked_axis1}")

print("\n" + "=" * 50)
print("SPLIT - Split Array into Multiple Sub-arrays")
print("=" * 50)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"Array: {arr}")

# Split into 3 equal parts
split = np.split(arr, 3)
print(f"\nSplit into 3 parts: {split}")

# Split 2D array
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"\nMatrix:\n{matrix}")

# Split rows
row_split = np.split(matrix, 3, axis=0)
print(f"\nSplit rows:")
for i, part in enumerate(row_split):
    print(f"Part {i+1}:\n{part}")

# Split columns
col_split = np.split(matrix, 2, axis=1)
print(f"\nSplit columns:")
for i, part in enumerate(col_split):
    print(f"Part {i+1}:\n{part}")

print("\n" + "=" * 50)
print("RESIZE - Modify Array Size")
print("=" * 50)

arr = np.array([1, 2, 3, 4])
print(f"Original: {arr}")

# resize returns new array
resized = np.resize(arr, 6)
print(f"Resized to 6 elements: {resized}")  # Repeats elements

resized = np.resize(arr, 2)
print(f"Resized to 2 elements: {resized}")  # Truncates
