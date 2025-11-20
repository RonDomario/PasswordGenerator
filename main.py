from PyQt6 import QtWidgets, QtCore
import sys
import pyperclip
from stylesheets import label, button, slider, checkbox, browser, lcd
from secrets import choice, SystemRandom
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.password = ""
        self.pin = ""
        self.setWindowTitle("PGen")
        self.setFixedSize(200, 400)
        self.central = QtWidgets.QLabel()
        self.central.setStyleSheet(label.style)
        self.setCentralWidget(self.central)
        self.layout = QtWidgets.QVBoxLayout()
        self.central.setLayout(self.layout)

        self.password_label = QtWidgets.QLabel("Password Generator:")
        self.layout.addWidget(self.password_label)
        self.password_length_label = QtWidgets.QLabel("Length: 8")
        self.password_length_label.setStyleSheet(label.style)
        self.layout.addWidget(self.password_length_label)
        self.password_length_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.password_length_slider.setMinimum(8)
        self.password_length_slider.setMaximum(50)
        self.password_length_slider.setValue(8)
        self.password_length_slider.setStyleSheet(slider.style)
        self.password_length_slider.valueChanged.connect(self.update_password_length)
        self.layout.addWidget(self.password_length_slider)

        self.special_switch = QtWidgets.QCheckBox("Special Characters")
        self.special_switch.setStyleSheet(checkbox.style)
        self.layout.addWidget(self.special_switch)
        self.password_hide_switch = QtWidgets.QCheckBox("Hide Password")
        self.password_hide_switch.setStyleSheet(checkbox.style)
        self.password_hide_switch.setCheckState(QtCore.Qt.CheckState.Checked)
        self.password_hide_switch.checkStateChanged.connect(self.update_password_visibility)
        self.layout.addWidget(self.password_hide_switch)
        self.password_generate_button = QtWidgets.QPushButton("Generate and Copy")
        self.password_generate_button.setStyleSheet(button.style)
        self.password_generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.password_generate_button)
        self.password_browser = QtWidgets.QTextBrowser()
        self.password_browser.setLineWrapMode(QtWidgets.QTextBrowser.LineWrapMode.FixedColumnWidth)
        self.password_browser.setLineWrapColumnOrWidth(20)
        self.password_browser.setStyleSheet(browser.style)
        self.layout.addWidget(self.password_browser)

        self.pin_label = QtWidgets.QLabel("PIN Generator:")
        self.pin_label.setStyleSheet(label.style)
        self.layout.addWidget(self.pin_label)
        self.pin_length_label = QtWidgets.QLabel("Length: 4")
        self.pin_length_label.setStyleSheet(label.style)
        self.layout.addWidget(self.pin_length_label)
        self.pin_length_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.pin_length_slider.setMinimum(4)
        self.pin_length_slider.setMaximum(12)
        self.pin_length_slider.setValue(4)
        self.pin_length_slider.setStyleSheet(slider.style)
        self.pin_length_slider.valueChanged.connect(self.update_pin_length)
        self.layout.addWidget(self.pin_length_slider)
        self.pin_hide_switch = QtWidgets.QCheckBox("Hide PIN")
        self.pin_hide_switch.setStyleSheet(checkbox.style)
        self.pin_hide_switch.setCheckState(QtCore.Qt.CheckState.Checked)
        self.pin_hide_switch.checkStateChanged.connect(self.update_pin_visibility)
        self.layout.addWidget(self.pin_hide_switch)
        self.pin_generate_button = QtWidgets.QPushButton("Generate and Copy")
        self.pin_generate_button.setStyleSheet(button.style)
        self.pin_generate_button.clicked.connect(self.generate_pin)
        self.layout.addWidget(self.pin_generate_button)
        self.pin_display = QtWidgets.QLCDNumber()
        self.pin_display.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.pin_display.display("")
        self.pin_display.setNumDigits(4)
        self.pin_display.setStyleSheet(lcd.style)
        self.layout.addWidget(self.pin_display)
        self.show()

    def update_password_length(self, value):
        self.password_length_label.setText(f"Length: {value}")

    def update_pin_length(self, value):
        self.pin_length_label.setText(f"Length: {value}")

    def update_password_visibility(self):
        if self.password_hide_switch.isChecked():
            self.password_browser.setText("*" * len(self.password))
        else:
            self.password_browser.setText(self.password)

    def update_pin_visibility(self):
        if self.pin_hide_switch.isChecked():
            self.pin_display.display("P" * len(self.pin))
        else:
            self.pin_display.display(self.pin)

    def generate_password(self):
        password = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits)]
        collection = ascii_lowercase + ascii_uppercase + digits
        if self.special_switch.isChecked():
            collection += punctuation
            password.append(choice(punctuation))
        length = self.password_length_slider.value()
        password += [choice(collection) for _ in range(length - 3 - self.special_switch.isChecked())]
        SystemRandom().shuffle(password)
        self.password = "".join(password)
        if self.password_hide_switch.isChecked():
            self.password_browser.setText("*" * len(self.password))
        else:
            self.password_browser.setText(self.password)
        pyperclip.copy(self.password)

    def generate_pin(self):
        length = self.pin_length_slider.value()
        pin = [choice(digits) for _ in range(length)]
        SystemRandom().shuffle(pin)
        self.pin = "".join(pin)
        self.pin_display.setNumDigits(length)
        if self.pin_hide_switch.isChecked():
            self.pin_display.display("P" * len(self.pin))
        else:
            self.pin_display.display(self.pin)
        pyperclip.copy(self.pin)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
