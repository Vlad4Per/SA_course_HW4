import cv2, multiprocessing as mp
from Filters.BnW import BnW
from Filters.Border import Border
from Filters.Mirror import Mirror
from Filters.Resize import Resize


# global variables
FLIP_CODE = 1
THICKNESS = 25
WIDTH = 1440
HEIGHT = 480



def main():
    # video source opening
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open video source.")
        exit(0)

    # creating pipes
    pipe1 = mp.Pipe(duplex=False)
    pipe2 = mp.Pipe(duplex=False)
    pipe3 = mp.Pipe(duplex=False)
    pipe4 = mp.Pipe(duplex=False)
    pipe5 = mp.Pipe(duplex=False)

    # applying filters on pipes
    bnm_filter = BnW(pipe1[0], pipe2[1])
    mirror_filter = Mirror(pipe2[0], pipe3[1], FLIP_CODE)
    resize_filter = Resize(pipe3[0], pipe4[1], WIDTH, HEIGHT)
    border_filter = Border(pipe4[0], pipe5[1], THICKNESS)

    bnm_filter.start()
    mirror_filter.start()
    resize_filter.start()
    border_filter.start()

    try:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Error: Cannot read frame.")
                break

            # applying filters on current frame
            pipe1[1].send(frame)
            new_frame = pipe5[0].recv()

            # showing video with applied pipes and without
            cv2.imshow("Input", frame)
            cv2.imshow("Output", new_frame)

            # stopping criteria
            if not cv2.waitKey(1):
                break

        # stopping every process
        cap.release()
        cv2.destroyAllWindows()
        pipe1[1].send(None)
        bnm_filter.join()
        mirror_filter.join()
        resize_filter.join()
        border_filter.join()

    # stopping criteria
    except KeyboardInterrupt:
        try:
            cap.release()
            cv2.destroyAllWindows()
            pipe1[1].send(None)
            bnm_filter.join()
            mirror_filter.join()
            resize_filter.join()
            border_filter.join()
        except Exception:
            return


if __name__ == "__main__":
    main()
