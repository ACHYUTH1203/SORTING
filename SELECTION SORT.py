#SELECTION SORT

arr=[12,21,321,32,34,68]

def selection_sort(arr):
    n=len(arr)
    
    for i in range(0,n-1):
        minimum=i
        for j in range (i,n):
            
            if arr[j]<arr[minimum]:
                minimum= j
            
        arr[i],arr[minimum]=arr[minimum],arr[i]
    return arr
            

a=selection_sort(arr)
print(a)