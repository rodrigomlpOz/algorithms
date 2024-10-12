import collections
def fourSumCount(A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hash = collections.defaultdict(int)
        for i in A:
            for j in B:
                hash[i+j] += 1


        count = 0
        for i in C:
            for j in D:
                curr_sum = (i + j) * (-1)
                if hash[curr_sum] > 0:
                    count += hash[curr_sum]
        return count


# Example 1
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(fourSumCount(A, B, C, D))  # Output: 2

# Example 2
A = [0, 1, -1]
B = [-1, 1, 0]
C = [0, 0, 1]
D = [-1, 1, 1]
print(fourSumCount(A, B, C, D))  # Output: 17

# Example 3
A = [1, 2, 3]
B = [4, -2, -1]
C = [5, -1, 1]
D = [-3, -2, -1]
print(fourSumCount(A, B, C, D))  # Output: 6

# Example 4
A = [0]
B = [0]
C = [0]
D = [0]
print(fourSumCount(A, B, C, D))  # Output: 1
