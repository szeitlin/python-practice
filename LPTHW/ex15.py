from sys import argv  #from the command line, take arguments

script, filename = argv #expect two arguments: the name of this script, and a file

txt = open(filename) #open the file

print "Here's your file %r:" %filename #this just prints the name of the file 
print txt.read() #this prints the contents of the file using the function .read on the variable txt, which calls the files

print "Type the filename again:" #another way to read the file is to ask for it from the command line
file_again = raw_input(">") #this gives a prompt that lets you type the name of the file a second time

txt_again= open(file_again) #this opens the file that you called at the prompt
print txt_again.read() #this runs the function .read on the variable txt_again and prints its contents

txt_again.close()
