#ds-prep-python-sets

trail_mix = {"m&ms", "peanuts", "raisins"}
print(trail_mix)

print("cashews" in trail_mix)
print("peanuts" in trail_mix)

trail_mix.add("pretzels")
trail_mix.update(["peanuts", "banana chips", "bits of jerkey"])
print(trail_mix)

trail_mix.remove("m&ms")
trail_mix.discard("raisins")
trail_mix.discard("rat poison")
print(trail_mix)

nuts = {"peanuts", "cashews", "almonds", "walnuts", "pecans"}

print(nuts.union(trail_mix))
print(trail_mix.intersection(nuts))
print(trail_mix.difference(nuts))
print(nuts.difference(trail_mix))
