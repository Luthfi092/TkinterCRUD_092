import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv

DB_FILE = 'nilai_siswa.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi REAL NOT NULL,
            fisika REAL NOT NULL,
            inggris REAL NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(nama, bio, fis, ing, prediksi):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, bio, fis, ing, prediksi))
    conn.commit()
    conn.close()

def update_data(id_val, nama, bio, fis, ing, prediksi):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE nilai_siswa
        SET nama_siswa=?, biologi=?, fisika=?, inggris=?, prediksi_fakultas=?
        WHERE id=?
    ''', (nama, bio, fis, ing, prediksi, id_val))
    conn.commit()
    conn.close()

def delete_data(id_val):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM nilai_siswa WHERE id=?', (id_val,))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nama_siswa, biologi, fisika, inggris, prediksi_fakultas FROM nilai_siswa ORDER BY id DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows

def predict_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        max_val = max(biologi, fisika, inggris)
        if biologi == max_val:
            return "Kedokteran"
        elif fisika == max_val:
            return "Teknik"
        else:
            return "Bahasa"

class NilaiApp:
    def __init__(self, root):
        self.root = root
        root.title('Input Nilai Siswa - SQLite')
        root.geometry('900x520')
        root.minsize(800, 480)

        style = ttk.Style()
        try:
            style.theme_use('clam')
        except Exception:
            pass

        style.configure('TLabel', font=('Segoe UI', 10))
        style.configure('TButton', font=('Segoe UI', 10), padding=6)
        style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'))
        style.configure('Treeview.Heading', font=('Segoe UI', 11, 'bold'))
        style.configure('Treeview', font=('Segoe UI', 10))

        frm_left = ttk.LabelFrame(root, text='Form Input', padding=(12, 12))
        frm_left.grid(row=0, column=0, sticky='nw', padx=12, pady=12)

        frm_right = ttk.LabelFrame(root, text='Data Tersimpan', padding=(8, 8))
        frm_right.grid(row=0, column=1, sticky='nsew', padx=12, pady=12)

        ttk.Label(frm_left, text='Nama Siswa:', style='Header.TLabel').grid(row=0, column=0, sticky='w')
        self.entry_nama = ttk.Entry(frm_left, width=34)
        self.entry_nama.grid(row=1, column=0, pady=6, sticky='w')

        lbl_nilai = ttk.Label(frm_left, text='Nilai (0-100):', style='Header.TLabel')
        lbl_nilai.grid(row=2, column=0, sticky='w', pady=(8, 0))

        inner = ttk.Frame(frm_left)
        inner.grid(row=3, column=0, sticky='w')
        ttk.Label(inner, text='Biologi').grid(row=0, column=0, padx=(0, 6))
        self.entry_bio = ttk.Entry(inner, width=8)
        self.entry_bio.grid(row=0, column=1, padx=(0, 12))

        ttk.Label(inner, text='Fisika').grid(row=0, column=2, padx=(0, 6))
        self.entry_fis = ttk.Entry(inner, width=8)
        self.entry_fis.grid(row=0, column=3, padx=(0, 12))

        ttk.Label(inner, text='Inggris').grid(row=0, column=4, padx=(0, 6))
        self.entry_ing = ttk.Entry(inner, width=8)
        self.entry_ing.grid(row=0, column=5)

     