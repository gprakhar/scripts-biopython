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
flag_once = 0
print filenames
filenames.sort()
print filenames

for filename in filenames:
	'''protName_new = filename[8:14]
	if flag_once == 0:
		pass
	else:
		if protName != protName_new:
			print '---XXXX---' * 10
	flag_once = flag_once + 1
	protName = filename[8:14]'''
	print '\nProtien Name = %s' % filename[8:14]
	qresults = SearchIO.parse(filename,'hmmer3-text')
	'''for qresult in qresults:
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
				print '\n%d.Name of Hit =  %s' % (flag, hit.id)
				print 'number of HSP = %d' % (len(hit))
#				print 'Discription of Query %s' % hit.query_description
				flag2 = 0
			for hsp in hit:
				flag2 = flag2 +1
				if flag2 > 3:
					print '.'
	               	                break
				else:
					print 'HSP bitscore : %s' % (str(hsp.bitscore))
		print '##' * 10'''
