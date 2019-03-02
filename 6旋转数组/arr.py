# 非减旋转数组找出最小值
# 思路：一般情况下，数组的前半部分有序数组比后半部分有序数组大
# 二分法，p1，p2分别指向头尾，与中间的数字m比较，如果m>=p1指向数字，将p1指向m所在位置
# 若m<=p2所指数字，p2指向m所在位置，不断缩小查找范围，直到p1+1 = p2，此时p2指向即为最小数字
# 特例：1.有序数列是一种特别的旋转数组,首个数字就是最小数字
# 2.如果缩小到某个范围时，p1，p2指向的数字与m相等，那么不可以缩小查找范围，只能通过遍历数组找到最小值


# 遍历数组找到最小数字
def find_min(arr):
    result = arr[0]
    for x in arr:
        if x < result:
            result = x
    return result


class Solution:

    def minNumberInRotateArray(self, rotateArray):
        # write code here
        p1 = 0
        p2 = len(rotateArray) - 1
        # 如果数组本身有序的话，直接返回首个数字
        if rotateArray[p2] > rotateArray[p1]:
            return rotateArray[p1]
        # 按二分法查找
        while not (p1 + 1 == p2):
            m = (p1 + p2) // 2
            # 如果无法缩小范围，遍历整个数组找到最小值
            if (rotateArray[m] == rotateArray[p1]) \
                    & (rotateArray[m] == rotateArray[p2]):
                return find_min(rotateArray)
            if rotateArray[m] >= rotateArray[p1]:
                p1 = m
            elif rotateArray[m] <= rotateArray[p2]:
                p2 = m
        return rotateArray[p2]


s = Solution()

re = s.minNumberInRotateArray([1, 1, 1, 0, 1])
print(re)
