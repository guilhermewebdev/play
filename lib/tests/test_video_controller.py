from lib.controllers.video import VideoController


def test_video():
    controller = VideoController()
    controller.play("fake/frame.png")