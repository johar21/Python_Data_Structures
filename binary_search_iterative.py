def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Update the left pointer
        else:
            right = mid - 1  # Update the right pointer

    return -1  # Element not found in the array

if __name__ =="__main__":
    # In binary search array should be sorted 
    arr=[1,3,5,40,10]
    arr.sort()
    print(arr)
    target=10
    
    result=binary_search(arr,target)
    if(result==-1):
        print("Element is not present in array")
    else: 
        print("Element in present",result)