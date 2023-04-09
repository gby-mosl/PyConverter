from pathlib import Path

from PIL import Image


class CustomImage:
    def __init__(self, path, folder="reduced"):
        self.image = Image.open(path)
        self.width, self.height = self.image.size
        self.path = Path(path)
        self.reduced_dir = self.path.parent / folder
        self.reduced_path = self.reduced_dir / self.path.name

    def reduce_image(self, size=0.5, quality=75):
        new_width = round(self.width * size)
        new_height = round(self.height * size)
        self.image = self.image.resize((new_width, new_height), Image.LANCZOS)
        self.reduced_dir.mkdir(exist_ok=True)
        self.image.save(self.reduced_path, 'JPEG', quality=quality)
        return self.reduced_path.exists()


if __name__ == '__main__':
    i = CustomImage("/Users/guillaume/Pictures/UDEMY/karsten-winegeart-fd1cQ3mmBTE-unsplash.jpg")
    i.reduce_image(size=1, quality=50)
    print(i.reduce_image())