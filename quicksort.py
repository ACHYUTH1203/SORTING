arr=[11,312,212,43,21,56,78]
def quicksort(arr,low,high):
    if(low<high):
        partition=partitionfunc(arr,low,high)
        
        quicksort(arr,low,partition-1)
        quicksort(arr,partition+1,high)

def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    
    while(i<j):
        while(arr[i]<pivot and i<high):

            i+=1
        while(arr[j]>pivot and j>low):
            j+=1
        if (i<j):
            arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j
quicksort(arr,0,len(arr)-1)
print(arr)
