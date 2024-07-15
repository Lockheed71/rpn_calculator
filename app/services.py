# coding: utf-8


from app.models import Stack


stack = Stack() 

def stack_len():
	return len(stack)

def stack_push(value: float):
	stack.push(value)

	return value

def stack_get():
	return stack.get()

def stack_get_stack():
	return stack.stack

def stack_pop():
	return stack.pop()

def stack_clear():
	stack.clear()

	return stack.stack

def stack_addition():
	r, l = stack.pop(), stack.pop()
	res = l + r
	stack_push(res)

	return res

def stack_substract():
	r, l = stack.pop(), stack.pop()
	res = l - r
	stack_push(res)

	return res

def stack_multiply():
	r, l = stack.pop(), stack.pop()
	res = l * r
	stack_push(res)

	return res

def stack_divide():
	r, l = stack.pop(), stack.pop()

	if b == 0:
		raise ZeroDivisionError()

	res = l / b
	stack_push(res)

	return res