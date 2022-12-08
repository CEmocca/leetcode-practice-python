from .list_node import ListNode

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