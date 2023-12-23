'''
Write a function AMCount() in Python, which should read each character of a text file STORY.TXT, 
should count and display the occurance of alphabets A and M (including small cases a and m too).
For Example:
If the file content is as follows:
Updated information
As simplified by official websites.
The EUCount() function should display the output as:
A or a:4
M or m :2
'''

def AMcount():
    file = open('notes.txt','r')
    data = file.read()
    counta=0
    countm=0
    for letter in data:
        if letter == 'A' or letter =='a':
            counta += 1
        elif letter == 'M' or letter =='m':
            countm += 1

    file.close()
    print('A or a:',counta)
    print('M or m:',countm)

AMcount()
