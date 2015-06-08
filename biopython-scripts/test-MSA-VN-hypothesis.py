#Script to test out a hypothesis proposed by VN
#author: prakhar gaur
#date: Sat May 30 IST 2015

import argparse
from userdefinedFunctions import genrateSequence, callMuscle, tandemDuplication
from sys import exit

#argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('lenghtofAminoAcidSeq', metavar='N', help='lenght of the amino acid sequence', type=int)
parser.add_argument('-v', '--numberofVariants', default='6', help='Input number of variant sequences with tandem duplications, to produce for Multiple sequence alignment. Default "6". Value should not be greater than 33', type=int)
args = parser.parse_args()

lenght = args.lenghtofAminoAcidSeq*3
numVar = args.numberofVariants #default is assumed to be 6

if numVar > 33:
	print "***ERROR***\n Number of variant sequences (the option -v) cannot be more than 33\n Please use a value either equal to or less than 33\n"
	parser.print_help()
	exit()

#call to funtion genrateSequence() to generate random sequence
nuclSeq = genrateSequence(lenght, numVar)

#initialize the variant details file
with open('output_%dvariants-details.txt' % numVar,'w') as fileHandle2:
	fileHandle2.write('seq-name\tlocation\tduplication-percent\tduplication-size\ttotal-length-variant\n')
	fileHandle2.close()

#call function tandemDuplication(numVar, nuclSeq) to generate duplication and writw them to file
tandemDuplication(numVar, nuclSeq, lenght)

#call function to launch muscle 
callMuscle(numVar)
