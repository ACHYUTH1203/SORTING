def bubblesort(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[4,2,3,11,32,42]              
p=print(bubblesort(arr))
