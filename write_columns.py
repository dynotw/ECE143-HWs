def write_columns(data,fname):
    '''
    purpose is to do this
    :param data: input character
    :param fname
    :return: None
    :type data: list of integer/float
    :type fname: string
    '''


    assert isinstance(data,list)
    for i in data:
        assert isinstance(i,(int,float))
    assert isinstance(fname, str)

    f=open(fname,'w')


    for i in data:
        f.write('{:.2f},{:.2f},{:.2f}\n'.format(i,i**2,(i+i**2)/3))

    f.close()