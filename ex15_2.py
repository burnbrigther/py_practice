# imports the argv feature from the sys package
from sys import argv
# Takes  input values from argv and squishes them together (these are the two command line items)
# then unpacks two arguments sent to argv and assigns them to script and filename
script, filename = argv
# Takes the value from the command line argument (filename), open reads what's in filename
# and assigns the value to the variable txt
txt = open(filename)
# Print the string and value of the variable substitution given from filename above.
print "Here's your file %r:" % filename

print txt.read()

print "Here is your file again:"
file_again = open(filename)

txt_again = open(file_again)

print txt_again.read()