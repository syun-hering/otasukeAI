import PySimpleGUI as sg
import os
from PIL import Image, ImageTk
import io
import numpy as np
import time

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
        no_titlebar=False, 
        transparent_color='#aaaaaa', grab_anywhere = True,
        background_color='#aaaaaa',
        resizable=True,
        keep_on_top=True,
        right_click_menu=['Unused', ['Next', 'Back', 'Random', 'Exit']])
    return win

def main():
    files = os.listdir('./image/')
    file_len = len(files)
    num = 0;
    filename = './image/' + files[num]
    image_elem = sg.Image(data=get_img_data(filename, first=True), background_color='#aaaaaa', 
    enable_events=False,key='illust')
    window = show_image(image_elem)
    print(type(window))
    # イベントループ
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        if event == 'Exit':
            break
        if event == 'Next':
            num+=1
            if num >= file_len:
                num = 0

            filename = './image/' + files[num]
            image_elem.update(data=get_img_data(filename, first=False))
        if event == 'Back':
            print("Press Back")
            num-=1
            if num < 0:
                num = file_len-1
            filename = './image/' + files[num]
            image_elem.update(data=get_img_data(filename, first=True))
        if event == 'Random':
            num = np.random.randint(low=0, high=file_len-1)
            filename = './image/' + files[num]
            image_elem.update(data=get_img_data(filename, first=True))
        
    window.close()

if __name__ == "__main__":
    main()