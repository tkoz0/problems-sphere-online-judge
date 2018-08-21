import math

# Z(N) = number of zeroes at end of Z!
# min(multiplicity of 2, multiplicity of 5)

nmax = 10**9

p2 = list(2**i for i in range(1,1+int(math.log2(nmax))))
p5 = list(5**i for i in range(1,1+int(math.log(nmax)/math.log(5.0))))

T = int(input())

for z in range(T):
    N = int(input())
    assert 1 <= N <= nmax
    m2, m5 = 0, 0
    for f in p2:
        if f > N: break
        m2 += N//f
    for f in p5:
        if f > N: break
        m5 += N//f
    print(min(m2,m5))
