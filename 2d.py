import numpy as np 
array_1d = np.array([23, 1, 45, 34, 7, 15, 92, 5]) 
print("Original 1D Array:", array_1d) 
sorted_1d = np.sort(array_1d) 
print("Sorted 1D Array:", sorted_1d)  
array_2d = np.array([[34, 23, 5], [12, 92, 7], [45, 1, 15]]) 
print("\nOriginal 2D Array:\n", array_2d)  
sorted_2d_row = np.sort(array_2d, axis=1) 
print("\n2D Array Sorted Along Rows:\n", sorted_2d_row) 
sorted_2d_col = np.sort(array_2d, axis=0) 
print("\n2D Array Sorted Along Columns:\n", sorted_2d_col) 
data = np.array( 
[ 
], 
(3, "apple"), 
(1, "banana"), 
(2, "cherry"), 
dtype=[("id", int), ("name", "U10")], 
)  
sorted_by_id = np.sort(data, order="id") 
print("\nStructured Array Sorted by 'id':\n", sorted_by_id)  
sorted_by_name = np.sort(data, order="name") 
print("\nStructured Array Sorted by 'name':\n", sorted_by_name)  
print("\nOriginal 1D Array for argsort:", array_1d) 
indices = np.argsort(array_1d) 
print("Indices of Sorted Array:", indices) 
sorted_using_indices = array_1d[indices] 
print("Array Sorted Using Indices:", sorted_using_indices)