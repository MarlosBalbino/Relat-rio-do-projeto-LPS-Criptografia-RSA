from string import hexdigits
from turtle import color, width
from gui.widgets.my_widgets import HiddenMenu
from qt_core import *
from threading import Thread
import math
import time

class RSA_HiddenMenu(HiddenMenu):

    def __init__(self, parent: QFrame):
        super().__init__(parent)

        self.central_widget = QWidget()

        
        area = AreaOne(self.central_widget, 0)
        btn = QPushButton(self.central_widget)
        btn.move(0, 300)   
       
        self.set_central_widget(self.central_widget)

class AreaOne(QFrame):

    def __init__(self, teste: QWidget, n):
        super().__init__(teste)
        
        self._size = 200
        self._width = self._size
        self._height = self._size        
        self.setStyleSheet("background-color: #707070")
        self.setFixedSize(QSize(self._width, self._height))

        x = 0
        y = 0

        def g(n):
            return ((((-1)**n)*1) + 1) / (2*(2**(n/2)))
        
        width = self._width
        height = self._height

        for n in range(1, 20):

            area = QFrame(self)            
            area.setStyleSheet(f"background-color: #504b43")
            layout = QHBoxLayout(area)            
            layout.setContentsMargins(1,1,1,1)
            fill = QFrame()
            fill.setStyleSheet("background-color: #7dba84")
            layout.addWidget(fill)
            
            y = math.ceil(g(n) * self._size)
            if n % 2 == 0:
                x += y

            # print(f"{n} - coord: {(x, y)}")

            if n % 2 != 0:
                width /= 2
            else:
                height /= 2
            
            area.setGeometry(x, y, width, height)
           

class Buraco:

    def __init__(self, teste: QWidget):

        colors = ["#8fd694", "#7dba84", "#77ad78", "#6f8f72", "#504b43"]

        j = 81
        for i in range(6):

            if i == 0:
                layout = QVBoxLayout(teste)
                layout.setContentsMargins(0,0,0,0)

            else:
                frame = QFrame()
                frame.setStyleSheet(f"background-color: {colors[i-1]}")
                layout.addWidget(frame)
                layout = QVBoxLayout(frame)
                layout.setContentsMargins(j,j,j,j)
                j /= 2