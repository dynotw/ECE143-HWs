import os
def split_by_n(fname,n=3):
    '''

    :param fname: input, file
    :param n: input, int
    :return: output, n files
    '''

    assert isinstance(fname,str)
    assert isinstance(n,int)
    assert 1<=n<=99

    sum = os.path.getsize(fname)

    ave = sum/n

    with open(fname,'r') as f:
        lines = f.readlines()
    # lines = [line.rstrip('\n') for line in open(fname)]
    # read file by lines, and put these lines into list

    # nn=0
    # for i in lines:
    #     nn+=len(i)
    # print(nn)


    list1=[0]
    part=0

# the loop is to find line splitting the files
    for i in range(len(lines)):
        if part <= ave:
            part=part+len(lines[i])
        elif part>ave:
            list1.append(i-1)
            part=len(lines[i])+len(lines[i-1])
            if len(list1) >= n:
                break

    list1.append(len(lines))

    # print(list1)

    # num = 0
    # no meaning, only for showing the result when test

    for (x, y) in zip(range(n), list1[1:]):
        # print('x is', x)
        # print('y is', y)
        f = open(('{}{}{:0>2d}{}'.format(fname,'_', x ,'.txt')), 'wb')
        # use 'wt' write module doesn't work well in the number of bytes, so have to use 'wb'

        for i in (lines[list1[list1.index(y)-1]:y]):
            f.write(i.encode('utf8'))
            # use the 'wb' write module, so have to encode

        f.close()

        # with open(('{}{}{:0>2d}{}'.format(fname, '_', x, '.txt')), 'r') as g:
        #     content = g.readlines()
        #     print(content[-1])

        # num+=os.path.getsize(('{}{}{:0>2d}{}'.format(fname, '_', x, '.txt')))
        # print('num is', num)

    return





