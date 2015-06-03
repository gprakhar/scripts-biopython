#Script to test out a hypothesis proposed by VN
#author: prakhar gaur
#date: Fri Oct 10 10:36:35 IST 2014

import argparse
from random import randint
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('lenghtofSeq', metavar='N', help='lenght of the nucleotide sequence', type=int)
parser.add_argument('-v', '--numberofVariants', default='6', help='Input number of variant sequences with tandem duplications, to produce for Multiple sequence alignment. Half will have tandem  and other half non tandem Default "6".', type=int)
args = parser.parse_args()

lenght = args.lenghtofSeq
numVar = args.numberofVariants #default would be assumed to be 6
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

with open('output_%dvariants.fa' % numVar,'w') as fileHandle1:
	fileHandle1.write(">ori-seq\n")
	fileHandle1.write("".join(nuclSeq))
	fileHandle1.write("\n")
	fileHandle1.close()
	print ("".join(nuclSeq))

temp = list()
for itrate in range(numVar):
	locDup = randint(1,lenght)
	sizeDup = ((3*itrate)/100)*lenght
	if locDup < (lenght-locDup):
		temp.append(nuclSeq.insert(locDup, nuclSeq[locDup+1:locDup+1+sizeDup]))
	else:
		temp.append(nuclSeq.insert(locDup, nuclSeq[locDup-sizeDup:locDup]))
	print ("".join(temp))
	del temp[:]
'''	with open('output_%dvariants.fa' % numVar,'a') as fileHandle2:
		fileHandle2.write('>var-seq%d\n' % itrate)
		fileHandle2.write("".join(temp))
		fileHandle1.write("\n")
		fileHandle2.close()
	del temp[:]
'''



			
	

