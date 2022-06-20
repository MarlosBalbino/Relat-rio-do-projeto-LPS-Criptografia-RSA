from .my_slider import MySlider
from qt_core import QMouseEvent


class MyJumperSlider(MySlider):
    
    def __init__(self):
        super(MyJumperSlider, self).__init__()    

        self.steps = 0
        self.button_pressed = False

    def set_steps(self, steps: int):
        self.steps = steps
        self.multiples = [round(i*self.maximum()/steps) for i in range(0, steps + 1)]

    def get_steps(self):
        return self.steps

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.button_pressed = True
            
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.button_pressed:
            pos_x = round(event.pos().x() / (self.width()/self.maximum()))
            try:
                if pos_x in self.multiples:
                    self.setValue(pos_x)
            except:
                pass
      
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.button_pressed = False