#Script to parse Plain text output from HMMER 3.1b2
#Date: 28 Jul 2015 IST
#Author: Prakhar Gaur

from Bio import SearchIO
import os, glob
#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('HMMOutputFilename', metavar='f', help='name of hmmer3 plain text outputfile')

#args = parser.parse_args()
#inputfileName = str(args.HMMOutputFilename)

filenames = [os.path.basename(x) for x in glob.glob('*.out')]

for filename in filenames:
	qresults = SearchIO.parse(filename,'hmmer3-text')
	for qresult in qresults:
		print 'Query Name = %s' % (qresult.id)
		print 'Query Details = %s' % (qresult.description)
		print '\n\nNumber of Hits = %d' % len(qresult)
		flag = 0
		for hit in qresult:
			flag = flag + 1
			print '\n%d.Name of Hit =  %s' % (flag, hit.id)
			print 'number of HSP = %d' % (len(hit))
			print 'Discription of Query %s' % hit.description
			for hsp in hit:
				print 'HSP bitscore : %s' % (str(hsp.bitscore))
				print 'evalue of HSP : %s' % (str(hsp.evalue))
		print '##' * 10
