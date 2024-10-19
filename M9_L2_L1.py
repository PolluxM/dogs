#Делаем запрос к картинкам собак на dog.ceo по средствам JSON

from tkinter import *
import requests
from io import BytesIO

from image.utils import image_url


def show_image():
    inage_url = get_dog_image()
    if inage_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img.thumbnail((300, 300))
            label.config(image=img)
            label.image = img
        except Exception as e:
            mb.showerror()



window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = Label()
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)