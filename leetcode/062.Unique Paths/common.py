"""
Accepted
题目意思是一个m*n矩阵，从左上角到右下角有多少种走法（唯一）
先设每一个点的走法只有1，然后从左上角开始遍历，到右下角
因为走法只能从上到下或者从左到右，所以在加法的时候只考虑上面的点和左边的点的走法数
两个相加就是左上角那个点到这个点的走法数
"""


def func(m, n):
    result = [[1 for x in range(n)] for y in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            result[i][j] = result[i - 1][j] + result[i][j - 1]
    return result[-1][-1]


if __name__ == "__main__":
    m = 3
    n = 3
    print(func(m, n))
