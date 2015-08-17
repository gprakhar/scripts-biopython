#Script to parse Plain text output from HMMER 3.1b2, using the Biopython SerachIO library
#Date: 28 Jul 2015 IST
#Author: Prakhar Gaur

from Bio import SearchIO
import os, glob
#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('HMMOutputFilename', metavar='f', help='name of hmmer3 plain text outputfile')

#args = parser.parse_args()
#inputfileName = str(args.HMMOutputFilename)

filenames = [os.path.basename(x) for x in glob.glob('*.OUT')]
flag_once = 0

for filename in filenames:
	print '\nProtien Name = %s' % filename[:-4]
	qresults = SearchIO.parse(filename,'hmmer3-text')
	for qresult in qresults:
		print '\n\tDomain Query Name = %s' % (qresult.id)
		print '\tDomain Details = %s' % (qresult.description)
		print '\tNumber of Hits = %d' % len(qresult)
		flag = 0
		for hit in qresult:
			flag = flag + 1
			if flag > 5:
				print '\t\t..'
				print '\t\t..'
				break
			else:
				print '\n\t\t%d.Name of Hit =  %s' % (flag, hit.id)
				print '\t\tDescription of Hit = %s' % (hit.description)
				print '\t\tnumber of HSP = %d' % (len(hit))
				flag2 = 0
			for hsp in hit:
				flag2 = flag2 +1
				if flag2 > 3:
					print '\t\t\t...'
	               	                break
				else:
					print '\t\t\tHSP bitscore : %s' % (str(hsp.bitscore))
					print '\t\t\tevalue of HSP : %s' % (str(hsp.evalue))
	print '##' * 10


