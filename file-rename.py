##Script to rename file according to particular pattern
##Author : Prakhar Gaur
##Date Thu Aug 14 13:21:21 UTC 2014
# 26_S27_L001_R2_001.fastq
# 29_S2_L001_R1_001.fastq

import os, re

regex_fname = r"[0-9]{1,2}_S[0-9]{1,2}_L001_R[12]{1,1}_001\.fastq"
regex_replace_fr = r"_S[0-9]{1,2}_L001"
regex_replace_bw = r"_001"
#regex = re.compile(regex_fname)
#regex = re.compile(regex_replace)

#os.chdir("/data/raw_reads/")


for fname in os.listdir("."):
#    ans = regex.search(fname)
#    print ans.group()
    ans_1 = re.sub(regex_replace_fr, "", fname, 1)
#    print ans_1
    ans_2 = re.sub(regex_replace_bw, "", ans_1, 1)
    print ans_2
    os.rename(fname, ans_2)

    
