import TreeNode as trees


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    class Solution:
        def levelOrder(self, root):
            pass


if __name__ == "__main__":
    data = [1, 2, 2, 3, 4, 4, 3]
    data2 = [1, 2, 2, None, 3, None, 3]
    tree1 = trees.Tree()
    tree2 = trees.Tree()
    
    tree1.createTree(data)
    tree1.breadth_travel()
    print()
    tree2.createTree(data2)
    tree2.breadth_travel()
    # print('\n 验证二叉搜索树结果:', Solution().isValidBST(tree1.root))
    # print('\n 验证二叉搜索树结果:', Solution().isValidBST(tree2.root))