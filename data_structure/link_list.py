class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for ele in nodes:
                node.next = Node(data=ele.data)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node.next is not None:
            nodes.append(node.data)
            node = node.next
        node.append(None)
        return '  -->  '.join(nodes)

    def traverse(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def add_node_end(self, node):
        self_node = self.head
        if self_node is None:
            self_node = node
            return
        
        while self_node.next is not None:
            self_node = node.next
        self_node.next = node
        return

    def add_node_start(self, node):
        node.next = self.head
        self.head = node
        return

    def add_node_before(self, node, before_target):
        if self.head is None:
            self = node
            return

        if self.head.data == before_target:
            node.next = self.head
            self.head = node
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == before_target:
                node.next = current_node.next
                current_node.next = node
                return
            current_node = current_node.next
        # Edge case when no element is equal to target till the end of the list
        current_node.next = node
        return


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def __repr__(self):
        return self.data

