from qt_core import QPropertyAnimation, QGraphicsOpacityEffect, QFrame, QEasingCurve

class OpacityEffectAnimation(QPropertyAnimation):

    def __init__(self, effect: QGraphicsOpacityEffect, frame: QFrame):
        super().__init__(effect, b"opacity")

        self.setEasingCurve(QEasingCurve.InOutCubic)
        self.setDuration(250)

        self.effect = effect
        self.frame = frame

    def reset(self):
        # Current frame width
        frame_width = self.frame.width()

        # Check width
        if frame_width == 400:
            self.setStartValue(1.00)
            self.setEndValue(0)
            self.start()
        else:
            self.effect.setOpacity(1.00)