#Program to print Fibonacci series using both procedural method and Recursion
#learn usage of function() and commaand line arguments
#author: prakhar gaur
#date: Fri Oct 10 10:36:35 IST 2014

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('numberOfTimes', metavar='N', help='Number of terms to compute the Fibonacci series to', type=int)
parser.add_argument('-t', '--typeOfComputation', default='P', help='Mention type of computation, "R" for recursive and "P" for procedural, Default "P".')
args = parser.parse_args()

num = args.numberOfTimes
ComputationType = args.typeOfComputation

if ComputationType
