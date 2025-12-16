import numpy as np

a = np.array([10, 20, 30, 40, 50])
print(a[1:4])


#Multi-dimensional Arrays

b = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(b[1, 2])
#for row and column
print(b[1, :])
print(b[:, 2])



# two different array

a = np.array([[1,2,3],
            [4,5,6]])
b = np.array([[1,2,3],
            [4,5,6]])
print(a+b)
print(a*b)
print(np.sqrt(a))


#for mathematical functions
arr = np.array([10, 20, 30, 40, 50])
print(np.mean(arr))
print(np.std(arr))
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))


#manupulate array

c = np.array([1, 2, 3, 4, 5, 6])
print(c.reshape(3, 2))
print(c.flatten())

#concatenate arrays
d = np.array([7, 8, 9])
print(np.concatenate((c, d)))



print(np.random.rand(2, 3))
print(np.random.randint(0, 10, size=(2, 3)))


d = np.array([[1, 2],
             [3, 4]])

e = np.array([[5, 6],
             [7, 8]])

print(np.dot(d, e))
print(np.linalg.inv(d))             
