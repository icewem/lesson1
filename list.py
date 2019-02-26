#Списки, задание.

number_list =['3','5','7','9','10.5']
print(number_list)
number_list.append('Python')    # добавить в конец списка
print(len(number_list))         # посчитать длинну списка   
print(number_list)              
del number_list[2]              # удалить элемент под номером N+1(нумерация с 0)
print(number_list)
number_list.remove("3")         # удалить из списка элемент "3"
print(number_list)
number_list.append("3")
number_list.append("7")
print(number_list)
print(number_list[0])           # вывод на экран 1й элемент списка
print(number_list[-1])          # вывод на экран последний элемент списка
print(number_list[1:5])         # вывод элементов со 2го по 4й включительно
number_list.remove("Python")    # удалить из списка элемент "Python"
print(number_list)


# Dictionaries

product = {
    "name": "iPhone Xs",
    "stock": 24,
    "price": 65432.1
}

product["memory"] = 64          # добавить в product элемент 'memory' со значением '64'
print(product['price'])         # вывести значение словоря 'product' элемента 'price'
print(product)
product.get("discount", 0)      

print(product)


# Задания
# Создайте словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

city_list = {
    "city": "Москва", 
    "temperature": "20"
    }

print(city_list['city'])
city_list["temperature"] = int(city_list["temperature"]) + 5
print(city_list['temperature'])

# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением '27.05.2019'
# Выведите на экран длину словаря

print(city_list.get("country"), "Россия")

city_list["data"] = "27.05.2019"
print(city_list)