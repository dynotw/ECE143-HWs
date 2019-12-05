import random
def get_sample(nbits=3,prob=None,n=1):
	"""
	:param: nbits is lenth of keys in dictionary
	:param: prob is the dictionary of probability
	:param: n is the number of sample 
	:return:
	"""

	assert nbits>0
	assert isinstance(nbits,int)
	assert n>0
	assert isinstance(n,int)
	assert isinstance(prob,dict)
	assert (0<=x<=1 for x in prob.values())
	assert sum(list(prob.values()))==1
	assert (len(y)==nbits for y in prob.keys())
	assert len(list(prob.keys()))==2**nbits 

	population=list(prob.keys())
	weights=list(prob.values())

	a=random.choices(population,weights,k=n)
	return list(a)

# p={'000':0.125,'001':0.125,'010':0.125,'011':0.125,'100':0.125,'101':0.125,'110':0.125,'111':0.125,}

# x=get_sample(3,p,1)
# print(x)

