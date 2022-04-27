import PySimpleGUI as sg
import os
import io
from PIL import Image, ImageTk

#画像データの作成
def get_img_data(f, maxsize=(600, 600), first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)

#画像の表示
def show_image(image_elem):
    sg.theme('SystemDefault')
    layout = [
    [image_elem]
    ]

    win = sg.Window('画像', layout=layout, 
        no_titlebar=True, 
        transparent_color='#aaaaaa', 
        grab_anywhere = True,
        background_color='#aaaaaa',
        resizable=True,
        keep_on_top=True,
        right_click_menu=['Unused', ['Next', 'Back', 'Random', 'Exit']])
    return win