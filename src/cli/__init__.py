import sys

from controllers.video import VideoController


def play():
    controller = VideoController()
    for path in sys.argv[1:]:
        controller.play(path)