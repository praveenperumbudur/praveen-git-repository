import numpy as np

'''
digits = np.array([
        [1,2,3], 
        [4,5,6],
        [7,8,9]
    ])
print(digits)
print(digits.shape) #size of an array
row_vector = digits[:,np.newaxis]
print("digits", row_vector)
col_vector = digits[np.newaxis:]
print("digits", col_vector)
'''
'''
CURVE_CENTER = 80
grades = np.array([72,35,64,88,51,90,74,12])
average = grades.mean();
print(average)
change = CURVE_CENTER - average
print(change)
def curves(grades):
    average = grades.mean();
    #print(average)
    change = CURVE_CENTER - average
    new_grades = grades + change #vectorization
    return np.clip(new_grades,grades,100)#broadcasting

print(curves(grades))

'''
'''
temperatures = np.array([29.3,42.2,18.8,16.1,38.0,12.5,12.6,49.5,38.6,
                         31.3,9.2,22.2]).reshape(2,2,3)
print(temperatures.shape)
print(temperatures)

print("*"*60)
print(np.swapaxes(temperatures,1,2))



batting_averages = np.array([
    [50,30,70,100],
    [20,60,90,70],
    [100,100,100,100],
    [40,30,20,0],
    ])
print("size of an array: ",batting_averages.shape)
print("Maximum average: ", batting_averages.max())
print("Maximum average column: ",batting_averages.max(axis=0))
print("Maximum average row: ",batting_averages.max(axis=1))

'''
'''
numbers = np.linspace(5,51,24,dtype=int).reshape(4,6)
print(numbers)

'''
'''
nums = np.arange(32).reshape(4,1,8)
print(nums)
nums_1 = np.arange(48).reshape(1,6,8)
print(nums_1)
print("*" * 60)
print(nums + nums_1)

'''
'''
arr1 = np.arange(10,100,5,dtype=int).reshape(3,6)
print(arr1)
print("*"  * 60)
print(arr1)
arr2 = np.arange(10,100,5,dtype=int).reshape(3,6)
print(arr2)
sum_of_2_arrays = arr1+arr2
print(sum_of_2_arrays)
product_of_2_arrays = arr1*arr2

print(product_of_2_arrays)
'''

square = np.array([
    [16,3,2,13],
    [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1]
    ])

"""for i in range(4):
   print(square[:,i].sum()==34)
   print(square[i,:].sum()==34)
"""

#print(square[:2,:2])
#print(square[2:,2:])

numbers = np.linspace(5,50,24,dtype="int").reshape(4,-1)
#print(numbers)
print("-"*60)
#mask = numbers%5==0 #vectorized boolean computation
#print(mask)

#filtering
#print("all the values divisible by 5 ", numbers[mask]) #converting a resultant array
#print("all the values divisible by 5 ", numbers[numbers%8==0])

print(numbers.T) #Transposing
print("Horizontal Sorting", np.sort(numbers,axis=0))
print("Vertical Sorting", np.sort(numbers,axis=0))

a= np.array([[4,8],[6,1]])
b= np.array([[3,5],[7,2]])

print(np.concatenate((b,a)))#merging two array
print(np.concatenate((b,a),axis=None))#merging two array and converting it into single
print(np.hstack((a,b)))#horizontal merging of 2 or more arrays
print(np.hstack((a,b)))#vertical merging of 2 or more arrays

stock_prices = np.random.random((30,10))
print("stock_prices")
print(stock_prices)










































      
