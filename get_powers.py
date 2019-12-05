def get_power_of3(x):
    '''
    purpose is to do this
    :param x: input character
    :return: a list
    :type x: integer
    '''
    import itertools as it
    '''itertools is a very powerful module 
    '''
    assert isinstance(x,int)
    assert x>=1 and x<=40

    y=it.product([-1,0,1],repeat=4)
    # about itertools.product(), see the web https://www.cnblogs.com/happystudyeveryday/p/10815325.html
    # repeat=4, like it.product([-1,0,1],[-1,0,1],[-1,0,1],[-1,0,1])

    for i in y:
        if (1*i[0]+3*i[1]+9*i[2]+27*i[3]) == x:
            break

    a=list(i)
    return a






