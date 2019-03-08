# 将数组奇偶数分割且保持初始相对位置不变
# 思路: 遍历一遍数组，统计奇数个数，在辅助数组中用两个索引分别指向奇数开头和偶数开头，
# 遍历一遍原数组，逐个添加
def func(arr):
    # 输入判断
    if (arr is None) | (len(arr) == 0):
        return None
    # 记录奇数个数
    c_odd = 0
    for x in arr:
        if (x % 2) == 1:
            c_odd = c_odd + 1
    length = len(arr)

    # 辅助数组
    b = [0 for i in range(length)]

    # odd指向奇数部分，even指向偶数部分
    odd = 0
    even = c_odd
    for i in arr:
        if (odd < c_odd) & (i % 2 == 1):
            b[odd] = i
            odd = odd + 1
        if (even < length) & (i % 2 == 0):
            b[even] = i
            even = even + 1

    return b


hh = func([1, 2, 3, 4, 5, 6, 7])
print(hh)
