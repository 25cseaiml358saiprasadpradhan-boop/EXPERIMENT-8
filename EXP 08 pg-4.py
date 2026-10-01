import numpy as np
a = np.array([[10, 20, 30],
              [40, 50, 60]])
print("Array:",a)
# Statistical Operations
print("Statistical Operations")
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))
# Statistical operations along rows and columns
print("Sum of each column:", np.sum(a, axis=0))
print("Sum of each row:", np.sum(a, axis=1))
print("Mean of each column:", np.mean(a, axis=0))
print("Mean of each row:", np.mean(a, axis=1))
# Broadcasting
print(" Broadcasting")
b = a + 5
print("Array + 5:",b)
c = a * 2
print("Array * 2:",c)
d = np.array([1, 2, 3])
e = a + d
print("Array + [1, 2, 3]:",e)
