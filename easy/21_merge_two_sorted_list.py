from typing import Optional

import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.list_node import ListNode
from utils.list_utils import *

class MergeTwoSortedList:
    def __init__(self) -> None:
        pass

    def mergeTwoLists_brute_force(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_result = []
        if(list1 == None):
            return list2
        elif(list2 == None):
            return list1
        else:
            while(list1 != None or list2 != None):
                if (list1 != None and list2 != None and list1.val <= list2.val):
                    merged_result.append(list1.val)
                    list1 = list1.next
                elif (list1 != None and list2 != None and list1.val > list2.val):
                    merged_result.append(list2.val)
                    list2 = list2.next
                elif (list1 != None and list2 == None):
                    merged_result.append(list1.val)
                    list1 = list1.next
                elif (list2 != None and list1 == None):
                    merged_result.append(list2.val)
                    list2 = list2.next
            return self.create_node_list(merged_result)

    def mergeTwoList_after_look_at_solution(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while list1 and list2:
            if list1 and list2 and list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1: # list1 != None 
           current.next = list1
        else:
            current.next = list2 

        return head.next



def main():
    solution = MergeTwoSortedList()
    example1 = create_node_list([1,2,4])
    example2 = create_node_list([1,3,4])
    example3 = create_node_list([])
    example4 = create_node_list([0])
    example5 = create_node_list([1])
    example6 = create_node_list([2])
    print_result(example1)
    print_result(example2)
    print_result(example3)
    print_result(example4)
    print("--------------- result ---------------")
    print_result(solution.mergeTwoList_after_look_at_solution(example1, example2))
    print_result(solution.mergeTwoList_after_look_at_solution(example3, example3))
    print_result(solution.mergeTwoList_after_look_at_solution(example3, example4))
    print_result(solution.mergeTwoList_after_look_at_solution(example6, example5))

main()