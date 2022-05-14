import pytest
from DoublyLinkedList import DoublyListList


class TestDoublyLinkedLinkedList:
    ownDoublyLinkedList = DoublyListList()
    @pytest.mark.parametrize('obj, exp_out',[(1,[1]),(2,[1,2]),(3,[1,2,3])])
    def test_append(self,obj, exp_out):
        self.ownDoublyLinkedList.append(obj)
        assert self.ownDoublyLinkedList.print_list() == exp_out

    def test_prepend(self):
        self.ownDoublyLinkedList.prepend(0)
        assert self.ownDoublyLinkedList.print_list() == [0,1,2,3]

    def test_add_after_node(self):
        self.ownDoublyLinkedList.add_after_node(key=3, data=4)
        assert self.ownDoublyLinkedList.print_list() == [0,1,2,3,4]

    def test_add_before_node(self):
        self.ownDoublyLinkedList.add_before_node(key=0, data=99)
        assert self.ownDoublyLinkedList.print_list() == [99,0,1,2,3,4]

    def test_delete(self):
        self.ownDoublyLinkedList.delete(99)
        self.ownDoublyLinkedList.delete(0)
        self.ownDoublyLinkedList.delete(4)
        assert self.ownDoublyLinkedList.print_list() == [1,2,3]

    def test_remove_diplicates(self):
        self.ownDoublyLinkedList.append(4)
        self.ownDoublyLinkedList.append(5)
        self.ownDoublyLinkedList.append(5)
        self.ownDoublyLinkedList.append(6)
        self.ownDoublyLinkedList.append(6)
        self.ownDoublyLinkedList.remove_duplicates()
        assert self.ownDoublyLinkedList.print_list() == [1,2,3,4,5,6]


    def test_pairs_with_sum(self):
        assert self.ownDoublyLinkedList.pairs_with_sum(sum_val=9) == [[4,5],[3,6]]

