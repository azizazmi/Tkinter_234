#Mengimpor tkinter sebagai library untuk membuat aplikasi berbasis GUI
import tkinter as tk
#Mengimpor messagebox untuk menampilkan pop-up error message
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try: 
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

#Membuat jendela utama dengan judul "Aplikasi Prediksi Prodi Pilihan" dan ukuran 500x600 piksel
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
#digunakan untuk mengatur warna background jendela utama
root.configure(bg="#b8a2ac")

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#b86776", fg="#f0f0f0")
judul_label.pack(pady=20)

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#b86776")
frame_input.pack(pady=10)

#Menambahkan 10 label untuk menyimpan nilai sesuai dengan yang diminta di soal untuk menginput 10 nilai mata pelajaran
entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#b86776", fg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12), fg="#b86776")
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

#Membuat tombol prediksi_button untuk memicu fungsi saat tombol ditekan
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#b86776", fg="white")
prediksi_button.pack(pady=30)

#Membuat perintah untuk menampilkan hasil prediksi setelah semua nilai yang diinput divalidasi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="#f0f0f0", bg="#b86776")
hasil_label.pack(pady=20)

#Memulai mainloop dari tkinter untuk menjalankan GUI dan menunggu interaksi pengguna
root.mainloop()