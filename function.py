# работа по видео уроку

def discounted(price,discount,max_discount=50):
    price  = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
          raise ValueError("Максимальная скидка не может быть больше 99%")
    if discount >= max_discount:
        price_witch_discount = price
    else:
        price_witch_discount = price - price * discount / 100
    return(price_witch_discount)

print(discounted(100,40))

# Задание 1
# Создайте функцию get_summ(one, two, delimiter='&') которая принимает два парамтера, вприводит их к строке и отдает объединеными через разделитель delimteter
# Вызовите функцию, пердав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран
# Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ(one, two, delimiter='&')