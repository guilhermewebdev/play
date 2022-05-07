import cv2
from src.entities.frame import Frame


def render_frame(image):
    frame = Frame(image, 120)
    rendered = frame.generate_image()
    assert isinstance(rendered, str)

def test_frame():
    video = cv2.VideoCapture("fake/frame.png")
    assert video.isOpened()
    while(video.isOpened()):
        ret, frame = video.read()
        if ret == True:
            render_frame(frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()
