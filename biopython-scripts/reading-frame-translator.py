#Script to translate CDS sequence to corresponding protei seq
#author: Prakhar gaur
#date: 13 July 2015

from Bio import SeqIO
from Bio.SeqUtils import six_frame_translations

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('nameofInputfile', metavar='I', help='Name of fasta input file with CDS sequences')

args = parser.parse_args()

filename = args.nameofInputfile

for seq_record in SeqIO.parse(filename, 'fasta'):
	print(seq_record.id) #Print Seq Id
	print(seq_record.seq) # print the seq itself
	print(len(seq_record)) # print lenght of seq
	print('Translation: First Frame')
	print(seq_record.seq.translate(to_stop=True)) #Translate the sequence
#	print('Translation: Second Frame')
#	print(seq_record.seq[1:].translate(to_stop=True))
#	print('Translation: Third Frame')
#	print(seq_record.seq[2:].translate(to_stop=True))
