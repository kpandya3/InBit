# Given ranges and a new range with start and end, merge the new range with the rest removing overlaps and duplicates

class Range(object):
	def __init__(self, start, end):
		super(Range, self).__init__()
		self.start = start
		self.end = end
	def __str__(self):
		return "[start:"+str(self.start)+",end:"+str(self.end)+"]"

def MergeRange(r_arr, r):
	res = []
	for ran in r_arr:
		if ran.start > r.end or ran.end < ran.start:
			res.append(ran)
		else:
			r.start = min(r.start, ran.start)
			r.end = max(r.end, ran.end)
	res.append(r)
	return res

r1 = Range(9,13)
r2 = Range(1,5)
r3 = Range(17,20)
rr = Range(4,10)
r = MergeRange([r1,r2,r3],rr)