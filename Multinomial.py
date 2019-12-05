import itertools as it
import functools as fu
import math as ma
import random

def multinomial_sample(n,p,k=1):
    '''

    :param n: input, int
    :param p: input, list
    :param k: input, int
    :return: list
    '''

    assert isinstance(n,int)
    assert n>0
    assert isinstance(p,list)
    assert sum(p)==1
    assert isinstance(k,int)
    assert k>0

    list1=[]
    prob=[]
    m=len(p)

    for i in (it.product(list(range(n+1)), repeat=m)):
        if sum(i)==n:
            i=list(i)
            list1.append(i)

    print(list1)
    mm = fu.reduce(lambda x, y: x * y, range(1, n + 1))

    for x in list1:
        pp=mm
        for y in x:
            if y == 0:
                pp*=ma.pow(p[x.index(y)],y)
            elif y>0:
                pp *= (ma.pow(p[x.index(y)], y) / (fu.reduce(lambda x1, y1: x1 * y1, range(1, y + 1))))
        prob.append(pp)
    print(prob)
    print(sum(prob))

    a = random.choices(list1, prob, k=k)

    return a


    # for x,y in list
    #
    # def multinomial(lst):
    #     res, i = 1, 1
    #     for a in lst:
    #         for j in range(1, a + 1):
    #             res *= i
    #             res //= j
    #             i += 1
    #     return res