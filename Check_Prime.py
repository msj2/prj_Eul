#ver1
import math


prime = input("Enter the number to check:")
max = int(math.sqrt(float(prime)))

print "Will check until",max,"+1"
#Just take the next no. to max
max = max + 1
i = 0
if (prime % 2 == 0):
	print prime,"is an even number, So, it is not prime"
else:
	print prime," is not even number, So checking for prime no...\
continues"
	for i in range(3,max,1):
		if ((prime % i) == 0):
			print i,"divides",prime
			break
			#exit # This does not exit the for loop, Loop continues
		else:
			print i,"does not divides", prime
	#else:

		print "i is now",i	
		if (i>= (max)):
			print i,"is >=",max, "So, ",prime, " is prime number"
		else:
			print i," < ", max, "So, ",prime, " is not prim"
