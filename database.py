from tkinter import *
import PyPDF2
import tkinter
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog
from tkinter import ttk

from PIL import ImageTk, Image
import sqlite3




# Create a database or connect to one
conn = sqlite3.connect('dane_uczniow.db')

#Create cursor
c = conn.cursor()

c.execute("""
CREATE TABLE uczniowie(
        id_ucznia INTEGER PRIMARY KEY AUTOINCREMENT,
        imie text NOT NULL,
        nazwisko text NOT NULL,
        placowka text NOT NULL,
        klasa text not NULL)
""")
#done
c.execute("""
CREATE TABLE miesiac(
        id_miesiaca INTEGER PRIMARY KEY AUTOINCREMENT,
        nazwa text NOT NULL,
        rok text NOT NULL,
        ilosc_dni_do_zaplaty real,
        kwota_za_dzien real)
""")
#done
c.execute("""
CREATE TABLE nr_konta(
        nr_konta INTEGER PRIMARY KEY )
""")


c.execute("""
CREATE TABLE naleznosc(
       id_naleznosci INTEGER PRIMARY KEY AUTOINCREMENT,
       id_miesiaca INTEGER NOT NULL,
       id_ucznia INTEGER NOT NULL,
       kwota REAL NOT NULL,
       FOREIGN KEY (id_miesiaca) REFERENCES miesiac (id_miesiaca),
       FOREIGN KEY (id_ucznia) REFERENCES uczen (id_ucznia))
""")
c.execute("""
CREATE TABLE odpisy(
       id_odpisu INTEGER PRIMARY KEY AUTOINCREMENT,
       id_miesiaca INTEGER NOT NULL,
       id_ucznia INTEGER NOT NULL,
       Data DATE NOT NULL,
       FOREIGN KEY (id_miesiaca) REFERENCES miesiac (id_miesiaca),
       FOREIGN KEY (id_ucznia) REFERENCES uczen (id_ucznia))
""")
c.execute("""
CREATE TABLE transakcje(
       id_transakcji INTEGER PRIMARY KEY AUTOINCREMENT,
       nr_konta INTEGER NOT NULL,
       kwota REAL NOT NULL,
       Data DATE NOT NULL,
       FOREIGN KEY (nr_konta) REFERENCES nr_konta (nr_konta))
""")
c.execute("""
CREATE TABLE konto_uczen(
       nr_konta INTEGER NOT NULL,
       id_ucznia INTEGER NOT NULL,
       FOREIGN KEY (nr_konta) REFERENCES nr_konta (nr_konta),
       FOREIGN KEY (id_ucznia) REFERENCES uczen (id_ucznia))
""")
