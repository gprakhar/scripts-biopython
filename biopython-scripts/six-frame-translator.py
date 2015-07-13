#Script to translate fasta sequence to six reading frames
#author: Prakhar gaur
#date: 13 July 2015

from Bio import SeqIO
from Bio.SeqUtils import six_frame_translations


for seq_record in SeqIO.parse("test.fa", "fasta"):
	print(seq_record.id)
#	print(seq_record.seq)
#	print(len(seq_record))
	print(six_frame_translations(seq_record.seq))


'''
print(record.seq.translate(to_stop=True))
print("Offset by one")
print(record.seq[1:].translate(to_stop=True))
print("Offset by two")
print(record.seq[2:].translate(to_stop=True))
'''
