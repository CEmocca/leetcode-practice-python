from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

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

def create_node_list(nums: list[int]) -> ListNode:
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

def print_result(results: ListNode) -> None:
        if (results == None):
            print([])
        else:
            vals = []
            iter_node = results
            while(iter_node != None):
                vals.append(iter_node.val)
                iter_node = iter_node.next
            print(vals)

main()
