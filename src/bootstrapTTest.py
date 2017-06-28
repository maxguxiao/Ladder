#!/usr/bin/python2.7
import numpy as np
import scipy as sp


def Resample(array):
	N = len(array)
	sample = np.random.choice(array, N, replace=True)
	return sample

def ResampleDF(df):
    N = len(df)
    indexes = df.index
    newIndex = Resample(indexes)
    newDF = df.loc[newIndex,]
    newDF.reset_index(drop=True, inplace=True)
    return newDF

def getMean(array):
	return array.mean()

def NPBootstrap(array, B):
	output = []
	for i in range(B):
		sample = Resample(array)
		mu = getMean(sample)
		output.append(mu)
	return output

def WechTtest(arr1, arr2, B=400):
	rearr1 = NPBootstrap(arr1, B)
	rearr2 = NPBootstrap(arr2, B)
	test = sp.stats.ttest_ind(rearr1, rearr2, equal_var=False)
	return rearr1, rearr2, test

    