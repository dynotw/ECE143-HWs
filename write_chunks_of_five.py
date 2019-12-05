def write_chunks_of_five(words,fname):
    '''

    :param words: list of word
    :param fname: string
    :return: none
    '''

    assert isinstance(words,list)
    for i in words:
        assert isinstance(i,str)
    assert isinstance(fname,str)

    f=open(fname,'w')

    for id, val in enumerate(words):
        if (id%5)==4:
            f.write('{}\n'.format(val))

        else:
            f.write('{} '.format(val))

    f.close()