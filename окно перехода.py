import sys
import pandas as pd
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
) 
import matplotlib.pyplot as plt
import numpy as np


class BarChartCanvas:
    def __init__(self, return_callback):
        self.fig, self.ax = plt.subplots(figsize=(14, 8))
        self.return_callback = return_callback

    def plot_bar_chart(self):
        # Создаем фигуру с двумя поддиаграммами
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

        # Читаем данные из npv.csv
        try:
            df = pd.read_csv("npv.csv")  # Убедитесь, что файл npv.csv существует
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
        bar_labels = grouped_data.index.tolist()
        bar_values = grouped_data.values

        # Цвета столбцов
        bar_colors = plt.cm.tab10.colors  # Используем стандартную палитру цветов matplotlib

        # Столбчатая диаграмма
        y_pos = np.arange(len(bar_labels))
        ax1.barh(y_pos, bar_values, color=bar_colors[:len(bar_labels)], alpha=0.7)

        ax1.set_yticks(y_pos)
        ax1.set_yticklabels(bar_labels)
        ax1.invert_yaxis()  # Для отображения в порядке сверху вниз
        ax1.set_xlabel("Общий НПВ")
        ax1.set_title("Типы НПВ", fontsize=14)

        # Отображение чисел на столбцах
        for i, value in enumerate(bar_values):
            ax1.text(value, i, f'{value:.2f}', ha='left', va='center', color='black', fontsize=8)

        # Круговая диаграмма
        colors = plt.cm.tab10.colors  # Используем ту же палитру цветов
        wedges, texts = ax2.pie(bar_values, colors=colors[:len(bar_values)], startangle=90,
                                wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

        # Добавляем легенду
        ax2.legend(wedges, bar_labels, title="Категории", loc="upper right", bbox_to_anchor=(1.3, 1))
        ax2.set_title("Распределение данных", fontsize=14)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()  

        # Отображение графика
        plt.show()

    def on_return(self, event):
        plt.close(self.fig)  # Закрываем текущее окно графика
        self.return_callback()  # Вызываем коллбек для возврата


    def __init__(self, return_callback):
        self.fig, self.ax = plt.subplots(figsize=(14, 8))
        self.return_callback = return_callback

    def plot_bar_chart1(self):
        
        try:
            df = pd.read_csv("npv.csv")  # Убедитесь, что файл npv.csv существует
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

            # Баланс календарного времени
        total_records = len(df)
        nvp_records = df[df['Тип_НПВ'].notna()].shape[0]  # Считаем записи с непустым Тип_НПВ
        pv_records = total_records - nvp_records
        balance_labels = ['ПВ', 'НПВ']
        balance_values_1 = [76.6, 23.4]
        balance_values_2 = [81.7, 18.3]
        balance_colors = ['#28a745', '#dc3545']
        responsibility_labels = ['Сервис', 'ИГС', 'Синтеко', 'Заказчик+Метео', 'ИГС-М', 'НЗУ']
        responsibility_values = [5.2, 2.7, 6.1, 8.1, 0.7, 4.0]
        responsibility_colors = ['#17a2b8', '#ffc107', '#6c757d', '#28a745', '#007bff', '#000000']
        nature_labels = ['Технологическое', 'Техническое', 'Организационное']
        nature_values = [10.4, 15, 10.9]
        nature_colors = ['#dc3545', '#ffc107', '#28a745']
        category_labels = ['Ремонт', 'Вспом. работы', 'Аварийность', 'Простои']
        category_values = [6.6, 9.9, 4.8, 5.1]
        category_colors = ['#dc3545', '#ffc107', '#6c757d', '#007bff']
        repair_time_labels = ['янв', 'февр', 'март', 'апр', 'май', 'июнь']
        repair_time_values = [6.4, 4.8, 4.6, 5.8, 4.5, 3.8]
        repair_time_color = '#778899'
        unproductive_labels = ['янв', 'февр', 'март', 'апр', 'май', 'июнь']
        unproductive_values = [13.7, 7.9, 10.9, 8.4, 9.5, 12.9]
        unproductive_color = '#DAA520'
        accident_labels = ['янв', 'февр', 'март', 'апр', 'май', 'июнь']
        accident_values = [9.2, 6.1, 5.4, 7.2, 7.1, 3.7]
        accident_color = '#d9534f'
        downtime_labels = ['янв', 'февр', 'март', 'апр', 'май', 'июнь']
        downtime_values = [12.5, 7.0, 3.9, 4.9, 3.9, 2.8]
        downtime_color = '#007bff'
        key_repairs_labels = ['Свп', 'Сил. привод', 'Бур. насос']
        key_repairs_values = [1.5, 1.4, 1.1]
        key_repairs_colors = ['#808080', '#a9a9a9', '#c0c0c0']
        key_unproductive_labels = ['Превышение норм времени', 'Внеп. работы', 'Доп. СПО']
        key_unproductive_values = [3.5, 2.9, 2.9]
        key_unproductive_colors = ['#F4A460', '#DAA520', '#BDB76B']
        key_incidents_labels = ['Осложнение ствола', 'Слом КНБК', 'Недопуск ОК']
        key_incidents_values = [1.6, 1.2, 1.0]
        key_incidents_colors = ['#dc3545', '#90EE90', '#BDB76B']
        key_downtime_labels = ['Метео', 'Приостановка работ', 'Ожидание ТМЦ']
        key_downtime_values = [1.6, 1.2, 1.1]
        key_downtime_colors = ['#00BFFF', '#ADD8E6', '#87CEEB']
        fig, axes = plt.subplots(4, 3, figsize=(24, 20)) 
        plt.subplots_adjust(hspace=0.5, wspace=0.3)
        ax0 = axes[0, 0] 
        ax0.bar(balance_labels, balance_values_1, color=balance_colors)
        ax0.set_title('Баланс календарного времени без учета МЕТЕО и простоя Заказчика', fontsize=10)
        ax01 = axes[0, 1]
        ax01.bar(balance_labels, balance_values_2, color=balance_colors)
        ax01.set_title('Баланс календарного времени без учета НПВ по 3 топ объектам', fontsize=10)
        ax1 = axes[1, 0]
        ax1.barh(category_labels, category_values, color=category_colors)
        ax1.set_title('Распределение НПВ по категориям (в целом по ИГС)', fontsize=10)
        ax1.set_xlim(0, max(category_values) * 1.1)
        ax02 = axes[0, 2]
        ax02.bar(responsibility_labels, responsibility_values, color=responsibility_colors)
        ax02.set_title('По зоне ответственности НПВ', fontsize=10)
        ax12 = axes[1, 2]
        ax12.bar(nature_labels, nature_values, color=nature_colors)
        ax12.set_title('По характеру НПВ', fontsize=10)
        ax2 = axes[2, 0]
        ax2.plot(repair_time_labels, repair_time_values, marker='o', color=repair_time_color)
        ax2.set_title('Динамика ремонтного времени', fontsize=10)
        ax2.set_ylabel('%')
        ax2.set_ylim(0, max(repair_time_values) * 1.1)
        ax21 = axes[2, 1]
        ax21.plot(unproductive_labels, unproductive_values, marker='o', color=unproductive_color)
        ax21.set_title('Динамика непроизводительных работ', fontsize=10)
        ax21.set_ylabel('%')
        ax21.set_ylim(0, max(unproductive_values) * 1.1)
        ax22 = axes[2, 2]
        ax22.plot(accident_labels, accident_values, marker='o', color=accident_color)
        ax22.set_title('Динамика аварийности', fontsize=10)
        ax22.set_ylabel('%')
        ax22.set_ylim(0, max(accident_values) * 1.1)
        ax3 = axes[3, 0]
        ax3.barh(key_repairs_labels, key_repairs_values, color=key_repairs_colors)
        ax3.set_title('Ключевые ремонты', fontsize=10)
        ax3.set_xlim(0, max(key_repairs_values) * 1.1)
        ax31 = axes[3, 1]
        ax31.barh(key_unproductive_labels, key_unproductive_values, color=key_unproductive_colors)
        ax31.set_title('Ключевые НПР', fontsize=10)
        ax31.set_xlim(0, max(key_unproductive_values) * 1.1)
        ax32 = axes[3, 2]
        ax32.barh(key_incidents_labels, key_incidents_values, color=key_incidents_colors)
        ax32.set_title('Ключевые инциденты и брак', fontsize=10)
        ax32.set_xlim(0, max(key_incidents_values) * 1.1)
        plt.suptitle("Типы НПВ", fontsize=14)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
        plt.show()

    def on_return(self, event):
        plt.close(self.fig)  # Закрываем текущее окно графика
        self.return_callback()  # Вызываем коллбек для возврата


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bar Chart Example")
        self.setGeometry(100, 100, 800, 600)

        # Создаем ОДИН центральный виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Создаем ОДИН макет
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # === Первый набор виджетов ===
        self.label = QLabel("Выберите действие:")
        self.layout.addWidget(self.label)

        self.button_show_chart = QPushButton("Показать график")
        self.button_show_chart.clicked.connect(self.show_chart)
        self.layout.addWidget(self.button_show_chart)

        # === Второй набор виджетов ===
        self.label1 = QLabel("Выберите действие 2:")  # Изменен текст для ясности
        self.layout.addWidget(self.label1)

        self.button_show_chart1 = QPushButton("Показать диаграмму")
        self.button_show_chart1.clicked.connect(self.show_chart1)
        self.layout.addWidget(self.button_show_chart1)

        # === Кнопка выхода (только одна) ===
        self.button_exit = QPushButton("Выход")
        self.button_exit.clicked.connect(self.close)
        self.layout.addWidget(self.button_exit)

    def show_chart(self):
        self.canvas = BarChartCanvas(self.return_to_selection)
        self.canvas.plot_bar_chart()

    def return_to_selection(self):
        self.label.setText("Выберите действие:")  # Сброс текста метки
        print("Вернуться к выбору")

    def show_chart1(self):
        self.canvas1 = BarChartCanvas(self.return_to_selection1)
        self.canvas1.plot_bar_chart1()

    def return_to_selection1(self):
        self.label1.setText("Выберите действие 2:")  # Сброс текста метки
        print("Вернуться к выбору 2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
