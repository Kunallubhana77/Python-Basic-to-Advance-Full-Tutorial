# NumPy Introduction and Array Creation

import numpy as np

print("=" * 50)
print("WHAT IS NUMPY?")
print("=" * 50)

print("NumPy (Numerical Python) is a library for:")
print("  - Fast numerical computations")
print("  - Working with multi-dimensional arrays")
print("  - Mathematical and statistical operations")
print("  - Scientific computing")

print("\n" + "=" * 50)
print("CREATING NUMPY ARRAYS")
print("=" * 50)

# From Python list
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr1}")
print(f"Type: {type(arr1)}")
print(f"Data type: {arr1.dtype}")

# 2D Array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D Array:\n{arr2d}")
print(f"Shape: {arr2d.shape}")

# 3D Array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"\n3D Array:\n{arr3d}")
print(f"Shape: {arr3d.shape}")
print(f"Dimensions: {arr3d.ndim}")

print("\n" + "=" * 50)
print("ARRAY CREATION FUNCTIONS")
print("=" * 50)

# zeros - Array of zeros
zeros = np.zeros(5)
print(f"Zeros (1D): {zeros}")

zeros_2d = np.zeros((3, 4))
print(f"\nZeros (2D):\n{zeros_2d}")

# ones - Array of ones
ones = np.ones(5)
print(f"\nOnes (1D): {ones}")

ones_2d = np.ones((2, 3))
print(f"\nOnes (2D):\n{ones_2d}")

# full - Array with specific value
fives = np.full(5, 5)
print(f"\nFull (value=5): {fives}")

# arange - Similar to Python range
range_arr = np.arange(0, 10, 2)
print(f"\nArange (0 to 10, step 2): {range_arr}")

# linspace - Evenly spaced values
linspace_arr = np.linspace(0, 1, 5)
print(f"\nLinspace (0 to 1, 5 values): {linspace_arr}")

# eye - Identity matrix
identity = np.eye(3)
print(f"\nIdentity Matrix (3x3):\n{identity}")

# random arrays
random_arr = np.random.random(5)
print(f"\nRandom floats [0, 1): {random_arr}")

random_int = np.random.randint(1, 100, size=5)
print(f"Random integers [1, 100): {random_int}")

print("\n" + "=" * 50)
print("ARRAY ATTRIBUTES")
print("=" * 50)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"Array:\n{arr}")
print(f"\nShape: {arr.shape}")
print(f"Size (total elements): {arr.size}")
print(f"Dimensions: {arr.ndim}")
print(f"Data type: {arr.dtype}")
print(f"Item size (bytes): {arr.itemsize}")
print(f"Total bytes: {arr.nbytes}")

print("\n" + "=" * 50)
print("DATA TYPES IN NUMPY")
print("=" * 50)

# Integer array
int_arr = np.array([1, 2, 3], dtype=np.int32)
print(f"Int32 array: {int_arr}, dtype: {int_arr.dtype}")

# Float array
float_arr = np.array([1, 2, 3], dtype=np.float64)
print(f"Float64 array: {float_arr}, dtype: {float_arr.dtype}")

# Boolean array
bool_arr = np.array([True, False, True], dtype=bool)
print(f"Boolean array: {bool_arr}, dtype: {bool_arr.dtype}")

# String array
str_arr = np.array(['a', 'b', 'c'], dtype=str)
print(f"String array: {str_arr}, dtype: {str_arr.dtype}")

print("\n" + "=" * 50)
print("CONVERTING BETWEEN TYPES")
print("=" * 50)

# Float to int
float_arr = np.array([1.5, 2.7, 3.9])
int_converted = float_arr.astype(int)
print(f"Float: {float_arr}")
print(f"Converted to int: {int_converted}")

# Int to float
int_arr = np.array([1, 2, 3])
float_converted = int_arr.astype(float)
print(f"\nInt: {int_arr}")
print(f"Converted to float: {float_converted}")

print("\n" + "=" * 50)
print("COPYING ARRAYS")
print("=" * 50)

original = np.array([1, 2, 3, 4, 5])
print(f"Original: {original}")

# View (shares data)
view = original.view()
view[0] = 999
print(f"After modifying view: original={original}, view={view}")

# Copy (independent)
original = np.array([1, 2, 3, 4, 5])
copy = original.copy()
copy[0] = 999
print(f"After modifying copy: original={original}, copy={copy}")
