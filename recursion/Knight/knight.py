'''
Given a N*N board with the Knight placed on the first block of an empty board. Moving according to the rules of chess knight must visit each square exactly once. Print the order of each cell in which they are visited.

Example:

Input : 
N = 8
Output:
0  59  38  33  30  17   8  63
37  34  31  60   9  62  29  16
58   1  36  39  32  27  18   7
35  48  41  26  61  10  15  28
42  57   2  49  40  23   6  19
47  50  45  54  25  20  11  14
56  43  52   3  22  13  24   5
51  46  55  44  53   4  21  12
'''
# Python3 program to solve Knight Tour problem using Backtracking

Cant solve this (too computationally intensive), but still interesting.

# Chessboard Size
def knight(n):
    board = [[-1 for i in range(n)] for _ in range(n)]
    def is_safe(board, x, y):
        if 0 <= x < n and 0 <= y < n and board[x][y] == -1:
            return True 
        else:
            return False
    
    def backtrack(board, curr_x, curr_y, position):
        dirs = [(-1, -2), (-2,-1), (1, -2), (2, -1), (-1, 2), (-2, 1), (1, 2), (2,1)]
        if position == ((n*n)):
            return True 
        else:
            for dir in dirs:
                x, y = dir 
                next_x, next_y = x + curr_x, y + curr_y
                if is_safe(board, next_x, next_y):
                    board[curr_x][curr_y] = position 
                    if backtrack(board, next_x, next_y, position + 1):
                        return True
                    board[curr_x][curr_y] = -1
            return False

# This code is contributed by AAKASH PAL
