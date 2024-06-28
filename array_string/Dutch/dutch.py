'''
EPI 5.1
'''

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
    print(A)

A = [0, 1, 2, 0, 2, 1, 1]
index = 1
ans = dutch_flag_loop(A, index)
print(ans)
