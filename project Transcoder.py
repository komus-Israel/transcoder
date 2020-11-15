from tkinter import *
from tkinter import filedialog
import os
from pygame import mixer
import ffmpy
from ttkthemes import themed_tk as tk
from tkinter import ttk
import tkinter.messagebox


root = tk.ThemedTk()
root.get_themes()
root.set_theme('equilux')
root.title('Transcoder')
root.geometry('300x100')
root.config(bg = 'gray')

#icon picture
icon = Image('photo', file = 'metronome.png')
root.tk.call('wm','iconphoto',root._w,icon)

mixer.init()

#menus

main_menu = Menu(root, bg = 'azure4')
root.config(menu = main_menu)



#widgets

message = Message(root, text = '.wav Transcoder', width = 100,bg = 'gray', font = 'Uroob 12')
message.grid(column = 1, row = 1)


Entry_window = ttk.Entry(root, font = 'Times 10 roman')
Entry_window.grid(column = 1, row = 3)



#functions
def open_file():
    global file
    global files
    file = filedialog.askopenfilename(initialdir = '~/Music', filetypes = [('All supported', '.mp3 .ogg'), ('All files','*.*')])
    files = os.path.basename(file)
    Entry_window.insert(0,files)
    Entry_window.get()

def transcude_file():
    
    f = file[0:]
    if f[-4:] in ['.mp3', '.m4a', '.ogg']:
        if f in file:
            trans = ffmpy.FFmpeg(inputs ={f:None}, outputs = {f[0:-4] + '.wav': None})
            trans.run()
            print(trans)

    
        

    #if os.path.abspath('~/Music/wave') is True:
        

def about():
    tkinter.messagebox.showinfo('About', 'This is a transcoder app that converts .mp3, .m4a and .ogg files to .wav format')

def test_wav_file():
    wav_file = filedialog.askopenfilename(initialdir = '~/Music', filetypes = [('All supported', '.wav'), ('All files','*.*')])
    mixer.music.load(wav_file)
    mixer.music.play()

def stop_test():
    mixer.music.stop()
    

#creating sub menus

submenu = Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = 'File',font = 'Uroob 12',menu = submenu)
submenu.add_command(label = 'Open',font = 'Uroob 12',command = open_file)
submenu.add_command(label = 'Exit', font = 'Uroob 12',command = root.destroy)


submenu = Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = 'Test', font = 'Uroob 12', menu = submenu)
submenu.add_command(label = 'Test .wav file', font = 'Uroob 12',command = test_wav_file)
submenu.add_command(label = 'Halt Test', font = 'Uroob 12',command = stop_test)


#submenu = Menu(main_menu, tearoff = 0)
main_menu.add_command(label = 'About', font = 'Uroob 12', command = about)




# file button
file_button = Button(root, text = 'browse file', font = 'Uroob 12', width = 6, relief = 'sunken', bg = 'azure4',command = open_file)
file_button.grid(column = 2, row = 3)

# Transcribe button

transcude_button = Button(root, text = 'Transcode', font = 'Uroob 12',bg = 'azure4', relief = 'sunken', command = transcude_file)
transcude_button.grid(column = 1, row = 4)

root.mainloop()
    
