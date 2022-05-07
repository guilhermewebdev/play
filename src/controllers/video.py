from pathlib import Path

from entities.frame import Frame
from entities.video import Video
import os

class VideoController:

    def __init__(self, size=120):
        self.size = size

    def __start(self, video_path):
        video = Video(video_path, self.size, Frame)
        for frame in video.play():
            os.system('clear')
            print(frame, end='')

    def play(self, path):
        video = Path(path)
        if video.is_file() == False:
            raise FileNotFoundError(f"{path} is not a file")
        self.__start(video.as_posix())