#Script to test out a hypothesis proposed by VN
#author: prakhar gaur
#date: Sat May 30 IST 2015

import argparse
from random import randint
from Bio.Align.Applications import MuscleCommandline

parser = argparse.ArgumentParser()
parser.add_argument('lenghtofAminoAcidSeq', metavar='N', help='lenght of the amino acid sequence', type=int, default='34')
parser.add_argument('-v', '--numberofVariants', default='6', help='Input number of variant sequences with tandem duplications, to produce for Multiple sequence alignment. Half will have tandem  and other half non tandem Default "6".', type=int)
args = parser.parse_args()

lenght = args.lenghtofAminoAcidSeq*3
numVar = args.numberofVariants #default is assumed to be 6
nuclSeq = list()

##generate random nulcletide sequence
for i in range(0,lenght):
	numRand = randint(1,4)
	if numRand == 1:
		nuclSeq.append('A')
	elif numRand == 2:
		nuclSeq.append('T')
	elif numRand == 3:
                nuclSeq.append('G')
	elif numRand == 4:
                nuclSeq.append('C')
##write random nulcletide sequence to file
with open('output_%dvariants.fa' % numVar, 'w') as fileHandle1:
	fileHandle1.write(">ori-seq\n")
	fileHandle1.write("".join(nuclSeq))
	fileHandle1.write("\n")
	fileHandle1.close()

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
	with open('output_%dvariants.fa' % numVar,'a') as fileHandle2:
		fileHandle2.write('>var-seq%d\n' % itrate)
		fileHandle2.write("".join(varSeq))
		fileHandle2.write("\n")
		fileHandle2.close()
	del varSeq[:] #empty out the temp lists
        del nuclSeq_Slice[:]

#code for Muscle alignment of sequences
muscle_exe = r'/home/littleboy/local_bin/muscle-MSA/muscle3.8.31_i86linux64'
muscle_cline = MuscleCommandline(muscle_exe, input='output_%dvariants.fa' % numVar, out='muscle-out%dvariants.aln' % numVar, clw=True) #build command
muscle_cline() #execute command
