input = "ABBAC"
potions = {'A': 0, 'B': 1, 'C': 3}
total_potions = 0

for letter in input:
   total_potions += potions[letter]

print(total_potions)