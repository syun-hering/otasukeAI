import PySimpleGUI as sg
import os
from PIL import Image, ImageTk
import io
import numpy as np
import time
from func import image_func as imf
import subprocess


def main():
    files = os.listdir('./image/')
    file_len = len(files)
    num = 0;
    filename = './image/' + files[num]
    image_elem = sg.Image(data=imf.get_img_data(filename, first=True), background_color='#aaaaaa', 
    enable_events=False,key='illust')
    window = imf.show_image(image_elem)
    print(type(window))
    request_msg = "次へ"
    subprocess.run("D:/Software/assistantseika20220410u/SeikaSay2/SeikaSay2.exe -cid 2001 -t \"{msg}\"".format(msg=request_msg))
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
            image_elem.update(data=imf.get_img_data(filename, first=False))
            
            request_msg = "次へ"
            subprocess.run("D:/Software/assistantseika20220410u/SeikaSay2/SeikaSay2.exe -cid 2001 -t \"{msg}\"".format(msg=request_msg))
        if event == 'Back':
            print("Press Back")
            num-=1
            if num < 0:
                num = file_len-1
            filename = './image/' + files[num]
            image_elem.update(data=imf.get_img_data(filename, first=True))
            request_msg = "前へ"
            subprocess.run("D:/Software/assistantseika20220410u/SeikaSay2/SeikaSay2.exe -cid 2001 -t \"{msg}\"".format(msg=request_msg))
        if event == 'Random':
            num = np.random.randint(low=0, high=file_len-1)
            filename = './image/' + files[num]
            image_elem.update(data=imf.get_img_data(filename, first=True))
            request_msg = "ランダムに"
            subprocess.run("D:/Software/assistantseika20220410u/SeikaSay2/SeikaSay2.exe -cid 2001 -t \"{msg}\"".format(msg=request_msg))
        
    window.close()

if __name__ == "__main__":
    main()