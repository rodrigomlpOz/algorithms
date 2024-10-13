'''
GAME OF LIFE
https://leetcode.com/problems/game-of-life/
'''

DEAD = 0
ALIVE = 1
ALIVE_TO_DEAD = 2
DEAD_TO_ALIVE = 3
def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    def count_neighbours(grid, i , j):
        count = 0
        directions = [(-1,1), (-1,0), (-1,-1), (1,1), (1, 0), (1,-1), (0,1), (0,-1)]
        for dir in directions:
            next_x, next_y = i + dir[0], j + dir[1]
            if next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]) and grid[next_x][next_y] in (ALIVE, ALIVE_TO_DEAD):
                count += 1
        return count
    for row in range(len(board)):
        for col in range(len(board[0])):
            curr_count = count_neighbours(board, row, col)
            if board[row][col] == ALIVE and not (curr_count == 2 or curr_count == 3):
                board[row][col] = ALIVE_TO_DEAD
            if board[row][col] == DEAD and curr_count == 3:
                board[row][col] = DEAD_TO_ALIVE

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ALIVE_TO_DEAD:
                board[row][col] = 0
            if board[row][col] == DEAD_TO_ALIVE:
                board[row][col] = 1
