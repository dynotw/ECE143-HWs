# def get_power_of3(x):
#     '''
#     purpose is to do this
#     :param x: input character
#     :return: a list
#     :type x: integer
#     '''
#     import itertools as it
#     '''itertools is a very powerful module
#     '''
#     assert isinstance(x,int)
#     assert x>=1 and x<=40
#
#     try:
#         return get_powers_of3.d[n]
#     except AttributeError:
#         d -dict()
#         for i,j,k,l in (it.product([-1,0,1],repeat=4)):
#             d[sum([1*i+3*j+9*k+27*l])]=(i,j,k,l)
#         get_powers_of3.d = d
#         return get_power_of3.d[n]


def get_power_of3(n, mxpwr=3):
    '''
    purpose is to do this
    :param x: input character
    :return: a list
    :type x: integer
    '''
    import itertools as it
    from collections import defaultdict

    assert isinstance(n, int)
    assert isinstance(mxpwr, int)

    try:
        return get_powers_of3.d[mxpwr][n]
    except AttributeError:
        items = [[-1, 0, 1]] * (mxpwr + 1)
        for t in it.product(*items):
            sm = sum([k * 3 ** i for i, k in enumerate(t)])
            d[mxpwr][sm] = t
        return get_power_of3.d[mxpwr][n]