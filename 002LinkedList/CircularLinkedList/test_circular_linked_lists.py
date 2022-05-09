import pytest
from CircularLinkedList import CircularLinkedList



class TestCircularLinkedList:
    ownCircularLinkedList = CircularLinkedList()

    # for i in range(1,5):
    #     ownCircularLinkedList.append(data)

    @pytest.mark.parametrize('obj, exp_out',[(1,[1]),(2,[1,2]),(3,[1,2,3])])
    def test_append(self, obj, exp_out):
        self.ownCircularLinkedList.append(obj)
        assert self.ownCircularLinkedList.print_list() == exp_out

    
    def test_len(self):
        assert len(self.ownCircularLinkedList) == 3

    @pytest.mark.parametrize('obj, exp_out',[(0,[0,1,2,3]),(-1,[-1,0,1,2,3])])
    def test_prepend(self,obj,exp_out):
        self.ownCircularLinkedList.prepend(obj)
        assert self.ownCircularLinkedList.print_list() == exp_out


    def test_print_list(self):
        assert self.ownCircularLinkedList.print_list() == [-1,0,1,2,3]

    def test_get_last_node(self):
        assert self.ownCircularLinkedList.get_last_node().data == 3

    def test_remove(self):
        self.ownCircularLinkedList.remove(key=-1)
        assert self.ownCircularLinkedList.print_list() == [0,1,2,3]

    def test_split_list(self):
        splited_ll = self.ownCircularLinkedList.split_list()
        splited_ll = [ll.print_list() for ll in splited_ll]

        assert splited_ll == [[0,1],[2,3]]
        
    def test_josephus_circle(self):
        self.ownCircularLinkedList.append(2)
        self.ownCircularLinkedList.append(3)
        self.ownCircularLinkedList.josephus_circle(step=2)

        assert self.ownCircularLinkedList.print_list() == [0]