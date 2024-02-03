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

    # time complexity is O(N)
    # space complexity is O(1)
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if head is None:
            return None
        
        cur = head
        prev = None
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        return prev
    
    def reverse_list_rec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if head is None:
            return None
        
        cur = head
        prev = None
        
        def reverse(node: Optional[ListNode], prev: Optional[ListNode]): 
            if node is None:
                return prev
            
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
            
            return reverse(node, prev)
        
        return reverse(cur, prev)
    
#### 1
# cur = 1, prev = None
# next_node = 2     # 2 -> 3 -> 4 -> 5
# cur.next = prev   # 1 -> null
# prev = cur        # 1 -> null
# cur = next_node   # 2 -> 3 -> 4 -> 5

#### 2
# cur = 2, prev = 1 -> null
# next_node = 3     # 3 -> 4 -> 5
# cur.next = prev   # 2 -> 1 -> null
# prev = cur        # 2 -> 1 -> null
# cur = next_node   # 3 -> 4 -> 5

#### 3
# cur = 3, prev = 2 -> 1 -> null
# next_node = 4     # 4 -> 5
# cur.next = prev   # 3 -> 2 -> 1 -> null
# prev = cur        # 3 -> 2 -> 1 -> null
# cur = next_node   # 4 -> 5

solution = Solution()

print_result(solution.reverse_list(create_node_list([1,2,3,4,5])))
print_result(solution.reverse_list(create_node_list([1,2])))

print_result(solution.reverse_list_rec(create_node_list([1,2,3,4,5])))
print_result(solution.reverse_list_rec(create_node_list([1,2])))