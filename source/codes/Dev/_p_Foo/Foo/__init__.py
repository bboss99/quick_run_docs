
def ui_elements_goo(op):
	print('goo called')

def ui_elements_foo(op):
	print('fooooo called')
	from . import A
	A.a(op)

def ui_elements_boo(op):
	print('booooo called')
	from . import B
	B.b(op)