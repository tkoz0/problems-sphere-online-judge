
def convert(expr,a,b): # convert expression in range [a,b)
    assert 0 <= a < b <= len(expr), 'recursion parameter error a=%d b=%d'%(a,b)
    exprs = [] # list of [a,b) ranges to parse recursively
    op = ''
    i = a
    while i < b:
        if expr[i] in 'abcdefghijklmnopqrstuvwxyz':
            exprs.append((i,i+1))
            i += 1
            if i < b:
                assert expr[i] in '+-*/^', 'expected operator at i=%d'%i
                op = expr[i]
                i += 1
                assert i < b, 'expected expression at i=%d'%i
        elif expr[i] == '(': # read until matched )
            open = 1 # number of opening parenthesis to close
            j = i+1
            while j < b:
                if expr[j] == '(': open += 1
                elif expr[j] == ')':
                    open -= 1
                    if open == 0: break
                j += 1
            assert open == 0, 'bad parenthesis for expr from i=%d to j=%d'%(i,b)
            j += 1
            exprs.append((i,j))
            if j < b:
                assert expr[j] in '+-*/^', 'expected operator at j=%d'%j
                op = expr[j]
                j += 1
                assert j < b, 'expected expression at j=%d'%j
            i = j
    assert len(exprs) != 0, 'no expressions between i=%d and j=%d'%(a,b)
    assert len(exprs) <= 2, 'more than 2 operands from i=%d to j=%d'%(a,b)
    if len(exprs) == 1:
        if exprs[0][1]-exprs[0][0] == 1: # single char variable
            return expr[exprs[0][0]]
        else: # parse without outer parenthesis
            assert expr[exprs[0][0]] == '(' and expr[exprs[0][1]-1] == ')'
            return convert(expr,exprs[0][0]+1,exprs[0][1]-1)
    elif len(exprs) == 2:
        assert op != '', \
                'fail to find operator between 2 expression i=%d to j=%d'%(a,b)
        return convert(expr,exprs[0][0],exprs[0][1]) \
            + convert(expr,exprs[1][0],exprs[1][1]) + op

t = int(input())
assert t <= 100

for e in range(t):
    expr = input()
    assert 1 <= len(expr) <= 400
    print(convert(expr,0,len(expr)))
