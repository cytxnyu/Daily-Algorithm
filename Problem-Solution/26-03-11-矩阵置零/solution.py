from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        m , n = len(matrix) , len(matrix[0])
        row , col = [False] * m , [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix
#第一次遍历用来标记,只要是0所在的行和列都标记为True, 第二次的遍历只要行和列有一个为True
#就把这哥位置变为0
s = Solution()
matrix = [[1,2,3],[3,0,5],[1,9,0]]
print(s.setZeroes(matrix))

class Solutio:
    def setZeroes(self, matrix:List[List[int]]) -> None:
        m , n = len(matrix) , len(matrix[0])
        flag_col0 = False

        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n ):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m - 1 , -1 , -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0

w = Solutio()
matrix2 = [[222,0,0],[1,8,0],[2,4,67]]
w.setZeroes(matrix2)
print(matrix2)