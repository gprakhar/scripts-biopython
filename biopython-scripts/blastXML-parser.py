#blast xml output parser using BioPython
#author: prakhar gaur
#date: 14 July 2015

from Bio.Blast import NCBIXML
import os, glob

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('Xmlfilename', metavar='f', help='name of xml file')

args = parser.parse_args()
inputfileName = str(args.Xmlfilename)

#filenames = [os.path.basename(x) for x in glob.glob('*.xml')]

e_value_dict = {}

with open(inputfileName, 'r') as result_handle:
	#read xml output file
	blast_records = NCBIXML.parse(result_handle)
	for blast_record in blast_records:
		print '\n\n%s' % blast_record.query #prints query's full name
		print 'Query lenght: %d' % blast_record.query_length
		for description in blast_record.descriptions:
			for alignment in blast_record.alignments:
				print 'Hit name = %s' % description.title
				print 'evalue = %s' % str(description.e) # loops on all hits for the query and prints the corresponding e-value
				print 'Hit length = %s' % str(alignment.length)
				print 'Number of Alignments = %s' % str(description.num_alignments)
			#e_value_dict[blast_record.query] = description.e
			#print "%s : %s" % (blast_record.query, str(description.e))

'''			
with open("out1", "w") as out1, open("out2", "w") as out2:
        for (k,v) in e_value_dict.items():
                out1.write("%s\n" % k)
                out2.write("%s\n" % str(v))'''
