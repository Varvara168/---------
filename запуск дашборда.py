import sys
import webview
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка основного окна
        # self.setWindowTitle("PyQt5 + PyWebView Dashboard")
        # self.setGeometry(100, 100, 800, 600)

        # Основной layout
        layout = QVBoxLayout()

        # Создание контейнера для PyQt5
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Запускаем PyWebView в том же потоке
        self.start_webview()

    def start_webview(self):
        # Создаем окно
        window = webview.create_window("Dashboard", "https://datalens.yandex/y70kyl0gz5hgk")

        # Функция для удаления элемента после загрузки
        def remove_logo():
            js_code = """
                const logoSection = document.querySelector('.dl-header');
                if (logoSection) {
                    logoSection.remove();
                }
            """
            window.evaluate_js(js_code)

        # Запускаем webview и выполняем JavaScript после загрузки
        window.events.loaded += remove_logo
        webview.start(gui='qt') # Попробуйте использовать PyQt's event loop</u> 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec_())
# https://datalens.yandex/y70kyl0gz5hgk
