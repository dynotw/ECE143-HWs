def fibonacci(n):
    '''
    purpose is to do this
    :param n: input, int
    :return: list of int
    '''
    assert isinstance(n, int)
    assert 0 < n

    counter = 0
    a=1
    b=1

    while counter < n:
        yield a  # yield makes the function work as generator
        a, b = b, a + b
        counter += 1

    # a=1
    # b=1
    # list1=[]
    # while counter <n:
    #     list1.append(a)
    #     yield list1
    #     a, b=b, a+b
    #     counter +=1

