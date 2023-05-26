# Tuple
# Створити кортеж котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7
# Вивести кортеж у консоль
new_tuple = tuple((1, 2, 3, 4, 5, 6, 7))
print(f'Tuple: {new_tuple}\n')
# Set
# Створити set котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7
# Створити set котрий приймає в себе наступний ряд: 5, 6, 7, 8, 9, 10, 11
# Розширити перший сет за допомогою коменди .add(0)
# Виконати команду .intersection() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
# Виконати команду .difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
# Виконати команду .symmetric_difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
# Вивести всі змінні у консоль.
new_set = {1, 2, 3, 4, 5, 6, 7}
print(f'First Set: {new_set}')
new_set_2 = {5, 6, 7, 8, 9, 10, 11}
print(f'Second Set: {new_set_2}')
new_set.add(0)
print(f'First Set after add 0: {new_set}')


set_intersection = new_set.intersection(new_set_2)
print(f'Set use intersection: {set_intersection}')
set_difference = new_set.difference(new_set_2)
print(f'Set use difference: {set_difference}')
set_symmetric_difference = new_set.symmetric_difference(new_set_2)
print(f'Set use symmetric_difference: {set_symmetric_difference}')
