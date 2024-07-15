# coding: utf-8


class Stack:
	def __init__(self) :
		self._stack = []

	def push(self, value: float):
		self._stack.append(value)

	def pop(self):
		return self._stack.pop(-1)

	def get(self):
		return self._stack[-1]

	def clear(self):
		self._stack.clear()

	@property	
	def stack(self):
		return self._stack

	def __len__(self):
		return len(self._stack)
