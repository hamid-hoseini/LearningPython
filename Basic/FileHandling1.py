'''
A binary file "STUDENT.DAT" has structure (admission_number, Name, Percentage). Write a function count_rec() 
in Python that would read contents of the file "STUDENT.DAT" and display the details of those students whose 
percentage is above 75. Also display number of students scoring above 75%
'''

def count_rec():
    file = open("STUDENT.DAT","rb")
    count = 0
    try:
        while True:
            record = pickle.load(file)
            if record[2] > 75:
                print(record)
                count+=1
    except EOFError:
        pass
    print('No of students having more than 75% are', count)
    file.close()
