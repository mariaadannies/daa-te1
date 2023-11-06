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
---------------------------------------------------
### Penjelasan Algoritma Clustered Binary Insertion Sort

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

---------------------------------------------------
### Contoh Penerapan Algoritma Clustered Binary Insertion Sort

Input = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

Iteration 1:
    Key: 1
    Binary Search: [1]
    Swap: [1, 3]
    Result: [1, 3, 4, 1, 5, 9, 2, 6, 5, 3, 5]
Iteration 2:
    Key: 4
    Binary Search: [1, 3, 4]
    Swap: [1, 3, 1, 4]
    Result: [1, 1, 3, 4, 5, 9, 2, 6, 5, 3, 5]
Iteration 3:
    Key: 1
    Binary Search: [1, 1, 3, 4]
    Swap: [1, 1, 3, 4]
    Result: [1, 1, 3, 4, 5, 9, 2, 6, 5, 3, 5]
Iteration 4:
    Key: 5
    Binary Search: [1, 1, 3, 4, 5]
    Swap: [1, 1, 3, 4, 5]
    Result: [1, 1, 3, 4, 5, 9, 2, 6, 5, 3, 5]
Iteration 5:
    Key: 9
    Binary Search: [1, 1, 3, 4, 5, 9]
    Swap: [1, 1, 3, 4, 5, 9]
    Result: [1, 1, 3, 4, 5, 9, 2, 6, 5, 3, 5]
Iteration 6:
    Key: 2
    Binary Search: [1, 1, 3, 4, 5, 9, 2]
    Swap: [1, 1, 2, 3, 4, 5, 9]
    Result: [1, 1, 2, 3, 4, 5, 9, 6, 5, 3, 5]
Iteration 7:
    Key: 6
    Binary Search: [1, 1, 2, 3, 4, 5, 9, 6]
    Swap: [1, 1, 2, 3, 4, 5, 6, 9]
    Result: [1, 1, 2, 3, 4, 5, 6, 9, 5, 3, 5]
Iteration 8:
    Key: 5
    Binary Search: [1, 1, 2, 3, 4, 5, 6, 9, 5]
    Swap: [1, 1, 2, 3, 4, 5, 5, 6, 9]
    Result: [1, 1, 2, 3, 4, 5, 5, 6, 9, 3, 5]
Iteration 9:
    Key: 3
    Binary Search: [1, 1, 2, 3, 4, 5, 5, 6, 9, 3]
    Swap: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    Result: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9, 5]
Iteration 10:
    Key: 5
    Binary Search: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9, 5]
    Swap: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    Result: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

'''
