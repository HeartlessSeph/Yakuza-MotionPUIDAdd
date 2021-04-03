#!python3

# -*- coding: utf-8 -*-
import os
import json
import argparse
from collections import defaultdict
from collections import OrderedDict


def tree():
    def the_tree():
        return defaultdict(the_tree)
    return the_tree()
#


parser = argparse.ArgumentParser(description="PUID Entry Adding tool.")
parser.add_argument("-bep", "--file1", help="motion bep json")
parser.add_argument("-gmt", "--file2", help="motion gmt json")
parser.add_argument("-d", "--directory", help="Directory with gmt and bep lexus folders")
parser.add_argument("-old", "--oldrearmp", help="Uses old rearmp format",action="store_true")
args = parser.parse_args()
numargs = 0
filedict = OrderedDict()
kdirectory = args.directory
if args.file1 is not None:
	kfile1 = args.file1
	numargs = numargs + 1
	filedict["BEP"] = kfile1
	bepname = os.path.splitext(kfile1)[0]
if args.file2 is not None:
	kfile2 = args.file2
	numargs  = numargs + 1
	filedict["GMT"] = kfile2
	gmtname = os.path.splitext(kfile2)[0]
if numargs == 0:
	print("A gmt or bep json must be present to run the program.")
	input("Press ENTER to exit...")
	sys.exit()

NameDict = OrderedDict()


for argu in list(filedict.keys()):
	kfile = filedict[argu]
	with open(kfile, 'r', encoding='utf8') as file:
		if argu == "GMT":
			if os.path.isdir(kdirectory + "\\gmt.lexus2"): 
				motiondirectory = kdirectory + "\\gmt.lexus2"
				kfilenameonly = gmtname
			elif os.path.isdir(kdirectory + "\\gmt"): 
				motiondirectory = kdirectory + "\\gmt"
				kfilenameonly = gmtname
			else:
				input("No GMT directory present, press ENTER to exit... ")
				sys.exit()
		if argu == "BEP":
			if os.path.isdir(kdirectory + "\\bep.lexus2"): 
				motiondirectory = kdirectory + "\\bep.lexus2"
				kfilenameonly = bepname
			elif os.path.isdir(kdirectory + "\\bep"): 
				motiondirectory = kdirectory + "\\bep"
				kfilenameonly = bepname
			else:
				input("No GMT directory present, press ENTER to exit... ")
				sys.exit()
		print("")
		print("Adding " + argu + " entries to " + filedict[argu])
		
		jsonfile = tree()
		jsonfile.update(json.load(file))
		if args.oldrearmp:
			rowcount = list(jsonfile.values())[0]
			lastentry = int(list(jsonfile.keys())[rowcount])
		else:
			rowcount = list(jsonfile.values())[2]
			lastentry = int(list(jsonfile.keys())[rowcount+15])
		
		x = 0
		if args.oldrearmp: tablestart = 1
		else: tablestart = 16
		for entry in list(jsonfile.keys()):#Gets list of Movenames for verification purposes
			if x < tablestart:
				x = x + 1
			else:
				movename = list(jsonfile[entry].keys())[0]
				NameDict[movename] = ""
				x = x + 1
				
		for f in os.listdir(motiondirectory):
			entryname = os.path.splitext(f)[0]
			if entryname in NameDict:
				print(entryname + " skipped due to already being present")
			else:
				lastentry += 1
				rowcount += 1
				if args.oldrearmp:
					jsonfile[str(lastentry)] = entryname
				else:
					jsonfile[str(lastentry)][entryname]["reARMP_isValid"] = "1"
		jsonfile["ROW_COUNT"] = rowcount
		
		with open(kfilenameonly + ".json", 'w') as outfile:
			json.dump(jsonfile, outfile, indent=1, ensure_ascii=False)