from video import Video

def test_video():
    class TestRender:
        counter = 0
        
        def __init__(self, image):
            self.image = image

        def render(self):
            TestRender.counter += 1

    video = Video("fake/frame.png", TestRender)
    assert video.play()
    assert TestRender.counter == 1