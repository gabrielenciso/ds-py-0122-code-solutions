#ds-prep-python-dictionaries

person = {
  "first_name" : "Naruto",
  "last_name" : "Uzumaki",
  "hobby" : "Eating Ramen"
}
print(person)

first_name = person["first_name"]
last_name = person.get("last_name")
middle_name = person.get("middle_name")
#print(first_name + " " + middle_name + " " + last_name)


person["job"] = "ninja"
print(person["job"])

person["hobby"] = "training"
print(person["hobby"])

person.pop("last_name")
print(person)
