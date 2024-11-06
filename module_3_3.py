def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(2, 'строка1', False)
print_params(2, 'строка2')
print_params()

# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)
print_params(c = [1, 2, 3])

# Распаковка параметров:
values_list = [1, 'list', True]
values_dict = {'a': 1, 'b': 'Распаковка параметров', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = [1, 'list']
print_params(*values_list_2, 42)