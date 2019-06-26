
#from .Object_detection_video import choose_video
from tkinter import filedialog
from tkinter import Tk,Toplevel,PhotoImage,BOTH,RAISED,Canvas,CENTER
from tkinter import Label,Frame,Checkbutton,Button,LEFT,BOTTOM,X,Y,E,W,Entry,Menu,TOP,SUNKEN
from tkinter import *
#from .image_to_video1 import video_converter
import os

def toolbar_all():

    def donothing():
        print('nothing')
        
        

    root=Tk()
    root.geometry("600x600")

    def video1():
        sub=Toplevel(root)
        sub.geometry("400x400")
        os.system('python embed_video.py')


    def plot1():
        os.system('python plot1.py')


    def saved_files(filename):
        #os.system('python test_frames_main6f_alert.py')
        os.system('2.avi')
        

    def saved_files1(filename):
        #os.system('python test_frames_main6f_alert.py')
        #os.system('2.avi')
        #choose_video(filename)
        directory='./z1video_frames4/'
        #video=video_converter.main(directory)


    def browse_button():
        global folder_path
        #filename = filedialog.askopenfilename()
        filename = filedialog.askopenfilename(filetypes = (("avi files","*.avi"),("all files","*.*")))
        #saved_files1(filename)

        
    toolbar=Frame(root,bg='indigo',bd=2)
    insertbutt=Button(toolbar,text='video1',command=video1)
    insertbutt.pack(side=LEFT,padx=2,pady=2,ipadx=20)
    printexit1=Button(toolbar,text='browse_button',command=browse_button)
    printexit1.pack(side=LEFT,padx=2,pady=2,ipadx=20)
    printexit2=Button(toolbar,text='saved_files',command=saved_files)
    printexit2.pack(side=LEFT,padx=2,pady=2,ipadx=20)
    printexit3=Button(toolbar,text='plot1',command=plot1)
    printexit3.pack(side=LEFT,padx=2,pady=2,ipadx=20)


    toolbar.pack(side=TOP,fill=BOTH)
    #toolbar1=Frame(root,bg='red')
    toolbar1=Label(root,bg='indigo',bd=2)

    insertbutt1=Button(toolbar1,text='video1',command=video1)
    insertbutt1.pack(side=LEFT,padx=2,pady=2,ipadx=20)
    printexit11=Button(toolbar1,text='video2',command=video1)
    printexit11.pack(side=LEFT,padx=2,pady=2,ipadx=20)
    printexit21=Button(toolbar1,text='video3',command=video1)
    printexit21.pack(side=LEFT,padx=2,pady=2,ipadx=20)
    printexit31=Button(toolbar1,text='plot1',command=plot1)
    printexit31.pack(side=LEFT,padx=2,pady=2,ipadx=20)


    #canvas=Canvas(root,width=300,height=20)

    explanation = """MOBISAMADHAN"""


    w = Label(root, 
                 compound = CENTER,
                 text=explanation,bg='blue',pady=5,
                 font=('Courier',30,'bold')
                 ).pack(fill=BOTH,expand=True)

    #canvas.pack(expand=True)


         

#    logo = PhotoImage(file="practical/logo.png")

    explanation = """CONTRIBUTION TOWARDS INDIA'S SMART CITY MISSION"""


    canvas=Canvas(root,width=300,height=20)


    w = Label(root, 
                 compound = CENTER,
                 text=explanation,font=('Courier',20,'bold'),bg='white',
                 
                 #image=logo
                 ).pack(fill=BOTH,expand=True)

    canvas.pack(expand=True)




    status=Label(root,text='prepare to do nothing',bd=3,relief=SUNKEN,anchor=W)
    status.pack(side=BOTTOM,fill=BOTH)

    toolbar1.pack(side=BOTTOM,fill=BOTH)




    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate


    button1 = Button(root,bg='green',bd=3, text="Quit", command=_quit)
    button1.pack(side=BOTTOM,fill=BOTH)


    root.mainloop()

