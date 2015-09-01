# Assigns the string with a variable of x. 
# The substitution of 10 is done via a formatted signed integer operator.
x = "There are %d types of people." % 10

# Assigns the variable binary with the string value "binary".
binary = "binary"

# Assigns the variable do_not with the string value "don't"
do_not = "don't"

# Assigns a string to the variable y. The string has two replacement 
# variables which are python string formated variables (%s).
# This is the first place a string is put inside a string
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints the value of x
print x
# Prints the value of y
print y

# prints a string with a formated string variable replacement with the value of x above
# This is the second place a string is put inside a string. 
print "I said: %r." % x
# print a string with a formated string variable replacement with the value of y above
print "I also said: '%s'." % y

# Assigns the value of False to hilarious
hilarious = False
# Sets the string 'joke_evaluation' to the string containing the replacement value.
# We do not specify the replacement here, yet. It will be specified when we use the string.
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the value of the string 'joke_evaluation' and used the value of the string
# 'hilarious' as a replacement.
# This is the forth place where a sting is put inside a string.
print joke_evaluation % hilarious

# Assign the value of the string to w
w = "This is the left side of..."
# Assign the value of the string to e
e = "a string with a right side."

# Concatonate and print w and e
print w + e