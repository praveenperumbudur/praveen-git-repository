import numpy as np

import numpy as np

#create identity matrix
im = np.eye(4)
print(im)
temparr = np.array([
    [31.8,36.4,11.5],
    [30.2,31.4,0]
    ])
temparri = temparr.astype('int')
temparrb = temparr.astype('bool')
    
print(temparrb)

print("*"*60)

list_of_numbers = [x for x in range(0,101,2)]
arr =np.array(list_of_numbers).reshape(17,3)
print(arr)

print("*"*60)

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,3,4,2,5])
print(np.where(arr1==arr2))

print("*"*60)

arr =np.full((2,3),5)
print(arr)

print("*"*60)

arr = np.array([
    [1,2,3],
    [4,5,5]
    ])
newarr = np.tile(arr,10)

print(newarr)

print("*"*60)

#print(np.random.seed(123))
randarr = np.random.randint(0,10,size=(5,5))
randnormal = np.random.normal(size=(5,5))

print(randarr)
print(randnormal)

print("*"*60)

array = np.array([10,1,5,2])
indexes = np.argsort(array)
print(indexes)

arr = np.array([
    [1,2,3],
    [4,5,5]
    ])
print(np.all(arr>4))

print("*"*60)
