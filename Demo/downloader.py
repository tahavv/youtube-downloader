from tkinter import *
from pytube import YouTube


#Main screen
root = Tk()
root.wm_iconbitmap('down.ico')
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Video Downloader")


#labels
Label(root,text='Youtube video converter',font='arial 20 bold').pack()
link=StringVar()
Label(root, text='Paste Your link here:',font='arial 15 bold',fg='red').place(x= 160 , y = 60)
link_enter=Entry(root ,width=70, textvariable=link).place(x=50,y=90)

#functions
def DownloaderMp4():
    url =YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    Label(root, text = 'Downloaded succesfully ', font = 'arial 15',fg='green').place(x= 130 , y = 210)


Button(root,text='Download mp4',font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = DownloaderMp4).place(x=70 ,y = 150)
Button(root,text='Download mp3',font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=280 ,y = 150)

root.mainloop()