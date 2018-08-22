
T = int(input())

for z in range(T):
    line = input()
    _a, _s, _m = line.find('+'), line.find('-'), line.find('*')
    if _a != -1 or _s != -1: # addition or subtraction
        if _a != -1: n1, n2 = line.split('+')
        else: n1, n2 = line.split('-')
        in1, in2 = int(n1), int(n2)
        op = '-' if (_s != -1) else '+'
        l1 = n1
        l2 = op+n2
        l4 = str(in1+in2) if (_a != -1) else str(in1-in2)
        l3 = '-'*max(len(l2),len(l4))
#        assert l4[0] != '-'
        outlen = max(len(l1),len(l3))
        print((' '*(outlen-len(l1)))+l1)
        print((' '*(outlen-len(l2)))+l2)
        print((' '*(outlen-len(l3)))+l3)
        print((' '*(outlen-len(l4)))+l4)
    else:
        assert _m != -1
        n1, n2 = line.split('*')
        in1, in2 = int(n1), int(n2)
        if len(n2) == 1:
            l1 = n1
            l2 = '*'+n2
            l4 = str(int(n1)*int(n2))
            l3 = '-'*max(len(l2),len(l4))
            outlen = max(len(l1),len(l3))
            print((' '*(outlen-len(l1)))+l1)
            print((' '*(outlen-len(l2)))+l2)
            print((' '*(outlen-len(l3)))+l3)
            print((' '*(outlen-len(l4)))+l4)
        else:
            l1 = n1
            l2 = '*'+n2
            lmid = []
            for i,d in enumerate(n2[::-1]):
                lmid.append(str(in1*int(d))+(' '*i))
            l3 = '-'*max(len(l2),len(lmid[0]))
            lans = str(in1*in2)
            ldiv = '-'*max(len(lans),len(lmid[-1]))
            outlen = max(len(l3),max(len(l) for l in lmid),len(lans))
            print((' '*(outlen-len(l1)))+l1)
            print((' '*(outlen-len(l2)))+l2)
            print((' '*(outlen-len(l3)))+l3)
            for l in lmid:
                si = l.find(' ')
                if si == -1: si = len(l)
                print((' '*(outlen-len(l)))+l[:si])
            print((' '*(outlen-len(ldiv)))+ldiv)
            print((' '*(outlen-len(lans)))+lans)
    print()
