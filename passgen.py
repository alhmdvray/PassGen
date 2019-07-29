import random
import argparse


# Создаем парсер аргументов
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', '--path', default="./symbols.txt")
    parser.add_argument('-len', '--len', default=7)
    return parser


# Парсим аргументы консоли
parser = create_parser()
args = parser.parse_args()

# Переносим значения
path = args.path
pass_length = args.len

file_with_symbols = open(path, "r")  # Открываем файл с символами
symbols = file_with_symbols.read()  # Считываем все символы
coll_symbols = len(symbols)-1  # Количество символов
generated_password = ""  # Сгенерированный пароль

# Генерация пароля
for i in range(pass_length):
    generated_password += symbols[random.randint(0, coll_symbols)]
print(generated_password)

