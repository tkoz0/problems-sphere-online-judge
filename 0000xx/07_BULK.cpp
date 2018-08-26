#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
typedef uint32_t u32;
#define CUBE_SPACE 1000
#include <unordered_set>

struct face
{
    // represent by lower coordinate cube and direction of coordinate + 1
    u32 x, y, z, d;
    face(u32 _x, u32_y, u32_z, u32 _d)
    {
        // d value: 1 --> x+1, 2 --> y+1, 3 --> z+1
        assert(d == 1 or d == 2 or d == 3);
        x = _x;
        y = _y;
        z = _z;
        d = _d;
    }
};

struct point
{
    u32 x, y, z;
    point(u32 _x, u32 _y, u32 _z)
    {
        x = _x;
        y = _y;
        z = _z;
    }
};

int main(int argc, char **argv)
{
    u32 T, V;
    std::unordered_set<face> faces;
    std::unordered_set<point> points;
    int scanfr = scanf("%u",&T);
    assert(scanfr == 1);
    while (T--)
    {
        faces.clear();
        points.clear();
        u32 F, P, X, Y, Z;
        scanfr = scanf("%u",&F);
        assert(scanfr == 1);
        assert(6 <= F and F <= 250);
        while (F--)
        {
            scanfr = scanf("%u",&P);
            assert(scanfr == 1);
            assert(4 <= P <= 200);
            while (P--)
            {
                scanfr = scanf("%u%u%u",&X,&Y,&Z);
                assert(scanfr == 3);
                assert(X <= CUBE_SPACE);
                assert(Y <= CUBE_SPACE);
                assert(Z <= CUBE_SPACE);
            }
        }
        printf("The bulk is composed of %u units.\n",V);
    }
    return 0;
}
