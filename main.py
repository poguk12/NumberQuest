import random

qwer = True

print("Угадай число от 1 до 10!")

randomInt = random.randint(1, 11)

while(qwer):
    x = int(input())

    if (randomInt == x):
        print("Вы угадали!")
        qwer = False
    else:
        print("Вы не угадали! Попробуйте еще!")


