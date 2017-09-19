import numpy as np


def getTopK(myList, k):
	# Get top k from a list
	myList.sort(reverse = True)
	return myList[:k]

def getTopKIndex(myList, k):
	# Get top k's indice from a list
	new = zip(myList,range(len(myList)))
	new.sort(reverse = True, key = lambda x: x[0])
	return [x[1] for x in new[:k]]


def getTopKArr(myArr, k):
	return -np.sort(-myArr)[:k]

def getTopKIndexArr(myArr, k):
	return np.argsort(-myArr)[:k]