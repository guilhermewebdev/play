from video import Video

def test_video():
    class TestRender:
        counter = 0
        
        def __init__(self, image, size):
            self.image = image
            self.size = size

        def render(self):
            TestRender.counter += 1

    video = Video("fake/frame.png", 120, TestRender)
    assert video.play()
    assert TestRender.counter == 1