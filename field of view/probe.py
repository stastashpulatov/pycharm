def func_1():
    x = 34
    print('in f1 x =', x, 'locals() = ', locals())


x = 42
func_1()
print('x =', x)
