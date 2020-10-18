""""Сегодня поработаем с массивами. Давайте напишем функцию, которая на вход получает массив слов. Например:
[""apple banana"", ""orange"", ""banana"", ""kiwi strawberry blueberry""]
Видно, что в этом массиве в некоторых слотах затесалось сразу несколько слов. На выходе
функция должна вернуть такой массив, где одно слово будет в каждом элементе:
[""apple"", ""banana"", ""orange"", ""banana"", ""kiwi"", ""strawberry"", ""blueberry""]
Словом считается любой набор символов, обособленный пробелами или началом/концом строки.
"""


def alter_array (random_array):

    single_word_array = []

    for i in random_array:

        if len(i) <= 1:
            single_word_array.append(i)

        else:
            i = i.split()
            for j in i:
                single_word_array.append(j)

    return single_word_array

print("test1")
random_array = ["apple banana", "orange", "banana", "kiwi strawberry blueberry"]
print(alter_array(random_array))

print("test2")
random_array = []
print(alter_array(random_array))
