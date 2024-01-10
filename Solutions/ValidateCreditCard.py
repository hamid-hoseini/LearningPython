## Luhn Algorithm
### step 1, request input
number = input('Please enter credit card number:> ')
## Check validity of number
num_list = [int(char) for char in number]
num_len = len(num_list)
num_list_rev = num_list[::-1]
double = 0
single = 0
for i in range(0,num_len):
    if i%2 != 0:
        if 2*num_list_rev[i]>9:
            double = double + 2*num_list_rev[i] - 9
        else:
            double = double + 2 * num_list_rev[i]
    else:
        single = single + num_list_rev[i]

if (double+single)%10 == 0:
    print(f'{number} is a valid credit card number.')
else:
    print(f'{number} is not a valid credit card number.')

Credit Card Numbers:


371449635398431

378734493671000

5610591081018250

30569309025904

38520000023237

6011111111111117

6011000990139424

3530111333300000

3566002020360505

5555555555554444

5105105105105100

4111111111111111

4012888888881881

4222222222222
