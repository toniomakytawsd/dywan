import tkinter as tk
import webbrowser

def odpal_geometry_clicker():
    webbrowser.open("https://editor.p5js.org/toniomakyt/full/9avTSFZMg")

def odpal_nowa_gra():
    webbrowser.open("https://editor.p5js.org/toniomakyt/full/PUGEG4B1s")


window = tk.Tk()
window.title("dywan")
window.geometry("500x450")


KOLOR_TLA = "#1e1e2e"          
KOLOR_GUZIKA_1 = "#fab387"     
KOLOR_GUZIKA_2 = "#a6e3a1"     
KOLOR_TEKSTU_GUZIKA = "#11111b"

window.configure(bg=KOLOR_TLA)


tytul = tk.Label(
    window, 
    text="launcher gierek dywan", 
    font=("Segoe UI", 20, "bold"), 
    fg="#cdd6f4", 
    bg=KOLOR_TLA
)
tytul.pack(pady=(40, 10))

podtytul = tk.Label(
    window, 
    text="wybierz gre, albo chlebek albo dzem (ale sie zrymowalo)", 
    font=("Segoe UI", 11), 
    fg="#a6adc8", 
    bg=KOLOR_TLA
)
podtytul.pack(pady=(0, 40))


guzik1 = tk.Button(
    window, 
    text="🔺 Geometry Clicker", 
    command=odpal_geometry_clicker,
    font=("Segoe UI", 13, "bold"),
    bg=KOLOR_GUZIKA_1,
    fg=KOLOR_TEKSTU_GUZIKA,
    activebackground="#f9e2af", 
    width=22,
    height=2,
    cursor="hand2",             
    bd=0                        
)
guzik1.pack(pady=15)


guzik2 = tk.Button(
    window, 
    text="🍞 Bread Clicker", 
    command=odpal_nowa_gra,
    font=("Segoe UI", 13, "bold"),
    bg=KOLOR_GUZIKA_2,
    fg=KOLOR_TEKSTU_GUZIKA,
    activebackground="#b4befe", 
    width=22,
    height=2,
    cursor="hand2",
    bd=0
)
guzik2.pack(pady=15)


stopka = tk.Label(
    window, 
    text="v1.0.0 • by pannek_, dywan nie copyrighted", 
    font=("Segoe UI", 9), 
    fg="#585b70", 
    bg=KOLOR_TLA
)
stopka.pack(side="bottom", pady=20)

window.mainloop()
