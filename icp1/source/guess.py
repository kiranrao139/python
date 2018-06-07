import random
rannum = random.randint(0,9)
while True:
    num = int(input('enter number'))
    if rannum == num:
        print('Your answer is PERFECT!! Congratulations!!',rannum)
        break
    elif rannum < num:
        print('Your answer is low than required')
    else :
        print('Your answer is high than required')
