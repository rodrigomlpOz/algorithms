def dutch(A, index):
    val = A[index]
    less = 0
    equal = 0
    more = len(A)

    while equal < more:
        if A[equal] < val:
            A[less], A[equal] = A[equal], A[less]
            less += 1
            equal += 1
        elif A[equal] > val:
            more -= 1
            A[equal], A[more] = A[more], A[equal]
        else:
            equal += 1
    return A

A1 = [0, 1, 2, 0, 2, 1, 1]
index1 = 1
print(dutch(A1, index1))  # Output: [0, 0, 1, 1, 1, 2, 2]

A2 = [3, 3, 2, 1, 3, 2, 1]
index2 = 2
print(dutch(A2, index2))  # Output: [1, 1, 2, 3, 3, 3, 2]

A3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
index3 = 6
print(dutch(A3, index3))  # Output: [1, 1, 2, 3, 3, 4, 5, 9, 5, 6, 5]
