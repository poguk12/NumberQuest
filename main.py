from faker import Faker
import random

qwer = True

fake = Faker()  

print(fake.name(), fake.address())

'''
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
        # TODO: Добавить проверку на пустой код
        print("Вы не угадали! Попробуйте еще!")

print("date 12/09/25")
'''