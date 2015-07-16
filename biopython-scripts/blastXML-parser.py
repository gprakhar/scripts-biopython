#blast xml output parser using BioPython
#author: prakhar gaur
#date: 14 July 2015

from Bio.Blast import NCBIXML
import os, glob
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('lenghtofAminoAcidSe', metavar='N', help='lenght of the amino acid sequence', type=int)
parser.add_argument('-v',
'''

filenames = [os.path.basename(x) for x in glob.glob('*.xml')]

e_value_dict = {}

for name in filenames:
	with open(name, 'r') as result_handle:
		#read xml output file
		blast_records = NCBIXML.parse(result_handle)
		for blast_record in blast_records:
			#print (blast_record.query) #prints query's full name
			for description in blast_record.descriptions:
				#print description.e # loops on all hits for the query and prints the corresponding e-value
				#e_value_dict[blast_record.query] = description.e
				print "%s : %s" % (blast_record.query, str(description.e))

'''			
with open("out1", "w") as out1, open("out2", "w") as out2:
        for (k,v) in e_value_dict.items():
                out1.write("%s\n" % k)
                out2.write("%s\n" % str(v))'''
