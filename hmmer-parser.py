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
	print '\nProtien Name = %s' % filename[:-4]
	for qresult in SearchIO.parse(filename,'hmmer3-text'):
		print 'lenght of qresult = %d' % len(qresult)
		print 'Query Id = %s' % (qresult.id)
		flag = 0
		for hit in qresult:
			flag = flag + 1
			if flag > 5:
				print '.'
				print '.'
				print '.'
				break
			else:
				#print '\nQuery Id = %s' % (qresult.id)
				print '%d. number of HSP = %d' % (flag, len(hit))
				#print hit
#				beste = hit[0].hsps[0].evalue
	       			Hit = hit.id
	  #      		hit = hit[0].id.replace('.hmm', '')
#		        	print query + ',' + hit + ',' + str(beste)
				print 'Name of Hit =  %s' % Hit
#				print 'Discription of Query %s' % hit.query_description
				flag2 = 0
			for hsp in hit:
				flag2 = flag2 +1
				if flag2 > 3:
					print '.'
	                                print '.'
        	                        print '.'
                	                break
				else:
					print 'HSP bitscore : %s' % (str(hsp.bitscore))
	print '*' * 100
