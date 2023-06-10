import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas=tk.Tk()
canvas.title("MusicPlayer")
canvas.geometry("600x800")
canvas.config(bg='pink')

rootpath="C:\\Users\\nandi\\Desktop\\Music Player"
pattern="*.mp3"

mixer.init()

def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath+"\\"+listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def play_next():
    next_song=listbox.curselection()
    next_song=next_song[0]+1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    
    mixer.music.load(rootpath+"\\"+ next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    next_song=listbox.curselection()
    next_song=next_song[0]-1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    
    mixer.music.load(rootpath+"\\"+ next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def pause_song():
    if pauseButton["text"]=="Pause":
        mixer.music.pause()
        pauseButton["text"]="Resume"
    else:
        mixer.music.unpause()
        pauseButton["text"]="Pause"


listbox=tk.Listbox(canvas,fg="cyan",bg="black",width=100,font=('DS-Digital',18))
listbox.pack(padx=15,pady=15)

top=tk.Frame(canvas,bg="pink")
top.pack(padx=10,pady=5,anchor='center')

label=tk.Label(canvas,text='',bg='pink',fg='red',font=('DS-Digital',18))
label.pack(pady=15)

prevButton=tk.Button(canvas,text="<<",command=play_prev)
prevButton.pack(pady=15,in_=top,side='left')

stopButton=tk.Button(canvas,text="Stop",command=stop)
stopButton.pack(pady=15,in_=top,side='left')

playButton=tk.Button(canvas,text="Play",command=select)
playButton.pack(pady=15,in_=top,side='left')

pauseButton=tk.Button(canvas,text="Pause",command=pause_song)
pauseButton.pack(pady=15,in_=top,side='left')

nextButton=tk.Button(canvas,text=">>",command=play_next)
nextButton.pack(pady=15,in_=top,side='left')

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert('end',filename)
canvas.mainloop()