#Script to test out a hypothesis proposed by VN
#author: prakhar gaur
#date: Fri Oct 10 10:36:35 IST 2014

import argparse
from random import randint

parser = argparse.ArgumentParser()
parser.add_argument('lenghtofSeq', metavar='N', help='lenght of the nucleotide sequence', type=int)
parser.add_argument('-v', '--numberofVariants', default='6', help='Input number of variant sequences with tandem duplications, to produce for Multiple sequence alignment. Half will have tandem  and other half non tandem Default "6".')
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

print ''.join(nuclSeq)

