import copy

# Рядки:
# Навести приклад простого рядка
# Навести приклад багаторядкового рядка (Вірш, хоку - щоб показати форматування)
# Навести приклад рядка з ігноруванням екрануючих символів (Raw)
# Навести приклад форматування довгих рядків
print('Привіт \n')
print('''Спить собака.
Різкий дзвін.
Зелений лист.\n''')

print(r'Спить \"собака\"\n''\n\"собака\"')

print('\nСпить\nдуже\nдовго\nс\tо\tб\tа\tк\tа\n')
# Списки:
# Створити простий список
# Створити змінну з посиланням на перший список
# Створити поверхову (Shallow copy) копію першого списка
# Створити глибоку (повну) (Deep copy) першого списка
# Вивести значення всіх списків
# Змінити перший список і ще раз вивести значення всіх списків
easy_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
referring_list = easy_list
list_shel = easy_list.copy()
deep_copy = copy.deepcopy(easy_list)
print('Посиланння на перший список: {}, and values {}'.format(id(easy_list), easy_list))
print('Посиланння на нову зміну: {}, and values {}'.format(id(referring_list), referring_list))
print('Посиланння на Shallow copy: {} and values {}'.format(id(list_shel), list_shel))
print('Посиланння на Deep copy: {} and values {}\n'.format(id(deep_copy), deep_copy))
easy_list.append(11)
print('Посиланння після зміни на перший список: {}, and values {}'.format(id(easy_list), easy_list))
print('Посиланння на нову зміну: {}, and values {}'.format(id(referring_list), referring_list))
print('Посиланння після змін на Shallow copy: {} and values {}'.format(id(list_shel), list_shel))
print('Посиланння після змін на Deep copy: {} and values {}\n'.format(id(deep_copy), deep_copy))
# Словники:
# Створити пустий словник одним з наведених в лекції способів
# Створити новий словник з 2-3 парами ключ:значення
# Додати одну пару ключ:значення до першого словника
# Додати до першого словника другий словник використовуючи .update()
# видалити один елемент словника за допомогою .pop()
# Видалити один елемент за допомогою .popitem()
# Зробити глибоку копію першого словника в нову змінну
# Додати до нового словника новий ключ, а як значення передати перший словник
# Вивести список ключів
# Вивести список значень

empty_dict = {}
new_dict = {
    'name': 'Serhii',
    'surname': 'Yatsiuk',
    'city': 'Kiyv'
}
empty_dict['country'] = 'Ukraine'
empty_dict.update(new_dict)
pop_dict = empty_dict.copy()
pop_dict.pop('city')
print(pop_dict)
pop_dict.popitem()
print(pop_dict)
deep_dict = copy.deepcopy(empty_dict)
deep_dict['dictionary'] = empty_dict
print(deep_dict)
print(deep_dict.keys())
print(deep_dict.values())

# Тернарний if - 2 приклади.
if 'name' in empty_dict:
    print(empty_dict['name'])
else:
    print('\nError')

if id(easy_list) == id(list_shel):
    print('True\n')
else:
    print('False\n')

# Вкладені структури:
# Створити 3 вимірний список (список 3х списків)
# Змінити, будь який, елемент, будь якого, спику.
# Вивести значення до та після
# Створити список зі вкладеним словником
# Створити словник зі вкладеним списком
# Зберегти вкладений список зі словника у нову змінну
three_list = [1, 2, 3, 4, 5, [10, 20, 30, 40, 50, [100, 200, 300], 60, 70, 80, 90], 6, 7, 8, 9]
print('значення до :{}'.format(three_list))
three_list[5][5][0] = 999
print('значення після зміни 100 на 999 :{}'.format(three_list))
list_dict = [1, 2, 3, 4, 5, {'name': 'Serhii',
    'surname': 'Yatsiuk'}]
print(list_dict)
dict_with_list = {'country': 'Ukraine',
                  'city': 'Kiyv',
                  'list': ['Apple', 'Pineapple', 'Peach', 'Banana']
}
print(dict_with_list)
print('\n')

# Побітові операції:
# побітове AND:
# Порівняти два різних цілих і два однакових числа і вивести результат
# Порівняти два різних рядка і два однакових рядка і вивести результат
# Повторити дії і та іі з пункту а для решти операцій (OR, XOR, NOT)
# Виконати побітовий зсув вліво для:
# Цілого числа на 1, 2 та 3 біти
# Рядка на 1, 2 та 3 біти
# Виконати побітовий зсув вправо для:
# Цілого числа на 1, 2 та 3 біти
# Рядка на 1, 2 та 3 біти
# Кожну логічну частину коду відділяти пустим рядком та коментарем (Опціонально)

a = 2
b = 4
print('a & b =', a & b)
print('a | b =', a | b)
print('~a =', ~a)
print('a ^ b =', a ^ b)