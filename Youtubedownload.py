from tkinter import E
from matplotlib.pyplot import new_figure_manager
from pytube import YouTube
from pytube.cli import on_progress
import os

link = input("Insira seu Link ")

Ytd = YouTube(link, on_progress_callback = on_progress)

print(Ytd.title)

print('Video = 1')
print("Audio = 2")

resposta = int(input("Informe sua opção "))

if resposta == 1:
    print("Baixando seu Video")
    ys = Ytd.streams.get_highest_resolution()
    ys.download()

    
elif resposta == 2:
    print("Convertendo seu Video")
    ys = Ytd.streams.get_audio_only()
    out_file = ys.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mpeg'
    os.rename(out_file, new_file)
    
  
 