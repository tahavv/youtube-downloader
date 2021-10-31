from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


FileLocation=""

#function
def openFileLocation():
    FileLocation=filedialog.askdirectory()
    if(len(FileLocation) > 1):
        locationEroorMsg.config(text=FileLocation,fg='green')
    else :
        locationEroorMsg.config(text='Please Choose Folder',fg='red')

def downlaodVideo():
    quality = ytbchoices.get()
    url = link_entery.get()
    if(len(url)>1):
        error.config(text='')
        yt=YouTube(url)
        if(quality==str(ytbchoices[0])):
            select = yt.streams.first()
        elif(quality==ytbchoices[1]):
            select=yt.streams.last()
        elif(quality==ytbchoices[2]):
            select = yt.streams.filter(only_audio=True).first() 
    else:
        error.config(Text='Paste link agaoin',fg='red')           
    
    select.download(FileLocation)
    error.config(text='Download Completed',fg='green')


#main screen 
root = Tk()
root.geometry('350x400')
root.columnconfigure(0,weight=1)
root.resizable(0,0)
root.title("Youtube Video Downloader")

#labels
l1=Label(root,text='Youtube video converter',font=("jost",20),fg='gold2')
l1.grid()

link=StringVar()

l2=Label(root, text='Paste Your link here:',font=("jost",13))
l2.grid()

link_entery=Entry(root ,width=50, textvariable=link)
link_entery.grid()


error= Label(root,text="Link Unvailable",font=("jost",10),fg='red')
error.grid()

save=Label(root, text='Choose path to save:',font=("jost",13))
save.grid()

btn1=Button(root,text='Choose path',font ="jost" ,bg ='gold2', padx=2, command=openFileLocation)
btn1.grid()

locationEroorMsg=Label(root, text='Path Unvailable',font=("jost",10),fg='red')
locationEroorMsg.grid()

quality=Label(root, text='Select Quality',font=("jost",13))
quality.grid()

choices=["High quality(720p)","Low quality(144p)","audio only"]
ytbchoices=ttk.Combobox(root,values=choices)
ytbchoices.grid()


download=Button(root,text='Download',font = 'jost' ,bg = 'gold2',padx=2, command = downlaodVideo)
download.grid()

root.mainloop()

#https://youtu.be/BPhvbluq7uM