# import argv from the system module
# allows us to take info from the command line and make it
# available to the program
from sys import argv
# argv will expect two input variables from CL.  First will
# be the name of the script and the other will be the filename
# we will be working with
script, filename = argv

print "Opening the file..."
# filename is open and readable via the 'r' parameter and assigned to the variable (or object) target
target = open(filename, 'r')

# Now we create a for loop in which we circulate through all lines in target, then we simply print
# the lines out.
# https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
for line in target:
    print line,

# Finally, clean up.  Good programmer
print "And finally, we close it."
target.close()