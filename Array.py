#declare an array
arr =[1,3,4,5]

#print value at index value 3
print(arr[3])

print("\n")

import array

#array of array

arr1 = array.array('i', [1, 2, 3])

#print(arr1)

arr1.append(4)

for i in range (len(arr1)):
    print(arr1[i], end=" ")

print("\n")
    
arr1.insert(2,6)

for j in range (len(arr1)):
    print(arr1[j] ,end=" ")