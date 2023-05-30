import random
def check_input(val_bool, text1, text2):
    while True:
         try:
             if val_bool:
                 request = list(map(int, input(text1).split()))
             else:
                 request = int(input(text1))
             break
         except ValueError:
             print(f"{text2} Повторите ввод")
    return request

list_numbers = check_input(1, "Введите последовательность чисел через пробел: ",
                           "В последовательности должны быть только числа.")
number = check_input(0, "Введите любое число: ", "Это не число.")

def qsort(list_n, left, right):
    p = random.choice(list_n[left:right + 1])
    i, j = left, right
    while i <= j:
        while list_n[i] < p:
            i += 1
        while list_n[j] > p:
            j -= 1
        if i <= j:
            list_n[i], list_n[j] = list_n[j], list_n[i]
            i += 1
            j -= 1
    if j > left:
        qsort(list_n, left, j)
    if right > i:
        qsort(list_n, i, right)
    return list_n

def binary_search(list_n, element, left, right):
    middle = (right + left) // 2
    if element > list_n[middle - 1] and element <= list_n[middle]:
        return f'Индекс числа, меньше введенного числа "{element}": {middle-1}'
    elif element < list_n[middle]:
        return binary_search(list_n, element, left, middle - 1)
    else:
        return binary_search(list_n, element, middle + 1, right)

sort_list_numbers = qsort(list_numbers, 0, len(list_numbers)-1)
print("____РЕШЕНИЕ ЗАДАЧИ____")
print(f"Отсортированный список: {sort_list_numbers}")

if number <= sort_list_numbers[0]:
    print (f'Число, которое меньше введенного чиcла "{number}", отсутствует в последовательности')
elif number > sort_list_numbers[len(sort_list_numbers)-1]:
    print(f'Индекс числа, меньше введенного числа "{number}": {len(sort_list_numbers)-1}')
else:
    print(binary_search(sort_list_numbers, number, 0, len(sort_list_numbers)))