#ds-prep-python-variables

first_name = 'Gabriel'
last_name = "Enciso"

full_name = first_name + " " + last_name
print(full_name)

height_in_inches = 67
print(height_in_inches, type(height_in_inches))

height_in_inches_float = float(height_in_inches)
print(height_in_inches_float, type(height_in_inches_float))

height_in_meters = (height_in_inches_float * 2.54) / 100
print(height_in_meters)

eats_plants = True
eats_animals = False

is_animal = eats_animals == True or eats_plants == True
is_omnivore = eats_plants == True and eats_animals == True
is_plant = is_animal != True

print(is_animal, is_omnivore, is_plant)

mean_height_in_meters = 1.7155
short_threshold_in_meters = 1.576
tall_threshold_in_meters = 1.860

is_mean_height = (height_in_meters == mean_height_in_meters)
is_short = (height_in_meters < short_threshold_in_meters)
is_tall = (height_in_meters > tall_threshold_in_meters)
is_normal_height = (height_in_meters >= short_threshold_in_meters and height_in_meters < tall_threshold_in_meters)

print(is_mean_height, is_short, is_tall, is_normal_height)

nothing = None
print(nothing, type(nothing))
