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

    def len_iterative(self) -> int:
        # return the length iteratively
        count = 0
        cursor = self.head

        while cursor:
            cursor = cursor.next
            count += 1
        
        return count

    def len_recursive(self, node: Node) -> int:
        # return the length recursively
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def get_neighboors(self, val:object) -> list:
        #return surrounding nodes
        current = self.head
        prev = None
        while current.data != val:
            prev = current
            current = current.next

        return [prev if  prev else None, current.next if  current.next else None]
    
    def get_node(self, val: object) -> Node:
        # return the node with same value
        cursor = self.head
        while cursor.data != val:
            cursor = cursor.next
        return cursor

    def swap_nodes(self, first_val:object, second_val:object) -> None:
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

    def reverse_iteratively(self) -> None:
        # reverse it iteratively
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    
    def reverse_recusively(self) -> None:
        # reverse it recursively
        def _reverse_rec(cur, prev):
            if not cur:
                return prev
            
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            return _reverse_rec(cur, prev)
        
        self.head = _reverse_rec(self.head, None)

    def merge(self, llist) -> Node:
        # merge two ordered linked list
        """
        Start by creating another pointer 
        go ahead and do the first merge and save your new head
        then do a while loop until one of the nodes gets empty
        without forgeting that from the start if one of the nodes
        is emtpy add to it the rest of the other node and exit ^^^
        """
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not p:
            return p

        # to setup the new head
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self) -> None:
        # remove any duplicates
        curr = self.head
        prev = None
        history = {}

        while curr:
            key = str(curr.data)
            if key in history:
                prev.next = curr.next
            else:
                history[key] = 1
            prev = curr
            curr = curr.next

    def get_n_th_from_last(self, n_th:int) -> Node:
        # return n_th node from last
        total_length = self.len_iterative()
        current_node = self.head

        while n_th + 1 != total_length:
            # print(current_node.data)
            current_node = current_node.next
            total_length -= 1
        
        if not current_node:
            return
        return current_node

    def count_occurences_iteratively(self, data:object) -> int:
        # return the number of occurence for data iteratively
        count = 0
        current_node = self.head

        while current_node:
            if current_node.data == data:
                count += 1
            current_node = current_node.next

        return count

    def count_occurences_recursively(self,head: Node, data: object) -> int:
        # return the number of occurence for data recursively
        if not head:
            return 0
        if head.data == data:
            return 1 + self.count_occurences_recursively(head.next, data)
        else:
            return self.count_occurences_recursively(head.next, data)

    def pivote(self, k: object) -> None:
        current_node = self.head
          
        while current_node.data != k:
            current_node = current_node.next
        # in case it's the last node do NOTHING ^^
        if not current_node.next:
            return

        new_head = current_node.next
        current_node.next = None

        last_elem = new_head
        prev = None

        while last_elem:
            prev = last_elem
            last_elem = last_elem.next

        prev.next = self.head
        self.head = new_head
    
    def is_palindrome_stack(self) -> bool:
        # check if it's a palindrome with a stack - list
        ls = []
        cursor = self.head
        length = self.len_iterative()
        limit = length // 2
        pass_center = False if length % 2 == 0 else True
        count = 0
        result = True

        while cursor:
            if count < limit:
                ls.append(cursor.data)
            
            else:
                if pass_center and count == limit:
                    pass
                else:
                    elem = ls.pop()
                    if not cursor.data == elem:
                        result = False
                        break

            count += 1
            cursor = cursor.next
        return result

    def is_palindrome_string(self) -> bool:
        # check if palindrome using srings
        cursor = self.head
        tmp = ""
        
        while cursor:
            tmp += str(cursor.data)
            cursor = cursor.next

        return tmp == tmp[::-1]

    def move_head_to_tail(self) -> None:
        cursor = self.head
        prev = None
        old_head = cursor

        while cursor.next:
            prev = cursor
            cursor = cursor.next
        
        new_head = cursor
        prev.next = None
        new_head.next = old_head
        self.head = new_head

    def sum_two_lists(self, llist) -> int:
        # return the sum of the whole number represented inside in each linked list
        p = self.head
        q = llist.head
        num_p = num_q = ''

        while p and q:
            num_p += str(p.data)
            num_q += str(q.data)
            q = q.next
            p = p.next
        

        # cast to int
        tmp1 = tmp2 = 0

        for i, num in enumerate(num_p):
            tmp1 += int(num) * 10 ** i
        for i, num in enumerate(num_q):
            tmp2 += int(num) * 10 ** i
        
        return tmp1 + tmp2



