#Script to split a file based on some string
#Date: 29 July 2015 IST
#Author: Prakhar Gaur

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('HMMOutputFilename', metavar='f', help='name of hmmer3 plain text outputfile, with multiple entries')

args = parser.parse_args()
inputfileName = str(args.HMMOutputFilename)

def files():
    #n = 0
    while True:
        #n += 1
	pfamIDs = ['PF01064', 'PF00069', 'PF08515', 'DEL']
	protName = 'P36897'
	for pfamID in pfamIDs:
		yield open('%s_%s.out' % (pfamID,protName), 'w')
		
patternString = r'[ok]'
fs = files()
outfile = next(fs) 
#flag = 1

with open(inputfileName) as infile:
    for line in infile:
        if patternString not in line:
            outfile.write(line)
        else:
            items = line.split(patternString)
	    outfile.write(patternString)
	    outfile = next(fs)
#	    flag += 1

##Add code to delete the | '%d.part' % flag | file.
#since this the last file and is empty and useless
