#ds-prep-python-functions

#bool_to_int
bool_to_int = lambda value : int(value)

#get_smaller
get_smaller = lambda a,b : max(a,b)

def cube(base):
  return base ** 3

print(cube(5))

def absolute_difference(a,b):
  return abs(a - b)

print(absolute_difference(14,11))

def squared_difference(a,b):
  return (a-b) ** 2

print(squared_difference(14,11))

def hours_to_minutes(hours):
  return hours * 60

print(hours_to_minutes(hours = 12))

import math
def get_circumference(radius):
  return 2 * math.pi * radius

print(get_circumference(radius = 9.2))

def linear_transform(x, slope, intercept):
  return (slope * x) + intercept

print(linear_transform(x = 5.0, slope = 3.0, intercept = -8.5))

def standardize(x, x_center, scale_size):
  return (x - x_center) / abs(scale_size)

print(standardize(scale_size = 4.83, x = 8.2, x_center = 13.8))
