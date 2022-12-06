from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class IntersectionTwoLinkedList:
    def __init__(self) -> None:
        pass

    def is_valid_subset(self, headA: ListNode, headB: ListNode) -> bool:
        len_a = 0
        len_b = 0

        is_valid = True
        while headA and headB:

            if headA.val != headB.val:
                is_valid = False
                break
            
            if headA.next:
                len_a += 1
            
            if headB.next:
                len_b += 1
            
            headA = headA.next
            headB = headB.next

        return is_valid and len_a == len_b

    # Wrong solution, in the quesion it only need to check pointer ref not values of each node
    # At first I think it want to find longest subset of two linked list
    def getIntersectionNode_check_sub_set(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        w_dict = dict()

        while headA:
            if headA.val in w_dict:
                w_dict[headA.val].append(headA)
            
            else:
                w_dict[headA.val] = [headA]

            headA = headA.next

        result = None
        while headB:
            if headB.val in w_dict:
                dict_value = w_dict[headB.val]  # array of node
                is_valid_subset = False
                for value in dict_value:
                    if value == headB:
                        result = value
                        break
                    temp_node_headB = headB         # to check all node intersect
                    temp_node_value = value

                    is_valid_subset = self.is_valid_subset(temp_node_value, temp_node_headB)

                    if is_valid_subset == True:
                        result = value
                        break

            if result:
                break
            headB = headB.next
        
        return result

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        w_dict = dict()

        while headA:
            if headA.val in w_dict:
                w_dict[headA.val].append(headA)
            
            else:
                w_dict[headA.val] = [headA]

            headA = headA.next

        result = None
        while headB:
            if headB.val in w_dict:
                dict_value = w_dict[headB.val]  # array of node
                for value in dict_value:
                    if value == headB:
                        result = value
                        break

            if result:
                break
            headB = headB.next
        
        return result
                    
                    
def main():
    solution = IntersectionTwoLinkedList()
    print_result(solution.getIntersectionNode(create_node_list([4,1,8,4,5]), create_node_list([5,6,1,8,4,5])))
    print_result(solution.getIntersectionNode(create_node_list([1,9,1,2,4]), create_node_list([3,2,4])))
    print_result(solution.getIntersectionNode(create_node_list([2,6,4]), create_node_list([1,5])))

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