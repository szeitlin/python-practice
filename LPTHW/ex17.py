from sys import argv
from os.path import exists #exists is a python command that reads out true/false

script, from_file, to_file = argv #I had to create the from and to files also

print "Copying from %s to %s" %(from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata) #this uses len to measure the length

print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Ok, all done."

out_file.close()
in_file.close()
