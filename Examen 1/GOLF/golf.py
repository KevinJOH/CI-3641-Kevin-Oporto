import math as m
from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
	return n if n<3 else (f(n-1) + f(n-2) + f(n-3))
def N(n,k):
	return (1/n)*m.comb(n,k)*m.comb(n,k-1)
def M(n):
	return f(m.floor(m.log2(N(n,m.floor(m.log2(n)))))+1)
n=50
print(M(n))