#include <stdio.h>
void main()
{
		unsigned int a = 0,sum = 0;
	for (; a<= 1000; a++)
	{
		if ( (!(a %3)) || (!(a%5) ) )
		printf("\n adding %u to %u", a, sum),sum += a;
	}
	printf("\nSum = %u", sum);
}	
