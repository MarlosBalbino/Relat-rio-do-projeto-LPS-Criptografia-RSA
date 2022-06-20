from qt_core import QScrollBar


class MyScrollBar(QScrollBar):

    def __init__(
        self, 
        mim_height=30,
        scroll_width=10,
        scroll_color="#282a36",
        handle_color="#8489a6",
        handle_hover_color="#c3ccdf",
        handle_pressed_color="#44475a",
        btn_height=10
        ):
        super().__init__()

        self.setStyleSheet(f"""
            /*VERTICAL SCROLL BAR*/
            QScrollBar:vertical {{
                border: none;
                background-color: {scroll_color};
                width: {scroll_width}px;
                margin: {btn_height}px 0 {btn_height}px 0;
                border-radius: {scroll_width/2}px;
            }}
            /*VERTICAL SCROLL BAR HENDLE*/
            QScrollBar::handle:vertical {{
                background-color: {handle_color};
                min-height: {mim_height}px;
                border-radius: {scroll_width/2}px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: {handle_hover_color};
            }}
            QScrollBar::handle:vertical:pressed {{
                background-color: {handle_pressed_color}
            }}
            /*SCROLL BAR TOP BUTTOM*/
            QScrollBar::sub-line:vertical {{
                border: none;
                background-color: {handle_color};
                height: {btn_height}px;
                /*
                border-top-left-radius: {scroll_width/2}px;
                border-top-right-radius: {scroll_width/2}px;
                */
                border-radius: {scroll_width/2}px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }}
            QScrollBar::sub-line:vertical:hover {{
                background-color: {handle_hover_color};
            }}
            QScrollBar::sub-line:vertical:pressed {{
                background-color: {handle_pressed_color};
            }}
            /*SCROLL BAR BOTTOM BUTTOM*/
            QScrollBar::add-line:vertical {{
                border: none;
                background-color: {handle_color};
                height: {btn_height}px;
                /*
                border-bottom-left-radius: {scroll_width/2}px;
                border-bottom-right-radius: {scroll_width/2}px;
                */
                border-radius: {scroll_width/2}px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }}
            QScrollBar::add-line:vertical:hover {{
                background-color: {handle_hover_color};
            }}
            QScrollBar::add-line:vertical:pressed {{
                background-color: {handle_pressed_color};
            }}
            /*RESET ARROW*/
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
                background: none;
            }}
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                background: none;
            }}


            /*HORIZONTAL SCROLL BAR*/
            QScrollBar:horizontal {{
                border: none;
                background-color: {scroll_color};
                height: {scroll_width}px;                
                border-radius: {scroll_width/2}px;
                margin: 0 {btn_height}px 0 {btn_height}px;
            }}
            /*HORIZONTAL SCROLL BAR HENDLE*/
            QScrollBar::handle:horizontal {{
                background-color: {handle_color};
                min-width: {mim_height}px;
                border-radius: {scroll_width/2}px;
            }}
            QScrollBar::handle:horizontal:hover {{
                background-color: {handle_hover_color};
            }}
            QScrollBar::handle:horizontal:pressed {{
                background-color: {handle_pressed_color}
            }}
            /*SCROLL BAR LEFT BUTTOM*/
            QScrollBar::sub-line:horizontal {{
                border: none;
                background-color: {handle_color};
                width: {btn_height}px;
                /*
                border-top-left-radius: {scroll_width/2}px;
                border-top-right-radius: {scroll_width/2}px;
                */
                border-radius: {scroll_width/2}px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }}
            QScrollBar::sub-line:horizontal:hover {{
                background-color: {handle_hover_color};
            }}
            QScrollBar::sub-line:horizontal:pressed {{
                background-color: {handle_pressed_color};
            }}
            /*SCROLL BAR RIGHT BUTTOM*/
            QScrollBar::add-line:horizontal {{
                border: none;
                background-color: {handle_color};
                width: {btn_height}px;
                /*
                border-bottom-left-radius: {scroll_width/2}px;
                border-bottom-right-radius: {scroll_width/2}px;
                */
                border-radius: {scroll_width/2}px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }}
            QScrollBar::add-line:horizontal:hover {{
                background-color: {handle_hover_color};
            }}
            QScrollBar::add-line:horizontal:pressed {{
                background-color: {handle_pressed_color};
            }}
            /*RESET ARROW*/
            QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {{
                background: none;
            }}
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
                background: none;
            }}
        """)

    