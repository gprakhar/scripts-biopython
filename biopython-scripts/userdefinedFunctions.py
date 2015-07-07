#module for user defined functions in the script - test-MSA-VN-hypothesis.py
#author -- prakhar gaur
#date -- Mon 8 Jun 2015

from random import randint
from Bio.Align.Applications import MuscleCommandline

##function to generate random nulcletide sequence
def genrateSequence(lenght, numVar):
        nuclSeq = list()
        for i in range(0,lenght):
                numRand = randint(1,4)
                if numRand == 1:
                        nuclSeq.append('A')
                elif numRand == 2:
                        nuclSeq.append('T')
                elif numRand == 3:
                        nuclSeq.append('G')
                elif numRand == 4:
                        nuclSeq.append('C')
        ##write random nulcletide sequence to file
        with open('output_%dvariants.fa' % numVar, 'w') as fileHandle1:
                fileHandle1.write(">ori-seq\n")
                fileHandle1.write("".join(nuclSeq))
                fileHandle1.write("\n")
                fileHandle1.close()
	return nuclSeq



##function to run muscle from inside main script
def callMuscle(numVar):
	#code for Muscle alignment of sequences
	muscle_exe = r'/home/littleboy/local_bin/muscle-MSA/muscle3.8.31_i86linux64'
	#build command
	muscle_cline = MuscleCommandline(muscle_exe, input='output_%dvariants.fa' % numVar, out='muscle-out_%dvariants.afa' % numVar)
	muscle_cline() #execute command




##function to generate single tandem duplication, with size in multiples of 3

def tandemDuplication(numVar, nuclSeq, lenght):

	varSeq = list()
	nuclSeq_Slice = list()

	for itrate in range(1,numVar+1):
        	locDup = randint(0,lenght) #random location for duplication insertion
#       print "temp%d location of dplication: %d" % (itrate, locDup)
        	#size of duplication based on percentage (in multiples of 3), the value has to be converted to int before useage
	        sizeDup = ((3*itrate)/100.0)*lenght # BUG what will happen when itrate value goes above 100 # SOLUTION conditional to not let percentage go beyond 49%
#       print "temp%d size of duplication in int: %f" % (itrate, int(sizeDup))
        	#if location of duplication insertion is greater than half of lenght of sequence, than copy duplication from upstream otherwise         downstream
	        if locDup < (lenght-locDup):
        	        NuclSeq_Slice = nuclSeq[locDup:int(locDup+sizeDup)]
#               print "NuclSeq_Slice len = %d :%s" % (len(NuclSeq_Slice), NuclSeq_Slice)
#               print "temp%d: len=%d :%s" % (itrate, len(varSeq), varSeq)
                	varSeq = nuclSeq[:locDup]
#               print "temp%d: R1 len=%d :%s" % (itrate, len(varSeq), varSeq)
			varSeq.extend(NuclSeq_Slice)
#               print "temp%d: R2 len=%d :%s" % (itrate, len(varSeq), varSeq)
        	        varSeq.extend(nuclSeq[locDup:])
        	else:
                	NuclSeq_Slice = nuclSeq[int(locDup-sizeDup):locDup]
#               print "NuclSeq_Slice len = %d :%s" % (len(NuclSeq_Slice), NuclSeq_Slice)
#               print "temp%d: len=%d :%s" % (itrate, len(varSeq), varSeq)
	                varSeq = nuclSeq[:int(locDup-sizeDup)]
#               print "temp%d: R1 len=%d :%s" % (itrate, len(varSeq), varSeq)
        	        varSeq.extend(NuclSeq_Slice)
#               print "temp%d: R2 len=%d :%s" % (itrate, len(varSeq), varSeq)
                	varSeq.extend(nuclSeq[int(locDup-sizeDup):])

#       print "temp%d: R-fi len=%d :%s" % (itrate, len(varSeq), varSeq)
	        #write the variant sequence to file
        	with open('output_%dvariants.fa' % numVar,'a') as fileHandle3:
                	fileHandle3.write('>var-seq%d\n' % itrate)
	                fileHandle3.write("".join(varSeq))
        	        fileHandle3.write("\n")
                	fileHandle3.close()
	        #write variant sequence details to file 
        	with open('output_%dvariants-details.txt' % numVar,'a') as fileHandle4:
                	fileHandle4.write('var-seq%d\t%d\t%d\t%d\t%d\n' % (itrate, locDup, itrate*3, int(sizeDup), len(varSeq)))
	                fileHandle4.close()	
        
		del varSeq[:] #empty out the temp lists
	        del nuclSeq_Slice[:]
