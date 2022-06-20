from .ui_page import UI_ApplicationPage, QLabel
from app.rsa import RSA
from gui.widgets.my_widgets.exception import FieldEmptyError
from gui.widgets.my_widgets.my_text_box import TextBox

class UI_ApplicationPage3(UI_ApplicationPage):

    def __init__(self, application_pages, warning_label: QLabel): 
        
        super().__init__(
            application_pages, 
            warning_label,
            warning_msg_1 = "Warning: insira uma chave válida!",
            warning_msg_2 = "Warning: o campo está vazio!",
            warning_msg_3 = "Warning: insira uma mensagem válida!",
            label_text_1 = "Escreva uma mensagem para",
            label_tittle = "descriptografar:",
            tittle_color = "#be2444",
            label_text_2 = "Mensagem descriptografada:",
            keys_label_text = "Inserir chaves privadas:",
            unique_key_label= "Chave privada única:",
            key_label_1 = "p",
            key_label_2 = "q"
        )

        self.key_box_3 = TextBox(scroll_mim_height=15)
        self.key_box_3.setPlaceholderText("e")
        self.keys_window.add_text_box(self.key_box_3)

    def cryptography(self):

        decrypter = RSA()

        self.decrypted_str = decrypter.decrypt(
            int(self.key_box_1.toPlainText()), 
            int(self.key_box_2.toPlainText()), 
            int(self.key_box_3.toPlainText()), 
            self.text)

        print(self.decrypted_str)
        self.text_box_2.clear()
        self.text_box_2.insertPlainText(self.decrypted_str)
