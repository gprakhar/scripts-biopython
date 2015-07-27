#!/bin/bash
#$ -cwd
#$ -N fail-0
#$ -V
#$ -q all.q@node001
#$ -S /bin/bash
#$ -o $JOB_ID.$JOB_NAME.out
#$ -e $JOB_ID.$JOB_NAME.err

/bin/bash;  pick_otus.py -i /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_/POTU_KYrb_.0.fasta -r /home/ubuntu/qiime_software/gg_otus-13_8-release/rep_set/97_otus.fasta -m uclust_ref --suppress_new_clusters -o /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_ -s 0.97    --max_accepts 20 --max_rejects 500 --stepwords 20 --w 12   ; mv /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_/POTU_KYrb_.0_otus.log /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_.0_otus.log; mv /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_/POTU_KYrb_.0_otus.txt /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_.0_otus.txt; mv /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_/POTU_KYrb_.0_failures.txt /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_.0_failures.txt; mv /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_/POTU_KYrb_.0_clusters.uc /data/closed-ref_OUT-pick_run-4/uclust_ref_picked_otus/POTU_KYrb_.0_clusters.uc ; exit
