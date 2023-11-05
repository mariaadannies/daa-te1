def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  

def clustered_binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr[:i], key)  
        arr[j + 1:i + 1] = arr[j:i] 
        arr[j] = key  
    return arr


# Example usage:
a_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = clustered_binary_insertion_sort(a_list)
print(sorted_list)
