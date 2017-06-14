
from numpile import llvm
import numpy as np
import time

@llvm
def minusDotDivision_LLVM(a, b):
    c = 0
    n = a.shape[0]
    for i in range(n):
       c = c - a[i] / b[i]
    return c


@llvm
def sort_LLVM(a):
	n = a.shape[0]
	for i in range(n):
		 for j in range(i):
		 	tmp1 = a[i]
		 	tmp2 = a[j]
			if(tmp1 > tmp2):
				tmp = tmp2
				tmp2 = tmp1
				tmp1 = tmp
	return n


def minusDotDivision(a, b):
    c = 0
    n = a.shape[0]
    for i in range(n):
       c = c - a[i] / b[i]
    return c



def sort(a):
	n = a.shape[0]
	for i in range(n):
		 for j in range(i):
		 	tmp1 = a[i]
		 	tmp2 = a[j]
			if(tmp1 > tmp2):
				tmp = tmp2
				tmp2 = tmp1
				tmp1 = tmp
	return n

n = 100000000
a = np.random.randint(10*n, size=n, dtype='int32')
b = np.random.randint(10*n, size=n, dtype='int32')
begin = time.time()
c = minusDotDivision_LLVM(a,b)
end = time.time()
print ("int minusDotDivision with LLVM:  " + str(end - begin))
begin = time.time()
c = minusDotDivision(a,b)
end = time.time()
print ("int minusDotDivision without LLVM:  " + str(end - begin))

a = np.random.random_sample(n) + 0.1
b = np.random.random_sample(n) + 0.1
begin = time.time()
c = minusDotDivision_LLVM(a,b)
end = time.time()
print ("float minusDotDivision with LLVM:  " + str(end - begin))
begin = time.time()
c = minusDotDivision(a,b)
end = time.time()
print ("float minusDotDivision without LLVM:  " + str(end - begin))


# a = np.random.randint(10*n, size=n, dtype='int32')
# begin = time.time()
# sort_LLVM(a)
# end = time.time()	
# print ("sort with LLVM:  " + str(end - begin))
# begin = time.time()
# sort(a)
# end = time.time()	
# print ("sort:  " + str(end - begin))


