def word_search(board, word):
    """
    Determines if the word exists in the 2D board by searching horizontally or vertically.
    
    :param board: 2D list of characters representing the grid.
    :param word: The word to be found.
    :return: True if the word exists in the board, otherwise False.
    """
    def dfs(i, j, idx):
        if idx == len(word):
            return True
        letter = word[idx]
        if letter != board[i][j]:
            return False
        board[i][j] = "*"
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        for dir in directions:
            next_x, next_y = i + dir[0], j + dir[1]
            if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != "*":
                if dfs(next_x, next_y, idx+1):
                    return True
        board[i][j] = letter
        return False


    for i in range(len(board)):
        for j in range(len(board[0])):
            if word[0] == board[i][j] and dfs(i, j, 0):
                return True
    return False




board = [
  ['A','B','C','E'],
  ['S','F','B','S'],
  ['A','D','E','E']
]
word = "ABCB"

ans = word_search(board, word)
print(ans)  # Expected Output: False
