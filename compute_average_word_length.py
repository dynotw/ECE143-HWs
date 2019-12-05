def compute_average_word_length(instring,unique=False):
    '''
    purpose is to do this
    :param x: string
    :return: length
    type instring: string
    '''

    assert isinstance(instring,str)

    list1 = instring.split()
    list2 = []

    for i in list1:
        if unique==False:
            list2.append(i)
        elif unique==True:
            if i not in list2:
                list2.append(i)

    sum=0
    for i in list2:
        sum += len(i)

    ave=sum/len(list2)

    return(ave)



