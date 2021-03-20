
def ui_elements_1(op):
	print('1 called')

def ui_elements_foo(op):
	print('fooooo called')
	from . import A
	A.a(op)

def ui_elements_boo(op):
	print('booooo called')
	from . import B
	B.b(op)