import random
from re import L

def More5():
    # Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
    #  Используйте для решения лямбда-функцию.
    # 2, 3, 4, 6, 7, 8 -> 6, 7, 8
    numbers = [random.randint(1, 10) for i in range(10)]
    print(numbers)
    result = lambda x: x > 5
    numbers = list(filter(result, numbers))
    print(numbers)


def Height():
    # Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
    # описывающие возрастающую последовательность. Порядок элементов менять нельзя.
    # [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    numbers = [random.randint(1, 10) for i in range (10)]
    print(numbers)

    result = [0]
    
    while len(result) < 2:
        index = random.randint(0, 9)  # случайный индекс, с которого начнем возрастающую последовательность
        result = [numbers[index]]
        for i in numbers[index:]:
            if i > result[len(result)-1]:
                result.append(i)    
        
    print(result)    


def UnicEl():
    # Задача 3. Задайте список случайных чисел от 1 до 10. 
    # Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
    numbers = [random.randint(1, 10) for i in range(10)]
    print(numbers)
    print("Количество повторяющихся элементов ", len(list(filter(lambda x: numbers.count(x) > 1, numbers))))
    # res = list(map(lambda x: numbers.remove(x) , list(filter(lambda x: numbers.count(x) > 1,  numbers))))
    result = []
    for i in numbers:
        if numbers.count(i) > 1:
            numbers.remove(i)
    print("Список уникальных элементов:")
    print(numbers)

# More5()
# Height()
UnicEl()