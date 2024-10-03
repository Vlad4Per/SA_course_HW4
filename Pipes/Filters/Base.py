import multiprocessing as mp


# base class for all filters
class Filter(mp.Process):
    def __init__(self, in_pipe, out_pipe):
        super().__init__()
        self.in_pipe = in_pipe
        self.out_pipe = out_pipe


    def run(self):
        # receiving and sending each frame to next pipe
        while True:
            frame = self.in_pipe.recv()

            if frame is None:
                self.out_pipe.send(None)
                break

            new_frame = self.process(frame)
            self.out_pipe.send(new_frame)


    def process(self, frame):
        return frame