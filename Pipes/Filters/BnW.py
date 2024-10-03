import cv2
from Filters.Base import Filter


# black and white filter
class BnW(Filter):
    def process(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
