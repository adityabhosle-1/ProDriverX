import os
def output_counter():
	lines=[]
	with open("output.txt","r") as f:
		lines=f.readlines()
	


	count=len(lines)-1
	print("No of output lines are")
	return count
