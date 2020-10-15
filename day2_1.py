"""
"Сегодня предлагаю написать программу, которая будет работать с текстом.
Надо написать функцию, которая на вход принимает текстовое значение и число - указание максимальной длины.
Результатом ее работы должен стать анализ этого текста по следующим правилам:

- Функция должна напечатать количество символов в тексте.
- Функция должна напечатать количество символов без учета пробелов.
- Функция должна напечатать ""количество символов в тексте четное"" или ""количество символов в тексте нечетное"" в
зависимости от количества символов (тут пробелы учитываем).
- Функция должна напечатать ""длина текста превышает длину {N} символов"", где N - это целочисленное значение,
которое передается вторым параметром в функцию. Само собой, если на самом деле длина текста меньше максимальной, то это писать не надо."
"""

def inspect_text(text_input, max_lenght):

    char_count_total = len(text_input)
    char_count_no_spaces = len("".join(list(text_input.replace(" ", ""))))
    number_type = even_odd()
    compare_to_max_lenght_result = compare_to_max_lenght()

    return ("The number of symbols in the text is {}, without spaces is {}.\nThe number of symbols is {}.{}".format(char_count_total, char_count_no_spaces, number_type, compare_to_max_lenght_result))

def even_odd():
    if len(text_input) % 2 == 0:
        return "even"
    elif len(text_input) % 2 != 0:
        return "odd"
    else:
        print("Something is wrong")

def compare_to_max_lenght():
    if len(text_input) > max_lenght:
        return "\nThe leght of text exceeds {} symbols.".format(max_lenght)
    else:
        return ("")

print("test 1")
text_input = "hey how are you"
max_lenght = 10

print(inspect_text(text_input, max_lenght))

print("\ntest 2")
text_input = "Sunnyvale"
max_lenght = 30

print(inspect_text(text_input, max_lenght))

print("\ntest 3")
text_input = ""
max_lenght = 0

print(inspect_text(text_input, max_lenght))
