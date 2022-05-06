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


def reverse_string(my_string: str) ->str:
	"""
	func that will return the reverse of the given string
	Arguments:
			my_string: a string
	Returns:
			a string
	"""
	own_stack = MyStack()
	reversed_str = ''

	# insert all letters in the stack
	for char in my_string:
		own_stack.push(char)
	
	# extract all element from the stack
	while not own_stack.is_empty():
		reversed_str += own_stack.pop()

	return reversed_str


def convert_int_to_bin(dec_num: int) -> str:

	own_stack = MyStack()
	result = dec_num

	if result == 0:
		return '0'

	while result != 0:
		remainder = result % 2
		result //= 2
		own_stack.push(remainder)

	ls = ''.join(str(elem) for elem in own_stack.get_elements())

	## since get_elements return the stack elements in reverse
	return ls[::-1]
