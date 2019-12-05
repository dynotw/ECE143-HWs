def compute_sum_to_n(n):
    '''
    purpose is to do this
    :param n: input character
    :return: the sum of non-negtive number which is less than n
    :type n: digit
    '''

    assert n >=0

    sum = 0
    a=int(n)
    for i in range(a+1):
        sum +=i
    return sum
