import random

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot_index = random_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

def random_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
   
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
randomized_quick_sort(arr, 0, len(arr) - 1)
print(arr)
