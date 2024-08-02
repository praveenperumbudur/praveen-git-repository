import numpy as np
'''
array = np.arange(30).reshape(6,5)
print (array)
print()

print(np.argmax(array))
print(np.argmax(array, axis=1))
# argmax: used to return the indices of the max elements
# elements of the given array along with the specified axis
print(np.argmax(array, axis=0))
'''

'''
array = np. array([

[3, 7, 1],

[10, 3, 2],

[5, 6, 7]

])

print (array)

print()

# Sort the whole array

print(np.sort(array, axis=None))

# Sort along each row

print(np. sort(array, axis=1))

# Sort along each column

print(np. sort(array, axis=0))

'''
'''
list = [

    np. array ([3, 2, 8, 9]),
    np. array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

result = []
for i in range(len(list)):
    result.append(np.mean(list[i]))
print(result)

'''
'''
array = np. array([

[3, 2, 8],

[4, 12, 34],

[23, 12, 67]

])

newRow = np.array([2, 1, 8])
newArray = np. vstack((array, newRow))
print (newArray)
'''
'''
array = np. array ([3, 6, 7, 2, 5, 1, 8]) 
reversedArray = np.flipud(array)
print (reversedArray)
'''

'''
matrix1 = [
    [3, 4, 2],
    [5, 1, 8],
    [3, 1, 9]
    ]

matrix2 = [
    [3, 7, 51],
    [2, 9, 8],
    [1, 5, 8]
    ]

result = np.dot(matrix1, matrix2)
print(result)

'''
n = 8

# Create a nxn matrix filled with 0
matrix = np.zeros((n,n), dtype=int)

# f111 1 with alternate rows and column
matrix[::2, 1::2] = 1
matrix[1::2, ::2] = 1

# Print the checkerboard pattern
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

'''
