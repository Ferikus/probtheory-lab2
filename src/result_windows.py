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


# class ResultWindowN3(QtWidgets.QWidget):
#     def __init__(self, accepted_count, rejected_count):
#         super().__init__()
#         self.setWindowTitle("Проверка гипотезы")
#         self.setGeometry(100, 100, 400, 300)
#
#         layout = QtWidgets.QVBoxLayout(self)
#
#         # self.r0_label = QtWidgets.QLabel(self)
#         # self.r0_label.setText(f"Значение статистики R0: {r0:.4f}")
#         # layout.addWidget(self.r0_label)
#         #
#         # self.chi2_label = QtWidgets.QLabel(self)
#         # self.chi2_label.setText(f"Критическое значение χ²({df}, {alpha:.2f}): {chi2_critical:.4f}")
#         # layout.addWidget(self.chi2_label)
#
#         self.table_widget = QtWidgets.QTableWidget(self)
#         self.table_widget.setRowCount(2)
#         self.table_widget.setColumnCount(2)
#         self.table_widget.setHorizontalHeaderLabels(["Результат", "Количество"])
#
#         self.table_widget.setItem(0, 0, QtWidgets.QTableWidgetItem("Принятые гипотезы"))
#         self.table_widget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(accepted_count)))
#
#         self.table_widget.setItem(1, 0, QtWidgets.QTableWidgetItem("Отклоненные гипотезы"))
#         self.table_widget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(rejected_count)))
#
#         layout.addWidget(self.table_widget)
#
#         self.setLayout(layout)

class ResultWindowN3(QtWidgets.QWidget):
    def __init__(self, accepted_num, rejected_num, alpha, check_num, f_values, outputs):
        super().__init__()
        self.setWindowTitle("Проверка гипотезы")
        self.setGeometry(100, 100, 600, 400)

        layout = QtWidgets.QVBoxLayout(self)

        alpha_label = QtWidgets.QLabel(self)
        alpha_label.setText(f"Уровень значимости (alpha): {alpha:.2f}")
        layout.addWidget(alpha_label)

        check_num_label = QtWidgets.QLabel(self)
        check_num_label.setText(f"Количество проверок гипотезы: {check_num}")
        layout.addWidget(check_num_label)

        result_table = QtWidgets.QTableWidget(self)
        result_table.setRowCount(len(f_values))
        result_table.setColumnCount(2)
        result_table.setHorizontalHeaderLabels(["F_(R0)", "Решение"])
        result_table.setColumnWidth(1, 200)
        result_table.setFixedHeight(500)

        for i, (f_value, output) in enumerate(zip(f_values, outputs)):
            result_table.setItem(i, 0, QtWidgets.QTableWidgetItem(f"{f_value:.4f}"))
            result_table.setItem(i, 1, QtWidgets.QTableWidgetItem(output))

        layout.addWidget(result_table)

        summary_table = QtWidgets.QTableWidget(self)
        summary_table.setRowCount(2)
        summary_table.setColumnCount(2)
        summary_table.setHorizontalHeaderLabels(["Результат", "Количество"])
        summary_table.setFixedHeight(100)

        summary_table.setItem(0, 0, QtWidgets.QTableWidgetItem("Принятые гипотезы"))
        summary_table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(accepted_num)))

        summary_table.setItem(1, 0, QtWidgets.QTableWidgetItem("Отклоненные гипотезы"))
        summary_table.setItem(1, 1, QtWidgets.QTableWidgetItem(str(rejected_num)))

        layout.addWidget(summary_table)

        self.setLayout(layout)