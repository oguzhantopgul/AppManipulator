#!/usr/bin/python

__author__ = 'Oguzhan Topgul'

from subprocess import call
import argparse
import fileinput
import fnmatch
import os
import shutil
import string
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser(description='AppManipulator APK Repackager')
parser.add_argument('-i','--input', help='Input APK file',required=True)
parser.add_argument('-o','--output',help='Output APK file', required=False)
parser.add_argument('-f','--file', help='File to Manipulate',required=True)
parser.add_argument('-s','--search', help='Text To Search',required=True)
parser.add_argument('-r','--replace', help='Text To Replace',required=True)
args = parser.parse_args()


random = ''.join(random.choice(string.ascii_uppercase) for i in range(25))
tempFolder = random
fileToSearch = args.file
textToSearch = args.search
textToReplace = args.replace
appToBesigned = os.path.normcase(tempFolder + "/dist/" + args.input)

if not args.output:
	resultingFileName = random + ".apk"
else:
	resultingFileName = args.output

print bcolors.OKGREEN + "AppManipulator Output [*] Disassemling APK..." + bcolors.ENDC 
'''Disassemble App''' 
try:
	call(["tools/apktool", "d", args.input, "-o", tempFolder])
except Exception,err:
	print err

'''Search for file name'''
matchedFiles = []
for root, dirnames, filenames in os.walk(tempFolder):
    for filename in fnmatch.filter(filenames, fileToSearch):
        matchedFiles.append(os.path.join(root, filename))

if not matchedFiles:
	print "File can not be found!"
else:
	print "Folloing files are being replaced"
	for matched in matchedFiles:
		print bcolors.OKBLUE + "AppManipulatorOutput [*] File:" + matched + bcolors.ENDC 

print bcolors.OKGREEN + "AppManipulator Output [*] Replacing Strings..." + bcolors.ENDC 

'''Find and Replace'''
for matchedFile in matchedFiles:
	f = open(matchedFile,'r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace(textToSearch,textToReplace)

	f = open(matchedFile,'w')
	f.write(newdata)
	f.close()

print bcolors.OKGREEN + "AppManipulator Output [*] Assembling APK Again..." + bcolors.ENDC 

'''Assemble App Again'''
call(["tools/apktool", "b", tempFolder])

print bcolors.OKGREEN + "AppManipulator Output [*] Signing Repackaged APK..." + bcolors.ENDC 

'''Sign App'''
call(["tools/jarsigner", "-sigalg", "SHA1withRSA", "-digestalg", "SHA1", "-keystore", "testkeystore", "-storepass", "testtest", appToBesigned, "testkey"])

'''Move Output File'''
shutil.move(appToBesigned, resultingFileName)
print bcolors.OKGREEN + "AppManipulator Output [*] Repackaged APK Succesfully Created!" + bcolors.ENDC

'''Remove Temp Directory'''
print bcolors.OKBLUE + "AppManipulator Output [*] Clean Up in Progres..." + bcolors.ENDC
shutil.rmtree(tempFolder)

print bcolors.OKGREEN + "AppManipulator Output [*] DONE!" + bcolors.ENDC

