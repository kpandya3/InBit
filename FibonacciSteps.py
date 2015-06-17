# You are climbing a stair case. Each time you can either   make 1 step or 2 steps. The staircase has n steps. In how many distinct ways can you climb the staircase ?

# steps(n) to take n steps in singles/doubles
allSteps = []
def steps(n, stepsSoFar=""):
	if n == 0:
		allSteps.append(stepsSoFar)
	elif n == 1:
		stepsSoFar+="1"
		allSteps.append(stepsSoFar)
	else:
		stepsSoFar2 = stepsSoFar
		stepsSoFar += "1"
		steps(n-1, stepsSoFar)
		stepsSoFar2 += "2"
		steps(n-2, stepsSoFar2)

steps(3)
print(allSteps)
