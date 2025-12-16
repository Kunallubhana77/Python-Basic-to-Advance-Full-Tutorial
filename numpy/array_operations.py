# NumPy Array Operations

import numpy as np

print("=" * 50)
print("ARITHMETIC OPERATIONS")
print("=" * 50)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print(f"arr1: {arr1}")
print(f"arr2: {arr2}")

# Element-wise operations
print(f"\nAddition: {arr1 + arr2}")
print(f"Subtraction: {arr2 - arr1}")
print(f"Multiplication: {arr1 * arr2}")
print(f"Division: {arr2 / arr1}")
print(f"Power: {arr1 ** 2}")
print(f"Modulus: {arr2 % arr1}")

# Operations with scalar
print(f"\narr1 + 10: {arr1 + 10}")
print(f"arr1 * 3: {arr1 * 3}")
print(f"arr1 ** 2: {arr1 ** 2}")

print("\n" + "=" * 50)
print("UNIVERSAL FUNCTIONS (ufuncs)")
print("=" * 50)

arr = np.array([1, 4, 9, 16, 25])
print(f"Array: {arr}")

print(f"\nSquare root: {np.sqrt(arr)}")
print(f"Exponential: {np.exp(arr[:3])}")  # First 3 elements
print(f"Natural log: {np.log(arr)}")
print(f"Log base 10: {np.log10(arr)}")

# Trigonometric functions
angles = np.array([0, 30, 45, 60, 90])
radians = np.deg2rad(angles)
print(f"\nAngles (degrees): {angles}")
print(f"Sin: {np.sin(radians)}")
print(f"Cos: {np.cos(radians)}")

# Rounding
decimals = np.array([1.234, 2.567, 3.891])
print(f"\nDecimals: {decimals}")
print(f"Round: {np.round(decimals)}")
print(f"Floor: {np.floor(decimals)}")
print(f"Ceil: {np.ceil(decimals)}")

print("\n" + "=" * 50)
print("STATISTICAL OPERATIONS")
print("=" * 50)

data = np.array([10, 20, 30, 40, 50])
print(f"Data: {data}")

print(f"\nSum: {np.sum(data)}")
print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Standard Deviation: {np.std(data)}")
print(f"Variance: {np.var(data)}")
print(f"Min: {np.min(data)}")
print(f"Max: {np.max(data)}")

# Index of min/max
print(f"\nIndex of min: {np.argmin(data)}")
print(f"Index of max: {np.argmax(data)}")

# Cumulative operations
print(f"\nCumulative sum: {np.cumsum(data)}")
print(f"Cumulative product: {np.cumprod([1, 2, 3, 4])}")

print("\n" + "=" * 50)
print("OPERATIONS ON 2D ARRAYS")
print("=" * 50)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matrix:\n{matrix}")

print(f"\nSum of all elements: {np.sum(matrix)}")
print(f"Sum along axis 0 (columns): {np.sum(matrix, axis=0)}")
print(f"Sum along axis 1 (rows): {np.sum(matrix, axis=1)}")

print(f"\nMean: {np.mean(matrix)}")
print(f"Mean along columns: {np.mean(matrix, axis=0)}")
print(f"Mean along rows: {np.mean(matrix, axis=1)}")

print("\n" + "=" * 50)
print("COMPARISON OPERATIONS")
print("=" * 50)

arr = np.array([10, 20, 30, 40, 50])
print(f"Array: {arr}")

print(f"\nGreater than 25: {arr > 25}")
print(f"Equal to 30: {arr == 30}")
print(f"Not equal to 20: {arr != 20}")

# Logical operations
print(f"\nBetween 20 and 40: {np.logical_and(arr >= 20, arr <= 40)}")
print(f"Less than 15 or greater than 45: {np.logical_or(arr < 15, arr > 45)}")

print("\n" + "=" * 50)
print("ARRAY FILTERING")
print("=" * 50)

arr = np.array([10, 25, 30, 15, 45, 20])
print(f"Array: {arr}")

# Boolean indexing
filtered = arr[arr > 20]
print(f"\nValues > 20: {filtered}")

# Multiple conditions
filtered_multi = arr[(arr > 15) & (arr < 40)]
print(f"Values between 15 and 40: {filtered_multi}")

print("\n" + "=" * 50)
print("DOT PRODUCT AND MATRIX MULTIPLICATION")
print("=" * 50)

# Dot product (1D)
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
dot_product = np.dot(vec1, vec2)
print(f"vec1: {vec1}")
print(f"vec2: {vec2}")
print(f"Dot product: {dot_product}")  # 1*4 + 2*5 + 3*6 = 32

# Matrix multiplication (2D)
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
print(f"\nmat1:\n{mat1}")
print(f"mat2:\n{mat2}")
print(f"Matrix multiplication:\n{np.matmul(mat1, mat2)}")
# Or use @ operator
print(f"Using @ operator:\n{mat1 @ mat2}")

print("\n" + "=" * 50)
print("BROADCASTING")
print("=" * 50)

# Scalar broadcasting
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original:\n{arr}")
print(f"\nAdd scalar 10:\n{arr + 10}")

# 1D array broadcasting
row = np.array([10, 20, 30])
print(f"\nAdd row {row}:\n{arr + row}")

column = np.array([[10], [20]])
print(f"\nAdd column:\n{arr + column}")
