def map_bitstring(x):
    '''

    :param x: input, list
    :return: dict
    '''

    assert isinstance(x,list)
    for i in x:
        assert isinstance(i,str)

    dict1=dict()

    for i in x:
        if i.count('0') > i.count('1'):
            dict1[i]=0
        else:
            dict1[i]=1

    return dict1
