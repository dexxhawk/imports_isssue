# Так не работает:
import a as lib 

# Так работает:
# import packages.a as lib 

def bar():
    print(lib.foo())
