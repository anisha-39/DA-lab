import numpy as np 
# Create a sample NumPy array 
array = np.array([[1, 2, 3], [4, 5, 6]]) 
# Display the NumPy array 
print("Array:") 
print(array) 
# Basic characteristics of the NumPy array 
print("\nArray Characteristics:") 
print(f"Shape: {array.shape}")  # Shape of the array 
print(f"Size: {array.size}")    # Total number of elements in the array 
print(f"Dimensions: {array.ndim}")  # Number of dimensions 
print(f"Data Type: {array.dtype}")  # Data type of elements 
print(f"Item Size: {array.itemsize} bytes")  # Memory size of one array element 
print(f"Total Memory: {array.nbytes} bytes")  # Total memory consumed by the array 
