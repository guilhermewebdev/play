from pathlib import Path

from lib.entities.frame import Frame
from lib.entities.video import Video
from os import system, name

class VideoController:

    def __clear(self):
        if name == 'nt':
            system('cls')
        else:
            system('clear')

    def __start(self, video_path):
        video = Video(video_path, Frame)
        for frame in video.play():
            self.__clear()
            print(frame, end='')

    def play(self, path):
        video = Path(path)
        if video.is_file() == False:
            raise FileNotFoundError(f"{path} is not a file")
        self.__start(video.as_posix())