#Script to parse Plain text output from Blast+2.30 blastp on Dicty protien set
#Date: 01 Aug 2015 IST
#Author: Prakhar Gaur

from Bio import SearchIO
import os, glob
#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('HMMOutputFilename', metavar='f', help='name of hmmer3 plain text outputfile')

#args = parser.parse_args()
#inputfileName = str(args.HMMOutputFilename)

filenames = [os.path.basename(x) for x in glob.glob('*.xml')]

for filename in filenames:
	qresults = SearchIO.parse(filename,'blast-xml')
	for qresult in qresults:
		print 'Query Name = %s' % (qresult.id)
		print 'Query Details = %s' % (qresult.description)
		print '\n\nNumber of Hits = %d' % len(qresult)
		flag = 0
		for hit in qresult:
			flag = flag + 1
			if flag > 5:
				print '.'
				print '.'
				print '.'
				break
			else:
				print '\n%d. ID of Hit =  %s' % (flag, hit.id)
				print 'Name of Hit = %s' % (hit.description)
				print 'number of HSP = %d' % (len(hit))
				flag2 = 0
			for hsp in hit:
				flag2 = flag2 +1
				if flag2 > 3:
					print '.'
	               	                break
				else:
					print 'HSP bitscore : %s' % (str(hsp.bitscore))
					print 'evalue of HSP : %s' % (str(hsp.evalue))
		print '##' * 10
