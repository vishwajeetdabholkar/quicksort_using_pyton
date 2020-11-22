def partition(arr,low,high):
    """
    This function takes last element as pivot, places 
    the pivot element at its correct position in sorted 
     array, and places all smaller (smaller than pivot) 
    to left of pivot and all greater elements to right 
    of pivot 
    """
    i = (low-1)
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] < pivot:            
            i = i+1
            arr[i], arr[j] = arr[j],arr[i]
            
    arr[i+1], arr[high] = arr[high],arr[i+1]
    return (i+1)
    
def quicksort(arr,low,high):
    """
    The main function that implements QuickSort 
    arr[] --> Array to be sorted, 
    low  --> Starting index, 
    high  --> Ending index 

    """

    if low < high :
        pi = partition(arr,low,high)
        
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
        
if __name__=='__main__':
    n = int(input("Enter number of elements :"))
    for i in range(0,n):
        print("Enter element for ",i,"location")
        x = int(input())
        arr.append(x)
    quicksort(arr,0,n-1)
    print(arr)
