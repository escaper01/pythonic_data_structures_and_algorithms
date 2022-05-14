class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

    

class DoublyListList:
    def __init__(self):
        self.head =None
    

    def append(self, data:object) -> None:
        new_node = Node(data)
        if self.head == None:
            self.head = new_node

        else:
            cursor = self.head
            while cursor.next:
                cursor = cursor.next
                
            cursor.next = new_node
            new_node.prev = cursor
        

    def print_list(self) -> None:
        cursor = self.head
        ls = []
        if not cursor:
            return ls
        
        while cursor:
            previous_val = cursor.prev.data if cursor.prev else None
            next_val = cursor.next.data if cursor.next else None
            ls.append(cursor.data)
            cursor = cursor.next
        return ls

    def prepend(self, data:object) -> None:
        new_node = Node(data)
        old_head = self.head

        if old_head == None:
            self.head = new_node
        
        else:
            new_node.next = old_head
            old_head.prev = new_node
            self.head = new_node

    def add_after_node(self,key:object, data:object) -> None:
        new_node = Node(data)
        cursor = self.head
        while cursor:
            if cursor.data == key:
                tmp = cursor.next
                cursor.next = new_node
                new_node.prev = cursor
                new_node.next = tmp
                # if we wannted to insert after the last node
                # no need to setup the prev of last node since it's NONE
                if tmp:
                    tmp.prev = new_node
                break
            cursor = cursor.next


    def add_before_node(self,key:object, data:object) -> None:
        new_node = Node(data)
        cursor = self.head

        if cursor.data == key:
            new_node.next = cursor
            cursor.prev = new_node
            self.head = new_node
            return

        while cursor:
            if cursor.data == key:
                tmp = cursor.prev
                cursor.prev = new_node
                new_node.next = cursor
                new_node.prev = tmp
                tmp.next = new_node
                break
            cursor = cursor.next

    
    def delete(self, key:object) -> None:
        cursor = self.head
        # case of one node which is basically the head node
        if cursor.data == key and not cursor.next:
            cursor = None
            self.head = None
            return
        # case of head and still other nodes
        if cursor.data == key and cursor.next:
            self.head = cursor.next
            cursor.next = None
            cursor = None
            self.head.prev = None
            return
        while cursor:
            if cursor.data == key:
                #  case of current is not None
                if cursor.next:
                    tmp_next = cursor.next
                    tmp_prev = cursor.prev
                    cursor.prev = cursor = None

                    tmp_prev.next = tmp_next
                    tmp_next.prev = tmp_prev
                    return
                else:
                #  case of current is None (LAST NODE)
                    cursor.prev.next = None
                    cursor.prev = cursor = None
                    return


            cursor = cursor.next
    

    def reverse(self) -> None:
        cursor = self.head

        while cursor.next:
            tmp = cursor.next
            cursor.next,cursor.prev = cursor.prev , cursor.next
            cursor = tmp

        cursor.next,cursor.prev = cursor.prev , cursor.next
        self.head = cursor

    def remove_duplicates(self):
        cursor = self.head
        history = dict()

        while cursor:
            if str(cursor.data) in history:
                self.delete(key= cursor.data)
            else:
                history[str(cursor.data)] = 1
            cursor = cursor.next

    def pairs_with_sum(self, sum_val:int) -> list:
        # get all posible pairs to get the sum_val
        expected = []
        result = []
        cursor = self.head
        while cursor:
            hoped_val = sum_val - cursor.data
            for sub_list in expected:
                if sub_list[1] == cursor.data:
                    result.append(sub_list)
            expected.append([cursor.data, hoped_val])
            cursor = cursor.next
        
        return result

