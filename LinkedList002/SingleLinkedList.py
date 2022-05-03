class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self,elem: object) -> None:
        # add a node
        if self.head == None:
            self.head = Node(elem)
            return

        cursor = self.head
        while cursor.next is not None:
            cursor = cursor.next
        
        cursor.next = Node(elem)

    def get_all(self) -> list:
        ls = []
        # print all nodes
        cursor = self.head
        while cursor:
            ls.append(cursor.data)
            cursor = cursor.next
        return ls

    def prepend(self, elem: object) -> None:
        # add a node to the beginning
        old_head = self.head
        new_head = Node(elem)
        self.head = new_head
        new_head.next = old_head

    def insert_after_node(self, prev_data: object, new_data: object) -> None:
        cursor = self.head
        while cursor.data is not prev_data:
            cursor = cursor.next
        new_node = Node(new_data)
        new_node.next = cursor.next
        cursor.next = new_node

    
    def delete_by_val(self, val: object) -> None:
        # delete a node by value
        if self.head.data == val:
            self.head = self.head.next
            return
        
        cursor = self.head
        prev = None

        while cursor:
            if cursor.data == val:
                break

            prev = cursor
            cursor = cursor.next
        
        prev.next = cursor.next

    
    def delete_by_pos(self, pos: int) -> None:
        # delete a node by position
        if pos == 0 :
            self.head = self.head.next
            return
        
        count = 0
        cursor = self.head
        prev = None

        while count != pos:
            prev = cursor
            cursor = cursor.next
            count += 1
        
        prev.next = cursor.next

    def len_iterative(self):
        # return the length iteratively
        count = 0
        cursor = self.head

        while cursor:
            cursor = cursor.next
            count += 1
        
        return count

    def len_recursive(self, node):
        # return the length recursively
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def get_neighboors(self, val):
        #return surrounding nodes
        current = self.head
        prev = None
        while current.data != val:
            prev = current
            current = current.next

        return [prev if  prev else None, current.next if  current.next else None]
    
    def get_node(self, val):
        # return the node with same value
        cursor = self.head
        while cursor.data != val:
            cursor = cursor.next
        return cursor

    def swap_nodes(self, first_val, second_val):
        # swap node by value
        first_node_neighboors = self.get_neighboors(first_val)
        second_node_neighboors = self.get_neighboors(second_val)

        first_node = self.get_node(first_val)
        second_node = self.get_node(second_val)

        

        if self.head == first_node:
            second_node_neighboors[0].next = first_node
            second_node.next = first_node.next
            first_node.next = None
            self.head = second_node
            return
        
        if self.head == second_node:
            first_node_neighboors[0].next = second_node
            first_node.next = second_node.next
            second_node.next = None
            self.head = first_node
            return

        
        first_node_neighboors[0].next = second_node

        temp = second_node.next
        if first_node.next == second_node:
            second_node.next = first_node
        else:
            second_node.next = first_node.next

        second_node_neighboors[0].next = first_node
        first_node.next = temp



