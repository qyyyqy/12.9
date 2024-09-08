from functions import read_sales_data, total_sales_per_product, sales_over_time
import matplotlib.pyplot as plt
from datetime import datetime


# Результаты функций
result_of_function1 = read_sales_data('data.txt')
result_of_function2 = total_sales_per_product(result_of_function1)
result_of_function3 = sales_over_time(result_of_function1)
# Продукт принёсший наибольшую выручку и день с наибольшей суммой продаж
max_product = max(result_of_function2, key=result_of_function2.get)
max_day = max(result_of_function3, key=result_of_function3.get)
print(f'Продукт принёсший наибольшую выручку: {max_product}\nДень с наибольшей суммой продаж: {max_day}')

# Подготовка данных для построения графиков
products = list(result_of_function2.keys())
total_sales_product = list(result_of_function2.values())
dates = list(result_of_function3.keys())
total_sales_date = list(result_of_function3.values())
# Преобразование строковых дат в даты формата datetime для сортировки
date_sales_pairs = sorted(zip(dates, total_sales_date), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
sorted_dates, sorted_total_sales_date = zip(*date_sales_pairs)

# Создание полотна с двумя графиками (2 строки, 1 столбец)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Первый график (общая сумма продаж по продуктам)
ax1.bar(products, total_sales_product, color='#4956a7')
ax1.set_title('Total sales for each product')
ax1.set_ylabel('Total sales')
ax1.set_xlabel('Products')
ax1.set_xticks(range(len(products)))
ax1.set_xticklabels(products)
ax1.grid(True)

# Второй график (общая сумма продаж по дням)
ax2.plot(sorted_dates, sorted_total_sales_date, marker='o', color='#4956a7')
ax2.set_title('Total sales by date')
ax2.set_ylabel('Total sales')
ax2.set_xlabel('Dates')
ax2.set_xticks(range(len(sorted_dates)))
ax2.set_xticklabels(sorted_dates)
ax2.grid(True)

# Регулировка отступов между графиками и их вывод
plt.tight_layout()
plt.show()