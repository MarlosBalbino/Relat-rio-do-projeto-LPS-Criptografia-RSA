from qt_core import QScrollArea, QWheelEvent, QPropertyAnimation


class MyScrollArea(QScrollArea):

    def __init__(
        self,
        anim_duration=100,
        end_step=200
        ):

        super().__init__()
        self.verticalScrollBar().setSingleStep(0)
        self.anim_duration = anim_duration
        self.end_step = end_step

    def wheelEvent(self, event: QWheelEvent) -> None:

        self.animation = QPropertyAnimation(self.verticalScrollBar(), b"value")
        self.animation.setDuration(self.anim_duration)
        self.animation.setStartValue(self.verticalScrollBar().value())

        if event.angleDelta().y() == -120:
            
            print("baixo")
            self.animation.setEndValue(self.verticalScrollBar().value() + self.end_step)

        else:
            print("cima")
            self.animation.setEndValue(self.verticalScrollBar().value() - self.end_step)
        
        self.animation.start()