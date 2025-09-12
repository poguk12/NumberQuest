import random

qwer = True

print("Угадай число от 1 до 1000!")

randomInt = random.randint(1, 11)

def sravnit(a, b):
    if (a == b):
        return True
    else:
        return False

while(qwer):
    x = int(input())

    if (sravnit(x, randomInt) == True):
        print("ВЫ УГАДАЛИ!")
        qwer = False
    else:
        print("ВЫ НЕ УГАДАЛИ! ПОПРОБУЙСТЕ ЕЩЕ РАZЗЗЗ!")

print("date 12/09/25")