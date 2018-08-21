
N = int(input())
for z in range(N):
    a, b = input().split()
    s = str(int(a[::-1])+int(b[::-1]))[::-1]
    while s[0] == '0': s = s[1:]
    print(s)
