#Script to parse Plain text output from HMMER 3.1b2
#Date: 28 Jul 2015 IST
#Author: Prakhar Gaur

from Bio import SearchIO
import os, glob
import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('HMMOutputFilename', metavar='f', help='name of hmmer3 plain text outputfile')

#args = parser.parse_args()
#inputfileName = str(args.HMMOutputFilename)

filenames = [os.path.basename(x) for x in glob.glob('*.out')]

for filename in filenames:
	print filename
	for qresult in SearchIO.parse(filename,'hmmer3-text'):
		print 'lenght of qresult = %d' % len(qresult)
		for hit in qresult:
			print 'lenght of hit = %d' % len(hit)
#			beste = hit[0].hsps[0].evalue
 #       		query = hit[0].query_id
  #      		hit = hit[0].id.replace('.hmm', '')
#	        	print query + ',' + hit + ',' + str(beste)
			
	
	
