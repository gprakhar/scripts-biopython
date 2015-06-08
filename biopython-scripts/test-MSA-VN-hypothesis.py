#Script to test out a hypothesis proposed by VN
#author: prakhar gaur
#date: Sat May 30 IST 2015

import argparse
from random import randint
from Bio.Align.Applications import MuscleCommandline
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
'''
#temp list variables for generating variants
varSeq = list()
nuclSeq_Slice = list()

#the variant generation loop
for itrate in range(1,numVar+1):
	locDup = randint(0,lenght) #random location for duplication insertion
#	print "temp%d location of dplication: %d" % (itrate, locDup)
	#size of duplication based on percentage (in multiples of 3), the value has to be converted to int before useage
	sizeDup = ((3*itrate)/100.0)*lenght # BUG what will happen when itrate value goes above 100 # SOLUTION conditional to not let percentage go beyond 49%
#	print "temp%d size of duplication in int: %f" % (itrate, int(sizeDup))
	#if location of duplication insertion is greater than half of lenght of sequence, than copy duplication from upstream otherwise		downstream
	if locDup < (lenght-locDup):
		NuclSeq_Slice = nuclSeq[locDup:int(locDup+sizeDup)]
#		print "NuclSeq_Slice len = %d :%s" % (len(NuclSeq_Slice), NuclSeq_Slice)
#		print "temp%d: len=%d :%s" % (itrate, len(varSeq), varSeq)
		varSeq = nuclSeq[:locDup]
#		print "temp%d: R1 len=%d :%s" % (itrate, len(varSeq), varSeq)
		varSeq.extend(NuclSeq_Slice)
#		print "temp%d: R2 len=%d :%s" % (itrate, len(varSeq), varSeq)
		varSeq.extend(nuclSeq[locDup:])
	else:
		NuclSeq_Slice = nuclSeq[int(locDup-sizeDup):locDup]
#		print "NuclSeq_Slice len = %d :%s" % (len(NuclSeq_Slice), NuclSeq_Slice)
#               print "temp%d: len=%d :%s" % (itrate, len(varSeq), varSeq)
		varSeq = nuclSeq[:int(locDup-sizeDup)]
#		print "temp%d: R1 len=%d :%s" % (itrate, len(varSeq), varSeq)
                varSeq.extend(NuclSeq_Slice)
#		print "temp%d: R2 len=%d :%s" % (itrate, len(varSeq), varSeq)
                varSeq.extend(nuclSeq[int(locDup-sizeDup):])
#	print "temp%d: R-fi len=%d :%s" % (itrate, len(varSeq), varSeq)
	#write the variant sequence to file
	with open('output_%dvariants.fa' % numVar,'a') as fileHandle3:
		fileHandle3.write('>var-seq%d\n' % itrate)
		fileHandle3.write("".join(varSeq))
		fileHandle3.write("\n")
		fileHandle3.close()
	#write variant sequence details to file 
	with open('output_%dvariants-details.txt' % numVar,'a') as fileHandle4:
		fileHandle4.write('var-seq%d\t%d\t%d\t%d\t%d\n' % (itrate, locDup, itrate*3, int(sizeDup), len(varSeq)))
		fileHandle4.close()
	del varSeq[:] #empty out the temp lists
        del nuclSeq_Slice[:]

'''
callMuscle(numVar)
