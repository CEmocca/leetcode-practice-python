from typing import Optional
import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.list_node import ListNode
from utils.list_utils import *

class Solution:

    def __init__(self):
        pass
    
    def copy_link_lest(self, head):
        if head is None:
            return head
        
        new_head_node = ListNode(head.val)
        
        new_head_node.next = self.copy_link_lest(head.next)
        
        return new_head_node

    # time complexity is O(N)
    # space complexity is O(N)
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        # edge case: 1 node is palindrom
        if head.next is None:
            return True
        
        original_head = self.copy_link_lest(head)
        prev = None
        cur = head
        
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            
        reversed_node = prev
        
        while original_head:
            if original_head.val != reversed_node.val:
                return False
            original_head = original_head.next
            reversed_node = reversed_node.next
            
        return True
        
        
    

solution = Solution()

print(solution.is_palindrome(create_node_list([1,2,2,1])))
print(solution.is_palindrome(create_node_list([1,2])))
print(solution.is_palindrome(create_node_list([1,1,2,1])))