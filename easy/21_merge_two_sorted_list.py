from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class MergeTwoSortedList:
    def __init__(self) -> None:
        pass

    def create_node_list(self, nums: list[int]) -> ListNode:
        if (nums == []):
            return None
        else:
            root_node = None
            list_node = root_node
            for item in nums:
                node = ListNode(item)
                if(list_node == None):
                    root_node = list_node = node
                else:
                    list_node.next = node
                    list_node = node
            return root_node

    def print_result(self, results: ListNode) -> None:
        if (results == None):
            print([])
        else:
            vals = []
            iter_node = results
            while(iter_node != None):
                vals.append(iter_node.val)
                iter_node = iter_node.next
            print(vals)

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
        
        if list1: # list1 != None or list2 != None
           current.next = list1
        else:
            current.next = list2 

        return head.next



def main():
    solution = MergeTwoSortedList()
    example1 = solution.create_node_list([1,2,4])
    example2 = solution.create_node_list([1,3,4])
    example3 = solution.create_node_list([])
    example4 = solution.create_node_list([0])
    example5 = solution.create_node_list([1])
    example6 = solution.create_node_list([2])
    solution.print_result(example1)
    solution.print_result(example2)
    solution.print_result(example3)
    solution.print_result(example4)
    print("--------------- result ---------------")
    solution.print_result(solution.mergeTwoList_after_look_at_solution(example1, example2))
    solution.print_result(solution.mergeTwoList_after_look_at_solution(example3, example3))
    solution.print_result(solution.mergeTwoList_after_look_at_solution(example3, example4))
    solution.print_result(solution.mergeTwoList_after_look_at_solution(example6, example5))

main()