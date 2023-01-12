from tkinter import *
import PyPDF2
import tkinter
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog
from tkinter import ttk
from query import *
from PIL import ImageTk, Image
import sqlite3

app = tb.Window(themename="darkly")

# create the vertical tab alignment
app.style.configure('long.TNotebook', tabposition='wn')

my_notebook = tb.Notebook(app, style='long.TNotebook')
my_notebook.grid(row=1, column=2)
#----------------------------------------------------------------

#Zakładki
#----------------------------------------------------------------
przeglad_danych = ttk.Frame(my_notebook, width=1200, height=800)
dodaj = ttk.Frame(my_notebook, width=1200, height=800)
magazyn = ttk.Frame(my_notebook, width=1200, height=800)
odpisy = ttk.Frame(my_notebook, width=1200, height=800)
miesiace = ttk.Frame(my_notebook, width=1200, height=800)
wyszukiwarka = ttk.Frame(my_notebook, width=1200, height=800)


my_notebook.add(przeglad_danych, text="Przeglad danych")
my_notebook.add(dodaj, text="Dodaj/Edytuj/Usuń")
my_notebook.add(magazyn, text="Magazyn")
my_notebook.add(odpisy, text="Odpisy")
my_notebook.add(miesiace, text="Miesiace")
my_notebook.add(wyszukiwarka, text="Wyszukiwarka")
# Create a database or connect to one
conn = sqlite3.connect('dane_uczniow.db')

#Create cursor
c = conn.cursor()

#Etykiety które wyświetlają dane
query_label = Label(przeglad_danych, text="")
query_label.grid(row=1, column=0, columnspan=2)

query_label_1 = Label(przeglad_danych, text="")
query_label_1.grid(row=1, column=0)

query_label_2 = Label(przeglad_danych, text="")
query_label_2.grid(row=1, column=1)

query_label_3 = Label(przeglad_danych, text="")
query_label_3.grid(row=1, column=2)

query_label_4 = Label(przeglad_danych, text="")
query_label_4.grid(row=1, column=3)

# Create a Query Button MIESIACE
miesiace_btn = Button(przeglad_danych, text="Miesiace", command=lambda: query_miesiac(query_label_1,query_label_2,query_label_3,query_label_4))
miesiace_btn.grid(row=0, column=0, pady=10, padx=10, ipadx=13)
miesiace_btn.config(font="Helvetica 16 bold", fg='white', pady=10)

# Create a Query Button UCZNIOWIE
uczniowie_btn = Button(przeglad_danych, text="Uczniowie", command=lambda: query_uczniowie(query_label_1,query_label_2,query_label_3,query_label_4))
uczniowie_btn.grid(row=0, column=1, pady=10, ipadx=13)
uczniowie_btn.config(font="Helvetica 16 bold", fg='white', pady=10)

# Create a Query Button ODPISY
odpisy_btn = Button(przeglad_danych, text="Odpisy", command=lambda: query_odpisy(query_label_1,query_label_2,query_label_3,query_label_4))
odpisy_btn.grid(row=0, column=2, pady=10, padx=10, ipadx=13)
odpisy_btn.config(font="Helvetica 16 bold", fg='white', pady=10)

#----------------------------------------------------------------
#DODAJ/EDYTUJ/USUN
#----------------------------------------------------------------
ql = Label(wyszukiwarka, text="")
ql.grid(row=3, column=0, columnspan=2)

ql1 = Label(wyszukiwarka, text="")
ql1.grid(row=3, column=0)

ql2 = Label(wyszukiwarka, text="")
ql2.grid(row=3, column=1)

ql3 = Label(wyszukiwarka, text="")
ql3.grid(row=3, column=2)

ql4 = Label(wyszukiwarka, text="")
ql4.grid(row=3, column=3)

#Wyszukiwarka
szukaj = Entry(wyszukiwarka, width=50)
szukaj.grid(row=1, column=1)
btn_wy = Button(wyszukiwarka, text="Search",command=lambda: query_szukaj(szukaj, ql1, ql2, ql3, ql4))
btn_wy.grid(row=0, column=0, pady=10, padx=10, ipadx=13)
btn_wy.config(font="Helvetica 16 bold", fg='white', pady=10)



#


btn = Button(dodaj, text="Dodaj")
btn.grid(row=0, column=0, pady=10, padx=10, ipadx=13)
btn.config(font="Helvetica 16 bold", fg='white', pady=10)

btn = Button(dodaj, text="Edytuj")
btn.grid(row=0, column=1, pady=10, padx=10, ipadx=13)
btn.config(font="Helvetica 16 bold", fg='white', pady=10)


# ODPISY
btn = Button(dodaj, text="Usun")
btn.grid(row=0, column=2, pady=10, padx=10, ipadx=13)
btn.config(font="Helvetica 16 bold", fg='white', pady=10)

# Create Text Boxes
imie = Entry(dodaj, width=30)
imie.grid(row=2, column=1)

nazwisko = Entry(dodaj, width=30)
nazwisko.grid(row=3, column=1, pady=10)

placowka = Entry(dodaj, width=30)
placowka.grid(row=4, column=1, pady=10)

klasa = Entry(dodaj, width=30)
klasa.grid(row=5, column=1, pady=10)

# Create Text Box Labels
imie_label = Label(dodaj, text="Imie")
imie_label.grid(row=2, column=0)
imie_label.config(font="Helvetica 16 bold", fg='white', pady=10)

# imie_label.config(bg="#343a40", font="times 24 bold", fg='white', pady=15)
nazwisko_label = Label(dodaj, text="Nazwisko")
nazwisko_label.grid(row=3, column=0)
nazwisko_label.config(font="Helvetica 16 bold", fg='white', pady=10)

placowka_label = Label(dodaj, text="Placowka")
placowka_label.grid(row=4, column=0)
placowka_label.config(font="Helvetica 16 bold", fg='white', pady=10)

klasa_label = Label(dodaj, text="Klasa")
klasa_label.grid(row=5, column=0)
klasa_label.config(font="Helvetica 16 bold", fg='white', pady=10)

# Create Submit Button
submit_btn = Button(dodaj, text="Dodaj Rekord do Bazy Danych", command=lambda: submit(imie,nazwisko,placowka,klasa))
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=13)
submit_btn.config(font="Helvetica 16 bold", fg='white', pady=10, activebackground='blue')

delete_box = Entry(dodaj, width=30)
delete_box.grid(row=9, column=1)

delete_box_label = Label(dodaj, text="Numer ID")
delete_box_label.grid(row=9, column=0)
delete_box_label.config(font="Helvetica 16 bold", fg='white', pady=10)

# Create a textbox
my_text = Text(dodaj, height=30, width=60)
my_text.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# my_text.pack(pady=10)

# Clear the textbox


# Open our pdf file


# button_frame = Frame(dodaj)
# button_frame.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

get_text_button = Button(dodaj, text="Get Text", command=lambda: get_text(imie,nazwisko,placowka,klasa,my_text))
get_text_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
get_text_button.config(font="Helvetica 16 bold", fg='white', pady=10)

# Create a Delete Button
query_btn = Button(dodaj, text="Usuń Rekord", command=lambda: delete)
query_btn.grid(row=10, column=0, columnspan=2, padx=10, ipadx=13)
query_btn.config(font="Helvetica 16 bold", fg='white', pady=10)

#Commit Changes
conn.commit()
#Close Connection
conn.close()





# -----------------------------------------

#Create A menu

my_menu = Menu(app)
app.config(menu=my_menu)

#Add some dropdown menus
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text_box)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)


app.mainloop()