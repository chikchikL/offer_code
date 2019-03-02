# -*- coding:utf-8 -*-
# 思路：一个负责模拟进队，一个负责模拟出队
class Solution:
    s1 = []
    s2 = []

    def push(self, node):
        # write code here
        # 如果s2是非空的，需要将s1全部压入s2才能进队，否则次序错误
        if len(self.s2) > 0:
            while not (len(self.s1) == 0):
                self.s2.append(self.s1.pop())

        self.s1.append(node)


    def pop(self):
        # return xx
        # s1,s2都为空 = 队列空，不可出
        if (len(self.s1) == 0) & (len(self.s2) == 0):
            return None
        # s2非空，直接出队
        if len(self.s2) > 0:
            return self.s2.pop()
        # s1非空，s2空，将s1元素全部压到s2后出
        elif len(self.s1) > 0:
            while not (len(self.s1) == 0):
                self.s2.append(self.s1.pop())
            # 出队
            return self.s2.pop()


solution = Solution()
solution.push(1)
solution.push(2)
solution.push(3)
print('s1:',solution.s1,'---s2:',solution.s2)
print(solution.pop())
print(solution.pop())
print('s1:',solution.s1,'---s2:',solution.s2)
solution.push(4)
print('s1:',solution.s1,'---s2:',solution.s2)
print(solution.pop())
print('s1:',solution.s1,'---s2:',solution.s2)
solution.push(5)

print(solution.pop())
print(solution.pop())

