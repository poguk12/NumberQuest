import random

print("Угадай число от 1 до 10!")

randomInt = random.randint(1, 10)

x = int(input())

if (randomInt == x):
    print("Вы угадали!")
else:
    print("NO, ЗАГАДАННОЕ ЧИСЛО: ", randomInt)