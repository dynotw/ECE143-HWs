from types import GeneratorType
from time import sleep
import random
from datetime import datetime
import itertools as it

def tracker(p,limit=3):
    '''

    :param p: input, genrator
    :param limit: input, int
    :return:
    '''

    assert isinstance(p,GeneratorType)
    assert isinstance(limit,int)
    assert limit>0

    count=0

    while count<limit:

        a=next(p)
        x=a.seconds
        y=int(x)

        if not (y % 2) == 0:
            count+=1
        threshold = yield count
        if threshold:
            limit=threshold