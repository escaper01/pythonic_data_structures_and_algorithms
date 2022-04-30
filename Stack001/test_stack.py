import pytest
from stack import MyStack
from challenges import is_balanced


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


@pytest.mark.parametrize('parentheses, expected_output',[("[][]]]",False),("(({[]}))",True),('[][{}[',False)])
def test_valid_parenthesese(parentheses, expected_output):
    assert is_balanced(parentheses) == expected_output