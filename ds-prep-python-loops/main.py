#ds-prep-python-loops

record = (1, "Grimdiana", "Bones", "boulders")
row = ""

for x in record:
   row = row + str(x) + ","
print(row)

values_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]

for x in values_list:
  print(x)

index_list = list()

for i in range(len(values_list)):
  index_list.insert(0, i)
print(index_list)
print(len(index_list) == len(values_list))

for val in index_list:
  if val % 2 != 0:
    index_list.remove(val)
print(index_list)
print(values_list)

vowels = {"A", "E", "I", "O", "U"}
parts_of_the_big_letter = {"L", "M", "N", "O", "P"}

for x in vowels:
  if x in parts_of_the_big_letter:
    parts_of_the_big_letter.remove(x)
print(parts_of_the_big_letter)

player_positions = {
  "Who": "1B",
  "What": "2B",
  "I Don't Know": "3B",
  "Why": "LF",
  "Because": "CF",
  "Tomorrow": "P",
  "Today": "C",
  "I Don't Care": "SS"
}

players = list()
for x in player_positions.keys():
  players.append(x)
print(players)

positions = set()
for x in player_positions.values():
  positions.add(x)
print(positions)

for x in player_positions.items():
  print(x[0] + " " + "is on" + " " + x[1])
