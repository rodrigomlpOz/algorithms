def intersection(A, m, B, n):
    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1


        
    


arr1 = [5,13,17,0, 0, 0, 0, 0]
arr2 = [3,7,11,19]
ans = intersection(arr1, 3, arr2, 4)
print(ans)