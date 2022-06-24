import sys
import os
import json
cur_loc=os.getcwd()
if(sys.argv[1]=="--ss"):
	if(sys.argv[2]=="make"):
		from helper import giveFileNames
		from helper import dirmake
		from helper import deletestuff
		from taketoDrive import doDrive,doGAS
		photoid=[]
		if(dirmake()):
			uName = raw_input("Name: ")
			uMID = raw_input("Moodle ID:")
			subName= raw_input("Subject: ")
			expNo=raw_input("Exp No:")
			uRollNo = raw_input("Roll Number: ")
			uYOS = raw_input("Year: ")
			uDiv = raw_input("Division")
			photonameslist=giveFileNames()
			for i in range(0,len(photonameslist)):
				os.chdir(cur_loc)
				photoid.append(doDrive(photonameslist[i]))
			sent_to_gas={
			"creds":{
			"name":uName,
			"rollno":uRollNo,
			"moodleid":uMID,
			"sub_name":subName,
			"exp_no":expNo,
			"div":uDiv
			},
			"code_ss_urls":photoid
			}
			sent_to_gas_str=json.dumps(sent_to_gas)
			os.chdir(cur_loc)
			res_gas=doGAS(2,sent_to_gas_str)
			print(res_gas['response']['result'])
			os.chdir(cur_loc)
			deletestuff()
		
		
		
	else:
		print("Apps name:"+str(sys.argv[2]))
		from scr_oa import scroa
		scroa(sys.argv[2])
	
elif(sys.argv[1].find(".")):
	from helper import giveFileNames
	from helper import dirmake
	from helper import deletestuff
	from scr_final import beginSS
	from uploader import doDrive,doGAS
	photoid=[]
	uName = raw_input("Name: ")
	uMID = raw_input("Moodle ID:")
	subName= raw_input("Subject: ")
	expNo=raw_input("Exp No:")
	uRollNo = raw_input("Roll Number: ")
	uYOS = raw_input("Year: ")
	uDiv = raw_input("Division")
	def filenamegiver(argument):
		spl2 = argument.split(".")
		print(spl2)
		filename = spl2[0].strip()
		ext = spl2[1].strip()
		return filename,ext
	print("Welcome I am ProDriverX")
	if(dirmake()):
		filename,ext=filenamegiver(sys.argv[1])
		print("the filename is "+filename)
		os.chdir(cur_loc)
		beginSS(filename,ext)
		photonameslist=[]
		photonameslist=giveFileNames()
		for i in range(0,len(photonameslist)):
			os.chdir(cur_loc)
			photoid.append(doDrive(photonameslist[i]))
	code_content=""
	with open(sys.argv[1],"r") as f:
		 code_content=f.read()

	sent_to_gas={
	"creds":{
	"name":uName,
	"rollno":uRollNo,
	"moodleid":uMID,
	"sub_name":subName,
	"exp_no":expNo,
	"div":uDiv
	},
	"code_content":code_content,
	"code_ss_urls":photoid
	}
	sent_to_gas_str=json.dumps(sent_to_gas)
	res_gas=doGAS(1,sent_to_gas_str)
	print(res_gas['response']['result'])
	os.chdir(cur_loc)
	deletestuff()
