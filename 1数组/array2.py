# 不修改数组找出重复数字,长度n+1的数组，数字范围1-n
# 思路：二分法找出重复数字的范围
# 样例：{2,3,5,4,3,2,6,7}

# l是值的左边界，r为右边界，函数作用是判断arr是否在指定值域内有重复数字
def judge(arr, l, r):
    count = 0
    for i in arr:
        if (i <= r) & (i >= l):
            count = count + 1
    if count > (r - l + 1):
        return True
    return False


def find_duplicate(arr):
    if (arr == None) | (len(arr) == 0):
        print('输入有误')

    # 值域范围1-n
    left = 1
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        # 判断在左值域还是右值域
        if judge(arr, left, mid):
            right = mid
            continue
        # 走到这代表左边值域无重复，右边值域也无重复的话则不存在重复数字
        if not judge(arr, mid + 1, right):
            print('无重复数字！')
            return

        left = mid + 1

    print('重复数字为:', left)


arr = [int(n) for n in input().split(',')]
print(arr)
find_duplicate(arr)
