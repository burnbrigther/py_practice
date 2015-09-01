import math

precisionPi = int(raw_input("How precise should pi be: ")) 
print 'PI = %.*f' % (precisionPi, math.pi)