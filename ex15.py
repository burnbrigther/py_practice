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
# Take the object "txt" (the variable assignment created above from open(filename) and apply
# the dot operator (do this operation on the object) and do add read function to it.  All functions
# require parameters.  If you aren't passing any parameters, then you leave them blank "()".
# Print this results of the above
print txt.read()
# Now we will do this from inside the script with raw_input, taking user input and assigning the string to file_again
print "Type the filename again:"
file_again = raw_input(">")
# Open the contents of file_again and assign them to txt_again
txt_again = open(file_again)
# Apply the read function on txt_again and print the contents
print txt_again.read()