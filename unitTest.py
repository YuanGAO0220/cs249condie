
from numpile import llvm
import numpy as np
import time
from random import randint

@llvm
def testIf_LLVM(a):
	tmp1 = a[0]
	tmp2 = a[1]
	tmp = tmp2
	if(tmp1 > tmp2):
		tmp = tmp1
	return tmp

@llvm
def testSub_LLVM(a):
	tmp1 = a[0]
	tmp2 = a[1]
	return tmp1 - tmp2

@llvm
def testDiv_LLVM(a):
	tmp1 = a[0]
	tmp2 = a[1]
	return tmp1 / tmp2

def testIf(a):
    tmp1 = a[0]
    tmp2 = a[1]
    tmp = tmp2
    if(tmp1 > tmp2):
    	tmp = tmp1
    return tmp

def testSub(a):
	tmp1 = a[0]
	tmp2 = a[1]
	return tmp1 - tmp2

def testDiv(a):
	tmp1 = a[0]
	tmp2 = a[1]
	return tmp1 / tmp2



a = np.random.randint(100, size=2, dtype='int32')
res1 = testIf_LLVM(a)
res2 = testIf(a)
if (res1 == res2):
	print ("IF unit test pass")
else :
	print ("IF unit test failed")


res1 = testSub_LLVM(a)
res2 = testSub(a)
if (res1 == res2):
	print ("Subtract unit test pass")
else :
	print ("Subtract unit test failed")

res1 = testDiv_LLVM(a)
res2 = testDiv(a)
if (res1 == res2):
	print ("Division unit test pass")
else :
	print ("Division unit test failed")


