def rhythm(str):
    str = str.split()
    list = []
    for word in str:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])

print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
str = input()
if rhythm(str):
    print('Парам пам-пам')
else:
    print('Пам парам')

#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
#которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    print(a)
    for i in a:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)

# Задание 1 необязательное Сделайте локальный чат-бот с внешним хранилищем. Тема чат-бота - любая вам интересная

import json
import time

mp3 = []
mp3.append('Руки Вверх')
mp3.append("Света")
mp3.append("Максим")
mp3.append("Что то крутое  ")

def load():
    for percent in range(20):
        print('|', end='')
        time.sleep(0.1)
def save():
    with open('mp3.json','w',encoding='utf-8') as X:
        X.write(json.dump(mp3,ensure_ascii=False))
    print('Все сохранено в фал mp3.json')


while True:
    komanda = input('Не знаешь что вводить, введи /help 🤔')
    if komanda == '/start':
        print('Добро пожаловать')
    elif komanda == '/stop':
        print('Bay-bay')
        break
    elif komanda == '/sall':
        print('Вот что у меня есть из музыки 😎')
        print(*mp3, sep='\n')
    elif komanda == '/add':
        x = (input('Какое музыкальное произведение добавим ? 🎵 '))
        mp3.append(x.title())
        print('Загрузка ',end='')
        load()
        print(f'-OK {x.title()} Успешно добавлен в библоетку 🤘')
    elif komanda == '/save':
        save()
    elif komanda == '/help':
        print(f'/stop - Закончить работу с ботом\n'
              f'/add - Добавить музыку в библиотек\n'
              f'/sall - Показать доступную музыку\n')
    elif komanda == '/del':
        print(*mp3,sep='\n')
        dl = input('Что убрать из библиотеки ')
        x = 0
        while x == 0:
            if dl.title() in mp3:
                mp3.remove(dl.title())
                print('Удаляю 😔')
                load()
                print(f' > {dl.title()} <  больше нет в библиотке 😭')
                break
            else:
                dl = input("Такого тут и не было 🤥\n Попробуй еще раз или вернись назад /b,"
                           " что бы еще раз вывести список - /sall : ")
                if dl == '/b':
                    x = 1
                elif dl == '/sall':
                    print(*mp3, sep='\n')


    else:
        print('Неверрная команда, введите /help')
