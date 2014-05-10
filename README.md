Contracts
=========
Contracts is a small library that implements pre and post condition contracts using assert statements in python.
It also contains a typechecking library, Typecheck, that acts as a python typechecker, in the form of a decorator.


##requires() and ensures()
To use pre and post conditions, simply place them in the document where you want them asserted. 

##@typecheck
Just put in the argument types. Use the keyword arg out to declare an output type.
Usage: 

```python
#int -> int function
@typecheck(int, out = int)
def f(x):
	return x + 5
#put None, typecheck.void for arguments you don't want to typecheck
#add typecheck.self for class methods
#also, out is optional
@typecheck(typecheck.self, int, int)
def __init__(self, x, y):
	return x + y
```

###Why typecheck Python?

There are a lot of reasons why Python shouldn't be typechecked generally. The weak typing is an advantage of the language, and is useful in a lot of contexts. However, there are times when being able to control the types of a function allows you to better debug your code and prove correctness. Type systems are important in this aspect. @typecheck is a compromise between the two, allowing you to choose when functions and which arguments should and should not be typechecked. 