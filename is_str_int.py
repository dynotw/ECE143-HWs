def is_string_integer(x):
    '''
    purpose is to do this
    :param x: input character
    :return: whether x is a digit
    :type x: str
    '''
    assert len(x)==1
    return x.isdigit()

def r(list1):
    sum = 0
    for i in list1:
        sum +=i
    return sum



