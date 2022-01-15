# Data Set: Do Not Modify
from tabnanny import check


columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = [
    (2005, 6),
    (2001, 5),
    (2013, 8),
    (2011, 10),
    (2017, 5),
    (2006, 5),
    (2009, 8),
    (2021, 7),
    (2002, 6),
    (2007, 5),
    (2012, 9),
    (2014, 7),
    (2003, 6),
    (2019, 4),
    (2016, 5),
    (2015, 6),
    (2018, 4),
    (2008, 5),
    (2010, 11),
    (2004, 6),
    (2020, 4)
]

# Write your code below this line:

#i
def last_appearing_series_point(series_points):
  return series_points[-1]
print(last_appearing_series_point(unemployment_rates))

#ii
def first_five_series_points(series_points):
  return series_points[:5]
print(first_five_series_points(unemployment_rates))

#iii
def check_year(series_points, *input_year):
  year = [item[0] for item in series_points]
  check_year = []

  for x in input_year:
    check_year.append(x in year)
  return check_year
print(check_year(unemployment_rates, 2000, 2010))

#iv
def get_recent_rate(series_points):
  years = [year[0] for year in series_points]
  return series_points[years.index(max(years))][1]
print(get_recent_rate(unemployment_rates))

#v
def unique_years(series_points):
  return set([year[0] for year in series_points])
print(unique_years(unemployment_rates))

#vi
def ordered_rates_by_year(series_points):
  return [rate[1] for rate in sorted(series_points)]
print(ordered_rates_by_year(unemployment_rates))

#vii
def largest_rate(series_points):
  return (max([rate[1] for rate in series_points]))
print(largest_rate(unemployment_rates))

#viii
def employment_rate(series_points):
  new_series = []
  for val in series_points:
    new_series.append((val[0], 100 - val[1]))
  return new_series
print(employment_rate(unemployment_rates))

#ix
def rate_less_than_7(series_points):
  new_series = []
  for x in series_points:
    if x[1] >= 7:
      new_series.append(x)
    else:
      pass
  return new_series
print(rate_less_than_7(unemployment_rates))

#x
def rate_frequency(series_points):
  frequency = {}
  rate = [rate[1] for rate in series_points]
  for x in rate:
    frequency[x] = rate.count(x)
  return frequency
print(rate_frequency(unemployment_rates))
