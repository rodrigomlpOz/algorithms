def maze_solve(maze, e):
    def find_path(maze, x, y, e, path, visited):
        if not (0<=x<len(maze) and 0<=y<len(maze[0]) and (x,y) not in visited and maze[x][y] == 0):
            return False
        visited.add((x,y))
        path.append((x,y))
        if (x,y) == e:
            return True
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for dir in directions:
            if find_path(maze, x + dir[0], y + dir[1], e, path, visited):
                return True
        visited.remove((x,y))
        del path[-1]
        return False
    path = []
    find_path(maze, len(maze)-1, 0, e, path, set())
    print(path)

maze = [ [1,1,0,0],
         [0,1,1,0],
         [0,0,1,0],
         [0,0,0,0]]


maze_solve(maze, (0,len(maze[0])-1))