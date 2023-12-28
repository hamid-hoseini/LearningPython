# sample 1

alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_text = 'hello'
output = ''

for char in input_text:
    alpha_index = alphabet.find(char)
    output = output + alphabet[alpha_index+3]
print(output)    


# sample 2
# if cipher index goes beyond end of alphabet

def shift_amount(i):
    '''Will determine the shift, taking into account the length of the alphabet. Takes integer - returns integer'''
    return i%26
  
output_1 = ''
for char in input_text:
    alpha_index = alphabet.find(char)
    output_1 = output_1 + alphabet[shift_amount(alpha_index+30)]
print(output_1) 


# sample 3
# A complete function
def encrypt(text,required_shift):
    out_string = ''
    text = text.lower()
    for char in text:
        if char not in alphabet:
            out_string = out_string + char
        else:    
            alpha_index = alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index +required_shift)]
    return out_string


# Execute:
basker = '''I confess at these words a shudder passed
through me. There was a thrill in the doctor’s voice
which showed that he was himself deeply moved
by that which he told us. Holmes leaned forward
in his excitement and his eyes had the hard, dry
glitter which shot from them when he was keenly
interested.'''

encrypt_basker = encrypt(basker,10)
print(encrypt_basker)

# output:
'''
s myxpocc kd droco gybnc k crennob zkccon
drbyeqr wo. drobo gkc k drbsvv sx dro nymdyb’c fysmo
grsmr crygon drkd ro gkc rswcovp noozvi wyfon
li drkd grsmr ro dyvn ec. ryvwoc vokxon pybgkbn
sx rsc ohmsdowoxd kxn rsc oioc rkn dro rkbn, nbi
qvsddob grsmr cryd pbyw drow grox ro gkc uooxvi
sxdobocdon.
'''

print(encrypt(encrypt_basker,-10))

# output:
'''
I confess at these words a shudder passed
through me. There was a thrill in the doctor’s voice
which showed that he was himself deeply moved
by that which he told us. Holmes leaned forward
in his excitement and his eyes had the hard, dry
glitter which shot from them when he was keenly
interested.
'''
