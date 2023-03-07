# from python
#convert radians to degrees
# usiing pi

from math import pi, radians, degrees

# this implies that;

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90)
print(ar == pi/2)

#the function should convert the radians into degrees and vice versa

pi = 22/7
radians = float(input("input radians: "))
degree = radians*(180/pi)
print(degree)

pi = 22/7
degree = float(input("input degree: "))
radians = degree/(180*pi)
print(radians)
