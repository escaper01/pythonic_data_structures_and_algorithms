import unittest
from stack import MyStack


def is_matched(elem1: str, elem2: str) -> bool:
    """
    func that match each open bracket with its closed bracket
    { & } --> true
    ( & ) --> true
    [ & ] --> true
    Arguments:
            elem1: a string
            elem2: a string
    Returns:
            a boolean
    """
    
    if elem1 == '{' and elem2 == '}':
        return True

    if elem1 == '(' and elem2 == ')':
        return True

    if elem1 == '[' and elem2 == ']':
        return True

    return False

def is_balanced(brackets: str) -> bool:
    """
    func that will evaluates whether the given brackets are balanced or not
    Arguments:
            brackets: a string
    Returns:
            a boolean
    """
    cursor = 0
    open_brackets = '{(['
    own_stack = MyStack()
    result = True

    
    while cursor < len(brackets) and result:
        # print(own_stack.get_elements(),'stack')
        if brackets[cursor] in open_brackets:
            own_stack.push(brackets[cursor])
        else:
            if own_stack.is_empty():
                result = False
            else:
                result = is_matched(own_stack.pop(), brackets[cursor]) 
        cursor += 1


    if own_stack.is_empty():
        return result

    return False



print(is_balanced('[][{}')) # false
print(is_balanced('(({[]}))')) # true
print(is_balanced('[][]]]')) # false