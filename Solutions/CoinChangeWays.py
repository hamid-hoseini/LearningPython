# How many ways can you make change with coins and a total amount?
'''
In the example, we have provided coin denominations [1, 2, 5] and the total amount of 5. 
In return, we got five ways we can make the change. 
'''

def solve_coin_change(denominations, amount):
    solution = [0] * (amount + 1)
    solution[0] = 1
    for den in denominations:
        for i in range(den, amount + 1):
            solution[i] += solution[i - den]

    return solution[len(solution) - 1]

denominations = [1,2,5]
amount = 5
