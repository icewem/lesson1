# сделайте так, чтобы программа приветствовала вас,
# используя переменную name и форматирование строк например "Привет, Миша!"

name = 'Artem'
format_name = f'Привет {name}'
print(format_name)  

age = int(input('Сколько вам лет? '))
birth_year = 2019 - age # Ошибка
print(f'Вы родились в {birth_year} году.')

# поправьте код, чтобы выводилось число
# на 10 больше, чем введённое
# например, пользователь ввел 10, программа 

v = int(input('Введите число от 1 до 10: '))
print(v+10)

# поправьте код, чтобы выводитась строка:
# Привет, ИМЯ! Как дела?

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Какое чудесное у тебя имя!')  

print(float('1'))
print(int('25'))
print(bool(1))
print(bool(''))
print(bool(0))