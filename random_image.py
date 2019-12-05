import numpy as np
import random

def gen_rand_slash(m=6,n=6,direction='back'):
    '''

	:param m: input, int, number of rows in the image
	:param n: input, int, number of column in the image
	:param direction: input, string
	:return:
	'''
    assert isinstance(m,int)
    assert m>1
    assert isinstance(n,int)
    assert n>1
    assert isinstance(direction, str)
    assert direction == 'back' or direction=='forward'


	if direction == 'back':
		m_loc=random.choice(range(m-1))
		# m is the row number of the start point
		n_loc=random.choice(range(n-1))
		# n is the column number of the start point
		a= np.zeros((m,n))

		length=random.choice(range(2,min(m-m_loc-1,n-n_loc-1)+2))
		#length is a random number which means how many number'1' we could fill in  in matrix

		for i in range(length):
			if m_loc<0 or m_loc>=m or n_loc<0 or n_loc>=n:
				break
			a[m_loc][n_loc]=1
			# fill in the number '1' to the matrix
			m_loc +=1
			#start point move
			n_loc +=1
	else:
		m_loc=random.choice(range(m-1))
		n_loc=random.choice(range(1,n))
		a= np.zeros((m,n))

		length=random.choice(range(2,min(n_loc,m-m_loc-1)+2))

		for j in range(length):
			if m_loc<0 or m_loc>=m or n_loc<0 or n_loc>=n:
				break
			a[m_loc][n_loc]=1
			m_loc +=1
			n_loc -=1
	return a 
