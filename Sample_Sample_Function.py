def func(n):
    print("my 1st function")
    def func1():
        print("*** my 1st child function ***")
    def func2():
        print("*** my 2nd child function ***")
    def funcerror():
        print("*** Error. Plase check the number***")
    if n==1:
        func1()
    elif n==2:
        func2()
    else:
        funcerror();

func(3)
