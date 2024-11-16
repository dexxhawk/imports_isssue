# Так не работает, protoc генерирует именно такие импорты:
import a as lib 

# Так работает:
# import packages.a as lib

def bar():
    print(lib.foo())
