#Делаем запрос к картинкам собак на dog.ceo по средствам JSON

from tkinter import *
import requests
from PIL import Image, ImageTK
from io import BytesIO

window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = Label()
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)