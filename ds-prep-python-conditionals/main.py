#ds-prep-python-conditionals

day_of_week = "monday"

if day_of_week.lower() == "saturday" or day_of_week.lower() == "sunday":
  print("Have a good weekend!")
else:
  print("It's a weekday!")

student_1_score = 65

if student_1_score >= 70:
  pass_or_fail = "You passed!"
else:
  pass_or_fail = "You failed :("
print(student_1_score, pass_or_fail)

student_2_score = 53

if student_2_score < 60:
  letter_grade = "F"
elif student_2_score >= 60 and student_2_score < 70:
  letter_grade = "D"
elif student_2_score >= 70 and student_2_score < 80:
  letter_grade = "C"
elif student_2_score >= 80 and student_2_score < 90:
  letter_grade = "B"
elif student_2_score >= 90 and student_2_score < 100:
  letter_grade = "A"
else:
  letter_grade = "A+"
print(student_2_score, letter_grade)

def get_season_info(season):
  if season.lower() == "summer":
    return "Statistically, it's likely to be hotter today than in 6 months from now. Don't sweat it, though."
  elif season.lower() == "spring":
    return "The flowers are blooming while it's spring, but that is correlation, not causation."
  elif season.lower() == "autumn":
    return "The leaves seem to regress to warmer colors as autumn approaches its end."
  elif season.lower() == "winter":
    return "There may only be a high likelihood of it being cold today, but there's a 100 percent chance of me wanting that sweater."
  else:
    return "That's not a season. Most likely"

print(get_season_info("Summer"))
print(get_season_info("spring"))
print(get_season_info("autumn"))
print(get_season_info("Winter"))
print(get_season_info("fall"))

age = 42
print("adult") if age >= 18 else print("child")
