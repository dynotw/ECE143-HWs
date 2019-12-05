import numpy as np
def solvefrob(coefs,b):
    '''
    :param coefs:
    :param b:
    :return:
    '''
    assert isinstance(coefs,list)
    assert isinstance(b,int)

    # calculate the maximum of x_n
    max_x=[]
    for i in coefs:
        max_x.append(int(b/i))

    # calculate every a_n * x_n
    x_array=[]
    for i in range(len(coefs)):
        x_array.append(np.arange(max_x[i]+1)*np.array([coefs[i]]))
    # print(x_array)
    # print(type(x_array[1]))

    sum_ax=0
    for i in range(len(x_array)):
        list1=[]
        for j in range(len(coefs)):
            if j == i:
                list1.append(max_x[i]+1)
            else:
                list1.append(1)
        re=tuple(list1)
        # print(x_array[i])
        # print(re)
        ax=x_array[i].reshape(re)
        # print(ax)
        # print(np.shape(ax))
        sum_ax = sum_ax+ax
    # print(sum_ax)

    solution=[tuple(i) for i in np.array(np.where(sum_ax==b)).T]

    return solution

    # for iter in np.array(np.where(sum_ax==25)).T:
    #     print(f'{iter[0]} dimes, {iter[1]} nickles, {iter[2]} pennis.')

# if __name__ == '__main__':
#         print(solvefrob([1,2,3,5],10))

# #X as dimes, Y as nickles, Z as pennis
# X=np.arange(3)*np.array([10])
# Y=np.arange(6)*np.array([5])
# Z=np.arange(26)
#
# #broadcasting
# res = X[:,None,None]+Y[None,:,None]+Z[None,None,:]
#
# #Number of possible solutions 12
# print(len(np.where(res==25)[0]))
#
# #Output solutions
# for iter in np.array(np.where(res==25)).T:
#     print(f'{iter[0]} dimes, {iter[1]} nickles, {iter[2]} pennis.')
