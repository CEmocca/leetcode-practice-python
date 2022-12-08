from typing import Optional

import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.list_node import ListNode
from utils.list_utils import *

class RemoveLinkedListElements:

    def __init__(self) -> None:
        pass

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        previous = result = ListNode()
        cur = head

        while cur:
            if cur.val == val:
                previous.next = cur.next
            else:
                previous.next = cur
            previous = previous.next
            cur = cur.next

        return result.next

def main():
    solution = RemoveLinkedListElements()
    print_result(solution.removeElements(create_node_list([7,7,7,7]), 7))

main()