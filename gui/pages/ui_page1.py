from ctypes import alignment
from operator import mod
from turtle import pos
from gui.widgets.my_widgets import TextBoxWindow, TextBox, MyPushButton, MyJumperSlider
from qt_core import *

from app.rsa import RSA


class UI_ApplicationPage1(object):


    def __init__(self, application_pages, warning_label: QLabel):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        
        self.warning_label = warning_label

        # PAGE 1 CONTENT
        self.page = QWidget()
        
        self.verticalLayout = QVBoxLayout(self.page)

        self.central_frame = QFrame()
        #self.central_frame.setStyleSheet("background-color: grey")

        self.central_layout = QVBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(72, 0, 72, 0)
        self.central_layout.setSpacing(25)

        #PRIVATE KEYS WINDOW
        # ////////////////////////////////////////////////////////////////////////
        self.private_keys_window = TextBoxWindow(
            label_text="Chaves privadas:",
            btn1_text="Gerar chaves",
            btn1_width=120,
            btn2_text="Limpar",
            window_resize=None
        )
        self.text_box_1 = TextBox(scroll_mim_height=15)
        self.text_box_1.setPlaceholderText("p")
        self.text_box_2 = TextBox(scroll_mim_height=15)
        self.text_box_2.setPlaceholderText("q")
        self.text_box_3 = TextBox(scroll_mim_height=15)
        self.text_box_3.setPlaceholderText("e")
        self.text_box_6 = TextBox(scroll_mim_height=15, read_only=True)
        self.text_box_6.setPlaceholderText("Chave privada única")

        self.copy_btn_1 = MyPushButton("Copiar", set_disabled=True)
        self.save_btn_1 = MyPushButton("Salvar", set_disabled=True)
        self.save_btn_2 = MyPushButton("Salvar como", set_disabled=True)        

        self.private_keys_window.add_text_box(self.text_box_1)
        self.private_keys_window.add_text_box(self.text_box_2)
        self.private_keys_window.add_text_box(self.text_box_3)
        self.private_keys_window.add_sub_text_box(self.text_box_6)
        self.private_keys_window.add_button(self.copy_btn_1)
        self.private_keys_window.add_button(self.save_btn_1)
        self.private_keys_window.add_button(self.save_btn_2)        
        self.private_keys_window.setMaximumHeight(250)

        #PUBLIC KEYS WINDOW
        # ////////////////////////////////////////////////////////////////////////
        self.public_keys_window = TextBoxWindow(
            label_text="Chaves públicas:",
            btn1_text="Limpar",
            disable_btn1=True,
            hide_btn2=True,
            btn1_width=72,
            window_resize=False
        )
        self.text_box_4 = TextBox(text_box_color="#44475a", read_only=True, scroll_mim_height=15)
        self.text_box_4.setPlaceholderText("n")
        self.text_box_5 = TextBox(text_box_color="#44475a", read_only=True, scroll_mim_height=15)
        self.text_box_5.setPlaceholderText("e")
        self.text_box_7 = TextBox(text_box_color="#44475a", read_only=True, scroll_mim_height=15)
        self.text_box_7.setPlaceholderText("Chave pública única")
        self.copy_btn_2 = MyPushButton("Copiar", set_disabled=True)
        self.save_btn_3 = MyPushButton("Salvar", set_disabled=True)
        self.save_btn_4 = MyPushButton("Salvar como", set_disabled=True)        

        self.public_keys_window.add_text_box(self.text_box_4)
        self.public_keys_window.add_text_box(self.text_box_5)
        self.public_keys_window.add_sub_text_box(self.text_box_7)
        self.public_keys_window.add_button(self.copy_btn_2)
        self.public_keys_window.add_button(self.save_btn_3)
        self.public_keys_window.add_button(self.save_btn_4)        
        self.public_keys_window.setMaximumHeight(250)

        # SPACERS
        self.vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.horizontal_spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Preferred)

        # JUMPING SLIDER
        self.slider_frame = QFrame()        
        self.slider_layout = QVBoxLayout(self.slider_frame)
        self.label_layout = QHBoxLayout()

        # SLIDER LABEL TEXT
        self.security_level_label = QLabel()
        self.security_level_label.setText("Nível de segurança:")
        self.security_level_label.setStyleSheet("font: 700 12pt Segoe UI; color: rgb(255, 255, 255)")

        self.status_label = QLabel()
        self.status_label.setText("Mais seguro")
        self.status_label.setStyleSheet("font: italic 700 12pt Segoe UI; color: green")

        self.slider = MyJumperSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setValue(200)
        self.slider.setMaximumWidth(200)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setSingleStep(34)
        self.slider.set_steps(3)
        self.slider.valueChanged.connect(self.set_security_level)

        self.label_layout.addWidget(self.security_level_label)
        self.label_layout.addWidget(self.status_label)
        self.label_layout.addSpacerItem(self.horizontal_spacer)
        
        self.slider_layout.addLayout(self.label_layout)
        self.slider_layout.addWidget(self.slider)
        self.slider_layout.addSpacerItem(self.vertical_spacer) 

        self.central_layout.addSpacerItem(self.vertical_spacer)
        self.central_layout.addWidget(self.private_keys_window)
        self.central_layout.addWidget(self.public_keys_window)
        self.central_layout.addWidget(self.slider_frame)
        self.central_layout.addSpacerItem(self.vertical_spacer)

        self.verticalLayout.addWidget(self.central_frame)
        
        application_pages.addWidget(self.page)

        # CLICK EVENTS
        self.private_keys_window.btn_1.clicked.connect(self.generate_keys)
        self.private_keys_window.btn_2.clicked.connect(self.private_clear_handle)
        self.public_keys_window.btn_1.clicked.connect(self.public_clear_handle)

        self.text_box_1.textChanged.connect(self.private_change_handle)
        self.text_box_2.textChanged.connect(self.private_change_handle)
        self.text_box_3.textChanged.connect(self.private_change_handle)
        self.text_box_4.textChanged.connect(self.public_change_handle)

        self.text_box_1.selectionChanged.connect(self.private_selection_handle)
        self.text_box_2.selectionChanged.connect(self.private_selection_handle)
        self.text_box_3.selectionChanged.connect(self.private_selection_handle)
        self.text_box_4.selectionChanged.connect(self.public_selection_handle)
        self.text_box_5.selectionChanged.connect(self.public_selection_handle)

        # DEFAULT SECURITY LEVEL
        self.level = 3

    def set_security_level(self):
        first_step = self.slider.maximum() / self.slider.get_steps()

        level = [0, 1, 2, 3]
        status = ["Menos seguro", "Equlibrado", "Seguro", "Mais seguro"]
        color = ["red", "orange", "yellow", "green"]

        slider_pos = round(self.slider.value() / first_step)

        self.level = level[slider_pos]
        self.status = status[slider_pos]
        self.color = color[slider_pos]

        self.status_label.setText(self.status)
        self.status_label.setStyleSheet(f"font: italic 700 12pt Segoe UI; color: {self.color}")

    def generate_keys(self):

        rsa = RSA()
        try:
            rsa.generateKeys(self.level)
        except AttributeError:
            self.set_security_level()
            self.generate_keys()

        p = int(rsa.get_key_P())
        q = int(rsa.get_key_Q())
        e = int(rsa.get_key_E())
        n = int(rsa.get_key_N())
        d = int(rsa.get_key_D())

        if (d*e) % ((p-1) * (q-1)) == 1:
            print("d é inverso")
        else:
            print("d não é inverso")

        # PRIVATE KEYS
        self.text_box_1.setPlainText(rsa.get_key_P())
        self.text_box_2.setPlainText(rsa.get_key_Q())
        self.text_box_3.setPlainText(rsa.get_key_E())
        self.text_box_6.setPlainText(rsa.get_private_key())

        # PUBLIC KEYS
        self.text_box_4.setPlainText(rsa.get_key_N())
        self.text_box_5.setPlainText(rsa.get_key_E())
        self.text_box_7.setPlainText(rsa.get_public_key())

    def private_change_handle(self):
        self.warning_label.setText("")        
        for text_box in self.private_keys_window.central_frame.findChildren(TextBox):

            if text_box.toPlainText() != "":
                self.show_private_btns()
                break     
            else:
                self.hide_private_btns()
        
    def show_private_btns(self):
        self.private_keys_window.btn_2.set_disabled(False)
        self.save_btn_1.set_disabled(False)
        self.save_btn_2.set_disabled(False)
    
    def hide_private_btns(self):
        self.private_keys_window.btn_2.set_disabled(True)
        self.save_btn_1.set_disabled(True)
        self.save_btn_2.set_disabled(True)
        self.copy_btn_1.set_disabled(True)

    def private_clear_handle(self):
        self.text_box_1.clear()
        self.text_box_2.clear()
        self.text_box_3.clear()
        self.text_box_6.clear()     
        self.hide_private_btns()

    def private_selection_handle(self):
        for text_box in self.private_keys_window.central_frame.findChildren(TextBox):
            if text_box.textCursor().hasSelection():
                self.copy_btn_1.set_disabled(False)
                break
            else:
                self.copy_btn_1.set_disabled(True)

            # c = text_box.textCursor()
            # c.clearSelection()
            # text_box.setTextCursor(c)

    def public_change_handle(self):
        self.warning_label.setText("")
        for text_box in self.private_keys_window.central_frame.findChildren(TextBox):
            if text_box.toPlainText() != "":
                self.show_public_btns()
                break                
            else:
                self.hide_public_btns()

    def show_public_btns(self):
        self.public_keys_window.btn_1.set_disabled(False)
        self.save_btn_3.set_disabled(False)  
        self.save_btn_4.set_disabled(False)

    def hide_public_btns(self):
        self.public_keys_window.btn_1.set_disabled(True)
        self.save_btn_3.set_disabled(True)   
        self.save_btn_4.set_disabled(True)
        self.copy_btn_2.set_disabled(True)
    
    def public_clear_handle(self):
        self.text_box_4.clear()
        self.text_box_5.clear()
        self.text_box_7.clear()
        self.hide_public_btns()

    def public_selection_handle(self):
        for text_box in self.public_keys_window.central_frame.findChildren(TextBox):
            if text_box.textCursor().hasSelection():
                self.copy_btn_2.set_disabled(False)
                break
            else:
                self.copy_btn_2.set_disabled(True)

    def get_text(self):
        self.key_p = self.text_box_1.toPlainText()
        self.key_q = self.text_box_2.toPlainText()
        self.key_d = self.text_box_3.toPlainText()
        # self.key_e = self.text_box_4.toPlainText()
        # self.key_n = self.text_box_5.toPlainText()
