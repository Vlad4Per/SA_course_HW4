import cv2
from Filters.Base import Filter


# filter for applying resizing
class Resize(Filter):
    def __init__(self, in_pipe, out_pipe, width, height):
        super().__init__(in_pipe, out_pipe)
        self.width = width
        self.height = height

    def process(self, frame):
        return cv2.resize(frame, (self.width, self.height))
