keys = ['product_name', 'quantity', 'price', 'date']

# Первая функция
def read_sales_data(file_path):
    # Загрузка и чтение данных
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    total_list = []
    # Разбиение входного txt файла на строки (data.split('\n')) и на элементы (row.split(', '))
    for row in [row.split(', ') for row in data.split('\n')]:
        dict_row = dict()
        # Прохождение по каждому элементу каждой строки и присваивание соответствующих ключей
        for index, element in enumerate(row):
            dict_row[keys[index]] = element
        # Загрузка по одной строке в список (с учетом правила "одна строка - один товар")
        total_list.append(dict_row)
    return total_list

# Вторая функция
def total_sales_per_product(sales_data):
    total_dict = {}
    for row in sales_data:
        # Проверка на нахождение названия продукта рассматриваемой строки в словаре
        if row[keys[0]] in total_dict:
            # Если в словаре уже есть такое название продукта, то происходит суммирование значений
            total_dict[row[keys[0]]] += int(row[keys[1]]) * int(row[keys[2]])
        else:
            # Если в словаре нет такого названия продукта, то оно записывается как новое
            total_dict[row[keys[0]]] = int(row[keys[1]]) * int(row[keys[2]])
    return total_dict

# Третья функция
def sales_over_time(sales_data):
    total_dict = {}
    for row in sales_data:
        # Проверка на нахождение даты рассматриваемой строки в словаре
        if row[keys[3]] in total_dict:
            # Если в словаре уже есть такая дата, то происходит суммирование значений
            total_dict[row[keys[3]]] += int(row[keys[1]]) * int(row[keys[2]])
        else:
            # Если в словаре нет такой даты, то она записывается как новая
            total_dict[row[keys[3]]] = int(row[keys[1]]) * int(row[keys[2]])
    return total_dict