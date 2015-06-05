#Script to test out a hypothesis proposed by VN
#author: prakhar gaur
#date: Sat May 30 IST 2015

import argparse
from random import randint

parser = argparse.ArgumentParser()
parser.add_argument('lenghtofAminoAcidSeq', metavar='N', help='lenght of the amino acid sequence', type=int, default='34')
parser.add_argument('-v', '--numberofVariants', default='6', help='Input number of variant sequences with tandem duplications, to produce for Multiple sequence alignment. Half will have tandem  and other half non tandem Default "6".', type=int)
args = parser.parse_args()

lenght = args.lenghtofAminoAcidSeq*3
numVar = args.numberofVariants #default is assumed to be 6
nuclSeq = list()

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

with open('output_%dvariants.fa' % numVar, 'w') as fileHandle1:
	fileHandle1.write(">ori-seq\n")
	fileHandle1.write("".join(nuclSeq))
	fileHandle1.write("\n")
	fileHandle1.close()
	
print ("".join(nuclSeq))

varSeq = list()
nuclSeq_Slice = list()
for itrate in range(1,numVar+1):
	locDup = randint(0,lenght)
	print "temp%d location of dplication: %d" % (itrate, locDup)
	sizeDup = ((3*itrate)/100.0)*lenght # BUG what will happen when itrate value goes above 100 # SOLUTION conditional to not let percentage go beyond 49%
	print "temp%d size of duplication in int: %f" % (itrate, int(sizeDup))
	if locDup < (lenght-locDup):
		NuclSeq_Slice = nuclSeq[locDup:int(locDup+sizeDup)]
		print "NuclSeq_Slice len = %d :%s" % (len(NuclSeq_Slice), NuclSeq_Slice)
		print "temp%d: len=%d :%s" % (itrate, len(varSeq), varSeq)
		varSeq = nuclSeq[:locDup]
		print "temp%d: R1 len=%d :%s" % (itrate, len(varSeq), varSeq)
		varSeq.extend(NuclSeq_Slice)
		print "temp%d: R2 len=%d :%s" % (itrate, len(varSeq), varSeq)
		varSeq.extend(nuclSeq[locDup:])
	else:
		pass
#		temp.append(nuclSeq.insert(locDup, nuclSeq[locDup-sizeDup:locDup]))
	print "temp%d: R-fi len=%d :%s" % (itrate, len(varSeq), varSeq)
	del varSeq[:]
'''	with open('output_%dvariants.fa' % numVar,'a') as fileHandle2:
		fileHandle2.write('>var-seq%d\n' % itrate)
		fileHandle2.write("".join(temp))
		fileHandle1.write("\n")
		fileHandle2.close()
	del temp[:]
'''



			
	

