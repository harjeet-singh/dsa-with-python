def mergeSort(arr: list, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    temp = [None for _ in range(end - start + 1)]

    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1

    # update original array inplace
    for i in range(start, end + 1):
        arr[i] = temp[i - start]


input_arr = [3, 2, -1, 0, 23, 5, 6]
start_index = 0
end_index = 6
mergeSort(input_arr, start_index, end_index)
print(input_arr)
