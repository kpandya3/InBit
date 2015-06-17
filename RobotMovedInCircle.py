# A robot either moves forward ('G'), turns left ('L') or turns right ('R'). You are given a string that contains these robot movements.
# Given the string, determine if the robot goes in circle when the movements are run infinite time. Return "YES" if it does, otherwise return "NO"

import operator
op = {"+": operator.add, "-": operator.sub}
def doesCircleExists(commands):
	pos, ind, oprtr = doSingleRun([0,0], commands, 1, "+")
	pos, ind, oprtr = doSingleRun(pos, commands, ind, oprtr)
	pos, ind, oprtr = doSingleRun(pos, commands, ind, oprtr)
	pos, ind, oprtr = doSingleRun(pos, commands, ind, oprtr)
	if pos == [0, 0]
		return "YES"
	return "NO"

def doSingleRun(pos, commands, index, opr):
	direction = "N"
	# index to change for move (either 0 or 1), for north and south, 1, else 0
	ind = index
	# add or subtract
	oprtr = opr
	for i in commands:
		if i == "G":
			pos = moveInDir(pos, ind, oprtr)
		else:
			ind, oprtr = changeDir(ind, oprtr, i)
	return (pos, ind, oprtr)

def changeDir(cur_ind, cur_oprtr, cmd):
	if cur_ind == 1:
		if cmd == "L":
			if cur_oprtr == "+":
				return (0, "-")
			else:
				return (0, "+")
		else:
			if cur_oprtr == "+":
				return (0, "+")
			else:
				return (0, "-")
	else:
		if cmd == "L":
			if cur_oprtr == "+":
				return (1, "+")
			else:
				return (1, "-")
		else:
			if cur_oprtr == "+":
				return (1, "-")
			else:
				return (1, "+")

def moveInDir(pos, ind, oprtr):
	pos[ind] = op[oprtr](int(pos[ind]), 1)
	return pos

print(doesCircleExists('GGGGR'))
