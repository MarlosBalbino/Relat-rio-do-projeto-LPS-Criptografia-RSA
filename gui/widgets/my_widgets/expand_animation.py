from qt_core import QPropertyAnimation, QFrame


class ExpandAnimation(QPropertyAnimation):

    def __init__(
        self, 
        parent: QFrame,
        start_width, 
        end_width, 
        duration=300,
        animation_type=b"minimumWidth"
        ):

        super().__init__(parent, animation_type)

        self.frame = parent
        self.start_width = start_width
        self.end_width = end_width
        self._duration = duration
        self.animation_type = animation_type

    def reset(self):
        # Current frame width
        frame_width = None
        if self.animation_type == b"minimumWidth":
            frame_width = self.frame.width()
        if self.animation_type == b"minimumHeight":
            frame_width = self.frame.height()

        # Check width
        width = self.start_width
        if frame_width == self.start_width:
            width = self.end_width

        # Set animation values
        self.setStartValue(frame_width)
        self.setEndValue(width)
        self.setDuration(self._duration)
        self.start()