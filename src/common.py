import multiprocessing as mp
import pandas as pd

def gen_query(baseQuery, args):
    return baseQuery.format(**args)



def parallelCompute(pfunc,arglist):
	"""
	param:
	@pfunc: the partial function that will be used for parallel computing.
			There should be an output for the function.
	@arglist: the argment that will be used to fill the pfunc.
	"""
	pool = mp.Pool(processes = mp.cpu_count() * 2 / 3) # only use 2/3 of the total cpu to avoid overload
	results = pool.map(pfunc, arglist)
	pool.close()
	pool.join()
	return results
