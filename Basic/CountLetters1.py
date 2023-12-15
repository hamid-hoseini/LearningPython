sherlock = '''
Mr. Sherlock Holmes, who was usually very late in the 
mornings, save upon those not infrequent occasions when 
he stayed up all night, was seated at the breakfast table. 
I stood upon the hearth-rug and picked up the stick which our 
visitor had left behind him the night before. It was a fine, 
thick piece of wood, bulbous-headed, of the sort which is known 
as a “Penang lawyer.” Just under the head was a broad silver band, 
nearly an inch across. “To James Mortimer, M.R.C.S., from his 
friends of the C.C.H.,” was engraved upon it, with the date “1884.” 
It was just such a stick as the old-fashioned family practitioner 
used to carry—dignified, solid, and reassuring. “Well, Watson, 
what do you make of it?” Holmes was sitting with his back to me, 
and I had given him no sign of my occupation.
'''

letter_count = {}
for letter in sherlock:
   letter_count[letter.lower()] = letter_count.get(letter,0) + 1
    
print(letter_count)    

import matplotlib.pyplot as plt

x,y = zip(*letter_count.items())

plt.bar(x,y)
plt.show()
