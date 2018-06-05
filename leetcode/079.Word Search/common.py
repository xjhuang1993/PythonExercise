"""
Accepted
"""


def func(board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False


# check whether can find word, start at (i,j) position
def dfs(board, i, j, word):
    if len(word) == 0:  # all the characters are checked
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:  # 这个判断word[0] != board[i][j]放在这里很牛逼
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit again
    # check whether can find "word" along one direction
    res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(func(board, word))
