"""
Accepted
数独的意思是每一行每一列每一个九宫格的数字都不重复
"""


def func(board):
    if not board:
        return False
    # three 2d array to check each row, col and sub box
    check_row = [[False for i in range(9)] for j in range(9)]
    check_col = [[False for i in range(9)] for j in range(9)]
    check_box = [[False for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                num = int(board[i][j]) - 1  # need -1 because the index of array is 0~8
                k = i // 3 * 3 + j // 3  # k表示第几个九宫格
                # because if previously the same number of same row,col or box have exist, it is false
                if check_row[i][num] or check_col[j][num] or check_box[k][num]:
                    return False
                # assign value to all the checking 2d arrayes
                check_row[i][num] = check_col[j][num] = check_box[k][num] = True
    return True


if __name__ == "__main__":
    board = [
        [".", "8", "7", "6", "5", "4", "3", "2", "1"],
        ["2", ".", ".", ".", ".", ".", ".", ".", "."],
        ["3", ".", ".", ".", ".", ".", ".", ".", "."],
        ["4", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", ".", "."],
        ["6", ".", ".", ".", ".", ".", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        ["8", ".", ".", ".", ".", ".", ".", ".", "."],
        ["9", ".", ".", ".", ".", ".", ".", ".", "."]
    ]
    print(func(board))
