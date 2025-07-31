from .colors import *

style = """
            QSlider{
                background: %s;
            }
            QSlider::groove:horizontal {  
                height: 9px;
                border-radius: 5px;
                background: %s;
                border: %s;
            }
            QSlider::handle:horizontal {
                background: %s;
                border: %s;
                width: 13px;
                margin: -6px 0; 
                border-radius: 6px;
            }
            QSlider::sub-page:qlineargradient {
                background: %s;
                border-radius: 5px;
            }
        """ % (normal_background,
               normal_background, border,
               normal_background, border,
               normal_color)
