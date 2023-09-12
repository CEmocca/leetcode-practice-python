from typing import Optional

import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.tree import TreeNode

class BinaryTreeLevelOrder:

    def __init__(self) -> None:
        pass

    #
    #        3
    #      /   \
    #     9    20
    #          / \
    #         15  7
    # output = [[3], [9, 20], [15, 7]]
 
    #  (3, 0)
    # []


    def level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
        results = []
        if root is None:
            return results
        
        queue = [ (root, 0) ]

        while queue:
            (current, level) = queue.pop(0)
            
            if len(results) - 1 < level:
                results.append([current.val])
            else:
                results[level].append(current.val)

            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))
        
        return results

