import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Считывание данных из CSV файла
try:
    df = pd.read_csv("npv.csv")  # Замените "ваш_файл.csv" на имя вашего файла
except FileNotFoundError:
    print("Ошибка: Файл не найден. Убедитесь, что файл CSV существует и указано правильное имя.")
    exit()
except pd.errors.EmptyDataError:
    print("Ошибка: Файл CSV пуст.")
    exit()
except pd.errors.ParserError:
    print("Ошибка: Не удалось проанализировать CSV файл. Проверьте формат файла.")
    exit()

# Группировка данных по типу НПВ и суммирование затрат
grouped_data = df.groupby('Тип_НПВ')['Сумма затрат НПВ'].sum()

# Извлечение labels и values из сгруппированных данных
labels = grouped_data.index.tolist()
values = grouped_data.values.tolist()

# Цвета секторов (порядок должен соответствовать labels и values)
colors = [
    '#F44336',  # Красный (Превышение норм времени)
    '#FFEB3B',  # Желтый (Простой)
    '#E1BEE7',  # Сиреневый (Ремонт)
    '#FFB300',  # Оранжевый (Брак)
    '#2196F3',  # Синий (Инцедент)
    '#607D8B',  # Серый (Холостой рейс)
    '#4DB6AC',  # Бирюзовый (Ревизия КНБК)
    '#B2EBF2',  # Светло-голубой (Упущение времени)
    '#795548' #коричневый (Скрытые простои)
]

# Обновляем список цветов, чтобы он соответствовал labels
updated_colors = []
for label in labels:
    if label == 'Превышение норм времени':
        updated_colors.append('#F44336')
    elif label == 'Простой':
        updated_colors.append('#FFEB3B')
    elif label == 'Ремонт':
        updated_colors.append('#E1BEE7')
    elif label == 'Брак':
        updated_colors.append('#FFB300')
    elif label == 'Инцидент':
        updated_colors.append('#2196F3')
    elif label == 'Холостой рейс':
        updated_colors.append('#607D8B')
    elif label == 'Ревизия КНБК':
        updated_colors.append('#4DB6AC')
    elif label == 'Упущение времени':
        updated_colors.append('#B2EBF2')
    elif label == 'Скрытые простои':
        updated_colors.append('#795548')
    else:
        updated_colors.append('#808080')  # Если тип НПВ не найден, используем серый цвет

# Создаем круговую диаграмму
fig, ax = plt.subplots(figsize=(10, 8))  # Размер фигуры для лучшего отображения
wedges, texts = ax.pie(values, colors=updated_colors, startangle=90,
                       wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

# Добавляем подписи к секторам со значениями за пределами диаграммы
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(str(values[i]), xy=(x, y), xytext=(1.3*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

# Добавляем легенду (снизу диаграммы)
plt.legend(wedges, labels,
          title="Категории",
          loc="lower center",
          bbox_to_anchor=(0.5, -0.2), #расположение легенды
          ncol=3, #количество столбцов
          fontsize=10) #размер шрифта

# Заголовок диаграммы
ax.set_title("Распределение данных", fontsize=14) #заголовок
plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.show()