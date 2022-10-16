# задача 2
# number = int(input("Введите число: "))
# while(number < 0 or number > 10):
#     number = int(input("Введите число в диапазоне от 0 до 10: "))
# print(number**2)
#
# задача 1
# number = int(input("Введите число: "))
# number = number + 2
# print(number)
#
#задача 3
# name = input("Введите ваше имя и фамилию: ")
# age = int(input("Введите ваш возраст: "))
# weight = int(input("Введите ваш вес: "))
# if age < 30:
#     if weight >= 50 and weight <=120:
#         print(name, "Ваше состояние хорошее")
#     else:
#         print("А про вас в задаче не указано)")
# if age > 30 and age < 40:
#     if weight <= 50 or weight >= 120:
#         print(name, "Вам следует заняться собой")
#     else:
#         print("А про вас в задаче не указано)")
# if age > 40:
#     if weight <= 50 or weight >= 120:
#         print(name, "Вам требуется врачебный осмотр")
#     else:
#         print("А про вас в задаче не указано)")
#
# просто попробую сделать угадай число с "тепло/холодно"
from random import *
value = int(input("Попробуйте угадать число от 1 до 100: "))
number = randint(1, 100)
diff = number - value
while True:
    if value >= 1 and value <=100:
        while abs(diff) != 0:
            if abs(diff) >= 1 and abs(diff) <= 10:
                value = int(input("Очень горячо. Попробуйте угадать еще раз: "))
                diff = number - value
            elif abs(diff) > 10 and abs(diff) <= 20:
                value = int(input("Горячо. Попробуйте угадать еще раз: "))
                diff = number - value
            elif abs(diff) > 20 and abs(diff) <= 30:
                value = int(input("Прохладно. Попробуйте угадать еще раз: "))
                diff = number - value
            elif abs(diff) > 30 and abs(diff) <= 40:
                value = int(input("Холодно. Попробуйте угадать еще раз: "))
                diff = number - value
            elif abs(diff) > 40:
                value = int(input("Очень холодно. Попробуйте угадать еще раз: "))
                diff = number - value
        if diff == 0:
            print("Поздравляю, вы угадали!")
            break
    else:
        while value <= 0 or value >= 100:
            value = int(input("Введенное вами число не находится в диапазоне от 0 до 100. Введите число еще раз: "))
            diff = number - value