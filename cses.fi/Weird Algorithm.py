"""
Time limit: 1.00 s Memory limit: 512 MB
Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
3→10→5→16→8→4→2→1
Your task is to simulate the execution of the algorithm for a given value of n.

Input:
3

Output:
3 10 5 16 8 4 2 1
"""
#program
number=int(input());print(number,end=" ")
while number!=1:
	if number%2==0:number=number//2
	else:number=number*3+1
	print(number,end=" ")
