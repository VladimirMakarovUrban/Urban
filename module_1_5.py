immutable_var = (1, 2, 'a', 'b', [10, 20])
print('Кортеж: ', immutable_var)
# immutable_var[0] = 5
print('Кортеж не изменяемый')

mutable_list = [1, 2, 'a', 'b']
print('Исходный список: ', mutable_list)
mutable_list.append('c')
print('Добавили "c": ', mutable_list)
mutable_list[0] = 5
print('Заменили первое значение списка: ', mutable_list)