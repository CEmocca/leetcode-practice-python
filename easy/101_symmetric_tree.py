from typing import Optional

import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.tree import TreeNode

class SymmetricTree:
    def __init__(self):
        pass

    #         1
    #      /     \
    #     2        2
    #   /   \     /  \
    #  3     4   4    3

    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        symmetric = True
        queue = [(root, root)]

        while queue:
            current, slibing = queue.pop(0)

            if not current or not slibing:
                symmetric = False
                break
            elif current.val != slibing.val:
                symmetric = False
                break

            if current.left:
                queue.append((current.left, slibing.right))
            if current.right:
                queue.append((current.right, slibing.left))

        return symmetric
    
    def is_symmetric_recursive(self, root: Optional[TreeNode]) -> bool:

        def check_sym(current: Optional[TreeNode], slibing: Optional[TreeNode]):
            # base case
            if not current and not slibing:
                return True
            elif not current or not slibing:
                return False
            
            return current.val == slibing.val and check_sym(current.left, slibing.right) and check_sym(current.right, slibing.left)
        
        return check_sym(root, root)