from capitalize import capitalize

# if capitalize('hello') != 'Hello':
#     raise Exception('Функция не верно работает!')

# if capitalize('') != '':
#     raise Exception('Функция не верно работает!')


assert capitalize('') == ''
assert capitalize('hello') == 'Hello'

print('Все пройдено успешно')