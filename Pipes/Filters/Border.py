import cv2
from Filters.Base import Filter


# filter for adding borders
class Border(Filter):
    def __init__(self, in_pipe, out_pipe, color=(0, 255, 0), thickness=5):
        super().__init__(in_pipe, out_pipe)
        self.color = color
        self.thickness = thickness


    def process(self, frame):
        return cv2.copyMakeBorder(frame, self.thickness, self.thickness, self.thickness, self.thickness, cv2.BORDER_CONSTANT, value=self.color)
