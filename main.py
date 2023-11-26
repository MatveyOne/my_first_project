from PIL import Image
from filters import *
import os





def open_image(image_path):
    return Image.open(image_path).convert("RGB")


def apply_filter(image, filter_choice):
    filters = {
        1: RedFilter,
        2: GreenFilter,
        3: BlueFilter,
        4: InversionFilter,
        5: ContrastFilter,
        6: MultiFilter,
    }

    if filter_choice in filters:
        selected_filter = filters[filter_choice]()
        filtered_image = selected_filter.apply_to_image(image)  #
        return filtered_image
    else:
        return image


def save_image(image, save_path):
    image.save(save_path)
    print("Изображение успешно сохранено!")


def main():
    print("Добро пожаловать в консольный фоторедактор.")

    while True:
        path = input("Введите путь к файлу: ")
        while not os.path.exists(path):
            path = input("Файл не найден. Попробуйте еще раз: ")
        image_path = path
        image = open_image(image_path)

        print("Меню фильтров:")
        print("1: Красный фильтр")
        print("2: Зелёный фильтр")
        print("3: Синий фильтр")
        print("4: Инверсия")
        print("5: Увеличения контрастности")
        print('6: МультиФильтр')
        print("0: Выход")

        filter_choice = input("Выберите фильтр (или 0 для выхода): ")
        while not (filter_choice.isdigit() and 0 <= int(filter_choice) <= 6):
            print("Некорректный ввод!")
            filter_choice = input("Выберите фильтр (или 0 для выхода): ")
        filter_choice = int(filter_choice)

        if filter_choice == 0:
            print("До свидания!")
            break

        filtered_image = apply_filter(image, filter_choice)

        print("Применить фильтр к картинке? (Да/Нет): ")
        answer = input().lower()
        while not (answer == "да" or answer == "нет"):
            print("Некорректный ввод!")
            print("Применить фильтр к картинке? (Да/Нет): ")
            answer = input().lower()

        if answer == "да":
            save_path = input("Куда сохранить: ")
            Filter.saving(save_path)
            save_image(filtered_image, save_path)

        answer_next = input("Ещё раз? (Да/Нет): ").lower()
        while not (answer_next == "да" or answer_next == "нет"):
            print("Некорректный ввод!")
            answer_next = input("Ещё раз? (Да/Нет): ").lower()

        if answer_next == "нет":
            print("До свидания!")
            break


if __name__ == "__main__":
    main()