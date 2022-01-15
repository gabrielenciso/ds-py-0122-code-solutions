# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = {
    2002: 6,
    2020: 4,
    2007: 5,
    2015: 6,
    2010: 11,
    2014: 7,
    2001: 5,
    2006: 5,
    2004: 6,
    2009: 8,
    2013: 8,
    2008: 5,
    2021: 7,
    2018: 4,
    2011: 10,
    2005: 6,
    2016: 5,
    2019: 4,
    2012: 9,
    2017: 5,
    2003: 6
}

# Write your code below this line:

#i
def last_appearing_series_point(series_points, keys):
  return {keys[0]: list(series_points)[-1], keys[1]: list(series_points.values())[-1]}
print(last_appearing_series_point(unemployment_rates, columns))

#ii
def first_five_series_points(series_points):
  return list(series_points.items())[:5]
print(first_five_series_points(unemployment_rates))

#iii
def check_year(series_points, *input_year):
  check_year = []

  for x in input_year:
    if x in series_points.keys():
      check_year.append(str(x) + " " + "included")
    else:
      check_year.append(str(x) + " " + "not included")
  return check_year
print(check_year(unemployment_rates, 2000, 2010))

#iv
def get_recent_rate(series_points):
  return series_points[max(series_points.keys())]
print(get_recent_rate(unemployment_rates))

#v
def unique_years(series_points):
  return set(series_points.keys())
print(unique_years(unemployment_rates))

#vi
def ordered_rates_by_year(series_points):
  return [rate[1] for rate in sorted(series_points.items())]  ##
print(ordered_rates_by_year(unemployment_rates))

#vii
def largest_rate(series_points):
  return max(series_points.values())
print(largest_rate(unemployment_rates))

#viii
def employment_rate(series_points):
  employment_rate = [100 - x for x in series_points.values()]
  new_series_points = {}

  for idx, val in enumerate(series_points.keys()):
    new_series_points.update({val: employment_rate[idx]})
  return new_series_points
print(employment_rate(unemployment_rates))

#ix
def rate_less_than_7(series_points):
  series_dict = {key: val for key, val in series_points.items() if val >= 7}
  return series_dict
print(rate_less_than_7(unemployment_rates))

#x
def rate_frequency(series_points):
  frequency = {}

  for x in series_points.values():
    frequency[x] = list(series_points.values()).count(x)
  return frequency
print(rate_frequency(unemployment_rates))
