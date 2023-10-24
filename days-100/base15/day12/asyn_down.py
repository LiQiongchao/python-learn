"""
同步下载

@Author: QiongchaoLi
@Date: 2020/8/2 10:41
"""
import time
import tkinter
import tkinter.messagebox
from threading import Thread


def download():
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成')


def show_about():
    tkinter.messagebox.showinfo('关于', '关于人的一生')


def main():
    tk = tkinter.Tk()
    tk.title('单线程')
    tk.geometry('200x150')
    tk.wm_attributes('-topmost', True)

    panel = tkinter.Frame(tk)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


if __name__ == '__main__':
    main()
