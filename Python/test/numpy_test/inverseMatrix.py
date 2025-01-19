import numpy as np

arr1 = np.array([[1, 3], [5, 7]])
arr2 = np.array([[1,2,3],[0,1,4],[5,6,0]])

det = np.linalg.det(arr2)
arr_inv = np.linalg.inv(arr2)

print("delta=%s"%det)
print(arr_inv)
