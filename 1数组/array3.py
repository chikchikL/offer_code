# 二维数组查找指定数字，横竖方向都是递增的
# 思路：每个待查找矩阵右上角开始找，记为m，若小于m，排除此列，若大于m，排除此行
# 每次到新的右上角判断m是否为指定数字，直到左下角后截止

def find(tar, arr):
    # 初始行列为右上角
    x = 0
    y = len(arr[0]) - 1
    # 最大行数
    row = len(arr)

    while True:
        m = arr[x][y]
        if m == tar:
            print('下标',x, y)
            return True
        elif tar > m:
            # 去除行,需要判断是否超出行
            if x < row - 1:
                x = x + 1
            else:
                return False
        elif tar < m:
            # 去除列,需要判断是否超出列
            if y > 0:
                y = y - 1
            else:
                return False


# 输入行数
m = int(input())
# 初始化数组list,range从0开始且小于m
grid = [[] for i in range(m)]
for i in range(m):
    # 空格分隔输入元素
    line = input().split(' ')
    for j in range(len(line)):
        grid[i].append(int(line[j]))

if find(16, grid):
    print('找到了嗷')
else:
    print('没找到嗷')
