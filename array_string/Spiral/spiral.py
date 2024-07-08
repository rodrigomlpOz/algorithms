'''
EPI 5.18
'''

def spiral(matrix):
    directions = [(0,1), (1,0), (0,-1), [-1,0]]
    if not matrix:
        return []
    x, y = 0, 0
    curr_dir = 0
    ans = []
    num_of_spots = len(matrix)*len(matrix[0])

    for _ in range(num_of_spots):
        ans.append(matrix[x][y])
        matrix[x][y] = float('-inf')

        print(matrix)
        next_x, next_y = x + directions[curr_dir][0], y + directions[curr_dir][1]
        if next_x != len(matrix) and next_y != len(matrix[0]) and matrix[next_x][next_y] != float('-inf'):
            x, y = next_x, next_y
        else:
            curr_dir = (curr_dir + 1) % 4
            next_x, next_y = x + directions[curr_dir][0], y + directions[curr_dir][1]
            x, y = next_x, next_y
    return ans

        

A = [[1,2,3],[4,5,6],[7,8,9]]
