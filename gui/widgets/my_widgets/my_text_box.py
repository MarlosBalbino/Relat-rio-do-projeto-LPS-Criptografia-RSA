from qt_core import QTextEdit
from .my_scroll_bar import MyScrollBar


class TextBox(QTextEdit):

    def __init__(
        self,
        parent=None,
        text_box_color="#282a36",
        read_only=False,
        hide=False,
        scroll_mim_height=30
        ):
        
        super().__init__(parent)

        self._style = f"""
            QTextEdit {{ 
                color: #707070;
                font: italic;
                font-size: 12pt; 
                border-radius: 5; 
                background-color: {text_box_color};
            }}
        """

        self.text_style = f"""
            QTextEdit {{ 
                color: white;
                font-size: 12pt;
                border-radius: 5; 
                background-color: {text_box_color};
            }}
        """

        self.setStyleSheet(self._style)
        self.setReadOnly(read_only)
        
        # CUSTOM VERTICAL SCROLL BAR
        self.vertical_scroll_bar = MyScrollBar(scroll_mim_height)
        self.setVerticalScrollBar(self.vertical_scroll_bar)
        self.setAcceptRichText(True)

        # HIDE BOX
        if hide is True:
            self.hide()

        self.textChanged.connect(self.change_handle)
    
    def change_handle(self):
        if self.toPlainText() == "":
            self.setStyleSheet(self._style)
        else:
            self.setStyleSheet(self.text_style)