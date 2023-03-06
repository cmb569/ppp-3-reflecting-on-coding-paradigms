def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)