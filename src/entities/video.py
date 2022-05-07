from pathlib import Path
import cv2

class Video: 

    def __init__(self, path, drawer):
        self.video = cv2.VideoCapture(path)
        self.drawer = drawer

    def __render_frame(self, image):
        frame = self.drawer(image)
        frame.render()

    def play(self):
        if(self.video.isOpened() == False):
            raise Exception("Video is not opened")
        while(self.video.isOpened()):
            ret, frame = self.video.read()
            if ret == True:
                self.__render_frame(frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        self.video.release()
        cv2.destroyAllWindows()
        return True