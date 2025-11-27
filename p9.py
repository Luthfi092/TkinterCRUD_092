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





