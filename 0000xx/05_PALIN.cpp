#include <assert.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <iostream>
#include <string>
typedef uint32_t u32;

int main(int argc, char **argv)
{
    u32 t;
    int scanfr = scanf("%u",&t);
    assert(scanfr == 1);
    std::string K;
    std::getline(std::cin,K); // finish reading line containing t
    std::string s1, s2;
    while (t--)
    {
        std::getline(std::cin,K); // read number as a string
        assert(K != "");
        // first take 1st half in reverse order and compare it to 2nd half
        // if greater, output that, else increment first half (middle if number
        // is odd length), and output palindrome of that
        u32 i = K.length()/2; // i-1,i-2,...,0
        u32 j = K.length()-i; // j,j+1,...,len(K)-1
        bool greater = false;
        while (i--)
        {
            if (K[i] > K[j]) { greater = true; break; } // greater
            else if (K[i] < K[j]) { greater = false; break; } // less
            ++j;
        }
        if (greater) // output first half, (middle if len odd), then its reverse
        {
            s2 = "";
            for (u32 z = 0; z < K.length()/2; ++z) s2 += K[z];
            if (K.length() % 2) s2 += K[K.length()/2];
            for (u32 z = K.length()/2; z--;) s2 += K[z];
            std::cout << s2 << std::endl;
        }
        else // increment first half (middle if len odd)
        {
            if (K.length() % 2) // increment middle
            {
                K[K.length()/2] = K[K.length()/2]+1;
                u32 z = K.length()/2;
                while (z)
                {
                    if (K[z] == '0'+10) // carry
                    {
                        K[z] = '0';
                        --z;
                        K[z] = K[z]+1;
                    }
                    else break; // carry done
                }
                s2 = "";
                if (!z and K[0] == '0'+10) // must append extra digit
                {
                    K[0] = '0';
                    s2 += '1';
                    for (u32 y = 0; y < K.length()/2; ++y) s2 += K[y];
                    for (u32 y = K.length()/2; y--;) s2 += K[y];
                    s2 += '1';
                }
                else
                {
                    for (u32 y = 0; y <= K.length()/2; ++y) s2 += K[y];
                    for (u32 y = K.length()/2; y--;) s2 += K[y];
                }
                std::cout << s2 << std::endl;
            }
            else // increment first half
            {
                K[K.length()/2-1] = K[K.length()/2-1]+1;
                u32 z = K.length()/2-1;
                while (z)
                {
                    if (K[z] == '0'+10) // carry
                    {
                        K[z] = '0';
                        --z;
                        K[z] = K[z]+1;
                    }
                    else break; // carry done
                }
                s2 = "";
                if (!z and K[0] == '0'+10) // append extra digit
                {
                    K[0] = '0';
                    s2 += '1';
                    for (u32 y = 0; y <= K.length()/2-1; ++y) s2 += K[y];
                    for (u32 y = K.length()/2-1; y--;) s2 += K[y];
                    s2 += '1';
                }
                else
                {
                    for (u32 y = 0; y < K.length()/2; ++y) s2 += K[y];
                    for (u32 y = K.length()/2; y--;) s2 += K[y];
                }
                std::cout << s2 << std::endl;
            }
        }
    }
    return 0;
}
