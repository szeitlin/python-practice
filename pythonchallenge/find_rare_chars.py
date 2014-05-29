__author__ = 'szeitlin'

#import pandas
#import matplotlib.pyplot as plt

import numpy.numarray as na

#find rare characters in a mess of symbols

#if not in the list, append it
countlist = {}

def count_chars():
    for char in line:
        if char not in countlist:
            countlist.update({char:1})

#if in the list, count it
        elif char in countlist:
    #countlist = {char:(i+=1)}  #make a dict of key:value pairs, where the key = char and the value = count of that char
    #on subsequent times it appears, update the value in the dictionary by += 1
            countlist[char] += 1

    return countlist

with open("ocr.txt") as myfile:
    for line in myfile:
        #print line
        count_chars()
        #print countlist

        #make a histogram to visualize frequencies

#s = pandas.Series(countlist)
#s.plot(kind = 'bar', rot = 0)

#make x-axis labels, preserve order, immutable format

labels = countlist.keys()
#print labels

def visualize_type():
    """counts of each char -> bar graph"""

    xlocations = na.array(range(len(labels))) + 0.2  #na is numpy, 0.5 is the offset she determined empirically

    width = 0.2  #units are not known, see docs if you really want to know

    plt.bar(xlocations, countlist.values(), width=width) #left, height, width

    plt.xticks(xlocations + width/2, labels, rotation=90) #centered labels and make vertical

    plt.tick_params(axis='both', which='major', labelsize=8)

    plt.subplots_adjust(bottom=0.4)   #just so it's not cut off

    plt.rcParams["figure.figsize"] = 30, 8   #plot scale, units unknown

    plt.savefig("long.png")

    plt.clf()

    #should go back and try to add y-axis labels

#visualize_type()

coded = []

def extract_rare():
    for key, value in countlist.iteritems():
        if value == 1:
            coded.append(key)

    print coded

extract_rare()
