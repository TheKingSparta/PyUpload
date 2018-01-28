#!Python36
#Shebang!

#Import libraries
import os
#import oauth2client
import zipfile
import sys
#/Libs

print("Hello there!")



dir = input("What would you like to upload? ")
valid = os.path.isfile(dir)
if(dir == "quit"):
		quit()

while(valid != True):
	dir = input("Sorry, that doesn't seem to be a real directory, please pick a different one, or type 'quit' to cancel ")
	valid = os.path.isdir(dir)
	if(dir == "quit"):
		quit()

def Upload(file):
	return
	
def Download(file):
	return
	
def Zip(file, arcname):
	ZipFile.write(file, acrname)
	return 
	
def Unzip(file, destination):
	with ZipFile(file) as project:
		project.extractall(destination)
	return
	
def GetProject(unzip):
	return
	
def PushProject(zip):
	return
	