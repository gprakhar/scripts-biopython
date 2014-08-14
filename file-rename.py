cript to rename file according to particular pattern
##Author : Prakhar Gaur
##Date Thu Aug 14 13:21:21 UTC 2014
# 26_S27_L001_R2_001.fastq


import os, re

badprefix = "cheese_"
#fnames = listdir('.')

for fname in os.listdir("."):
#    if fname.startswith(badprefix*2):
     fname = re.sub
        rename(fname, fname.replace(badprefix, '', 1))
