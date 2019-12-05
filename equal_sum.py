import numpy as np
import itertools as it
def get_min_split(seq):
    '''

    :param seq:
    :return:
    '''

    assert isinstance(seq,(list,np.ndarray))

    y=[x for x in it.product([-1,1],repeat=len(seq))]
    min=abs(np.sum(np.array(y[0])*np.array(seq)))
    list1=[np.array(y[0])*np.array(seq)]

    for i in y[1:]:
        dif=abs(np.sum(np.array(i)*np.array(seq)))
        # print(dif)
        if dif==min:
            list1.append(np.array(i)*np.array(seq))
        elif dif < min:
            min=dif
            list1=[np.array(i)*np.array(seq)]
            # print('list1 is', list1)

    list2=[]
    for i in list1:
        greater_0 = list(i[np.where(i>0)])
        less_0 = list(-1*i[np.where(i<0)])
        li=[greater_0,less_0]
        li.sort(reverse=True)

        if li not in list2:
            list2.append(li)

    list3=[]
    for i in list2:
        i=tuple(i)
        list3.append(i)

    return list3





# if __name__ == '__main__':
#     seq=[5,10,15,20,25]
#     y=get_min_split(seq)
#     print(y)
