def threshold_values(seq,threshold=1):
    '''

    :param seq:
    :param threshold:
    :return:
    '''

    assert isinstance(seq,list)
    for i in seq:
        assert isinstance(i,str)
    assert isinstance(threshold, int)
    assert threshold>0

    from collections import Counter
    import heapq

    num = Counter(seq)

    assert threshold <=len(num.keys())

    maxvalue=[]
    for key, value in num.items():
        if key.count('0') <= key.count('1'):
            maxvalue.append(value)
    x=heapq.nlargest(threshold, maxvalue)

    list1=list(set(x))
    list1.sort(reverse=True)

    bitstring1=[]
    bitstring2=[]
    for i in range(len(list1)-1):
        for key,value in num.items():
                if value == list1[i]:
                    if key.count('0') <= key.count('1'):
                        bitstring1.append(key)

    for key,value in num.items():
        if value==list1[-1]:
            if key.count('0') <= key.count('1'):
                bitstring2.append(key)
    y = heapq.nsmallest((threshold-len(bitstring1)), bitstring2)

    z = bitstring1 + y

    for key, value in num.items():
        if key in z:
            num[key]=1
        else:
            num[key]=0

    return dict(num)






    # dict1=dict()
    #
    # for i in seq:
    #     dict1[i]=[]
    # for i in seq:
    #     if i.count('0') > i.count('1'):
    #         dict1[i].append(0)
    #     else:
    #         dict1[i].append(1)
    #
    # print(dict1)
    #
    # for key,value in dict1.items():
    #     if 1 in value:
    #         list1=[0]*threshold
    #         if len(value)>list1[0]:
    #             list1.insert(0,key)
    #         elif len(value)=list1[0]:
    #             if key <list[0]:
    #                 list1.insert(0,key)
    #             else:
    #                 len(value)>









