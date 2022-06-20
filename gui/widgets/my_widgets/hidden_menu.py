from qt_core import (QFrame, QHBoxLayout, QVBoxLayout, QGraphicsOpacityEffect, QMainWindow,
QPushButton, QPropertyAnimation, QWidget)

from .opacity_effect_anim import OpacityEffectAnimation


class HiddenMenu(QFrame):
    # LEFT HIDDEN MENU
    #////////////////////////////////////////////////////////////////////
    def __init__(self, parent: QFrame) -> None:
        super().__init__(parent)

        # HIDDEN FRAME        
        self.setStyleSheet("background-color: transparent")
        self.setMaximumWidth(3840)
        self.setMinimumWidth(3840)
        self.setMinimumHeight(2160)
        self.hide()

        # HIDDEN FRAME LAYOUT
        self.hidden_layout = QHBoxLayout(self)
        self.hidden_layout.setContentsMargins(0,0,0,0)
        self.hidden_layout.setSpacing(0)

        # HIDDEN MENU
        self.hidden_menu = QFrame()
        self.hidden_menu.setStyleSheet("background-color: #44475a")
        self.hidden_menu.setMaximumWidth(0)
        self.hidden_menu.setMinimumWidth(0)
        self.hidden_menu.setMaximumHeight(2160)

        # MENU LAYOUT
        self.menu_layout = QVBoxLayout(self.hidden_menu)
        self.menu_layout.setContentsMargins(0,0,0,0)
        self.menu_layout.setSpacing(0)

        # OPACITY EFFECT
        self.effect = QGraphicsOpacityEffect(self.hidden_menu)
        self.effect.setOpacity(1.00)

        # SET HIDDEN MENU EFFECT
        self.hidden_menu.setGraphicsEffect(self.effect)
        self.hidden_menu.setAutoFillBackground(True)

        # HIDDEN BTN FRAME
        self.hidden_btn_frame = QFrame()
        self.hidden_btn_frame.setStyleSheet("background-color: transparent")
        self.hidden_btn_frame.setMaximumHeight(2160)

        # HIDDEN BTN
        self.hidden_btn = QPushButton(self.hidden_btn_frame)
        self.hidden_btn.setStyleSheet("background-color: transparent")
        self.hidden_btn.setFixedSize(3840, 3840)
        
        # ADD HIDDEN BTN TO HIDDEN FRAME
        self.hidden_layout.addWidget(self.hidden_menu)
        self.hidden_layout.addWidget(self.hidden_btn_frame)

    def set_central_widget(self, widget):
        self.menu_layout.addWidget(widget)

    def set_opacity_animation(self):
        self.opacity_animation = OpacityEffectAnimation(
            self.effect, 
            self.hidden_menu
        )

    def start(self):
        # Get hidden menu width
        menu_width = self.hidden_menu.width()

        self.animation = QPropertyAnimation(
            self.hidden_menu,
            b"minimumWidth"
        )
        
        width = 400
        # Check width
        if menu_width != width:
            self.show()
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(width)
            self.animation.setDuration(150)
        
        else:
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.hide)
            self.animation.setDuration(250)
        
        self.animation.start()
        try:
            self.opacity_animation.reset()
        except AttributeError:
            pass
