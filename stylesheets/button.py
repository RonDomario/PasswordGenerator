from .colors import *

style = """
            QPushButton {
                background-color: %s;
                color: %s;
                border: %s;
            }

            QPushButton:hover:pressed {
                background-color: %s;
                color: %s;
            }

            QPushButton:disabled {
                background-color: rgb(20, 20, 20);
                color: rgb(50, 100, 50);
            }

            QPushButton:hover {
                background-color: %s;
                color: %s;
            }
        """ % (normal_background, normal_color, border,
               pressed_background, pressed_color,
               hover_background, hover_color)
