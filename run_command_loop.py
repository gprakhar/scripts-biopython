##Script to run PANDAseq to merge reads iteratively in all 39 samples
##incoming = 'arbit'
#result = '{0} hello world {0} hello world {0}'.format(incoming)

import os;
for i in range(1,40):
    if (i!=24 or i!=25):
      cmdstr = '/bin/echo {0}'.format(i)
      cmdPANDA = '/home/ec2-user/local_bin/PANDAseq/INSTALL/bin/pandaseq -f /data/raw_reads/{0}_R1.fastq  -r /data/raw_reads/{0}_R2.fastq -p CCTACGGGAGGCAGCAG -q ATTACCGCGGCTGCTGG -g {0}_PE-Read-assembly.log -T 8 -w {0}_out_aligned.fasta -U {0}_un-aligned.txt'.format(i) 
      os.system(cmdstr)
    else:
      print NA
#    os.system(cmdPANDA)



