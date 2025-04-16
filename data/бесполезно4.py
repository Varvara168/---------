import csv
import datetime

# Чтение данных из CSV
dates = []
npv = []
y_pred = []  # Прогнозированные значения

with open('npv_data.txt', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Пропустить заголовок
    for row in csv_reader:
        dates.append(row[0])  # Первая колонка - это даты
        npv.append(float(row[1]))  # Вторая колонка - это НПВ (конвертируем в float)
        y_pred.append(float(row[1]))  # Здесь просто пример, что это прогноз (замените на реальные прогнозы)

# Запись данных в новый CSV файл
output_filename = 'predictions.csv'

with open(output_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'True NPV', 'Predicted NPV'])  # Заголовки
    for date, true_npv, predicted_npv in zip(dates, npv, y_pred):
        writer.writerow([date, true_npv, predicted_npv])

print(f"Результаты записаны в {output_filename}")
