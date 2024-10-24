import cnama.mod1 as cm1 
# or :
# from cnama.mod1 import func1
# (if in same package(folder) : from .mod1 import func1)
# then use : 'func1' (directly available as var. in the namespace)

def func2():
    cm1.func1()
    print("func2")
