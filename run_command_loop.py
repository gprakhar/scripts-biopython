##Script to run PANDAseq to iteratively do something
#Python 3
#Author : prakhar gaur
#Date : Sep 4 IST 2014

import os;
for i in range(1,40):
    if i not in (24,25):      
        cmdstr = '/bin/echo {0}'.format(i)
        os.system(cmdstr)
    else:
      print 'NA'



