import os, sys, ctypes, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 3
__filename__ = "TextConverter"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:
            urllib.request.urlretrieve("http://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
            urllib.request.urlretrieve("http://quentium.fr/+++PythonDL/+Berlin.ttf", __savepath__ + "/+Berlin.ttf")
        except:pass
        ctypes.WinDLL('gdi32').AddFontResourceW(__savepath__ + "/+Berlin.ttf")

if connection == True:
    try:script_version = int(urllib.request.urlopen("http://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("http://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("http://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

import re, random, unidecode
from tkinter.filedialog import *
from tkinter import *

Morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..',

         '0': '-----', '1': '.----', '2': '..---',
         '3': '...--', '4': '....-', '5': '.....',
         '6': '-....', '7': '--...', '8': '---..',
         '9': '----.',

         ".": ".-.-.-", ",": "--..--", "=": "-...-",
         ":": "---...", "?": "..--..", "!": "-.-.--",
         "-": "-....-", "/": "-..-.", "+": ".-.-.",
         ";": "-.-.-.", "(": "-.--.", ")": "-.--.-",
         "_": "..--.-", '"': ".-..-.", "@": ".--.-.",
         "'": ".----.", "&": ".-...", " ": "/"
}

Morse_reversed = {value: key for key, value in Morse.items()}
txtboxfocus = ""
f_name = None

def append_box(value):
    Text2.delete("1.0", END)
    Text2.insert(END, value)

def sentence_to_binary():
    return append_box([bin(ord(x))[2:].zfill(8) for x in Text1.get("1.0", END)])

def sentence_to_hexadecimal():
    return append_box(" ".join("{:02x}".format(ord(x)) for x in Text1.get("1.0", END)))

def sentence_to_octal():
    return append_box([oct(ord(x))[2:].zfill(3) for x in Text1.get("1.0", END)])

def sentence_to_ascii():
    return append_box([ord(x) for x in Text1.get("1.0", END)])

def binary_to_sentence():
    return append_box("".join(chr(int(Text1.get("1.0", END).replace(" ", "")[i * 8:i * 8 + 8], 2)) for i in range(len(Text1.get("1.0", END).replace(" ", "")) // 8)))

def hexadecimal_to_sentence():
    return append_box("".join([chr(int("".join(x), 16)) for x in zip(Text1.get("1.0", END).replace(" ", "")[0::2], Text1.get("1.0", END).replace(" ", "")[1::2])]))

def octal_to_sentence():
    return append_box("".join([chr(int(x, 8)) for x in Text1.get("1.0", END).split()]))

def ascii_to_sentence():
    return append_box("".join([chr(int(x)) for x in Text1.get("1.0", END).split()]))

def sentence_to_morse():
    sentence_morse = ""
    for char in Text1.get("1.0", END):
        char = unidecode.unidecode(char)
        try:sentence_morse += Morse[char.upper()] + "   "
        except:sentence_morse += "?"
    return append_box(sentence_morse)

def morse_to_sentence():
    sentence_morse = "".join(Morse_reversed.get(x) for x in Text1.get("1.0", END).split())
    sentence_morse = sentence_morse.lower()
    if not sentence_morse == "":
        sentence_morse = sentence_morse[0].upper() + sentence_morse[1:]
    return append_box(sentence_morse)

def sentence_to_lowercase():
    return append_box(Text1.get("1.0", END).lower()[:-2])

def sentence_to_uppercase():
    return append_box(Text1.get("1.0", END).upper()[:-2])

def sentence_reverse():
    return append_box(Text1.get("1.0", END)[-2::-1])

def capitalize_words():
    temp = " ".join(x[0].upper() + x[1:] for x in Text1.get("1.0", END).split(" "))
    return append_box("\n".join(x[0].upper() + x[1:] for x in temp[:-2].split("\n")))

def capitalize_sentence():
    def repl_(match):
        return match.group(0).upper()
    return append_box(re.sub(r'^([a-z])|[\.|\?|\!|\n]\s*([a-z])|\s+([a-z])(?=\.)', repl_, Text1.get("1.0", END)[:-2]))

def sentence_randomcase():
    sentence_randomcase = ""
    for char in Text1.get("1.0", END):
        number = random.randint(0, 1)
        if number == 0:sentence_randomcase += char.lower()
        else:sentence_randomcase += char.upper()
    return append_box(sentence_randomcase[:-2])

# File menu #

def file_openfast(event):
    file_open()

def file_open():
    fname = askopenfilename(parent=textconverter, filetypes=[("Fichiers texte", "*.txt"),("All Files", "*.*")])
    if fname:
        try:
            filecontains = open(fname, "r", encoding="utf-8").read()
        except:
            filecontains = open(fname, "r", encoding="ANSI").read()
        Text1.delete("1.0", END)
        Text1.insert(END, filecontains)

def file_savefast(event):
    file_save()

def file_save():
    global f_name
    contents = Text2.get(1.0, "end-1c")
    if f_name is not None:
        with open(f_name, "w", encoding="utf-8") as file:
            file.write(contents)
            file.close()
    else:
        file_saveas()

def file_saveasfast(event):
    file_saveas()

def file_saveas():
    global f_name
    contents = Text2.get(1.0, "end-1c")
    f = asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt"),("All Files", "*.*")])
    if f is None:
        return
    f_name = f.name
    f.write(contents)
    f.close()

# Edit menu #

def edit_cut():
    global txtboxfocus
    if txtboxfocus:
        eval(txtboxfocus).event_generate("<<Cut>>")
    else:
        pass

def edit_copy():
    global txtboxfocus
    if txtboxfocus:
        eval(txtboxfocus).event_generate("<<Copy>>")
    else:
        pass

def edit_paste():
    global txtboxfocus
    if txtboxfocus:
        eval(txtboxfocus).event_generate("<<Paste>>")
    else:
        pass

def edit_selectall():
    global txtboxfocus
    if txtboxfocus:
        eval(txtboxfocus).tag_add(SEL, "1.0", END)
        eval(txtboxfocus).mark_set(INSERT, "1.0")
        eval(txtboxfocus).see(INSERT)
        return "break"
    else:
        pass

# ---Separator--- #

def edit_delupfast(event):
    edit_delup()

def edit_delup():
    Text1.delete("1.0", END)

def edit_deldownfast(event):
    edit_deldown()

def edit_deldown():
    Text2.delete("1.0", END)

def edit_delallfast(event):
    edit_delall()

def edit_delall():
    Text1.delete("1.0", END)
    Text2.delete("1.0", END)

# More menu #

def more_website():
    os.system("start https://quentium.fr/")

def more_progs():
    os.system("start https://quentium.fr/programs/")

def more_donation():
    os.system("start https://paypal.me/QuentiumYT/")

# ---Separator--- #

def more_proposfast(event):
    more_propos()

def more_propos():
    win_propos = Tk()
    win_propos.configure(bg="lightgray")
    width = 400
    height = 200
    win_propos.update_idletasks()
    x = (win_propos.winfo_screenwidth() - width) // 2
    y = (win_propos.winfo_screenheight() - height) // 2
    win_propos.geometry("{}x{}+{}+{}".format(width, height, int(x), int(y)))
    if os.path.exists(__iconpath__):
        win_propos.iconbitmap(__iconpath__)
    win_propos.title("À propos")
    win_propos.resizable(width=False, height=False)
    Label(win_propos, text="Programme créé et designé par Quentium. \nPour plus d'informations, \nmerci de me contacter par e-mail : \npro@quentium.fr", font=font1, fg="black", bg="lightgray").pack(pady=20)

    def close():
        win_propos.destroy()
    Buttonpropos = Button(win_propos, pady="0", relief=GROOVE, fg="black", command=close, font=font2, text="Fermer")
    Buttonpropos.place(relx=0.375, rely=0.70, height=40, width=100)

# Main window #

def onclose():
    if askokcancel("Quitter", "Voulez vous quitter le programme ?"):
        ctypes.WinDLL('gdi32').RemoveFontResourceW(__savepath__ + "/+Berlin.ttf")
        os._exit(1)

textconverter = Tk()
textconverter.state("zoomed")
textconverter.title(__filename__)
textconverter.configure(background="#000000")
textconverter.protocol("WM_DELETE_WINDOW", onclose)
if os.path.exists(__iconpath__):
    textconverter.iconbitmap(__iconpath__)
font1 = "-family {Berlin Sans FB Demi} -size 15 -weight bold -slant roman -underline 0 -overstrike 0"
if textconverter.winfo_screenheight() >= 1080:
    font2 = "-family {Berlin Sans FB Demi} -size 20 -weight bold -slant roman -underline 0 -overstrike 0"
else:
    font2 = "-family {Berlin Sans FB Demi} -size 17 -weight bold -slant roman -underline 0 -overstrike 0"
font3 = "-family {Berlin Sans FB Demi} -size 30 -weight bold -slant roman -underline 0 -overstrike 0"

# Menubar #

menubar = Menu(textconverter)
menu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menu1.add_command(label="Ouvrir", accelerator="Ctrl+O", command=file_open)
textconverter.bind("<Control-o>", file_openfast)
textconverter.bind("<Control-O>", file_openfast)
menu1.add_command(label="Enregister", accelerator="Ctrl+S", command=file_save)
textconverter.bind("<Control-s>", file_savefast)
textconverter.bind("<Control-S>", file_savefast)
menu1.add_command(label="Enregister sous", accelerator="Ctrl+Alt+S", command=file_saveas)
textconverter.bind("<Control-Shift-s>", file_saveasfast)
textconverter.bind("<Control-Shift-S>", file_saveasfast)
menu1.add_separator()
menu1.add_command(label="Quitter", accelerator="Alt+F4", command=onclose)

menu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Édition", menu=menu2)
menu2.add_command(label="Couper", accelerator="Ctrl+X", command=edit_cut)
menu2.add_command(label="Copier", accelerator="Ctrl+C", command=edit_copy)
menu2.add_command(label="Coller", accelerator="Ctrl+V", command=edit_paste)
menu2.add_command(label="Sélectionner tout", accelerator="Ctrl+A", command=edit_selectall)
menu2.add_separator()
menu2.add_command(label="Supprimer texte haut", accelerator="Alt+A", command=edit_delup)
textconverter.bind("<Alt-a>", edit_delupfast)
textconverter.bind("<Alt-A>", edit_delupfast)
menu2.add_command(label="Supprimer texte bas", accelerator="Alt+Q", command=edit_deldown)
textconverter.bind("<Alt-q>", edit_deldownfast)
textconverter.bind("<Alt-Q>", edit_deldownfast)
menu2.add_command(label="Tout supprimer", accelerator="Alt+W", command=edit_delall)
textconverter.bind("<Alt-w>", edit_delallfast)
textconverter.bind("<Alt-W>", edit_delallfast)

menu3 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Plus", menu=menu3)
menu3.add_command(label="Site web", command=more_website)
menu3.add_command(label="Autres programmes", command=more_progs)
menu3.add_command(label="Donation", command=more_donation)
menu3.add_separator()
menu3.add_command(label="À propos", accelerator="F1", command=more_propos)
textconverter.bind("<F1>", more_proposfast)
textconverter.config(menu=menubar)

# Widgets #

def get_focus(x):
    global txtboxfocus
    txtboxfocus = x

def get_size(size):
    return (textconverter.winfo_height() * size) / 1000

Text1 = Text(textconverter)
Text1.place(relx=0.01, rely=0.02, relheight=0.44, relwidth=0.65)
Text1.bind("<FocusIn>", lambda x: get_focus("Text1"))
Text1.configure(background="white")
Text1.configure(font=font2)
Text1.configure(foreground="black")
Text1.configure(highlightbackground="#d9d9d9")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="black")
Text1.configure(selectbackground="#c4c4c4")
Text1.configure(selectforeground="black")
Text1.configure(undo="1")
Text1.configure(width=1254)
Text1.configure(wrap=WORD)

Text2 = Text(textconverter)
Text2.place(relx=0.01, rely=0.54, relheight=0.44, relwidth=0.65)
Text2.bind("<FocusIn>", lambda x: get_focus("Text2"))
Text2.configure(background="white")
Text2.configure(font=font2)
Text2.configure(foreground="black")
Text2.configure(highlightbackground="#d9d9d9")
Text2.configure(highlightcolor="black")
Text2.configure(insertbackground="black")
Text2.configure(selectbackground="#c4c4c4")
Text2.configure(selectforeground="black")
Text2.configure(undo="1")
Text2.configure(width=1254)
Text2.configure(wrap=WORD)

Label1 = Label(textconverter)
Label1.place(relx=0.29, rely=0.48, height=29, width=210)
Label1.configure(activebackground="#f9f9f9")
Label1.configure(activeforeground="black")
Label1.configure(background="#000000")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font=font3)
Label1.configure(foreground="#ffffff")
Label1.configure(highlightbackground="#d9d9d9")
Label1.configure(highlightcolor="black")
Label1.configure(text="Convertir :")

Button1 = Button(textconverter)
Button1.place(relx=0.74, rely=0.02, height=get_size(38), width=get_size(428))
Button1.configure(activebackground="#d9d9d9")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#ffffff")
Button1.configure(command=sentence_to_binary)
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(font=font2)
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(padx="0")
Button1.configure(pady="0")
Button1.configure(text="Convertir Texte en Binaire")
Button1.configure(width=30)

Button2 = Button(textconverter)
Button2.place(relx=0.74, rely=0.08, height=get_size(38), width=get_size(428))
Button2.configure(activebackground="#d9d9d9")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#ffffff")
Button2.configure(command=sentence_to_hexadecimal)
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(font=font2)
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(padx="0")
Button2.configure(pady="0")
Button2.configure(text="Convertir Texte en Hexadécimal")
Button2.configure(width=30)

Button3 = Button(textconverter)
Button3.place(relx=0.74, rely=0.14, height=get_size(38), width=get_size(428))
Button3.configure(activebackground="#d9d9d9")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#ffffff")
Button3.configure(command=sentence_to_octal)
Button3.configure(disabledforeground="#a3a3a3")
Button3.configure(font=font2)
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(padx="0")
Button3.configure(pady="0")
Button3.configure(text="Convertir Texte en Octal")
Button3.configure(width=30)

Button4 = Button(textconverter)
Button4.place(relx=0.74, rely=0.2, height=get_size(38), width=get_size(428))
Button4.configure(activebackground="#d9d9d9")
Button4.configure(activeforeground="#000000")
Button4.configure(background="#ffffff")
Button4.configure(command=sentence_to_ascii)
Button4.configure(disabledforeground="#a3a3a3")
Button4.configure(font=font2)
Button4.configure(foreground="#000000")
Button4.configure(highlightbackground="#d9d9d9")
Button4.configure(highlightcolor="black")
Button4.configure(padx="0")
Button4.configure(pady="0")
Button4.configure(text="Convertir Texte en ASCII")
Button4.configure(width=30)

Button5 = Button(textconverter)
Button5.place(relx=0.74, rely=0.26, height=get_size(38), width=get_size(428))
Button5.configure(activebackground="#d9d9d9")
Button5.configure(activeforeground="#000000")
Button5.configure(background="#ffffff")
Button5.configure(command=binary_to_sentence)
Button5.configure(disabledforeground="#a3a3a3")
Button5.configure(font=font2)
Button5.configure(foreground="#000000")
Button5.configure(highlightbackground="#d9d9d9")
Button5.configure(highlightcolor="black")
Button5.configure(padx="0")
Button5.configure(pady="0")
Button5.configure(text="Convertir Binaire en Texte")
Button5.configure(width=30)

Button6 = Button(textconverter)
Button6.place(relx=0.74, rely=0.32, height=get_size(38), width=get_size(428))
Button6.configure(activebackground="#d9d9d9")
Button6.configure(activeforeground="#000000")
Button6.configure(background="#ffffff")
Button6.configure(command=hexadecimal_to_sentence)
Button6.configure(disabledforeground="#a3a3a3")
Button6.configure(font=font2)
Button6.configure(foreground="#000000")
Button6.configure(highlightbackground="#d9d9d9")
Button6.configure(highlightcolor="black")
Button6.configure(padx="0")
Button6.configure(pady="0")
Button6.configure(text="Convertir Hexadécimal en Texte")
Button6.configure(width=30)

Button7 = Button(textconverter)
Button7.place(relx=0.74, rely=0.38, height=get_size(38), width=get_size(428))
Button7.configure(activebackground="#d9d9d9")
Button7.configure(activeforeground="#000000")
Button7.configure(background="#ffffff")
Button7.configure(command=octal_to_sentence)
Button7.configure(disabledforeground="#a3a3a3")
Button7.configure(font=font2)
Button7.configure(foreground="#000000")
Button7.configure(highlightbackground="#d9d9d9")
Button7.configure(highlightcolor="black")
Button7.configure(padx="0")
Button7.configure(pady="0")
Button7.configure(text="Convertir Octal en Texte")
Button7.configure(width=30)

Button8 = Button(textconverter)
Button8.place(relx=0.74, rely=0.44, height=get_size(38), width=get_size(428))
Button8.configure(activebackground="#d9d9d9")
Button8.configure(activeforeground="#000000")
Button8.configure(background="#ffffff")
Button8.configure(command=ascii_to_sentence)
Button8.configure(disabledforeground="#a3a3a3")
Button8.configure(font=font2)
Button8.configure(foreground="#000000")
Button8.configure(highlightbackground="#d9d9d9")
Button8.configure(highlightcolor="black")
Button8.configure(padx="0")
Button8.configure(pady="0")
Button8.configure(text="Convertir ASCII en Texte")
Button8.configure(width=30)

Button9 = Button(textconverter)
Button9.place(relx=0.74, rely=0.52, height=get_size(38), width=get_size(428))
Button9.configure(activebackground="#d9d9d9")
Button9.configure(activeforeground="#000000")
Button9.configure(background="#ffffff")
Button9.configure(command=sentence_to_morse)
Button9.configure(disabledforeground="#a3a3a3")
Button9.configure(font=font2)
Button9.configure(foreground="#000000")
Button9.configure(highlightbackground="#d9d9d9")
Button9.configure(highlightcolor="black")
Button9.configure(padx="0")
Button9.configure(pady="0")
Button9.configure(text="Convertir Texte en Morse")
Button9.configure(width=30)

Button10 = Button(textconverter)
Button10.place(relx=0.74, rely=0.58, height=get_size(38), width=get_size(428))
Button10.configure(activebackground="#d9d9d9")
Button10.configure(activeforeground="#000000")
Button10.configure(background="#ffffff")
Button10.configure(command=morse_to_sentence)
Button10.configure(disabledforeground="#a3a3a3")
Button10.configure(font=font2)
Button10.configure(foreground="#000000")
Button10.configure(highlightbackground="#d9d9d9")
Button10.configure(highlightcolor="black")
Button10.configure(padx="0")
Button10.configure(pady="0")
Button10.configure(text="Convertir Morse en Texte")
Button10.configure(width=30)

Button11 = Button(textconverter)
Button11.place(relx=0.74, rely=0.64, height=get_size(38), width=get_size(428))
Button11.configure(activebackground="#d9d9d9")
Button11.configure(activeforeground="#000000")
Button11.configure(background="#ffffff")
Button11.configure(command=sentence_to_lowercase)
Button11.configure(disabledforeground="#a3a3a3")
Button11.configure(font=font2)
Button11.configure(foreground="#000000")
Button11.configure(highlightbackground="#d9d9d9")
Button11.configure(highlightcolor="black")
Button11.configure(padx="0")
Button11.configure(pady="0")
Button11.configure(text="Convertir Texte en Minuscule")
Button11.configure(width=30)

Button12 = Button(textconverter)
Button12.place(relx=0.74, rely=0.70, height=get_size(38), width=get_size(428))
Button12.configure(activebackground="#d9d9d9")
Button12.configure(activeforeground="#000000")
Button12.configure(background="#ffffff")
Button12.configure(command=sentence_to_uppercase)
Button12.configure(disabledforeground="#a3a3a3")
Button12.configure(font=font2)
Button12.configure(foreground="#000000")
Button12.configure(highlightbackground="#d9d9d9")
Button12.configure(highlightcolor="black")
Button12.configure(padx="0")
Button12.configure(pady="0")
Button12.configure(text="Convertir Texte en Majuscule")
Button12.configure(width=30)

Button13 = Button(textconverter)
Button13.place(relx=0.74, rely=0.76, height=get_size(38), width=get_size(428))
Button13.configure(activebackground="#d9d9d9")
Button13.configure(activeforeground="#000000")
Button13.configure(background="#ffffff")
Button13.configure(command=sentence_reverse)
Button13.configure(disabledforeground="#a3a3a3")
Button13.configure(font=font2)
Button13.configure(foreground="#000000")
Button13.configure(highlightbackground="#d9d9d9")
Button13.configure(highlightcolor="black")
Button13.configure(padx="0")
Button13.configure(pady="0")
Button13.configure(text="Texte inversé")
Button13.configure(width=30)

Button14 = Button(textconverter)
Button14.place(relx=0.74, rely=0.82, height=get_size(38), width=get_size(428))
Button14.configure(activebackground="#d9d9d9")
Button14.configure(activeforeground="#000000")
Button14.configure(background="#ffffff")
Button14.configure(command=capitalize_words)
Button14.configure(disabledforeground="#a3a3a3")
Button14.configure(font=font2)
Button14.configure(foreground="#000000")
Button14.configure(highlightbackground="#d9d9d9")
Button14.configure(highlightcolor="black")
Button14.configure(padx="0")
Button14.configure(pady="0")
Button14.configure(text="Majuscule Mots")
Button14.configure(width=30)

Button15 = Button(textconverter)
Button15.place(relx=0.74, rely=0.88, height=get_size(38), width=get_size(428))
Button15.configure(activebackground="#d9d9d9")
Button15.configure(activeforeground="#000000")
Button15.configure(background="#ffffff")
Button15.configure(command=capitalize_sentence)
Button15.configure(disabledforeground="#a3a3a3")
Button15.configure(font=font2)
Button15.configure(foreground="#000000")
Button15.configure(highlightbackground="#d9d9d9")
Button15.configure(highlightcolor="black")
Button15.configure(padx="0")
Button15.configure(pady="0")
Button15.configure(text="Majuscule Texte")
Button15.configure(width=30)

Button16 = Button(textconverter)
Button16.place(relx=0.74, rely=0.94, height=get_size(38), width=get_size(428))
Button16.configure(activebackground="#d9d9d9")
Button16.configure(activeforeground="#000000")
Button16.configure(background="#ffffff")
Button16.configure(command=sentence_randomcase)
Button16.configure(disabledforeground="#a3a3a3")
Button16.configure(font=font2)
Button16.configure(foreground="#000000")
Button16.configure(highlightbackground="#d9d9d9")
Button16.configure(highlightcolor="black")
Button16.configure(padx="0")
Button16.configure(pady="0")
Button16.configure(text="Majuscule aléatoire")
Button16.configure(width=30)

Canvas1 = Canvas(textconverter)
Canvas1.place(relx=0.74, rely=0.5, relheight=0.0001, relwidth=0.222)
Canvas1.configure(background="white")
Canvas1.configure(borderwidth="0")
Canvas1.configure(insertbackground="black")
Canvas1.configure(relief=RIDGE)
Canvas1.configure(selectbackground="#c4c4c4")
Canvas1.configure(selectforeground="black")
Canvas1.configure(width=556)

textconverter.mainloop()
