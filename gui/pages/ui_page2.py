from .ui_page import UI_ApplicationPage, QLabel
from app.rsa import RSA

class UI_ApplicationPage2(UI_ApplicationPage):

    def __init__(self, application_pages, warning_label: QLabel): 
        
        super().__init__(
            application_pages, 
            warning_label,
            warning_msg_1 = "Warning: insert a valid public key!",
            warning_msg_2 = "Warning: the field is empty!",
            warning_msg_3 = "",
            label_text_1 = "Escreva uma mensagem para",
            label_tittle = "criptografar:",
            tittle_color = "#8fd694",
            label_text_2 = "Mensagem criptografada:",
            keys_label_text = "Inserir chaves públicas:",
            unique_key_label= "Chave pública única:",
            key_label_1 = "n",
            key_label_2 = "e"
        )

    def cryptography(self):
        
        encrypter = RSA()
    
        self.encrypted_str = encrypter.encrypt(
            int(self.key_box_1.toPlainText()),
            int(self.key_box_2.toPlainText()), 
            self.text)
        
        self.text_box_2.clear()
        self.text_box_2.insertPlainText(self.encrypted_str)