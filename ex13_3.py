from sys import argv

script, second = argv

print "This only repeats the script name:", script
print ("Script name: %s" % str(sys.argv[0]))
print "And this prints the second argument of the input", second
print_back = raw_input("Now, here is your opportunity to give input:")
print "Here is your input %r" % (print_back)