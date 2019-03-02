# 找出数组中的第一个重复数字，限制，n个数的数组，所有数字都在0~n内
# 思路：用一个指针i从前往后遍历，设指向的数字为m，直到找到第一个m与i不同的位置
# 将m交换到其下标位置处，若m与其下标位置数已经相同，则停止输出，否则循环
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # 思路：遍历整个数组，下标i，值m，若i==m，判断下一个元素，
        # 否则将m放到与下标相同的位置上
        i = 0
        length = len(numbers)
        while (i < length):
            m = numbers[i]
            if m == i:
                i = i + 1
            else:
                # 交换时判断是否相等，如果相等则重复了
                temp = numbers[m]
                if temp == m:
                    # 找到一个重复的函数就停止函数
                    duplication[0] = m
                    return True
                numbers[m] = m
                numbers[i] = temp
                i = i + 1
        return False
