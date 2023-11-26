from PIL import Image, ImageOps

class Filter:
    def apply_to_pixel(self, pixel: int) -> int:
        raise NotImplementedError()

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        w, h = img.size
        for i in range(w):
            for j in range(h):
                pixel = img.getpixel((i, j))
                pixel = self.apply_to_pixel(pixel)
                img.putpixel((i, j), pixel)
        return img


class RedFilter(Filter):
    def __init__(self):
        self.name = "Красный фильтр"
        self.meaning = "Плавно усиливает красный оттенок на изображении."
    def apply_to_pixel(self, pixel: int) -> int:
        r, g, b = pixel
        return (255, g, b)


class GreenFilter(Filter):
    def apply_to_pixel(self, pixel: int) -> int:
        r, g, b = pixel
        return (r, 255, b)


class BlueFilter(Filter):
    def apply_to_pixel(self, pixel: int) -> int:
        r, g, b = pixel
        return (r, g, 255)


class InversionFilter(Filter):
    def apply_to_pixel(self, pixel: int) -> int:
        return tuple(255 - value for value in pixel)

class ContrastFilter(Filter):
    def __init__(self, contrast=1.0):
        self.contrast = contrast
    def apply_to_pixel(self, pixel: int) -> int:
        r, g, b = pixel
        new_pixel = (int((r + g + b) / 3), 255, int((r + g + b) / 3))
        return new_pixel