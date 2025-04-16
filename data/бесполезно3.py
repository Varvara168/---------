import csv
import matplotlib.pyplot as plt
import datetime

# Чтение данных из CSV-файла
dates = []
npv = []

with open('npv_data.txt', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Пропустить заголовок
    for row in csv_reader:
        dates.append(row[0])  # Первая колонка - это даты
        npv.append(float(row[1]))  # Вторая колонка - это НПВ (конвертируем в float)

# Преобразуем строки с датами в объекты datetime
dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates]

# Создаем график
plt.figure(figsize=(10, 6))
plt.plot(dates, npv, label="НПВ", color='blue', marker='o')

# Настройки графика
plt.title("Динамика НПВ по дням")
plt.xlabel("Дата")
plt.ylabel("НПВ")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  # Для правильного расположения меток

# Показать график
plt.show()
plt.legend()
