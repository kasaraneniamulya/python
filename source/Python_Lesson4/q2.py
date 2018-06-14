import numpy as np
arr = np.random.random((10,10)) #generating the random 10 X 10 array
print(arr)
print(np.min(arr,axis=1)) #finding minimum of each row
print(np.max(arr,axis=1)) #finding maximum of each row
#print(np.min(arr,axis=0))
#print(np.max(arr,axis=0))