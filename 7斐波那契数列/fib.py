# 求fib第n项
# 思路：生成一个39项的数字，从前往后遍历生成

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        l = [0 for i in range(n + 1)]
        l[0] = 0
        if n > 0:
            l[1] = 1
        i = 2
        while i <= n:
            l[i] = l[i - 1] + l[i - 2]
            i = i + 1

        return l[n]


s = Solution()
print(s.Fibonacci(0))
