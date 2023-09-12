from typing import Optional

import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.tree import TreeNode

class CousinInBinaryTree:

    def __init__(self):
        pass

    def is_cousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # result contains (parent, depth)
        x_result = None
        y_result = None

        queue = [(root, root, 0)]

        while queue:
            (current, parent, level) = queue.pop(0)

            if current.val == x:
                x_result = (parent, level)
            if current.val == y:
                y_result = (parent, level)

            if x_result and y_result:
                break
            
            if current.left:
                queue.append((current.left, current, level + 1))
            if current.right:
                queue.append((current.right, current, level + 1))

        return x_result[0] != y_result[0] and x_result[1] == y_result[1]

aaa = (1, 2, 3)

print(aaa[0])