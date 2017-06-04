#	-*- coding:utf-8 -*-

__author__ = "Link"

"""
模拟银行家算法
1. 能够给出当前状态是否为安全
2. 当给出新的请求的时候，能够给出请求是否合理
"""

def compareVector(vector1, vector2):
	"""
	compare two vector
	if each of vector1 >= vector2, return True
	else return False
	"""
	length = len(vector1)
	if length != len(vector2):
		print("two vector is not same length")
		return -2
	for i in range(length):
		if vector1[i] < vector2[i]:
			return False

	return True



def ProcessSafety(available, maxNeed, allocation, need):
	"""
	checkout whether this process is safety

	available: a vector save the rest resource
	maxNeed: a n*m matrix record n process which need No m's resource.for example: maxNeed[i][j] = t means the Pi need t j resource
	allocation: a n*m matrix record resource now operation system has allocato to each process 
	need: a n*m matrix record record resource now each process is needed
	"""
	work = available
	length = len(maxNeed)
	finish = [False]*length
	findProcess = False
	while False in finish:
		for i in range(length):
			if not finish[i] and compareVector(work, need[i]):
				work = [t1+t2 for t1,t2 in zip(work, allocation[i])]
				findProcess = True
				finish[i] = True
				break
		if not findProcess:
			return False
		findProcess = False

	return True

def newRequesti(available, maxNeed, allocation, need, request, index):
	"""
	if get new request, to checkout whether is safe or not
	

	available: a vector save the rest resource
	maxNeed: a n*m matrix record n process which need No m's resource.for example: maxNeed[i][j] = t means the Pi need t j resource
	allocation: a n*m matrix record resource now operation system has allocato to each process 
	need: a n*m matrix record record resource now each process is needed
	request: a array of new request for resource
	index: index of which process is request 
	"""
	if compareVector(request, need[index]):
		print("request is much than it !")
		return False
	if compareVector(request, available):
		print("not have enough resource")
		return False
	need[index] = [i-j for i,j in zip(need[index], request)]
	allocation[index] = [i+j for i,j in zip(allocation[index], request)]
	available = [i-j for i,j in zip(available, request)]

	return ProcessSafety(available, maxNeed, allocation, need)

if __name__ == '__main__':
	maxNeed = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
	allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
	need = [[7,4,3],[1,2,2],[6,0,0],[0,1,1],[4,3,1]]
	available = [3,3,2]
	if newRequesti(available, maxNeed, allocation, need, [1,0,2], 1):	
	# if ProcessSafety(available, maxNeed, allocation, need):
		print("get it !")
	else:
		print("something wrong...")