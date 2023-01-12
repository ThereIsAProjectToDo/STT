from tkinter import *
import PyPDF2
import tkinter
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog
from tkinter import ttk

from PIL import ImageTk, Image
import sqlite3


def clear_text_box(my_text):
    my_text.delete(1.0, END)

def open_pdf():
    # Grab the filename of the pdf file
    open_file = filedialog.askopenfilename(
       initialdir="C:/Users/Dawid/Desktop/",
       title="Open PDF file",
       filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")
        )
    )
    # Check to see if there is a file
    if open_file:
        # Open the pdf file
        pdf_file = PyPDF2.PdfReader(open_file)

        # Set the page to read
        page = pdf_file.pages[0]
        # Extract the text from the pdf file
        page_stuff = page.extract_text()

        # Add text to textbox
        my_text.insert(1.0, page_stuff)

    # -----------------------------------------

    # Grab the text ftom the text box
def get_text(imie,nazwisko,placowka,klasa,my_text):
   imie.insert(0, my_text.get(1.0, 1.9))
   nazwisko.insert(0, my_text.get(2.0, 2.9))
   placowka.insert(0, my_text.get(3.0, 3.9))
   klasa.insert(0, my_text.get(4.0, 4.9))

def submit_uczen(imie,nazwisko,placowka,klasa):
    # Create a database or connect to one
    conn = sqlite3.connect('dane_uczniow.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute(
        " INSERT INTO uczniowie (imie, nazwisko, placowka, klasa) VALUES (:imie, :nazwisko, :placowka, :klasa)",
        {
            'imie': imie.get(),
            'nazwisko': nazwisko.get(),
            'placowka': placowka.get(),
            'klasa': klasa.get()
        })


    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear The Text Boxes
    imie.delete(0, END)
    nazwisko.delete(0, END)
    placowka.delete(0, END)
    klasa.delete(0, END)

def submit_miesiac(imie,nazwisko,placowka,klasa):
    # Create a database or connect to one
    conn = sqlite3.connect('dane_uczniow.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute(
        " INSERT INTO uczniowie (imie, nazwisko, placowka, klasa) VALUES (:imie, :nazwisko, :placowka, :klasa)",
        {
            'imie': imie.get(),
            'nazwisko': nazwisko.get(),
            'placowka': placowka.get(),
            'klasa': klasa.get()
        })


    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear The Text Boxes
    imie.delete(0, END)
    nazwisko.delete(0, END)
    placowka.delete(0, END)
    klasa.delete(0, END)
def submit_odpis(imie,nazwisko,placowka,klasa):
    # Create a database or connect to one
    conn = sqlite3.connect('dane_uczniow.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute(
        " INSERT INTO uczniowie (imie, nazwisko, placowka, klasa) VALUES (:imie, :nazwisko, :placowka, :klasa)",
        {
            'imie': imie.get(),
            'nazwisko': nazwisko.get(),
            'placowka': placowka.get(),
            'klasa': klasa.get()
        })


    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear The Text Boxes
    imie.delete(0, END)
    nazwisko.delete(0, END)
    placowka.delete(0, END)
    klasa.delete(0, END)

def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('dane_uczniow.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from uczniowie WHERE oid=" + delete_box.get())

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def query_odpisy(query_label_1,query_label_2,query_label_3,query_label_4):
    # Create a database or connect to one
    conn = sqlite3.connect('dane_uczniow.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM odpisy")
    records = c.fetchall()
    print(records)

    # Loop Thru Results
    print_records = ""
    print_records_1 = "Id_Miesiaca \n"
    print_records_2 = "Id_Ucznia \n"
    print_records_3 = "DATA \n"
    print_records_4 = "Id_Odpisu \n"
    for record in records:
        # print_records += str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + "\n"
        print_records_1 += str(record[1]) + "\n"
        print_records_2 += str(record[2]) + "\n"
        print_records_3 += str(record[3]) + "\n"
        print_records_4 += str(record[0]) + "\n"
    query_label_1.config(text=print_records_1)
    query_label_2.config(text=print_records_2)
    query_label_3.config(text=print_records_3)
    query_label_4.config(text=print_records_4)


    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def query_uczniowie(query_label_1,query_label_2,query_label_3,query_label_4):
    # Create a database or connect to one
    conn = sqlite3.connect('dane_uczniow.db')
    # Create cursor
    c = conn.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM uczniowie")
    records = c.fetchall()
    print(records)

    # Loop Thru Results
    print_records = ""
    print_records_1 = "Imie \n"
    print_records_2 = "Nazwisko \n"
    print_records_3 = "Placówka \n"
    print_records_4 = "Klasa \n"
    for record in records:
        # print_records += str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + "\n"
        print_records_1 += str(record[1]) + "\n"
        print_records_2 += str(record[2]) + "\n"
        print_records_3 += str(record[3]) + "\n"
        print_records_4 += str(record[4]) + "\n"
    query_label_1.config(text=print_records_1)
    query_label_2.config(text=print_records_2)
    query_label_3.config(text=print_records_3)
    query_label_4.config(text=print_records_4)
    print("it worked")

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def query_miesiac(query_label_1,query_label_2,query_label_3,query_label_4):
    # Create a database or connect to one
    conn = sqlite3.connect('dane_uczniow.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM miesiac")
    records = c.fetchall()
    print(records)

    # Loop Thru Results
    print_records = ""
    print_records_1 = "Nazwa \n"
    print_records_2 = "Rok \n"
    print_records_3 = "Ilość dni \n"
    print_records_4 = "Kwota za dzień \n"
    for record in records:
        #print_records += str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + "\n"
        print_records_1 += str(record[1]) + "\n"
        print_records_2 += str(record[2]) + "\n"
        print_records_3 += str(record[3]) + "\n"
        print_records_4 += str(record[4]) + "\n"
    query_label_1.config(text=print_records_1)
    query_label_2.config(text=print_records_2)
    query_label_3.config(text=print_records_3)
    query_label_4.config(text=print_records_4)



    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def query_szukaj(szukaj,query_label_1,query_label_2,query_label_3,query_label_4):
    conn = sqlite3.connect('dane_uczniow.db')
    # Create cursor
    c = conn.cursor()
    c.execute(
        "SELECT * FROM Uczniowie WHERE imie=?",(szukaj.get(),))
    records = c.fetchall()
    print(records)

    print_records_1 = "Imie \n"
    print_records_2 = "Nazwisko \n"
    print_records_3 = "Placówka \n"
    print_records_4 = "Klasa \n"
    for record in records:
        # print_records += str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + "\n"
        print_records_1 += str(record[1]) + "\n"
        print_records_2 += str(record[2]) + "\n"
        print_records_3 += str(record[3]) + "\n"
        print_records_4 += str(record[4]) + "\n"
    query_label_1.config(text=print_records_1)
    query_label_2.config(text=print_records_2)
    query_label_3.config(text=print_records_3)
    query_label_4.config(text=print_records_4)


    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()