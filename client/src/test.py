def foo(arg1, *args):
    print(arg1)
    _args = args
    arg2 = args[0]
    arg2 = 3    
    print(type(_args))
    print(_args)
    print(type(args))
    print(args)
    
    
foo(1, 2, 3, 4, 5)