from lib.entities.video import Video

def test_video():
    class TestRender:
        counter = 0
        
        def __init__(self, image, size):
            self.image = image
            self.size = size

        def render(self):
            TestRender.counter += 1
            return f"{TestRender.counter}"

    video = Video("fake/frame.png", TestRender)
    counter_2 = 0
    for frame in video.play():
        if(frame): counter_2 += 1
    assert counter_2 == 1
    assert TestRender.counter == 1