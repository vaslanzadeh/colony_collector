#! /usr/bin/env python

#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 December 2019
#
#  Author:
#
#    Vahid Aslanzadeh
#
#  Parameters:
#
#    Input, integer p, the percentage of colonies to be collected.
#    p must be between 1 and 100.
#
#    Input, integer v, the number of total variants in the experiment, try to include the background for a better estimation. 
#
#    Output, a figure and the mean number of colonies that must be collected in order to just get p percentage distinct kinds.

from __future__ import division
from matplotlib import pyplot as plt


def colony_collector (p, v):
    from sys import exit
    desired_colonies=int((p/100)*v) #Total number of colonies desired to be be collected

    if ( v < desired_colonies ):
        exit('Fatal error! Percentage of desired colonies \n must be no more than 100')

    colonies = 0
    desired_colonies_x=[] 
    tobe_collected=[]
    for i in range ( 1, v + 1 ):
        desired_colonies_x.append(i)
        colonies = colonies + 1 / float ( v - i + 1 )
        tobe_collected.append(colonies * float ( v ))
        if not i > desired_colonies:
            colonies_ = colonies * float ( v )
            

    percentage = [(x / v)*100 for x in desired_colonies_x]
    
    return [p, colonies_, tobe_collected,percentage]

#Usage
result=colony_collector(95,40000) #Values should be changed according to your own specifications
plt.plot(result[2],result[3], c='k', )
plt.xlabel("Number of colected colonies")
plt.ylabel("Percentage of variants")
plt.axhline(result[0], c='r', linestyle='--')
plt.axvline(result[1], c='b', linestyle='--')
plt.grid()
plt.savefig("colony_colection.pdf", fmt='pdf')
plt.show()
print str(int(result[1])) +" colonies need to be harvested in order to achive "+str(result[0])+"% of the variants"

