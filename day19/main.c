#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

int main() {
  uint32_t r0 = 1, r1 = 0, r2 = 0, r4 = 0, r5 = 0;

  r1 = 1;
  r2 = 1;
  r4 = 961;
  while (r1<=r4)
  {
    printf("r0 = %d, r1 = %d\n", r0, r1);
    while (r2 <= r4)
    {
      r5 = r1*r2;
      if (r5 == r4)
      {
        r0 += r1;
      }
      r2 += 1;
    }
    r1 += 1;         //addi 1 1 1
  }
  printf("r0 = %d\n",r0);
  return 0;
}


/*
l0: goto l17;         //addi 3 16 3
l1: r1 = 1;           //seti 1 2 1
l2: r2 = 1;           //seti 1 1 2
l3: r5 = r1*r2;       //mulr 1 2 5
l4: if (r5 == r4)     //eqrr 5 4 5
                      //addr 5 3 3
      goto l7;
    else
      goto l6;
l6: goto l8; //r3 += 1; addi 3 1 3
l7: r0 += r1;         //addr 1 0 0
l8: r2 += 1;          //addi 2 1 2
l9: if (r2 > r4)      //gtrr 2 4 5
l10:                  //addr 3 5 3
      goto l12;
    else
      goto l11;
l11: goto l3;         //seti 2 3 3
l12: r1 += 1;         //addi 1 1 1
    //printf("r1 = %d, r2 = %d, r4 = %d\n", r1, r2, r4);
l13: if (r1 > r4)     //gtrr 1 4 5
l14:                  //addr 5 3 3
      goto l16;
    else
      goto l15;
l15: goto l2;         //seti 1 6 3
l16:                  //mulr 3 3 3
     printf("r0 = %d\n",r0);
     exit(0);
l17: r5 = 125;
     r4 = 961;
     printf("After init, r5 = %d and r4 = %d\n", r5, r4);
     fflush(stdout);
l25:                  //addr 3 0 3
    if (r0 == 1)
      goto l27;
    else if (r0 == 0)
      goto l26;
    else
      printf("unsupported r0 (%d) at line %d\n", r0, __LINE__);
l26: goto l1;         //seti 0 6 3
l27: r5 = 27;         //setr 3 5 5
l28: r5 *= 28;        //mulr 5 3 5
l29: r5 += 29;        //addr 3 5 5
l30: r5 *= 30;        //mulr 3 5 5
l31: r5 *= 14;        //muli 5 14 5
l32: r5 *= 32;        //mulr 5 3 5
l33: r4 += r5;        //addr 4 5 4
l34: r0 = 0;          //seti 0 5 0
     printf("After long init, r5 = %d and r4 = %d\n", r5, r4);
     fflush(stdout);
l35: goto l1;         //seti 0 1 3
}
*/
