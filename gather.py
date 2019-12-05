def get_sample(nbits=3,prob=None,n=1):
    '''
    purpose is to do this
    :param nbits: input, int, only for assert statement
    :param prob: input, dict,
    :param n: input, int
    :return: list
    '''

    import random
    import math

    assert isinstance(nbits,int)
    assert nbits>=1
    assert len(prob)==2**nbits
    assert isinstance(prob,dict)
    for key, value in prob.items():
        assert isinstance(key,str)
        assert len(key) == nbits
        assert isinstance(value,(int,float))
        assert 0<=value<=1
    assert math.isclose(sum(prob.values()),1)
    assert isinstance(n,int)
    assert n>=1

    po=[]
    we=[]
    for key, value in prob.items():
        po.append(key)
        we.append(value)

    x = random.choices(po, weights=we, k=n)
    return x

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

def gather_values(x):
    '''

    :param x: input, list
    :return: dict
    '''

    # from gather import map_bitstring
    from collections import Counter

    assert isinstance(x,list)
    for i in x:
        assert isinstance(i, str)

    num=Counter(x)

    val=map_bitstring(x)

    for key,value in num.items():
        list1=[]
        list1.append(val[key])
        val[key]=list1*value

    return val



    # dict1 = dict()
    #
    # for i in x:
    #     dict1[i] = []
    # for i in x:
    #     if i.count('0') > i.count('1'):
    #         dict1[i].append(0)
    #     else:
    #         dict1[i].append(1)
    #
    # return dict1




