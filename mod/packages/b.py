# import a as lib # Так не работает
# import packages.a as lib # Так работает

def bar():
    print(lib.foo())
