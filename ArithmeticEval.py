# Evaluate the expression given string with braces, + and - 
# i.e. input: "(2-(6+1+3)-5)+(8+7)", output: "2"

# Calculate answer given string with +, - operations and brackets
def popUntilStart(stack):
    tmp = []
    while len(stack) > 0:
        item = stack.pop()
        if item == '(':
            break
        tmp.append(item)
    return tmp

def simpleEval(l):
    val = int(l.pop())
    for i in range(len(l)-1, 0, -2):
        if l[i] == '+':
            val = val + int(l[i-1])
        else:
            val = val - int(l[i-1])
    return val

def evalCalc(exp):
    stack = []
    for i in range(len(exp)):
        if exp[i] == ')':
            tmp_stack = popUntilStart(stack)
            stack.append(simpleEval(tmp_stack))
        else:
            stack.append(exp[i])
    return simpleEval(stack)

print(evalCalc('(2-(6+1+3)-5)+(8+7)'))