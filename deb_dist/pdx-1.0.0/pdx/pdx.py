import sys
import os
import json
def main():
	cur_loc=os.getcwd()
	if len(sys.argv) > 1:
		if(sys.argv[1]=="--ss"):
			if(sys.argv[2]=="make"):
				from helper import giveFileNames
				from helper import dirmake
				from helper import deletestuff
				from uploader import doDrive,doGAS
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
					print("Pdf is ready Visit the url:")
					print(res_gas)
					print(res_gas['response']['result'])
					os.chdir(cur_loc)
					deletestuff()
		
		
		
			else:
				print("Apps name:"+str(sys.argv[2]))
				from scr_oa import scroa
				scroa(sys.argv[2])
	
		elif(sys.argv[1].find(".")!=-1):
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
			print("Pdf is ready at this url:")
			print("hey",res_gas)
			print(res_gas['response']['result'])
			os.chdir(cur_loc)
			deletestuff()
		elif(sys.argv[1].find("--v")==0 or sys.argv[1].find("--version")==0):
			print("this is the best version")
		elif(sys.argv[1].find("--h")==0 or sys.argv[1].find("--help")):
			print("Help Section")
			print("--v to see the version")
			print("Use pdx filename.c or filename.py or filename.java")
			print("Use pdx --ss Appname to take the ss of the active app")
			print("After all ss are taken using --ss use 'pdx --ss make' to create the pdf")
		else:
			print("Please put --h or --help to see how to use this")
	else:
		print("Please put --h or --help to see how to use this")

if __name__ == "__main__":
    main()
