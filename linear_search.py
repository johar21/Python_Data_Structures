# code to linear search a value in array

def linear_search(arr,N,x):
    
    for i in range(0,N):
        if (arr[i]==x):
            return i
    return -1

if __name__ =="__main__":
    arr=[1,3,5,10,40]
    x=40
    N=len(arr)
    
    result=linear_search(arr,N,x)
    if(result==-1):
        print("Element is not present in array")
    else: 
        print("Element in present",result)

#Time complexity is O(n) for worst case
#Time complexity is O(1) for best case