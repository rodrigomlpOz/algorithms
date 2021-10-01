#https://leetcode.com/problems/surrounded-regions/
def paint(maze, x, y):
    def explore(maze, x, y):
        if not (0<=x<len(maze) and 0<=y<len(maze[0]) and maze[x][y] == "O"):
            return
        maze[x][y] = "S"
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for dir in directions:
           explore(maze, x + dir[0], y + dir[1])
    
    num_rows, num_cols = len(maze), len(maze[0])
    for i in range(num_rows):
        if maze[i][0] == "O":
            explore(maze, i, 0)
        if maze[i][num_cols-1] == "O":
            explore(maze, i, num_cols-1)
    for j in range(num_cols):
        if maze[0][j] == "O":
            explore(maze, 0, j)
        if maze[num_rows-1][j] == "O":
            explore(maze, num_rows-1,j)

    for i in range(num_rows):
        for j in range(num_cols):
            if maze[i][j] == "O":
                maze[i][j] = "X"
    for i in range(num_rows):
        for j in range(num_cols):
            if maze[i][j] == "S":
                maze[i][j] = "O"
    print("hello")

maze = [ ["X", "X", "X", "X"],
         ["X", "O", "X", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "O", "X"]]


paint(maze, len(maze)-1, 0)
