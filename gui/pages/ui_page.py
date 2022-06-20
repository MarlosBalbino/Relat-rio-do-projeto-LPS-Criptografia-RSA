from abc import ABC, abstractmethod
from ctypes import alignment
from decimal import DivisionByZero
from gui.widgets.my_widgets.exception import CustomValueError
from qt_core import *
from gui.widgets.my_widgets import TextBoxWindow, ExpandAnimation, TextBox, FieldEmptyError, MyScrollArea, MyScrollBar


class UI_ApplicationPage(ABC):
        
    def __init__(
        self, 
        application_pages, 
        warning_label: QLabel,
        warning_msg_1,
        warning_msg_2,
        warning_msg_3,
        label_text_1,
        label_tittle,
        tittle_color,
        label_text_2,
        keys_label_text,
        unique_key_label,
        key_label_1,
        key_label_2
        ):

        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")

        self.warning_label = warning_label
        self.warning_msg_1 = warning_msg_1
        self.warning_msg_2 = warning_msg_2 
        self.warning_msg_3 = warning_msg_3

         # PAGE 2 CONTENT
        self.page = QWidget()

        # PAGE LAYOUT
        self.page_layout = QVBoxLayout(self.page)
        self.page_layout.setContentsMargins(0,0,0,0)

        # SCROLL AREA
        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet("border: none")
        self.scroll_area.setWidgetResizable(True)

        # CREATE CUSTOM SCROLL BAR
        self.vertical_scroll_bar = MyScrollBar(btn_height=0)
        self.horizontal_scroll_bar = MyScrollBar(btn_height=0)

        # SET CUSTOM SCROLL BAR
        self.scroll_area.setVerticalScrollBar(self.vertical_scroll_bar)
        self.scroll_area.setHorizontalScrollBar(self.horizontal_scroll_bar)

        # ADD SCROLL AREA TO PAGE LAYOUT
        self.page_layout.addWidget(self.scroll_area)

        # CONTENTS AREA
        self.contents_area = QWidget()
        self.contents_area_layout = QVBoxLayout(self.contents_area)
        self.contents_area_layout.setContentsMargins(0,0,0,0)

        self.contents_frame = QFrame()
        # self.contents_frame.setStyleSheet("background-color: blue")
        self.contents_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.main_layout = QGridLayout(self.contents_frame)
        self.main_layout.setSpacing(50)

        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: red")
        self.central_frame.setMaximumWidth(500)
        self.central_frame.setMaximumHeight(510)   
        
        self.central_layout = QVBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.central_layout.setSpacing(10)

        self.text_box_window_1 = TextBoxWindow(
            parent=self.page, 
            label_text=label_text_1,
            label_tittle=label_tittle, 
            tittle_color=tittle_color,
            btn1_text="Feito", 
            btn2_text="Limpar",
        )

        self.text_box_1 = TextBox()
        self.text_box_window_1.add_text_box(self.text_box_1)
        
        self.text_box_window_2 = TextBoxWindow(
            parent=self.page, 
            label_text=label_text_2, 
            btn1_text="Salvar",
            btn2_text="Salvar como",
            disable_btn2=False,
            window_resize=QSize(500, 96)
        )

        self.text_box_2 = TextBox()
        self.text_box_window_2.add_text_box(self.text_box_2)  

        self.central_layout.addWidget(self.text_box_window_1, 0, Qt.AlignTop)
        self.central_layout.addWidget(self.text_box_window_2, 0, Qt.AlignTop)

        self.keys_window = TextBoxWindow(
            label_text=keys_label_text,
            disable_btn1=True,
            disable_btns=True,
            window_resize=QSize(500, 180)
        )

        self.key_box_1 = TextBox(scroll_mim_height=15)
        self.key_box_1.setPlaceholderText(key_label_1)
        self.key_box_2 = TextBox(scroll_mim_height=15)
        self.key_box_2.setPlaceholderText(key_label_2)
        self.unique_keys = TextBox(scroll_mim_height=15)
        self.unique_keys.setPlaceholderText(unique_key_label)
        self.keys_window.add_text_box(self.key_box_1)
        self.keys_window.add_text_box(self.key_box_2)
        self.keys_window.add_sub_text_box(self.unique_keys)

        self.vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.main_layout.addItem(self.vertical_spacer)
        self.main_layout.addWidget(self.keys_window)
        self.main_layout.addWidget(self.central_frame)        
        self.main_layout.addItem(self.vertical_spacer)

        self.contents_area_layout.addWidget(self.contents_frame)        
        self.scroll_area.setWidget(self.contents_area)  
        application_pages.addWidget(self.page)
        
        # CREATING FRAME ANIMATIONS EXPAND/RETRACT
        self.text_box_animation = ExpandAnimation(
            self.text_box_window_2,
            start_width = 96,
            end_width = 250,
            animation_type = b"minimumHeight"
        )        

        # CLICK EVENTS
        # Get text from text box
        self.text_box_window_1.btn_1.clicked.connect(self.done_handle)
        self.text_box_window_1.btn_2.clicked.connect(self.clear_handle)
        self.text_box_1.textChanged.connect(self.change_handle)

    def change_handle(self):
        self.warning_label.setText("")
        try:
            self.get_text()
            self.text_box_window_1.btn_2.set_disabled(False)
            
        except FieldEmptyError:
            self.text_box_window_1.btn_2.set_disabled(True)

    def done_handle(self):               
        try:
            self.get_text() 
            self.cryptography()
            if self.text_box_window_2.height() == 96:  
                self.text_box_animation.reset()

        except ValueError:
            self.warning_label.setText(self.warning_msg_1)
        except FieldEmptyError:
            self.warning_label.setText(self.warning_msg_2)
        except CustomValueError:
            self.warning_label.setText(self.warning_msg_3)
        except ZeroDivisionError:
            self.warning_label.setText("Insert a 'e' valid key!")

    def clear_handle(self):
        self.text_box_1.clear()
        self.text_box_2.clear()        
        self.text_box_window_1.btn_2.set_disabled(True)
        if self.text_box_window_2.height() != 96:
            self.text_box_animation.reset()

    def get_text(self):
        self.text = self.text_box_1.toPlainText()
        if self.text == "":
            raise FieldEmptyError

    @abstractmethod
    def cryptography(self):
        pass