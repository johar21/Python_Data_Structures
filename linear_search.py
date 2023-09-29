# code to linear search a value in array
"""
    The above code implements a linear search algorithm to find a given value in an array and returns
    the index of the value if found, otherwise returns -1.
    
    :param arr: The array in which we want to search for the value
    :param N: The variable `N` represents the length of the array `arr`. It is calculated using the
    `len()` function, which returns the number of elements in the array
    :param x: The value you want to search for in the array
    :return: The linear_search function returns the index of the element if it is found in the array,
    and -1 if the element is not present in the array.
    """


def linear_search(arr, N, x):
    for i in range(0, N):
        if arr[i] == x:
            return i
    return -1

    if __name__ == "__main__":
        arr = [1, 3, 5, 10, 40]
        x = 40
    # `N=len(arr)` is calculating the length of the array `arr` and assigning it to the variable `N`.
    N = len(arr)

    result = linear_search(arr, N, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element in present", result)


# Time complexity is O(n) for worst case
# Time complexity is O(1) for best case qq
