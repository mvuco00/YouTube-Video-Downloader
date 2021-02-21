import tkinter as tk
from pytube import YouTube

# inicijalizacija tkintera
root = tk.Tk()
# postavke zaslona
root.geometry('700x500')
root.resizable(0,0)
root.title("Youtube video downloader")

# prikaz teksta na zaslonu
tk.Label(root,text = 'Download Youtube Video', font ='courier 20 bold', pady=15).pack()

# Holds a string; the default value is an empty string ""
# sluzi za spremanje linka koji korisnik unese
link = tk.StringVar()

tk.Label(root, text = 'Enter Youtube link:', font = 'courier 15', pady=10).pack()

# polje za unos
# preko textvariable dohvati se uneseni link, postavlja se na StringVar instancu
entered = tk.Entry(root, width = 90,textvariable = link)
entered.pack()


def Downloader():     
    # preko get() se dohvati link koji se nalazi u varijabli link i treba ga pretvorit u string
    url =YouTube(str(link.get()))
    
    # download videa
    video = url.streams.first()
    video.download()
    tk.Label(root, text = url.streams[0].title, font = 'courier 10', pady=10).pack()
    tk.Label(root, text = 'Downloaded successfully', font = 'arial 15 bold', fg='green').pack()
    entered.delete(0, "end")
    

tk.Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'goldenrod1', padx = 2, pady=5,
                            command = Downloader).pack()

# slusanje eventova dok se prozor ne zatvori
root.mainloop()