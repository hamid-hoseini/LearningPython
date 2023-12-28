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
