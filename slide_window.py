def slide_window(x,width,increment):
    '''
    purpose is to do this
    :param x: list
    :param width: int
    :param increment: int
    :return: a list
    '''


    assert isinstance(x,list)
    assert width > 0
    assert width<=len(x)
    assert isinstance(width,int)
    assert increment > 0
    assert isinstance(increment,int)

    list1=[]

    # return [x[i:i + width] for i in range(0, len(x), increment) if i <= len(x) - width]
    for i in range(0, len(x), increment):
        if i<=(len(x)-width):
            list1.append(x[i:i +width])

    return list1
