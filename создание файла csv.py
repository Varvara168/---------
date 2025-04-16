import csv
import random
from datetime import datetime, timedelta

# Настройки
projects = [f"Проект{i}" for i in range(1, 12)]
stages = [f"Этап{i}" for i in range(1, 8)]
crews = [f"Бригада{i}" for i in range(1, 11)]

npv_types = {
    "Превышение норм времени": 900.07,
    "Простой": 624.26,
    "Ремонт": 212.83,
    "Брак": 70.50,
    "Инцидент": 68.55,
    "Холостой рейс": 53.00,
    "Ревизия КНБК": 20.86,
    "Улучшение времени": 6.29,
    "Упущение времени": 5.96,
    "Скрытые простои": 5.00
}

# Переводим "часы" в минуты
npv_minutes = {k: int(v * 60) for k, v in npv_types.items()}

# Список, чтобы отслеживать занятые интервалы по проектам
project_timeline = {project: [] for project in projects}

# Генерация случайной даты в 2024 году
def random_start_time():
    start = datetime(2024, 1, 1, 0, 0)
    end = datetime(2024, 12, 31, 23, 59)
    delta = end - start
    random_minutes = random.randint(0, int(delta.total_seconds() // 60))
    return start + timedelta(minutes=random_minutes)

# Проверка пересечений для проекта
def is_available(project, start, end):
    for s, e in project_timeline[project]:
        if start < e and end > s:
            return False
    return True

# Генерация записей
records = []
record_id = 1

for npv_type, total_minutes in npv_minutes.items():
    remaining = total_minutes
    while remaining > 0:
        duration = min(random.randint(30, 240), remaining)  # эпизоды 0.5–4 ч
        project = random.choice(projects)
        stage = random.choice(stages)
        crew = random.choice(crews)

        # Найдём слот без пересечений
        for _ in range(1000):  # ограничим попытки
            start = random_start_time()
            end = start + timedelta(minutes=duration)
            if is_available(project, start, end):
                project_timeline[project].append((start, end))
                project_timeline[project].sort()
                break
        else:
            continue  # если не удалось найти свободное окно

        records.append([
            record_id,
            project,
            stage,
            crew,
            npv_type,
            start.strftime("%Y-%m-%d"),
            end.strftime("%Y-%m-%d")
        ])
        record_id += 1
        remaining -= duration

# Сортируем по дате начала
records.sort(key=lambda x: datetime.strptime(x[5], "%Y-%m-%d"))

# Запись в CSV
with open("npv.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["№", "Проект", "Этап", "Бригада", "Тип_НПВ", "Дата начала", "Дата конца", "доля_нвп", "доля_пв", "Сумма затрат НПВ","длительность_часы"])
    writer.writerows(records)

print("Готово! Файл 'npv.csv' создан.")
