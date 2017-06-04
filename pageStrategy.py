#	-*- coding:utf-8 -*-

from collections import OrderedDict

__author__ = "Link"

def Optimal(page, resLength, show = True):

	# use dist as page at now exchange with the next one
	dist = 0
	rest = []
	reElem = 0
	end = len(page)
	num = 0
	for i in range(end):
		dist = 0
		# if this one not in the pages
		if page[i] not in rest:
			if len(rest) < resLength:
				rest.append(page[i])
			else:
				for each in rest:
					try:
						tmp = page.index(each, i ,end)
						dist = max(tmp, dist)
						reElem = each if dist == tmp else reElem
					except Exception as e:
						dist = end + 1
						reElem = each
					# print("now re is %d"%reElem)
				rest.remove(reElem)
				rest.append(page[i])
			num += 1
			if show:
				print("Page Fault Happened at {} ,now rest is {}".format(page[i], rest))

	print("Page Fault happen %d times"%num)
	return rest

def LeastRecentUsed(page, resLength, show = True):
	# use dist as page at now exchange with the next one
	dist = 0
	rest = []
	reElem = -1
	end = len(page)
	num = 0
	for i in range(end):
		dist = 0
		# if this one not in the pages
		if page[i] not in rest:
			if len(rest) < resLength:
				rest.append(page[i])
			else:
				for each in rest:
					# find the 
					tmpPage = page[:i][::-1]
					# print(tmpPage)
					tmp = tmpPage.index(each, 0 ,i)
					dist = max(tmp, dist)
					reElem = each if dist == tmp else reElem
					# print("now re is %d"%reElem)
				rest.remove(reElem)
				rest.append(page[i])
			num += 1
			if show:
				print("Page Fault Happened at {} ,now rest is {}".format(page[i], rest))

	print("Page Fault happen %d times"%num)
	return rest


def readPage(page):
	for each in page:
		if page[each] == 0:
			return each
		page[each] = 0

	for each in page:
		if page[each] == 0:
			return each



def Clock(page, restLength, show = True):
	rest = OrderedDict()
	reElem = -1
	end = len(page)
	num = 0
	for i in range(end):
		dist = 0
		if page[i] not in rest:
			if len(rest) < restLength:
				rest[page[i]] = 1
			else:
				# use circle to delete the page
				reElem = readPage(rest)
				rest.pop(reElem)
				rest[page[i]] = 1
			if show:
				print("Page Fault Happened at {} ,now rest is {}".format(page[i], rest))
			num += 1
		else:
			rest[page[i]] = 1
	print("Page Fault happen %d times"%num)
	return rest


if __name__ == '__main__':
	test = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
	test2 = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
	for i in range(1,8):
		# Optimal(test ,i, False)
		# LeastRecentUsed(test, i, False)
		Clock(test, i, False)



			
