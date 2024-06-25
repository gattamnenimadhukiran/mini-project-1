import random
i=range(0,5)
sec_num =random.choice(i)
count =0
limit=2
while count < limit:
    guess= int(input('guess:'))
    count += 1
    if guess == sec_num:
       print("CONGRATULATIONS YOU GUESSED IT RIGHT")
       break
else:
    print('BETTER LUCK NEXT TIME')