import cv2
import time
import os
import sys

class Video: 

    def __init__(self, path, drawer):
        self.video = cv2.VideoCapture(path)
        self.drawer = drawer
        self.fps = int(self.video.get(cv2.CAP_PROP_FPS))
        self.running = True
        self.stop_tries = 0

    def __get_size(self):
        try:
            return os.get_terminal_size().columns
        except:
            return 120


    def __render_frame(self, image):
        frame = self.drawer(image, self.__get_size())
        return frame.render()
    
    def stop(self):
        if(self.stop_tries == 0):
            self.running = False
            self.stop_tries += 1
        else:
            print("Stopping...")
            sys.exit(0)

    def play(self):
        if(self.video.isOpened() == False and self.running):
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
        if(self.running == False): 
            print("Stopped")
        self.video.release()
        cv2.destroyAllWindows()