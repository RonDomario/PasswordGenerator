from PyQt6 import QtWidgets, QtCore
import sys
import pyperclip
from os.path import join, abspath
from random import choice, randint
from stylesheets import label, button, slider, checkbox, browser


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = abspath(".")
    return join(base_path, relative_path)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.password = ""
        self.setWindowTitle("PGen")
        self.setFixedSize(222, 222)
        self.central = QtWidgets.QLabel()
        self.central.setStyleSheet(label.style)
        self.setCentralWidget(self.central)
        self.layout = QtWidgets.QVBoxLayout()
        self.central.setLayout(self.layout)

        self.length_label = QtWidgets.QLabel("Length: 1")
        self.length_label.setStyleSheet(label.style)
        self.layout.addWidget(self.length_label)
        self.length_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.length_slider.setMinimum(1)
        self.length_slider.setMaximum(50)
        self.length_slider.setValue(1)
        self.length_slider.setStyleSheet(slider.style)
        self.length_slider.valueChanged.connect(self.update_length)
        self.layout.addWidget(self.length_slider)

        self.special_switch = QtWidgets.QCheckBox("Special Characters")
        self.special_switch.setStyleSheet(checkbox.style)
        self.layout.addWidget(self.special_switch)
        self.hide_switch = QtWidgets.QCheckBox("Hide Password")
        self.hide_switch.setStyleSheet(checkbox.style)
        self.hide_switch.setCheckState(QtCore.Qt.CheckState.Checked)
        self.hide_switch.checkStateChanged.connect(self.update_visibility)
        self.layout.addWidget(self.hide_switch)
        self.generate_button = QtWidgets.QPushButton("Generate and Copy")
        self.generate_button.setStyleSheet(button.style)
        self.generate_button.clicked.connect(self.generate)
        self.layout.addWidget(self.generate_button)
        self.password_browser = QtWidgets.QTextBrowser()
        self.password_browser.setStyleSheet(browser.style)
        self.layout.addWidget(self.password_browser)
        self.show()

    def update_length(self, value):
        self.length_label.setText(f"Length: {value}")

    def update_visibility(self):
        if self.hide_switch.isChecked():
            self.password_browser.setText("*" * len(self.password))
        else:
            self.password_browser.setText(self.password)

    def generate(self):
        characters = []
        alpha = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        special = "`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
        collection = alpha + numbers
        if self.special_switch.isChecked():
            collection += special
        length = self.length_slider.value()
        for _ in range(length):
            char = choice(collection)
            if char.isalpha():
                if randint(0, 1):
                    char = char.upper()
            characters.append(char)
        self.password = "".join(characters)
        if self.hide_switch.isChecked():
            self.password_browser.setText("*" * len(self.password))
        else:
            self.password_browser.setText(self.password)
        pyperclip.copy(self.password)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
