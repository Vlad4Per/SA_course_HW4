import cv2
from Filters.Base import Filter


# filter for applying mirroring effect
class Mirror(Filter):
    def __init__(self, in_pipe, out_pipe, flip_code=1):
        super().__init__(in_pipe, out_pipe)
        self.flip_code = flip_code


    def process(self, frame):
        return cv2.flip(frame, self.flip_code)