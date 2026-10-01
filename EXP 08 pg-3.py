import numpy as np
a = np.array([[10, 20, 30],
              [40, 50, 60]])
print("Array:",a)
# Array Properties
print("\n Array Properties")
print("Number of dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)
print("Data type:", a.dtype)
print("Item size:", a.itemsize)
# NumPy Functions
print("\n NumPy Functions")
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Standard deviation:", np.std(a))
# Reshape
print("\nReshaped Array:")
print(np.reshape(a, (3, 2)))
# Transpose 
print("\nTranspose:")
print(np.transpose(a))
# Sorting
print("\nSorted Array:")
print(np.sort(a))
