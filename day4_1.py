""""Сегодня нас ждет несложная алгоритмическая задачка.
Мы напишем функцию, которая на вход будет получать несортированный массив чисел первым параметром, и какой-то число вторым параметром.

Функция должна вернуть TRUE в случае, если в массиве есть два числа, которые в сумме датю то, которое мы передали вторым параметром.

Например

array: [1, 3, 2, 12, 11]
N: 5

result: TRUE // так как 3 и 2 в сумме дают 5"
"""

def check_sum(array1, number1):

    for i in range(len(array1)):
        for j in range(i + 1, (len(array1))):
            if array1[i] + array1[j] == number1:
                print(str(array1[i]) + " and " + str(array1[j]) + " gives us " + str(number1))
                return array1[i] + array1[j] == number1


print("test1")
print(check_sum([1, 3, 2, 12, 11], 5))

print("\ntest2")
print(check_sum([1, 1, 1, 1], 5))

print("\ntest3")
print(check_sum(['a', 'b', 'c'], 5))
