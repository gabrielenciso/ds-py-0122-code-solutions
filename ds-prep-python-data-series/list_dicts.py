# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = [
    {"unemployment_rate": 8, "year": 2013},
    {"unemployment_rate": 5, "year": 2006},
    {"unemployment_rate": 5, "year": 2017},
    {"unemployment_rate": 6, "year": 2015},
    {"unemployment_rate": 6, "year": 2002},
    {"unemployment_rate": 4, "year": 2019},
    {"unemployment_rate": 9, "year": 2012},
    {"unemployment_rate": 4, "year": 2018},
    {"unemployment_rate": 6, "year": 2003},
    {"unemployment_rate": 5, "year": 2007},
    {"unemployment_rate": 11, "year": 2010},
    {"unemployment_rate": 7, "year": 2014},
    {"unemployment_rate": 6, "year": 2004},
    {"unemployment_rate": 5, "year": 2016},
    {"unemployment_rate": 6, "year": 2005},
    {"unemployment_rate": 7, "year": 2021},
    {"unemployment_rate": 5, "year": 2001},
    {"unemployment_rate": 4, "year": 2020},
    {"unemployment_rate": 10, "year": 2011},
    {"unemployment_rate": 8, "year": 2009},
    {"unemployment_rate": 5, "year": 2008}
]

# Write your code below this line:

#i
def last_appearing_series_point(series_points):
  return unemployment_rates[-1]
print(last_appearing_series_point(unemployment_rates))

#ii
def first_five_series_points(series_points):
  series = []
  for item in series_points[:5]:
    point = (item["year"], item["unemployment_rate"])
    series.append(point)
  return series
print(first_five_series_points(unemployment_rates))

#iii
def check_year(series_points, *input_year):
  year = []
  check_year = []
  for idx, items in enumerate(series_points):
    year.append(series_points[idx]["year"])
  for x in input_year:
    if x in year:
      check_year.append(str(x) + " " + "included")
    else:
      check_year.append(str(x) + " " + "not included")
  return check_year
print(check_year(unemployment_rates, 2000, 2010))

#iv
def get_recent_rate(series_points):
  year = []
  for idx, items in enumerate(series_points):
    year.append(series_points[idx]["year"])
  return series_points[year.index(max(year))]["unemployment_rate"]
print(get_recent_rate(unemployment_rates))

#v
def unique_years(series_points):
  year = set()
  for idx, items in enumerate(series_points):
    year.add(series_points[idx]["year"])
  return year
print(unique_years(unemployment_rates))

#vi
def ordered_rates_by_year(series_points):
  ordered_rate = []
  for x in sorted(series_points, key=lambda i: i["year"]):   ##
    ordered_rate.append(x["unemployment_rate"])
  return ordered_rate
print(ordered_rates_by_year(unemployment_rates))

#vii
def largest_rate(series_points):
  rates = []
  for x in series_points:
    rates.append(x["unemployment_rate"])
  return max(rates)
print(largest_rate(unemployment_rates))

#viii
def employment_rate(series_points):
  new_series = []
  for x in series_points:
    new_series.append({"employment rate": 100 - x["unemployment_rate"], "year": x["year"]})
  return new_series
print(employment_rate(unemployment_rates))

#ix
def rate_less_than_7(series_points):
  new_series = []
  for x in series_points:
    if x["unemployment_rate"] >= 7:
      new_series.append(x)
    else:
      pass
  return new_series
print(rate_less_than_7(unemployment_rates))

#x
def rate_frequency(series_points):
  frequency = {}
  rate = [rate["unemployment_rate"] for rate in series_points]
  for x in rate:
    frequency[x] = rate.count(x)
  return frequency
print(rate_frequency(unemployment_rates))
