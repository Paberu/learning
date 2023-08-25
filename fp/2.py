from pymonad.tools import curry


@curry(2)
def glue_strings(str1, str2):
    return str1 + str2


hello = glue_strings('Hello, ')
print(hello('Vasya'))


@curry(4)
def first_step(greeting, comma_like, end_sentence, name):
    return greeting + comma_like + ' ' + name + end_sentence


final = first_step('Hello', ',', '!')
print(final('Petya'))
