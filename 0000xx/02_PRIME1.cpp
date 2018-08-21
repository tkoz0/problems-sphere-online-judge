#include <assert.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
typedef uint32_t u32;
#define PMAX 1000000000
#define GET_BIT(s,i) (s[i>>5] & (1 << (31-(i&31))))
#define SET_BIT(s,i) (s[i>>5] |= (1 << (31-(i&31))))

int main(int argc, char **argv)
{
    u32 *sieve = (u32*) calloc(1+(PMAX>>6),sizeof(u32)); // false/0 = prime
    // sieve only stores odd values, index i represents 2*i+1
    for (u32 i = 1; i*i <= PMAX; ++i)
    {
        u32 p = (i<<1)+1;
        if (GET_BIT(sieve,i)) continue; // composite
        for (u32 j = (p*p)>>1; j <= PMAX>>1; j += p) SET_BIT(sieve,j);
    }
    u32 t;
    int scanfr = scanf("%u",&t);
    assert(scanfr == 1);
    assert(t <= 10);
    while (t--)
    {
        u32 m, n;
        scanfr = scanf("%u%u",&m,&n);
        assert(scanfr == 2);
        assert(m and m <= n and n <= PMAX);
        if (m <= 2)
        {
            printf("2\n"); // handle only even prime separately
            m = 3;
        }
        for (u32 i = m>>1; i <= (n-1)>>1; ++i)
            if (!GET_BIT(sieve,i))
                printf("%u\n",(i<<1)+1);
        printf("\n");
    }
    free(sieve);
    return 0;
}
