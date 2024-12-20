def big_diff(arr):
    if len(arr) == 0:
        return 0  # No valid input for empty arrays

    # Initialize with the first element
    max_val = arr[0]
    min_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val - min_val
