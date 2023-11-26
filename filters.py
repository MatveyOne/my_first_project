from PIL import Image, ImageOps, ImageFilter

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
    def saving(img):
        while True:
            try:
                path = input('Введите место сохранения изображения\n').strip().lower()
                img.save(path)
                break
            except:
                print('вы неправильно ввели директорию места сохранения, повторите попытку')
                continue

class RedFilter(Filter):

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


class MultiFilter(Filter):

    def apply_to_image(self, img):
        rows = 2
        cols = 2
        width, height = img.size
        # ширина и длина одной части
        part_width = width // cols
        part_height = height // rows

        parts = []
        filter_array = [ImageFilter.GaussianBlur(100), ImageFilter.FIND_EDGES, ImageFilter.CONTOUR, ImageFilter.SHARPEN]
        # здесь мы делим изображение на части и применяем фильтры к этим частям
        for row in range(rows):
            for col in range(cols):
                left = col * part_width
                top = row * part_height
                right = left + min(part_width + 1, width) # если изображение состоит из нечетного количества пикселей
                bottom = top + min(part_height + 1, height) # если изображение состоит из нечетного количества пикселей

                part = img.crop((left, top, right, bottom))
                part = part.filter(filter_array.pop())
                parts.append(part)

        glued_image = Image.new("RGB", (height, width))
        # тут мы склеиваем отфильтрованные части
        for row in range(rows):
            for col in range(cols):
                part = parts[row * cols + col]
                left = col * min(part_width+1, width) # если изображение состоит из нечетного количества пикселей
                top = row * min(part_height+1, height) # если изображение состоит из нечетного количества пикселей
                glued_image.paste(part, (left, top))
        glued_image.show()
        return glued_image