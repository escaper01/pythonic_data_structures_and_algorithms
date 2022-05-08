import pytest
from stack import MyStack
from challenges import is_balanced, reverse_string, convert_int_to_bin


class TestClassMyStack:
    ownStack = MyStack()

    def test_push(self):
        self.ownStack.push('a')
        self.ownStack.push('b')
        self.ownStack.push('c')
        assert self.ownStack.get_elements() == ['a','b','c']

    
    def test_pop(self):
        assert self.ownStack.pop() == 'c'

    def test_peek(self):
        assert self.ownStack.peek() == 'b'

    def test_is_empty(self):
        self.ownStack.is_empty() == False

    def test_get_elements(self):
        self.ownStack.get_elements() == ['a','b']


@pytest.mark.parametrize('parentheses, exp_out',[("[][]]]",False),("(({[]}))",True),('[][{}[',False)])
def test_valid_parenthesese(parentheses, exp_out):
    assert is_balanced(parentheses) == exp_out


@pytest.mark.parametrize('mystring, exp_out',[("escaper",'repacse'),("moon",'noom'),('race','ecar')])
def test_reverse_string(mystring, exp_out):
    assert reverse_string(mystring) == exp_out

@pytest.mark.parametrize('myint, exp_out',[(8,'1000'),(1998,'11111001110'),(0,'0')])
def test_convert_int_binary(myint, exp_out):
    assert convert_int_to_bin(myint) == exp_out