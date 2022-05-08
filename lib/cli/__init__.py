import sys

from lib.controllers.video import VideoController


def play():
    try:
        controller = VideoController()
        for path in sys.argv[1:]:
            controller.play(path)
    except:
        pass