def calculate_sum_and_length(data):
    total_sum = 0
    total_length = 0

    if isinstance(data, tuple):
        for element in data:
            sub_sum, sub_length = calculate_sum_and_length(element)
            total_sum += sub_sum
            total_length += sub_length
    elif isinstance(data, list):
        for item in data:
            sub_sum, sub_length = calculate_sum_and_length(item)
            total_sum += sub_sum
            total_length += sub_length
    elif isinstance(data, (int, float)):
        total_sum += data
    elif isinstance(data, str):
        total_length += len(data)
    elif isinstance(data, dict):
        for value in data.values():
            sub_sum, sub_length = calculate_sum_and_length(value)
            total_sum += sub_sum
            total_length += sub_length
        for key in data.keys():
            sub_sum, sub_length = calculate_sum_and_length(key)
            total_sum += sub_sum
            total_length += sub_length
    elif isinstance(data, set):
        for element in data:
            sub_sum, sub_length = calculate_sum_and_length(element)
            total_sum += sub_sum
            total_length += sub_length

    return total_sum, total_length


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum, total_length = calculate_sum_and_length(data_structure)
print(f"Сумма всех чисел: {total_sum}")
print(f"Сумма длин всех строк: {total_length}")
print(f"Общая сумма: {total_sum + total_length}")
