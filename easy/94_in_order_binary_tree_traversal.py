from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InOrderBinaryTreeTraversal:
    def __init__(self) -> None:
        pass

    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        def traverse(node: Optional[TreeNode]):
            if not node:
                return

            if node.left:
                traverse(node.left)
            
            result.append(node.val)

            if node.right:
                traverse(node.right)

        traverse(root)

        return result


def main():
    solution = InOrderBinaryTreeTraversal()
    print(solution.inorderTraversal([1, None, 2, 3]))

main()