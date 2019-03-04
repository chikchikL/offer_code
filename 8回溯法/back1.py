class Solution:
    # 已经包含在路径中的格子不能再次进入，但是当某个路径尝试在中途失败后，被回溯的部分可以重新访问
    # 用一个矩阵记录该格子是否已经在路径中，不能重复进入
    visited = []

    # 思路：从任意结点出发，递归判断是否有路径
    # 参数应该是二维数组，行数，列数，路径字符串
    # 递归
    def recur(self, matrix, rows, cols, path, i, j):
        # 匹配成功
        if path == '':
            return True

        # 递归匹配,向下递归的约束条件为：
        # 1.坐标在矩阵范围内 2.与剩余路径首个字符匹配 3.没有包含在已经匹配的路径内
        if (i < rows) and (i >= 0) and (j < cols) and (j >= 0) and (matrix[i][j] == path[0]) and (
                self.visited[i][j] == 0):
            # 向上下左右四个方向找下个路径点,找到一个就算成功，如果都没成功需要回溯
            print(matrix[i][j])
            self.visited[i][j] = 1

            # 这里不能这样分割字符串，因为可能有与path[0]重复的字符，总之慎用split！
            # path_split = path.split(path[0])
            path_remain = path[1:]

            result = self.recur(matrix, rows, cols, path_remain, i + 1, j) \
                     | self.recur(matrix, rows, cols, path_remain, i - 1, j) \
                     | self.recur(matrix, rows, cols, path_remain, i, j + 1) \
                     | self.recur(matrix, rows, cols, path_remain, i, j - 1)

            # 未匹配成功回溯
            if not result:
                self.visited[i][j] = 0

            return result
        return False

    def hasPath(self, matrix, rows, cols, path):
        # write code here

        i = 0
        j = 0

        # 将字符串转化为矩阵
        matrix = [list(matrix[r*cols:cols+r*cols]) for r in range(rows)]
        print(matrix)

        for i in range(rows):
            for j in range(cols):
                # 重置visited数组
                self.visited = [[0 for x in range(cols)] for y in range(rows)]
                # 每次路径判断从一个新的点开始
                if self.recur(matrix, rows, cols, path, i, j):
                    return True
        return False

# a b c e s f c s a d e e
# matrix = [['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']]
matrix = 'abcesfcsadee'
path = 'abcb'
s = Solution()
has_path = s.hasPath(matrix, 3, 4, path)
print(has_path)
