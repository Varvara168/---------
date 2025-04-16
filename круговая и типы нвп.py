import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text

# Данные для круговой диаграммы
pie_labels = [
    'Превышение норм времени',
    'Упущение времени',
    'Простой',
    'Скрытые простои',
    'Ремонт',
    'Брак',
    'Инцидент',
    'Холостой рейс',
    'Ревизия КНБК'
]

pie_values = [
    900.07,
    624.26,
    212.83,
    70.50,
    68.55,
    53.00,
    20.86,
    6.29,
    5.96
]

pie_colors = [
    '#F44336',  # Красный (Превышение норм времени)
    '#FFEB3B',  # Желтый (Простой)
    '#E1BEE7',  # Сиреневый (Ремонт)
    '#FFB300',  # Оранжевый (Брак)
    '#2196F3',  # Синий (Инцедент)
    '#607D8B',  # Серый (Холостой рейс)
    '#4DB6AC',  # Бирюзовый (Ревизия КНБК)
    '#B2EBF2',  # Светло-голубой (Упущение времени)
    '#795548'  # Коричневый (Скрытые простои)
]

# Данные для горизонтальной столбчатой диаграммы
bar_labels = [
    'Превышение норм времени',
    'Простой',
    'Ремонт',
    'Брак',
    'Инцидент',
    'Холостой рейс',
    'Ревизия КНБК',
    'Упущение времени',
    'Скрытые простои'
]

bar_values = [
    [17.42, 151.19, 63.43, 105.34, 103.31, 93.65, 183.84, 108.29],  # Пример данных для первого типа столбцов
    [1.47, 59.35, 480.00],  # Пример данных для второго типа столбцов
    [39.92, 101.77],  # Пример данных для третьего типа столбцов
    [70.50],  # Пример данных для четвертого типа столбцов
    [28.00],  # Пример данных для пятого типа столбцов
    [4.50],  # Пример данных для шестого типа столбцов
    [16.00],  # Пример данных для седьмого типа столбцов
    [5.25],  # Пример данных для восьмого типа столбцов
    [2.34]  # Пример данных для девятого типа столбцов
]

bar_colors = [
    '#90EE90',  # Салатовый (1)
    '#FFDEAD',  # Светло-коричневый (2)
    '#DA70D6',  # Фиолетовый (3)
    '#0000CD',  # Синий (4)
    '#FF8C00',  # Оранжевый (5)
    '#808080',  # Серый (6)
    '#FFD700',  # Золотой (7)
    '#3CB371',  # Зелёный (8)
    '#DDA0DD'   # Пурпурный (9)
]

# Создаем фигуру с двумя поддиаграммами
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

# Создаем круговую диаграмму
wedges, texts = ax1.pie(pie_values, colors=pie_colors, startangle=90,
                        wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

# Добавляем подписи к секторам
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
    ax1.annotate(str(pie_values[i]), xy=(x, y), xytext=(1.3*np.sign(x), 1.4*y),
                 horizontalalignment=horizontalalignment, **kw)

# Добавляем легенду для круговой диаграммы
ax1.legend(wedges, pie_labels,
           title="Категории",
           loc="lower center",
           bbox_to_anchor=(0.5, -0.2),
           ncol=3,
           fontsize=10)

# Заголовок круговой диаграммы
ax1.set_title("Распределение данных", fontsize=14)

# Столбчатая диаграмма
y_pos = np.arange(len(bar_labels))

for i, label in enumerate(bar_labels):
    left_position = 0
    for j, value in enumerate(bar_values[i]):
        ax2.barh(y_pos[i], value, left=left_position, color=bar_colors[j])
        left_position += value

ax2.set_yticks(y_pos)
ax2.set_yticklabels(bar_labels)
ax2.invert_yaxis()  # Для отображения в порядке сверху вниз
ax2.set_xlabel("Общий НПВ")
ax2.set_title("Типы НПВ", fontsize=14)

# Отображение чисел на столбцах
for i, label in enumerate(bar_labels):
    left_position = 0
    for j, value in enumerate(bar_values[i]):
        ax2.text(left_position + value / 2, y_pos[i], f'{value:.2f}', ha='center', va='center', color='black', fontsize=8)
        left_position += value

# Добавление общей легенды для столбчатой диаграммы
handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in bar_colors]
ax2.legend(handles, [str(i+1) for i in range(len(bar_colors))], loc="lower right", title="Легенда", bbox_to_anchor=(1.2, 0))

# Отображение графиков
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Корректировка для отображения заголовков и легенд
plt.show()

