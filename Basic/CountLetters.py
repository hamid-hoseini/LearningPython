sherlockHolmes = '''
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

letterDictionary = {}

for letter in sherlockHolmes:
    letterDictionary[letter.lower()] = letterDictionary.get(letter.lower(), 0) + 1
    
print(letterDictionary) 
