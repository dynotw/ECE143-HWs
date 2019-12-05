import string
def encrypt_message(message, fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.

    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''

    assert isinstance(message,str)
    assert message.islower()
    mess=message.replace(' ','')
    assert mess.isalpha()
    assert isinstance(fname,str)

    with open(fname,'r') as f:
        lines = f.readlines()

    me=message.split()
    # di = {}
    # for key in me:
    #     di[key] = di.get(key, 0) + 1
    #     assert di[key] <= len(location[key])
        # read the content of fname by line, and write the line into a list 'lines'

    location=dict()
    # create a dict to write down the location of different words

    # list1=[]
    # list1 only for test, for autograder we can delete all codes including list1

    for i in range(len(lines)):
        t = lines[i].translate(str.maketrans('', '', string.punctuation))
        # take place of all punctuation by None
        t = t.lower()
        t = t.split()
        # split line by ' ', and the output is a list

        # list1.append(t)

        # the loop is for writing down the indexes of each word, and put the indexes into dict'location'
        # lines.index(i)+1 is about index of line; t.index(word)+1 is about index in the line
        for n in range(len(t)):
            if t[n] not in location:
                location[t[n]] = []
                location[t[n]].append((i + 1, n + 1))
                # the index of line showed in encryption is from 1 rather than 0
            else:
                location[t[n]].append((i + 1, n + 1))
    di = {}
    for key in me:
        di[key] = di.get(key, 0) + 1
        assert di[key] <= len(location[key])


        # 确保message中某word出现的次数小于此word在codebooks出现的次数
        # 这样可以保证在encryption中，相同word对应的index都可以不同

    # check whether the tuples are same as the sample given by autograder
    # for x,y in zip(me,[(1394, 2), (1773, 11), (894, 10), (840, 1), (541, 2), (1192, 5), (1984, 7), (2112, 6), (1557, 2), (959, 8), (53, 10), (2232, 8), (552, 5)]):
    #     print(y in location[x])
    print(location['let'])

    send=[]

    for i in me:
        assert i in location
        x=0
        place=location[i][x]
        while 1:
            if place not in send:
                send.append(place)
                break
            elif place in send:
                x+=1
                place = location[i][x]
    return send


def decrypt_message(inlist, fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message.
    
    :param inlist: input, inlist to decrypt
    :param fname: input, filename for source text, str
    :return: string decrypted message
    '''

    assert isinstance(inlist,list)
    for i in inlist:
        assert isinstance(i, tuple)
    assert (len(i)==2 for i in inlist)
    assert isinstance(fname,str)

    with open(fname, 'r') as f:
        lines = f.readlines()
        # read the content of fname by line, and write the line into a list 'lines'

    location = dict()
    # create a dict to write down the location of different words

    # list1=[]
    # list1 only for test, for autograder we can delete all codes including list1

    for i in range(len(lines)):
        t = lines[i].translate(str.maketrans('', '', string.punctuation))
        # take place of all punctuation by None
        t = t.lower()
        t = t.split()
        # split line by ' ', and the output is a list

        # list1.append(t)

        # the loop is for writing down the indexes of each word, and put the indexes into dict'location'
        # lines.index(i)+1 is about index of line; t.index(word)+1 is about index in the line
        for n in range(len(t)):
            if t[n] not in location:
                location[t[n]] = []
                location[t[n]].append((i + 1, n + 1))
                # the index of line showed in encryption is from 1 rather than 0
            else:
                location[t[n]].append((i + 1, n + 1))

    list1=[]

    for i in inlist:
        for word, places in location.items():
            if i in location[word]:
                list1.append(word)
                break

    me=' '.join(list1)
    return me


