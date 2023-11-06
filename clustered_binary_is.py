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

'''
Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

- Inisialisasi (line 25)
a_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

- Iterasi (line 16-20)
Iterasi setiap elemen pada array dari elemen kedua sampai elemen terakhir.
Pada setiap iterasi, elemen yang sedang diiterasi disimpan pada variabel key.

- Binary search (Pemanggilan fungsi binary search: line 18, Fungsi Binary Search: line 1-13)
Pada setiap iterasi, dilakukan binary search pada elemen yang sedang diiterasi
untuk mencari posisi yang tepat untuk memasukkan elemen yang sedang diiterasi.

- Shifting (line 19)
Setelah posisi yang tepat ditemukan, dilakukan shifting elemen-elemen yang
berada pada posisi yang tepat ke kanan sebanyak satu kali.

- Insertion (line 20)
Setelah dilakukan shifting, elemen yang sedang diiterasi dimasukkan ke posisi yang tepat.

'''
