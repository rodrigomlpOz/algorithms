'''
EPI 5.2
'''

def plus_one(A):
    remainder = 1
    for i in reversed(range(1, len(A))):
        A[i] += remainder
        remainder = A[i] // 10
        A[i] = A[i] % 10
    A[0] += remainder
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    print(A)

A = [8,9,9]
plus_one(A)
