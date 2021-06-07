#leetcode problem 79
def word_search(board, word):
    def dfs(board, word, x, y):
        if not word:
            return True
        if board[x][y] != word[0]:
            return False
        board[x][y] = "*"
        directions = [(0, 1), (1, 0), (0, -1), (-1,0)]
        for dir_x, dir_y in directions:
            next_x, next_y = x + dir_x, y + dir_y
            if next_x >= 0 and next_x < len(board) and next_y >= 0 and next_y < len(board[0]) and dfs(board, word[1:], next_x, next_y):
                return True
        board[x][y] = word[0]
        return False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j):
                return True
    return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"

ans = word_search(board, word)
print(ans)
