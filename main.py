# Merge Sort
def merge(arr, l, m, r):
    left_arr = arr[l:m + 1]
    right_arr = arr[m + 1:r + 1]
    i = 0
    j = 0
    k = l
    m = len(left_arr)
    n = len(right_arr)
    while i < m and j < n:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i = i + 1
            k = k + 1
        else:
            arr[k] = right_arr[j]
            j = j + 1
            k = k + 1

    while i < m:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if r > l:
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)


if __name__ == '__main__':
    lst = [10, 5, 30, 15, 7]
    mergeSort(lst, 0, len(lst) - 1)
    print(lst)
