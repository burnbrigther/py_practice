# Our static values
my_surfboard_length = 100 # inches
inches_to_centimeters = 2.63 # 1 inch equals 2.63 centimeters
my_surfboards_weight = 10.0
pounds_to_kilograms = .45
pounds_to_stones = .071 # 1 pound = .071 stones
surboard_in_stones = my_surfboards_weight * pounds_to_stones
my_gallons_of_beer = 10
liters_per_gallon = 4.55
# Let's first try inches to centimeters
print "I have a surfboard %d inches in length.  That's %d centimeters long." % (my_surfboard_length, my_surfboard_length * inches_to_centimeters)
# Now let's try pounds to kilograms
print "My surfboard weighs %r pounds, which is actually %r kilograms." % (my_surfboards_weight, my_surfboards_weight * pounds_to_kilograms)
# Now let's try pounds to stones
print "Now, for another conversion. My surfboard again weighs %r pounds, which is actually %r stones." % (my_surfboards_weight, surboard_in_stones)
# Now let's try liters to quarts.  By now, we've better have the methodology down!
print "Finally, if I have a %d gallon of beer, I have %r liters of the good stuff!" % (my_gallons_of_beer, my_gallons_of_beer * liters_per_gallon)