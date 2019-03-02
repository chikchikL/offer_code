class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]

    def printListFromTailToHead(self, listNode):
        # write code here
        # if not (listNode == None):
        #     self.printListFromTailToHead(listNode.next)
        #     self.l.append(listNode.val)
        #
        # return self.l
        if listNode == None:
            return []
        l = self.printListFromTailToHead(listNode.next)
        l.append(listNode.val)
        return l


n1 = ListNode(5)
n2 = ListNode(81)
n3 = ListNode(61)
n4 = ListNode(95)
n1.next = n2
n2.next = n3
n3.next = n4

so = Solution()
result = so.printListFromTailToHead(n1)
print(result)
