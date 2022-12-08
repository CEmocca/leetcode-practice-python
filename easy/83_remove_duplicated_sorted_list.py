from typing import Optional

import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.list_node import ListNode
from utils.list_utils import *

class RemoveDuplicatedSortedList:
    def __init__(self) -> None:
        pass

    # time complexity = O(n)
    # space complexity = O(n)
    def deleteDuplicates_first_solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        visited_num = []
        result = head
        result_root = result
        visited_num.append(head.val)
        while head:
            if head.val in visited_num:
                head = head.next
            else:
                visited_num.append(head.val)
                result.next = head
                result = result.next
                head = head.next
        
        if result.val in visited_num:
            result.next = None

        return result_root

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        cur = head
        while cur:
            if not cur.next:
                break

            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


def main():
    solution = RemoveDuplicatedSortedList()
    print_result(solution.deleteDuplicates(create_node_list([1,1,2])))
    print_result(solution.deleteDuplicates(create_node_list([1,1,2,3,3])))
    print_result(solution.deleteDuplicates(create_node_list([])))

main()
