print "I will now count my chickens:"

# The next line runs operands in order of precedence.  Division is done first, then addition.
# 30 is divided by 6, then 25 is added, which equals 30.
print "Hens", 25 + 30 / 6
# Same deal, but this time with the modulus operator.
# The % (modulo) operator yields the remainder from the division of the first argument by the second. 
# The numeric arguments are first converted to a common type. A zero right argument raises the 
# ZeroDivisionError exception. The arguments may be floating point numbers, e.g., 3.14%0.7 equals 
# 0.34 (since 3.14 equals 4*0.7 + 0.34.) The modulo operator always yields a result with the same 
# sign as its second operand (or zero); the absolute value of the result is strictly smaller than 
# the absolute value of the second operand [2].
# IN THIS SPECIFIC CASE: * and % have same precedence, so * is evaled first, then %.
# So it's (25 * 3) = 75, then 75 % 4 which is the remainder of 75 divided by 4 which is 75/4 = 18 with a remainder of 3
# Then the minus operator is evaled (subtracted) 100 - 3 and the final result is 97.  WHEW!
# Good explanation here: http://stackoverflow.com/questions/4729025/modulo-and-order-of-operation-in-python-zed-shaw-examples
print "Roosters", 100 - 25 * 3 % 4
# 
print "Now I will count the eggs:"

# Evaluated with modulus and division first, then left to right as standard
# Specifically 4%2 is 0, 1./4 is .25, so 3+2+1 = 6-5 = 1 + 0 = 1 - .25 = .75 + 6 = 6.75 
# One interesting thing is how the operator works on negative integers.

# As stated in the Python reference manual http://docs.python.org/reference...
# The modulo operator always yields a result with the same sign as its second operand (or zero); the absolute value of the 
# result is strictly smaller than the absolute value of the second operand
# So for example:
# 1% 4 = 1
# -1 % 4 = 3
# 1 % -4 = -3
# -1 % -4 = -1
# Specifically this does math of 4 % 2 first which is 0, then 1 / 4 which is 0 (.25 rounded down?) next
# ... then 3 + 2 + 1 = 6 - 5 + 0 - 0 + 6 = 7 
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# Simple print text
print "Is it true that 3 + 2 > 5 - 7?"

# Evaluates 5 > -2, which is True
print 3 + 2 > 5 - 7

# Evaluates 3 + 2 which is 5
print "What is 3 + 2?", 3 + 2

# Evaluates 5 - 7, which is -2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

# Evaluates True or False, but its true since 5 is greater than -2
print "Is it greater?", 5 > -2
# Evaluates True since 5 is greater than or equal to -2
print "Is it greater or equal?", 5 >= -2
# Evaluates False since 5 is not less than or equal to -2
print "Is it less or equal?", 5 <= -2