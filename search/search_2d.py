'''
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
def search_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] >= target:
            col -= 1
        else:
            row += 1
    return False
    

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 30
search_matrix(matrix, target)
