from typing import Optional

import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.tree import TreeNode
from utils.tree_utils import *

class ConvertToBST:

    def __init__(self):
        pass

    # input = [-10,-3,0,5,9]
    # output = [0,-3,9,-10,null,5]
    #               0
    #          /        \
    #        -3          9
    #       /  \        /
    #     -10  null    5

    # output = [0,-10,5,null,-3,null,9]
    #                  0
    #               /     \
    #             -10      5
    #               \        \
    #               -3         9

    # input = [0,1,2,3,4,5]
    #              3
    #            /   \
    #           1     4
    #         /   \     \
    #        0     2      5


    # this solution has a bug because I don't think about root of child node need to be handle
    # I thought I will append less value to be always as left or right side, but I forgot about root node need to be handle
    # due to the problem statement "height-balanced binary search tree"
    def sorted_array_to_BST(self, nums: list[int]) -> Optional[TreeNode]:
        # 5 -> 3, 4 -> 2
        mid = int(len(nums) / 2)
        left = mid - 1
        right = mid + 1

        root = TreeNode(nums[mid])
        current = root

        # iterate left side
        while left >= 0: # find break condition
            cur_value = nums[left]
            
            if cur_value < current.val:
                current.left = TreeNode(cur_value)
            else:
                current.right = TreeNode(cur_value)

            left = left - 1
            current = current.left
        
        current = root
        # iterate right side
        while right < len(nums):
            cur_value = nums[right]

            if cur_value < current.val:
                current.left = TreeNode(cur_value)
            else:
                current.right = TreeNode(cur_value)
            
            right = right + 1
            current = current.right

        return root
    
    def insert_binary_search_tree(self, node: Optional[TreeNode], val: int) -> None:
        # we are 100% confident that node is not null
        to_add = TreeNode(val)
        if val < node.val:
            node.left = to_add
        else:
            node.right = to_add
        
    
    def sorted_array_to_BST_iterative(self, nums: list[int]) -> Optional[TreeNode]:
        root = TreeNode()
        stack = [(root, 0, len(nums))]

        while stack:
            (current, left, right) = stack.pop()

            mid = (right - left + 1) // 2

            current.val = nums[mid]

            if mid > left:
                current.left = TreeNode()
                stack.append((current.left, left, mid))
            if mid + 1 < right:
                current.right = TreeNode()
                stack.append((current.right, mid + 1, right))


        return root
    
    def sorted_array_to_BST_recursive(self, nums: list[int]) -> Optional[TreeNode]:

        if len(nums) <= 0:
            return None

        mid = len(nums) // 2

        current = TreeNode(nums[mid])

        current.left = self.sorted_array_to_BST_recursive(nums[:mid])
        current.right = self.sorted_array_to_BST_recursive(nums[mid + 1:])

        return current

def main():
    solution = ConvertToBST()
    print_tree_in_order(solution.sorted_array_to_BST_recursive([-10,-3,0,5,9]))

main()