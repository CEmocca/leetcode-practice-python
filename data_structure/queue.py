class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, nodes):
        if nodes is not None:
            node = Node(data= nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(element.data)
                node = node.next
        else:
            self.head = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def dequeue(self):
        node_result = None
        if self.head is not None:
            node_result = self.head
            self.head = node_result.next
        
        return node_result

    def size(self):
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.next
        return size

    def print_element(self):
        node = self.head
        items = []
        while node is not None:
            items.append(node.data)
            node = node.next
        return ' ---> '.join(map(lambda i: str(i), items))

# class 

def main():
    queue = LinkedList(None)
    print(f'size = {queue.size()}')
    queue.enqueue(10)
    print(f'enqueue element 10: {queue.print_element()}')
    print(f'size = {queue.size()}')
    queue.enqueue(20)
    print(f'enqueue element 20: {queue.print_element()}')
    print(f'size = {queue.size()}')
    queue.dequeue()
    print(f'queue element 10: {queue.print_element()}')
    print(f'size = {queue.size()}')
    queue.dequeue()
    print(f'queue element 20: {queue.print_element()}')
    print(f'size = {queue.size()}')
    

if __name__ == '__main__':
    main()
