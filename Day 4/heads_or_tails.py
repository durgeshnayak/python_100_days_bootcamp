# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

outcome = random.randint(0, 1)

if outcome == 0:
    print("Tails")
elif outcome == 1:
    print("Heads")
else:
    print("SHIT HAPPENS!")

