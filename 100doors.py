#!/usr/bin/env python
#29th October 2016
#author Sebastian Znaj


import sys
doors  = [False]*100
list_of_doors = []

for index,door in enumerate(doors):
    for index2 in range(0,99, index+1):
        if doors [index2] == False:
            doors [index2] = True
        else:
            doors [index2] = False
    if door is True:
        list_of_doors.append((index))
print("The following doors are open:", "".join(str(list_of_doors)[1:-1]))
