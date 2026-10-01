import numpy as np
a = np.array([[10, 20, 30],
              [40, 50, 60]])
print("Saved array:",a)
# Saving the array 
np.save("myarray.npy", a)
print("Array saved successfully.")
# Loading the array 
b = np.load("myarray.npy")
print("Loaded array:",b)
