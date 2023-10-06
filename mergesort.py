def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input array in half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively apply merge_sort to both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Compare elements from both halves and add the smaller element to the result
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Add any remaining elements from both halves
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

# Example usage:
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
