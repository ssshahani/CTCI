# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 22:53:16 2018

@author: Sahil S
"""

# Increasing Sorted Array rotated Unknown Times. Find X

def search(arr, left, right, x):
    mid = int((left+right)/2)
    if(arr[mid] == x):
        return mid
        
    if(right < left):
        return -1
        
    if(arr[left] < arr[mid]):  #Left is normal
        if(x >= arr[left] and x < arr[mid]):
            return search(arr, left, mid - 1, x)
        else:
            return search(arr, mid + 1, right, x)
    elif(arr[left] > arr[mid]): #Right is normal
        if(x > arr[mid] and x <= arr[right]):
            return search(arr, mid + 1, right, x)
        else:
            return search(arr, left, mid - 1, x)
    elif (arr[mid] == arr[left]):
        if(arr[mid] != arr[right]):
            return search(arr, mid+1, right, x)
        else:
            result = search(arr, left, mid-1, x) 
            if( result == -1):
                return search(arr, mid+1, right, x)
            else:
                return result
    return -1
    
arr = [15,16,19,20,25,1,3,4,5,7,10,14]
outputIndex = search(arr, 0, 11, 5)
print(outputIndex)