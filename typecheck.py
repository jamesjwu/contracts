from contracts import *

"""
Typechecking tool used as decorator. Just put in the argument types 
Usage:

#int -> int function
@typecheck(int, out = int)
def f(x):
	return x + 5

#put None, typecheck.void for arguments you don't want to typecheck
#ignore self part
#also, out is optional
@typecheck(typecheck.self, int, int)
def __init__(self, x, y):
	return x + y

"""


class typecheck(object):
	void = None
	self = None
	def __init__(self, *args, **kwargs):
		requires(args)
		self.arg = args
		self.out = kwargs.get("out", None)


	def __call__(self, f):

		def checkf(*args, **kwargs):
			for a, b in zip(self.arg, args + tuple(kwargs.values())):
				if a != None and a != type(b):
					raise TypeError("Expected argument of " + repr(a) + ", " + 
													str(b) + " is " + str(type(b)))
			result = f(*args, **kwargs)

			if self.out != None and self.out != type(result):
				raise TypeError("Expected argument of " + repr(self.out) + ", " 
										  + str(result) + " is " + str(type(result)))
			return result
			

		return checkf

