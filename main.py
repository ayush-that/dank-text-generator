# dank text generator!

import random

normie_text = input("enter normie text: ")
stripped = list(normie_text.strip(" "))
dank_text = list()

odd_even = [0, 1]

for i in stripped:
    x = random.choice(odd_even)
    if x == 0:
        up = i.upper()
        dank_text.append(up)
    elif x == 1:
        down = i.lower()
        dank_text.append(down)

print(*dank_text, sep='')
