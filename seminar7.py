"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

from csv import DictReader, DictWriter
from os.path import exists


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


class PhoneError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_user_data():
    flag = False
    while not flag:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError('Неправильная длина!')
            last_name = input('Введите фамилию: ')
            phone_number = int(input("Введите телефон, начиная с 8: "))
            if len(str(phone_number)) != 11:
                raise PhoneError("Неверная длина номера!")
            flag = True
        except ValueError:
            print('Вы вводите символы вместо цифр!')
            continue
        except NameError as err:
            print(err)
            continue
        except PhoneError as err:
            print(err)
            continue
    return first_name, last_name, phone_number


def create_file(file_name):
    with open(file_name, "w", encoding="utf-8") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()


file_name = "phone.csv"
file_name_new = "phone_new.csv"


# create_file(file_name)

def read_file(file_name):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name):
    user_data = get_user_data()
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(user_data[2]):
            print("Такой пользователь уже существует")
            return
    obj = {"Имя": user_data[0], "Фамилия": user_data[1], "Телефон": user_data[2]}
    res.append(obj)
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(res)


def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
            print("Данные успешно записаны!")
        elif command == "r":
            if not exists(file_name):
                print("Файл не создан, создайте его!")
                continue
            print(read_file(file_name))


# main()

"""
Домашнее задание.
Дополнить справочник возможностью копирования данных из одного файла в другой. 
Пользователь вводит номер строки, которую необходимо перенести из одного 
файла в другой.


Комментарий
для домашки создаем функцию copy_data на вход имя файла откуда
 копируем (file name) и куда копируем (file name new)  и номер строки
 
 читаем все содержимое файла
 переменную res  взять по индексу (индекс-1)
 
 
 в новый список добавляем через append
"""


def copy_data(file_name, file_name_new):
    row_index = int(input("Какую строку копируем? "))
    res = read_file(file_name)
    obj = res[row_index - 1]
    result = read_file(file_name_new)
    result.append(obj)

    with open(file_name_new, "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(result)


copy_data(file_name, file_name_new)
