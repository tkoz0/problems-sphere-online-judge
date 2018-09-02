
TSIZE = 101

def hash(key):
    global TSIZE
    return (19*sum((i+1)*ord(key[i]) for i in range(len(key))))%TSIZE

# resolve collisions with open addressing:
# (hash(key) + j*j + 23*j) mod 101 for j in [1,19]
# after that assume insertion cant be done

t = int(input())
for case in range(t):
    numops = int(input())
    assert numops <= 1000
    ht = [None]*TSIZE # hash table
    htsize = 0 # number of keys saved
    for opnum in range(numops):
        op = input().split(':')
        if op[0] == 'ADD':
            h = hash(op[1])
            empty = -1
            intable = False
            for j in range(20): # try to insert key up to 20 times
                i = (h + j*j + 23*j)%TSIZE
                if empty == -1 and (ht[i] is None): empty = i # first empty
                if ht[i] == op[1]: intable = True
            if not intable and empty != -1: ht[empty] = op[1]; htsize += 1
        elif op[0] == 'DEL':
            h = hash(op[1])
            for j in range(20): # try to find key
                i = (h + j*j + 23*j)%TSIZE
                if ht[i] == op[1]: htsize -= 1; ht[i] = None; break
        else: assert 0 # ignore
    print(htsize)
    for i,k in enumerate(ht):
        if not (k is None): print('%d:%s'%(i,k))
