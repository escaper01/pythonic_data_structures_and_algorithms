import pytest
from SingleLinkedList import SingleLinkedList


class TestClassSingleLinkedList:
    ownLinkedList = SingleLinkedList()
    another_llist = SingleLinkedList()

    for i in range(0,20,3):
        another_llist.append(i)

    @pytest.mark.parametrize('obj, exp_out',[(1,[1]),(3,[1,3]),(7,[1,3,7])])
    def test_append(self, obj, exp_out):
        # empty
        self.ownLinkedList.append(obj)
        assert self.ownLinkedList.get_all() == exp_out


    def test_traverse(self):
        # 1,3,7
        self.ownLinkedList.append(11)
        assert self.ownLinkedList.get_all() == [1,3,7,11]


    def test_prepend(self):
        # 1,3,7,11
        self.ownLinkedList.prepend(20)
        assert self.ownLinkedList.get_all() == [20,1,3,7,11]

    
    def test_insert_after_node(self):
        # 20,1,3,7,11
        self.ownLinkedList.insert_after_node(7, 9)
        assert self.ownLinkedList.get_all() == [20,1,3,7,9,11]

    @pytest.mark.parametrize('val, exp_out',[(20,[1,3,7,9,11]),(11,[1,3,7,9])])
    def test_delete_by_val(self, val, exp_out):
        # 20,1,3,7,9,11
        self.ownLinkedList.delete_by_val(val)
        assert self.ownLinkedList.get_all() == exp_out
    
    def test_delete_by_pos(self):
        # 1,3,7,9
        self.ownLinkedList.delete_by_pos(1)
        assert self.ownLinkedList.get_all() == [1,7,9]

    
    def test_len_iterative(self):
        assert self.ownLinkedList.len_iterative() == 3

    def test_len_recursive(self):
        self.ownLinkedList.insert_after_node(1, 3)
        assert self.ownLinkedList.len_recursive(self.ownLinkedList.head) == 4

    @pytest.mark.parametrize('val, exp_out', [(1,[None, 3]),(7,[3,9]),(9,[7,None])])
    def test_get_neighboors(self, val , exp_out):
        # 1,3,7,9
        # insted of returning an array of node I cast every node to its value to facilitate the testing
        # [<SingleLinkedList.Node object at 0x000001D98A57EBE0>, <SingleLinkedList.Node object at 0x000001D98A57SEBE0>]
        #  ---> [1, 7]
        assert [node.data if node else node for node in self.ownLinkedList.get_neighboors(val)] == exp_out

    @pytest.mark.parametrize('val, exp_out', 
    [
        ([1, 9],[9,3,7,1]),
        ([7,3],[9,7,3,1]),
        ([1, 9],[1,7,3,9]),
        ([7,3],[1,3,7,9]),
     ])
    def test_swap_nodes(self, val, exp_out):
        self.ownLinkedList.swap_nodes(val[0], val[1])
        assert self.ownLinkedList.get_all() == exp_out

    def test_reverse_iteratively(self):
        self.ownLinkedList.reverse_iteratively()
        assert self.ownLinkedList.get_all() == [9,7,3,1]
    
    def test_reverse_recusively(self):
        self.ownLinkedList.reverse_recusively()
        assert self.ownLinkedList.get_all() == [1,3,7,9]

    def test_merge(self):
        # 0- 1 -3- 3 -6- 7 - 9 - 9 - 12 - 15 - 18
        self.ownLinkedList.merge(self.another_llist)
        assert self.ownLinkedList.get_all() == [0,1,3,3,6,7,9,9,12,15,18]

    def test_remove_duplicates(self):
        self.ownLinkedList.remove_duplicates()
        assert self.ownLinkedList.get_all() == [0,1,3,6,7,9,12,15,18]

    @pytest.mark.parametrize('val, exp_out', [(0,18),(3,9),(2,12)])
    def test_get_n_th_from_last(self,val, exp_out):
        assert self.ownLinkedList.get_n_th_from_last(val).data == exp_out

    def test_count_occurences_iteratively(self):
        self.ownLinkedList.append(15)
        assert self.ownLinkedList.count_occurences_iteratively(15) == 2

    def test_count_occurences_recursively(self):
        self.ownLinkedList.append(15)
        # [0,1,3,6,7,9,12,15,18,15,15]
        assert self.ownLinkedList.count_occurences_recursively(self.ownLinkedList.head,15) == 3

    @pytest.mark.parametrize('val, exp_out',
     [
        (12,[15,18,15,15,0,1,3,6,7,9,12]),
        (0,[1,3,6,7,9,12,15,18,15,15,0]),
        (1,[3,6,7,9,12,15,18,15,15,0,1])
     ])
    def test_pivote(self,val, exp_out):
        self.ownLinkedList.pivote(val)
        assert self.ownLinkedList.get_all() == exp_out

    def test_is_palindrome_stack(self):
        for elem in self.ownLinkedList.get_all():
            self.ownLinkedList.delete_by_val(elem)

        my_palindrome = ['m','a','d','a','m']
        for elem in my_palindrome:
            self.ownLinkedList.append(elem)

        assert self.ownLinkedList.is_palindrome_stack() == True


    def test_is_palindrome_string(self):
        for elem in self.ownLinkedList.get_all():
            self.ownLinkedList.delete_by_val(elem)

        my_palindrome = [1,2,3,0,3,2,1]
        for elem in my_palindrome:
            self.ownLinkedList.append(elem)

        assert self.ownLinkedList.is_palindrome_string() == True

    def test_move_head_to_tail(self):
        # [1,2,3,0,3,2,1]
        self.ownLinkedList.move_head_to_tail()
        assert self.ownLinkedList.get_all() == [1,1,2,3,0,3,2]

    
    def test_sum_two_lists(self):
        for elem in self.ownLinkedList.get_all():
            self.ownLinkedList.delete_by_val(elem)
        
        self.ownLinkedList.append(2)
        self.ownLinkedList.append(2)

        for elem in self.another_llist.get_all():
            self.another_llist.delete_by_val(elem)
        self.another_llist.append(3)
        self.another_llist.append(3)
        
        assert self.ownLinkedList.sum_two_lists(self.another_llist) == 55
        


    
    



    

    

    
        