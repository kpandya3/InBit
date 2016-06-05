# You are climbing a stair case. Each time you can either make 1 step or 2 steps.
# The staircase has n steps. In how many distinct ways can you climb the staircase ?

# steps(n) to take n steps in singles/doubles

_cache = {
	0: 0,
	1: 1
}

def steps(n):
	if n in _cache:
		return _cache[n]

	for i in xrange(2, n+1):
		_cache[i] = _cache[i - 1] + _cache[i - 2] + 2

	return _cache[n]

print steps(1)
print steps(2)
print steps(3)
print steps(4)

# allSteps = []

# _cache = {
# 	0: "",
# 	1: "1"
# }

# def steps(n, stepsSoFar=""):
# 	if n in _cache:
# 		stepsSoFar += _cache[n]
# 		allSteps.append(stepsSoFar)

# 	for i in xrange(2, n + 1):
# 		_cache[i] = 0

# 		for j in [1, 2]:
# 			if _ca

# 	stepsSoFar2 = stepsSoFar
# 	stepsSoFar += "1"
# 	steps(n-1, stepsSoFar)
# 	stepsSoFar2 += "2"
# 	steps(n-2, stepsSoFar2)

# steps(3)
# print(allSteps)
