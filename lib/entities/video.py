import cv2
import time
import os

class Video: 

    def __init__(self, path, drawer):
        self.video = cv2.VideoCapture(path)
        self.drawer = drawer
        try:
            self.size = os.get_terminal_size().columns
        except:
            self.size = 120
        self.fps = int(self.video.get(cv2.CAP_PROP_FPS))


    def __render_frame(self, image):
        frame = self.drawer(image, self.size)
        return frame.render()

    def play(self):
        if(self.video.isOpened() == False):
            raise Exception("Video is not opened")
        while(self.video.isOpened()):
            ret, frame = self.video.read()
            if ret:
                yield self.__render_frame(frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
            time.sleep(1 / self.fps)
        self.video.release()
        cv2.destroyAllWindows()