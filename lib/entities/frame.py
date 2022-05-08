from PIL import Image

class Frame:
    chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", ".", " "]
    
    def __init__(self, frame, size):
        self.frame = frame
        image = Image.fromarray(frame)
        width, height = image.size
        aspect_ratio = height/width
        self.size = size
        new_height = aspect_ratio * self.size * 0.55
        self.image = image.resize((self.size, int(new_height)))
        self.image = self.image.convert('L')
        self.pixels = self.image.getdata()

    def generate_image(self):
        new_pixels = [self.chars[pixel//23] for pixel in self.pixels]
        new_pixels = ''.join(new_pixels)
        new_pixels_count = len(new_pixels)
        ascii_image = [
            new_pixels[index:index + self.size] for index in range(0, new_pixels_count, self.size)
        ]
        ascii_image = "\n".join(ascii_image)
        return ascii_image

    def render(self):
        rendered = self.generate_image()
        return rendered