'''
EPI 18.2
'''
def paint(maze, x, y):
    def paint_path(maze, x, y, color):
        if not (0<=x<len(maze) and 0<=y<len(maze[0]) and  maze[x][y] == color):
            return 
        maze[x][y] = 1 - color
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for dir in directions:
           paint_path(maze, x + dir[0], y + dir[1], color)
    color = maze[x][y]
    paint_path(maze, x, y, color)


maze = [ [1,1,0,0],
         [0,1,1,0],
         [0,0,1,0],
         [0,0,1,0]]


paint(maze, len(maze)-1, 0)
