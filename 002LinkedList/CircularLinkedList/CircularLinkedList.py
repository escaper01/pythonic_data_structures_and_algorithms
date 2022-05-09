class Node:
    def __init__(self, data):
      self.data = data
      self.next = None


class CircularLinkedList:
    def __init__(self):
      self.head = None

    def __len__(self) -> int:
        # return the length of C_L_L
        current = self.head
        count = 1
        while current.next != self.head:
            count += 1
            current = current.next
        return count


    def prepend(self, data:object) -> None:
        # add a node at the beginning
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            old_head = self.head
            last_elem = old_head
            while last_elem.next != self.head:
                last_elem = last_elem.next
            

            self.head = new_node
            self.head.next = old_head
            last_elem.next = new_node



    def append(self, data:object) -> None:
        # add a node at the end of C_L_L
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            cursor = self.head
            while cursor.next != self.head:
                if not cursor.next:
                    break
                cursor = cursor.next
            cursor.next = new_node
            new_node.next = self.head


    def print_list(self) -> list:
        #return all node
        cursor = self.head
        if not cursor:
            return []

        ls = []
        while cursor.next != self.head:
            if not cursor.next:
                    break
            ls.append(cursor.data)
            cursor = cursor.next
        ls.append(cursor.data)
        return ls

    def get_last_node(self) -> Node:
        current = self.head
        if not current:
            return None
        while current:
            if current.next == self.head:
                return current
            current = current.next

    def remove(self, key: object) -> None:
        # remove a node
        if self.head.data == key:
            last_node = self.get_last_node()
            last_node.next = self.head.next
            self.head = last_node.next
        
        else:
            current, prev = self.head.next, None
            while current != self.head:
                if current.data == key:
                    prev.next = current.next
                    return
                prev = current
                current = current.next
            

    def is_circular(self) -> bool:
        current = self.head
        while current:
            current = current.next
            if current == self.head:
                return True
        return False
    
    def split_list(self):
        # return two halves of circular linked lists
        if self.__len__() < 4:
            return 'required 4 nodes at least'

        new_cl = CircularLinkedList()
        cursor = self.head
        mid = self.__len__() // 2
        count = 1

        while cursor.next:
            if count == mid:
                tmp = cursor.next
                cursor.next = self.head
                cursor = tmp
                new_cl.head = cursor

            if cursor.next == self.head:
                cursor.next = new_cl.head
                break

            else:
                cursor = cursor.next
            count += 1
        
        return [self, new_cl]
    
    def josephus_circle(self, step):
        """
        josephus problem
        There are n people standing in a circle waiting to be executed. 
        The counting out begins at some point in the circle and proceeds around the circle 
        in a fixed direction. In each step, a certain number of people are skipped 
        and the next person is executed. The elimination proceeds around the circle 
        (which is becoming smaller and smaller as the executed people are removed),
        until only the last person remains, who is given freedom.
        ***********************************************************************************
        Children often play a counting-out game to randomly select one person from the group
        by singing a rhyme. The purpose is to select one person, either as a straightforward winner,
        or as someone who is eliminated.

        Arguments:
                step : an integer that defines the number of skipped elements
         
        """
        length = self.__len__()

        cursor = self.head
        prev = None
        count = 1


        while length >= 1:
            tmp_step = step

            while tmp_step != 0:
                tmp_step -= 1

                if tmp_step == 0:
                    prev.next = cursor.next

                prev = cursor
                cursor = cursor.next

            length -= 1

