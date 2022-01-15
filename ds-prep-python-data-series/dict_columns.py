# Data Set: Do Not Modify
import enum


columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = {
    'year': [
        2009, 2011, 2005, 2016, 2001,
        2012, 2019, 2007, 2021, 2018,
        2010, 2013, 2006, 2017, 2015,
        2014, 2008, 2004, 2003, 2020,
        2002
    ],
    'unemployment_rate': [
        8, 10, 6, 5, 5,
        9, 4, 5, 7, 4,
        11, 8, 5, 5, 6,
        7, 5, 6, 6, 4,
        6
    ]
}

# Write your code below this line:

#i
def last_appearing_series_point(series_points, keys):
  return {keys[0]: series_points["year"][-1], keys[1]: series_points["unemployment_rate"][-1]}
print(last_appearing_series_point(unemployment_rates, columns))

#ii
def first_five_series_points(series_points):
  years = series_points["year"][:5]
  unemp_rates = series_points["unemployment_rate"][:5]
  first_five_series_points = []

  for idx, val in enumerate(years):
    point = (val, unemp_rates[idx])
    first_five_series_points.append(point)
  return first_five_series_points
print(first_five_series_points(unemployment_rates))

#iii
def check_year(series_points, *input_year):
  check_year = []

  for x in input_year:
    if x in series_points["year"]:
      check_year.append(str(x) + " " + "included")
    else:
      check_year.append(str(x) + " " + "not included")
  return check_year
print(check_year(unemployment_rates, 2000, 2010))

#iv
def get_recent_unemp_rate(series_points):
  years = series_points["year"]
  max_year = max(years)
  max_index = years.index(max_year)
  return (max_year, series_points["unemployment_rate"][max_index])
print(get_recent_unemp_rate(unemployment_rates))

#v
def unique_years(series_points):
  return set(series_points["year"])
print(unique_years(unemployment_rates))

#vi
def ordered_rates_by_year(series_points):
  series_dict = {}
  for idx, val in enumerate(series_points["year"]):
    point = {val : series_points["unemployment_rate"][idx]}
    series_dict.update(point)

  ordered_rates_by_year = []
  for x in sorted(series_dict.keys()):
    ordered_rates_by_year.append(series_dict[x])
  return ordered_rates_by_year
print(ordered_rates_by_year(unemployment_rates))

#vii
def largest_rate(series_points):
  return max(series_points["unemployment_rate"])
print(largest_rate(unemployment_rates))

#viii
def employment_rate(series_points):
  employment_rate = []
  new_series = {
    'year': series_points["year"],
    'unemployment_rate': series_points["unemployment_rate"]   ##why does it change og dictionary if I do new_series = series_points
  }
  unemployment_rate = new_series["unemployment_rate"]

  for x in unemployment_rate:
    employment_rate.append(100-x)
  new_series.update({"employment_rate": employment_rate})
  del new_series["unemployment_rate"]
  return new_series
print(employment_rate(unemployment_rates))

#ix
def rate_less_than_7(series_points):
  series_dict = {}
  for idx, val in enumerate(series_points["year"]):
    point = {val: series_points["unemployment_rate"][idx]}
    series_dict.update(point)

  series_dict = {key:val for key, val in series_dict.items() if val >= 7}
  series_dict = {
    'year': list(series_dict.keys()),
    'unemployment_rate': list(series_dict.values())
  }
  return series_dict
print(rate_less_than_7(unemployment_rates))

#x
def rate_frequency(series_points):
  frequency = {}
  rates = series_points["unemployment_rate"]

  for x in rates:
    frequency[x] = rates.count(x)
  return frequency
print(rate_frequency(unemployment_rates))
