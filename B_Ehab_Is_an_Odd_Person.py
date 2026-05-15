from functools import cmp_to_key
def quicksort_custom(a, low=0, high=None):
    if high is None:
        high = len(a) - 1
        
    if low < high:
        # p_idx is the final position of the pivot
        p_idx = partition(a, low, high)
        
        # Recursively sort elements before and after partition
        quicksort_custom(a, low, p_idx - 1)
        quicksort_custom(a, p_idx + 1, high)

def partition(a, low, high):
    pivot = a[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        # Rule 1: It must want to move to the left (ascending sort)
        # Rule 2: The sum of the moving element and pivot must be ODD
        if a[j] < pivot and (a[j] + pivot) % 2 == 1:
            i += 1
            a[i], a[j] = a[j], a[i]
            
    # Swap the pivot into its correct place if the sum condition allows it
    if (a[i + 1] + a[high]) % 2 == 1:
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1
        
    return high

size=int(input())
a=list(map(int,input().split()))
quicksort_custom(a)
print(*a)