from qt_core import QFrame, QSize, QSpacerItem, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QResizeEvent
from .my_push_button import MyPushButton
from .my_text_box import TextBox
from typing import Type

class TextBoxWindow(QFrame):
    # TEXT BOX
    #////////////////////////////////////////////////////////////////////
    def __init__(
        self, 
        parent=None, 
        label_text="",
        label_tittle="",
        tittle_color="rgb(255, 255, 255)",
        btn1_text="",
        btn1_width=72,
        disable_btn1=False,
        btn2_text="",
        btn2_width=72,
        disable_btn2=True,
        disable_btns=False,
        hide_btn1=False,
        hide_btn2=False,
        window_resize=QSize(500, 250)
    ):
        super().__init__(parent)

        # TEXT BOX FRAME            
        self.setStyleSheet("background-color: #44475a; border-radius: 5")
        if window_resize:
            self.setMaximumSize(window_resize)
            self.setMinimumSize(window_resize)

        # TOP FRAME
        self.top_frame = QFrame()
        self.top_frame.setMinimumHeight(25)
        # self.top_frame.setStyleSheet("background-color: blue")

        # TOP FRAME LAYOUT
        self.top_frame_layout = QHBoxLayout(self.top_frame)
        self.top_frame_layout.setContentsMargins(0,0,0,0)

        # LABEL TEXT
        self.text_label = QLabel(self)
        self.text_label.setText(label_text)
        self.text_label.setStyleSheet("font: 700 12pt Segoe UI; color: rgb(255, 255, 255)")

        # LABEL TEXT
        self.label_tittle = QLabel(self)
        self.label_tittle.setText(label_tittle)
        self.label_tittle.setStyleSheet(f"font: 700 13pt Segoe UI; color: {tittle_color}")

        # SPACER
        self.spacer = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        # ADD LABELS TO LAYOUT
        self.top_frame_layout.addWidget(self.text_label)
        self.top_frame_layout.addWidget(self.label_tittle)
        self.top_frame_layout.addSpacerItem(self.spacer)

        # CENTRAL FRAME
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: transparent")
        self.central_frame.setMinimumHeight(10)

        self.central_layout = QHBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.central_layout.setSpacing(9)

        # CENTRAL FRAME 3
        self.central_frame2 = QFrame()
        self.central_frame2.setMinimumHeight(0)
        self.central_frame2.setStyleSheet("background-color: transparent")

        self.central_layout2 = QHBoxLayout(self.central_frame2)
        self.central_layout2.setContentsMargins(0,0,0,0)
        self.central_layout2.setSpacing(9)

        # BTNS FRAME
        self.bottom_frame = QFrame()
        self.bottom_frame.setMinimumHeight(20)
        if disable_btns is True:
            self.bottom_frame.hide()        
        # self.bottom_frame.setStyleSheet("background-color: blue")

        # BTNS LAYOUT
        self.bottom_layout = QHBoxLayout(self.bottom_frame)
        self.bottom_layout.setContentsMargins(0,0,0,0)

        # DONE BUTTON
        self.btn_1 = MyPushButton(
            btn1_text, 
            maximum_width=btn1_width, 
            set_disabled=disable_btn1,
            hide=hide_btn1
        )
        # CLEAR BUTTON
        self.btn_2 = MyPushButton(
            btn2_text, 
            maximum_width=btn2_width, 
            set_disabled=disable_btn2,
            hide=hide_btn2
        )

        # SPACER FRAME
        self.spacer_frame = QFrame()
        
        # SPACER LAYOUT
        self.spacer_layout = QHBoxLayout(self.spacer_frame)
        self.spacer_layout.addSpacerItem(self.spacer)

        # ADD BTNS TO LAYOUT
        self.bottom_layout.addWidget(self.btn_1, 10)
        self.bottom_layout.addWidget(self.btn_2, 10)
        self.bottom_layout.addWidget(self.spacer_frame)

        # TEXT BOX LAYOUT
        self.text_box_layout = QVBoxLayout(self)
        self.text_box_layout.setContentsMargins(9,9,9,9)
        self.text_box_layout.setSpacing(9)
        self.text_box_layout.addWidget(self.top_frame)
        self.text_box_layout.addWidget(self.central_frame)
        self.text_box_layout.addWidget(self.central_frame2)
        self.text_box_layout.addWidget(self.bottom_frame)

    def add_text_box(self, text_box: Type[TextBox]) -> None:
        self.central_layout.addWidget(text_box)

    def add_sub_text_box(self, text_box: Type[TextBox]) -> None:
        self.central_layout2.addWidget(text_box)

    def add_button(self, button: Type[MyPushButton]) -> None:
        self.bottom_layout.addWidget(button, 10)