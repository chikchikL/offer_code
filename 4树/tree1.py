# 根据前序和中序遍历重构二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        # 思路：前序遍历的首个元素是根节点，在中序遍历中找到该节点，确定左右子树节点个数
        # 这时又分别得到左右子树的前中遍历字符串，递归处理

        # 如果遍历序列为空，则是空树，返回None
        pre = ''.join(pre)
        tin = ''.join(tin)
        if (pre == '') & (tin == ''):
            return None

        # 对任意子树，根为前序遍历首个元素
        x = pre[0]
        node = TreeNode(x)

        # 元素不重复，直接根据指定元素拆分得到左右子树中序遍历序列
        inorders = tin.split(x)

        # 根据左右子树个数截取前序遍历序列
        left_count = len(inorders[0])
        # [:]如果截取失败自动返回空字符串''，不用判断左右子树是否为空
        left_pre = pre[1:1 + left_count]
        right_pre = pre[1 + left_count:]

        # 递归处理左右子树
        node.left = self.reConstructBinaryTree(left_pre, inorders[0])
        node.right = self.reConstructBinaryTree(right_pre, inorders[1])

        return node

# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n1.right = n2
# n2.left = n3

def trace_tree(root):
    if root == None:
        return


    trace_tree(root.left)
    print(root.val)
    trace_tree(root.right)


solution = Solution()
root = solution.reConstructBinaryTree('123', '132')
print(root)

