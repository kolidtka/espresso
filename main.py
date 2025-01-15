import sys
import sqlite3
from PyQt6 import QtWidgets, uic


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        # Подключение к базе данных SQLite
        self.connection = sqlite3.connect("coffee.sqlite")
        self.load_data()

    def load_data(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM coffees")
        rows = cursor.fetchall()

        for row in rows:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            for i, item in enumerate(row):
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, i, QtWidgets.QTableWidgetItem(str(item)))

    def closeEvent(self, event):
        self.connection.close()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
