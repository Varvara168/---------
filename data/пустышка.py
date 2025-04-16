import sys
import matplotlib.pyplot as plt
import importlib  # Для перезагрузки модуля при изменениях
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,  QPushButton, QFileDialog, QMessageBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# Класс для отображения графика
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(24, 20))  # Устанавливаем общий размер Figure
        self.axes = fig.subplots(4, 3)  # Используем subplots для сетки
        super().__init__(fig)
        self.setParent(parent)


    def plot_graphs(self, module):
        """Отрисовывает графики, используя данные из импортированного модуля."""
        try:
            # Очищаем предыдущие графики
            for ax in self.axes.flatten():
                ax.clear()

            # Получаем данные из модуля
            balance_labels = module.balance_labels
            balance_values_1 = module.balance_values_1
            balance_values_2 = module.balance_values_2
            balance_colors = module.balance_colors
            responsibility_labels = module.responsibility_labels
            responsibility_values = module.responsibility_values
            responsibility_colors = module.responsibility_colors
            nature_labels = module.nature_labels
            nature_values = module.nature_values
            nature_colors = module.nature_colors
            category_labels = module.category_labels
            category_values = module.category_values


            #  Графики
            self.axes[0, 0].bar(balance_labels, balance_values_1, color=balance_colors)
            self.axes[0, 0].set_title('Баланс календарного времени без учета МЕТЕО и простоя Заказчика', fontsize=10)
            self.axes[0, 1].bar(module.balance_labels, module.balance_values_2, color=balance_colors)
            self.axes[0, 1].set_title('Баланс календарного времени без учета НПВ по 3 топ объектам', fontsize=10)
            self.axes[1, 0].barh(module.category_labels, module.category_values, color=module.category_colors)
            self.axes[1, 0].set_title('Распределение НПВ по категориям (в целом по ИГС)', fontsize=10)
            self.axes[1, 0].set_xlim(0, max(module.category_values) * 1.1)
            self.axes[0, 2].bar(module.responsibility_labels, module.responsibility_values, color=module.responsibility_colors)
            self.axes[0, 2].set_title('По зоне ответственности НПВ', fontsize=10)
            self.axes[1, 2].bar(module.nature_labels, module.nature_values, color=module.nature_colors)
            self.axes[1, 2].set_title('По характеру НПВ', fontsize=10)
            self.fig.suptitle("Типы НПВ", fontsize=16)
            self.fig.tight_layout(rect=[0, 0.03, 1, 0.95])
            self.draw()  # Перерисовываем canvas


        except AttributeError as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка доступа к данным в 'stolbiky.py': {e}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при отрисовке графика: {e}")



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики НПВ")

        self.plot_widget = PlotCanvas(self)
        self.button_update = QPushButton("Обновить графики")

        layout = QVBoxLayout()
        layout.addWidget(self.button_update)
        layout.addWidget(self.plot_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.button_update.clicked.connect(self.update_plots)

    def update_plots(self):
        try:
            import stolbiky  # Импортируем модуль
            importlib.reload(stolbiky)  # Перезагружаем модуль (если файл изменился)
            self.plot_widget.plot_graphs(stolbiky)  # Передаем модуль с данными
        except ImportError:
            QMessageBox.critical(self, "Ошибка", "Не удалось импортировать 'stolbiky.py'. Проверьте имя файла и его расположение.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())