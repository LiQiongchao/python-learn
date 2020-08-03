"""
如果使用多线程将耗时间的任务放到一个独立的线程中执行，这样就不会因为执行耗时间的任务而阻塞了主线程
在下载的同时，可以使用“关于”

@Author: QiongchaoLi
@Date: 2020/8/2 10:41
"""
import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():
    class DownloadTaskHandler(Thread):

        def run(self) -> None:
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '关于人的一生')

    tk = tkinter.Tk()
    tk.title('单线程')
    tk.geometry('200x150')
    tk.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(tk)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


if __name__ == '__main__':
    main()
