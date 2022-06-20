from qt_core import QSlider


class MySlider(QSlider):

    def __init__(
        self,
        margin = 3,
        bg_size = 10,
        bg_radius = 5,
        bg_color = "#1b1e23",
        bg_color_hover = "#1e2229",
        handle_margin = -3,
        handle_size = 16,
        handle_radius = 8,
        handle_color = "#8489a6",    
        handle_color_hover = "#c3ccdf",
        handle_color_pressed = "#44475a"
    ):
        super(MySlider, self).__init__()

        self.setStyleSheet(f"""
            QSlider {{ margin: {margin}px;}}

            /* HORIZONTAL */
            QSlider::groove:horizontal {{
                border-radius: {bg_radius}px;
                height: {bg_size}px;
                margin: 0px;
                background-color: {bg_color};
            }}
            QSlider::groove:horizontal:hover {{
                background-color: {bg_color_hover};
            }}
            QSlider::handle:horizontal {{
                border: node;
                height: 16px;
                width: 16px;
                margin: {handle_margin}px;
                border-radius: {handle_radius}px;
                background-color: {handle_color}
            }}
            QSlider::handle:horizontal:hover {{
                background-color: {handle_color_hover};
            }}
            QSlider::handle:horizontal:pressed {{
                background-color: {handle_color_pressed}
            }}

            /* VERTICAL */
            QSlider::groove:vertical {{
                border-radius: {bg_radius}px;
                height: {bg_size};
                margin: 0px;
                background-color: {bg_color};
            }}
            Qlider::groove:vertical:hover {{
                background-color: {bg_color_hover};
            }}
            Qlider::handle:vertical {{
                border: node;
                height: {handle_size}px;
                width: {handle_size}px;
                margin: {handle_margin}px;
                border-radius: {handle_radius}px;
                background-color: {handle_color};
            }}
            QSlider::handle:vertical:hover {{
                background-color: {handle_color_hover};
            }}
            QSlider::handle:vertical:pressed {{
                background-color: {handle_color_pressed}
            }}
        """
        )
