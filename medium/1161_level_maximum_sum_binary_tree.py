from typing import Optional

import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.tree import TreeNode

class LevelMaximumSumBinaryTree:
    def __init__(self):
        pass

    def max_level_sum(self, root: Optional[TreeNode]) -> int:
        level_sum_dict = dict()

        queue = [(root, 1)]

        while queue:
            current, level = queue.pop(0)

            if level in level_sum_dict:
                level_sum_dict[level] = level_sum_dict[level] + current.val
            else:
                level_sum_dict[level] = current.val

            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))
        
        # max value should be less than min_value of node
        max_value = -1000000
        max_level = 1
        for key, value in level_sum_dict.items():
            if value > max_value:
                max_value = value
                max_level = key 
        
        return max_level
    