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

hitDictionery = dict()
hitList = list()

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
			print '\n\t\t%d.Name of Hit =  %s' % (flag, hit.id)
			hitList.append(hit.id)
			print '\t\tDescription of Hit = %s' % (hit.description)
			print '\t\tnumber of HSP = %d' % (len(hit))
			for hsp in hit:
				print '\t\t\tHSP bitscore : %s' % (str(hsp.bitscore))
				print '\t\t\tevalue of HSP : %s' % (str(hsp.evalue))
		hitDictionery[qresult.id] = hitList
		hitList = list()
	print 'Dicty Proteins with all domains from the Human protien %s = %s' % (filename[:-4], reduce(lambda x,y: x&y, map(set, hitDictionery.values())) )
	print '##' * 10
	hitDictionery = dict()
