from f1 import sum2n

def test1():
    test = sum2n(1,1)
    if test == 2:
        print('test passed')
    else:
        print('test failed')

def test2():
    test = sum2n('2', '3')
    if type(test) != int:
        print('test failed')
    else:
        print('test passed')
test1()
test2()