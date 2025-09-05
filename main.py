import random

qwer = True

print("Угадай число от 1 до 10!")

randomInt = random.randint(1, 11)

def sravnit(a, b):
    if (a == b):
        return True
    else:
        return False

while(qwer):
    x = int(input())

    if (sravnit(x, randomInt) == True):
        print("Вы угадали!")
        qwer = False
    else:
        print("Вы не угадали! Попробуйте еще!")


