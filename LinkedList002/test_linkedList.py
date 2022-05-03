import pytest
from SingleLinkedList import SingleLinkedList


class TestClassSingleLinkedList:
    ownLinkedList = SingleLinkedList()

    @pytest.mark.parametrize('obj, expected_output',[('A',['A']),('B',['A','B']),('C',['A','B','C'])])
    def test_append(self, obj, expected_output):
        # empty
        self.ownLinkedList.append(obj)
        assert self.ownLinkedList.get_all() == expected_output


    def test_traverse(self):
        # 'A','B','C'
        self.ownLinkedList.append('E')
        assert self.ownLinkedList.get_all() == ['A','B','C','E']


    def test_prepend(self):
        # 'A','B','C','E'
        self.ownLinkedList.prepend('Z')
        assert self.ownLinkedList.get_all() == ['Z','A','B','C','E']

    
    def test_insert_after_node(self):
        # 'Z','A','B','C','E'
        self.ownLinkedList.insert_after_node('C', 'D')
        assert self.ownLinkedList.get_all() == ['Z','A','B','C','D','E']

    @pytest.mark.parametrize('val, expected_output',[('Z',['A','B','C','D','E']),('E',['A','B','C','D'])])
    def test_delete_by_val(self, val, expected_output):
        # 'Z','A','B','C','D','E'
        self.ownLinkedList.delete_by_val(val)
        assert self.ownLinkedList.get_all() == expected_output
    
    def test_delete_by_pos(self):
        # 'A','B','C','D'
        self.ownLinkedList.delete_by_pos(1)
        assert self.ownLinkedList.get_all() == ['A','C','D']

    
    def test_len_iterative(self):
        assert self.ownLinkedList.len_iterative() == 3

    def test_len_recursive(self):
        self.ownLinkedList.insert_after_node('A', 'B')
        assert self.ownLinkedList.len_recursive(self.ownLinkedList.head) == 4

    @pytest.mark.parametrize('val, expected_output', [('A',[None, 'B']),('C',['B','D']),('D',['C',None])])
    def test_get_neighboors(self, val , expected_output):
        # 'A','B','C','D'
        # insted of returning an array of node I cast every node to its value to facilitate the testing
        # [<SingleLinkedList.Node object at 0x000001D98A57EBE0>, <SingleLinkedList.Node object at 0x000001D98A57SEBE0>]
        #  ---> ['A', 'C']
        assert [node.data if node else node for node in self.ownLinkedList.get_neighboors(val)] == expected_output

    @pytest.mark.parametrize('val, expected_output', 
    [
        (['A', 'D'],['D','B','C','A']),
        (['C','B'],['D','C','B','A']),
        (['A', 'D'],['A','C','B','D']),
        (['C','B'],['A','B','C','D']),
     ])
    def test_swap_nodes(self, val, expected_output):
        self.ownLinkedList.swap_nodes(val[0], val[1])
        assert self.ownLinkedList.get_all() == expected_output
    
        