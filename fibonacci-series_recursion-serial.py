#Program to print Fibonacci series using both procedural method and Recursion
#learn usage of function() and commaand line arguments
#author: prakhar gaur
#date: Fri Oct 10 10:36:35 IST 2014

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("numberOfTimes", help="Number of terms to compute the Fibonacci series to", type=int)
parser.add_argument("-t", "--typeOfComputation", help="Mention type of computation, 'R' for recursive \n 'P' for procedural, Default 'P'. ")
parser.parse_args()

print args.numberOfTimes
print args.typeOfComputatio
