from qt_core import QPushButton


class MyPushButton(QPushButton):

    def __init__(
        self,
        text = "",
        color = "#8489a6", 
        border_radius = 10,
        font_size = 12,
        hover = "#c3ccdf",
        pressed = "#44475a",
        maximum_width = 72,
        maximum_heigth = 20,
        set_disabled=False,
        hide=False
    ):

        super().__init__()

        self.color = color
        self.border_radius = border_radius
        self.font_size = font_size
        self.hover = hover
        self.pressed = pressed
        self.disabled = set_disabled

        self.setText(text)        
        self.setMaximumWidth(maximum_width)
        self.setMaximumHeight(maximum_heigth)
        self.set_disabled(set_disabled)

        if hide:
            self.hide()

    def set_disabled(self, set_disabled):
        self.setDisabled(set_disabled)
        self.set_style(
            color = self.color, 
            border_radius = self.border_radius,
            font_size = self.font_size,
            hover = self.hover,
            pressed = self.pressed,
            disabled = set_disabled
        )

    def set_style(
        self,
        color = "#8489a6", 
        border_radius = 10,
        font_size = 12,
        hover = "#c3ccdf",
        pressed = "#44475a",
        disabled = False
        ):

        style = f"""
            QPushButton {{
                background-color: {color};
                border-radius: {border_radius}px;
                font-size: {font_size}pt;
            }}
            QPushButton:hover {{
                background-color: {hover};
            }}
            QPushButton:pressed {{
                background-color: {pressed};
            }}
        """

        disabled_style = f"""
            
            QPushButton:disabled {{
                background-color: #676b84;
                color: grey;
            }}
        """

        if disabled:
            self.setStyleSheet(style + disabled_style)
        else:
            self.setStyleSheet(style)