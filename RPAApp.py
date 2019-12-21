import pyautogui as pgui
import time
import tkinter as tk
import sys
import random
import pyperclip as pp


root = tk.Tk()
root.title("RPAApp")
root.geometry("500x200")


titlename = ("RPA")
label1 = tk.Label(root, text=titlename, font=("Ricty Diminished", 12)).pack()


box1 = tk.Entry()
box1.insert(tk.END,"")
box1.pack()

box2 = tk.Entry()
box2.insert(tk.END,"")
box2.pack()

box3 = tk.Entry()
box3.insert(tk.END,"")
box3.pack()


i = 1
name = 0
first = 0

def windowR ():
    pgui.hotkey('ctrl', 'right')
def windowL ():
    pgui.hotkey('ctrl', 'left')
def exit ():
    global i
    global name
    global first

    if i == 4:
        i = 1
        name = 0
        first = 0
        print(i,name,first)
    else :
        print("end")

def paste1 ():
    pgui.hotkey('command','v')

def Rclick ():
    pgui.click()

def firstskip ():
    global first
    if first == 0:
        return
    else:
        pgui.moveTo(373,141)
        time.sleep(0.1)
        pgui.click()

def textdata ():
    global name
    global i

    if i == 1:
        name = box1.get()
        pp.copy(name)
        i += 1 #ボタンが押されるたびにiの中身が入れ替わるのでファイル名重複を防ぐ
    elif i == 2:
        name = box2.get()
        pp.copy(name)
        i += 1 #ボタンが押されるたびにiの中身が入れ替わるのでファイル名重複を防ぐ
    elif i == 3:
        name = box3.get()
        pp.copy(name)
        i += 1 #ボタンが押されるたびにiの中身が入れ替わるのでファイル名重複を防ぐ

def screenshot():
    global name
    sc = pgui.screenshot(region=(900, 400, 2500, 1500))  #スクリーンショットを撮る
    ssname = str(name) + ".png"   #スクショしたファイルの名前指定の型
    sc.save(ssname)   #上の処理をここに入れている


def btn1():    #ボタンの処理
    windowR()#window右に一回スライド
    
    for y in range(1,4):

        global name
        global i
        global first

        # windowR()#window右に一回スライド
        textdata()
        firstskip()
        time.sleep(0.3)
        pgui.moveTo(243,141)
        pgui.click()#pguiでクリック
        paste1()
        pgui.press('enter')
        time.sleep(2)
        screenshot()
        first = first + 1
        exit()

    windowL()





# for xd in range(i):
#     i.append(xd)

btn = tk.Button(text="スタート", command = btn1) # ボタンを作成btn1を呼び出し
btn.pack()

root.mainloop()

