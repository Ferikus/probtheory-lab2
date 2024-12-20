from PyQt5 import QtWidgets


class ResultWindowN1(QtWidgets.QWidget):
    def __init__(self, results):
        super().__init__()
        self.setWindowTitle("Результаты розыгрыша")
        self.setGeometry(100, 100, 600, 100)

        layout = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setRowCount(1)
        self.table.setColumnCount(len(results))
        self.table.setHorizontalHeaderLabels([f"x({i + 1})" for i in range(len(results))])

        for i, value in enumerate(results):
            self.table.setItem(0, i, QtWidgets.QTableWidgetItem(f"{value:.4f}"))

        layout.addWidget(self.table)
        self.setLayout(layout)


class ResultWindowN2(QtWidgets.QWidget):
    def __init__(self, results, characteristics, d):
        super().__init__()
        self.setWindowTitle("Статистические характеристики")
        self.setGeometry(100, 100, 1000, 200)

        layout = QtWidgets.QVBoxLayout(self)

        # --- Таблица для результатов розыгрыша ---
        draw_table = QtWidgets.QTableWidget(self)
        draw_table.setRowCount(1)
        draw_table.setColumnCount(len(results))
        draw_table.setHorizontalHeaderLabels([f"x({i + 1})" for i in range(len(results))])

        for i, value in enumerate(results):
            draw_table.setItem(0, i, QtWidgets.QTableWidgetItem(f"{value:.4f}"))

        layout.addWidget(draw_table)

        # --- Таблица для характеристик ---
        characteristics_table = QtWidgets.QTableWidget(self)
        characteristics_table.setRowCount(1)
        characteristics_table.setColumnCount(len(characteristics) - 1)
        headers = list(characteristics.keys())
        characteristics_table.setHorizontalHeaderLabels(headers)

        for i, (name, value) in enumerate(characteristics.items()):
            characteristics_table.setItem(0, i, QtWidgets.QTableWidgetItem(f"{value:.4f}"))

        characteristics_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        layout.addWidget(characteristics_table)

        # ---  Label для D ---
        d_label = QtWidgets.QLabel(self)
        d_label.setText(f"<p>Расхождение D: {d:.4f}</p>")
        layout.addWidget(d_label)

        self.setLayout(layout)


class ResultWindowN2_2(QtWidgets.QWidget):
    def __init__(self, table_info, interval_bounds, max_height):
        super().__init__()
        self.setWindowTitle("Интервальная таблица")
        self.setGeometry(100, 100, 600, 200)  # Adjust size as needed

        layout = QtWidgets.QVBoxLayout(self)

        table = QtWidgets.QTableWidget(self)
        table.setRowCount(len(table_info))
        intervals_num = len(interval_bounds) - 1
        table.setColumnCount(intervals_num)

        # setting table headers
        header_labels = []
        for j in range(intervals_num):
            header_labels.append(f"[{interval_bounds[j]:.2f}, {interval_bounds[j+1]:.2f})")
        table.setHorizontalHeaderLabels(header_labels)
        table.setVerticalHeaderLabels(table_info.keys())

        # populate the table
        for i, (key, values) in enumerate(table_info.items()):
            for j in range(len(values)):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(f"{values[j]:.4f}"))

        # Set vertical header labels
        # self.table.setVerticalHeaderLabels(["nj", "f(zj)"])

        layout.addWidget(table)

        # ---  Label для максимальной высоты гистограммы ---
        max_height_label = QtWidgets.QLabel(self)
        max_height_label.setText(f"Максимальная высота: {max_height:.4f}")
        layout.addWidget(max_height_label)

        self.setLayout(layout)