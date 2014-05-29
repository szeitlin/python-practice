from sys import argv #don't start unless you have these
script, filename = argv #make sure you have a script and another file

print "We're going to erase %r." %filename #variable lets you put in any file
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") #the prompt looks like a question mark

print "Opening the file..."
target =open(filename, 'w') #opens the file with write permission

print "Truncating the file. Goodbye!"
target.truncate() #I think this clears the file...  

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ") #how about this
line2 = raw_input("line2: ") #try it this way
line3 = raw_input("line3: ") 

print "I'm going to write these to the file."

target.write(line1\n , line2\n , line3)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()
