#Script to rum Hmmer on Dicty Protiens
#Run it keeping in mind that HMM(s) from a particular DPM human holmolog protien are all checked against every Protien from Dicty
#Author : prakhar gaur
#date : Wed 16 July IST 2015

import os
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-C', '--numberofcores', help='Number of cores to run the blast on', type=int)
parser.add_argument('hmmfile', metavar='F', help='csv file with hmm entries, with first entry in each row as Uniprot id')

args = parser.parse_args()
cores = args.numberofcores
inputfileName = str(args.hmmfile)

hmmerExe = r'/home/interns/CHG_Nunjundiah-Project/local-bin/hmmer/hmmer-3.1b2-linux-intel-x86_64/binaries/'

pfamid = list()
with open(inputfileName) as inputfileHandle:
        keywordString = csv.reader(inputfileHandle)
        for row in keywordString:
                pfamid.append(row)

for idlist in pfamid:
	for item in idlist[1:]:
		hmmsearch_cmd = '%shmmsearch --cpu %d /home/interns/CHG_Nunjundiah-Project/raw-data/DPM-prot-HMM/%s.hmm dicty_primary_protein.fa >> %s.out' % (hmmerExe, cores, item, idlist[0])
		print hmmsearch_cmd
		os.system(hmmsearch_cmd)
