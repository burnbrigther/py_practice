# EXERCISE 16 PROBLEM 3
# There's too much repetition in this file. Use strings, formats, and escapes to 
# print out line1, line2, and line3 with just one target.write() command instead of six.
from sys import argv
# argv will expect two input variables from CL.  First will
# be the name of the script and the other will be the filename
# we will be working with
script, filename = argv
# print out the raw formated filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you DO want that, hit RETURN."
# After we print the above, we will wait for user input
# from the command line consisting of either return or cntrl-c out
raw_input("?")

print "Opening the file..."
# filename is open and writable via the 'w' parameter and assigned to the variable (or object) target
# If you are writing or appending (but not reading), a new file will be created with that
# name if it doesn't already exist
target = open(filename, 'w') # we could also use 'a' for append or 'r' for read
# see "pydoc file" for info (lots and lots)
# w = write (vs. r = read, a = append)
# r+ allows you to read AND write
# w+ allows you to write AND read
# r (read only) is default

print "Truncating the file. Goodbye!"
target.truncate() # truncate the variable target with no extra parameters

print "Now I'm going to ask you for the three lines."
# Input 3 lines of input.  These could be consolidated.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# take the raw_input created in each line and write the line to target from above
# http://stackoverflow.com/questions/6394170/very-basic-python-question-strings-formats-and-escapes
target.write("{0}\n{1}\n{2}\n".format(line1,line2,line3))

print "And finally, we close it."
target.close()