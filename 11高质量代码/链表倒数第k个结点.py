# 思路，先让一个指针走k-1步，如果走到空指针代表少于k个结点，输出空，否则两个指针一起走，直到先走的指针走到链尾
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reversedK(head, k):
    # 输入合法性不能忽略k，如果k <= 0,返回空
    if (head is None) or (k<=0):
        return None



    p1 = head
    p2 = head

    i = 1
    while i < k:
        p1 = p1.next
        i = i + 1

    if p1 is None:
        return None

    while p1.next != None:
        p1 = p1.next
        p2 = p2.next

    return p2


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

print(reversedK(n1,2).val)
