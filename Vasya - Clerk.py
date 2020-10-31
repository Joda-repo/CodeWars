"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge
line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

tickets([25, 25, 50]) # => YES
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change
(you can't make two bills of 25 from one of 50)
"""
# if we don't care about quee order.
"""
def tickets(people):
    money_dict = {25:0, 50:0, 100:0}
    for i in people:
        money_dict[i] = people.count(i)
    for x in range(0, money_dict.get(50)):
        money_dict[25] -= 1
        if money_dict[25] < 0:
            return "NO"
    for y in range(0, money_dict.get(100)):
        if money_dict[50] > 0:
            money_dict[50] -= 1
            money_dict[25] -= 1
        else:
            money_dict[25] -= 3
        if money_dict[50] < 0 or money_dict[25] < 0:
            return "NO"
    return "YES"
"""


# if we care about quee order.

def tickets(people):
    money_dict = {25: 0, 50: 0, 100: 0}
    for i in people:
        if money_dict[25] < 0 or money_dict[50] < 0 or money_dict[100] < 0:
            print('NO')
            return 'NO'
        if i == 25:
            money_dict[25] += 1
        else:
            if i == 50:
                money_dict[50] += 1
                money_dict[25] -= 1
            if i == 100 and money_dict[50] <= 0:
                money_dict[25] -= 3
            if i == 100 and money_dict[50] > 0:
                money_dict[50] -= 1
                money_dict[25] -= 1
    if money_dict[25] >= 0 and money_dict[50] >= 0 and money_dict[100] >= 0:
        print('YES')
        return "YES"
    else:
        print('NO')
        return 'NO'


tickets([25, 25, 50, 100])