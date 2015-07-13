#blast xml output parser using BioPython
#author: prakhar gaur
#date: 14 July 2015

from Bio.Blast import NCBIXML

#open the blast xml output file
result_handle = open("disco-out.xml")

#read xml output file
blast_records = NCBIXML.parse(result_handle)

'''
#evalue cutoff
E_VALUE_THRESH = 0.001

for blast_record in blast_records:
	for alignment in blast_record.alignments:
		for hsp in alignment.hsps:
#			if hsp.expect < E_VALUE_THRESH:
#				print('****Alignment****')
				print('sequence:', alignment.title)
				print('length:', alignment.length)
				print('e value:', hsp.expect)
#				print(hsp.query[0:75] + '...')
#				print(hsp.match[0:75] + '...')
#				print(hsp.sbjct[0:75] + '...')
'''

for blast_record in blast_records:
	print blast_record.query #prints query's full name
	for description in blast_record.descriptions:
		print description.e # loops on all hits for the query and prints the corresponding e-value

