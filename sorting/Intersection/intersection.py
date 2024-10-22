def intersection(arr1, arr2):
    ans = []
    if not arr1 or not arr2:  # Check for empty input lists
        return []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            # Add to the result only if it's not already in the answer list (to avoid duplicates)
            if not ans or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return ans

# Test Case
arr1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
arr2 = [5, 5, 6, 8, 8, 9, 10, 10]
ans = intersection(arr1, arr2)
print(ans)  # Expected Output: [5, 6, 8]
