import csv
import os

csv_filename = 'data_mahasiswa.csv'


# Menampilkan Menu Utama
def show_menu():
    print("\n==== Aplikasi Mahasiswa ====")
    print("[1] Lihat Daftar Mahasiswa")
    print("[2] Buat Data Mahasiswa Baru")
    print("[3] Edit Data Mahasiswa")
    print("[4] Hapus Data Mahasiswa")
    print("[5] Pencarian Data Mahasiswa")
    print("[6] Pengurutan Data Mahasiswa")
    print("[0] Keluar")
    print('-' * 30)

    select_menu = input("Pilih Menu (Dalam Bentuk Angka): ")

    if select_menu == '1':
        show_mahasiswa()
    elif select_menu == '2':
        create_mahasiswa()
    elif select_menu == '3':
        edit_mahasiswa()
    elif select_menu == '4':
        delete_mahasiswa()
    elif select_menu == '5':
        search_mahasiswa()
    elif select_menu == '6':
        sort_mahasiswa()
    elif select_menu == '0':
        exit()
    else:
        print("Menu Tidak Ada!")
        back_to_menu()

#Fitur Kembali Ke Menu
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


# Menampilkan Data Mahasiswa
def show_mahasiswa():

    data_mahasiswa = []

    # Validasi File
    if not os.path.exists(csv_filename):
        print("Tidak ada data!")
        back_to_menu()
        return

    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=",")

        for line in csv_reader:
            if len(line) == 4: # Banyak Baris yang di proses
                data_mahasiswa.append(line)

    if len(data_mahasiswa) > 0:
        labels = data_mahasiswa.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t {labels[2]} \t {labels[3]}")
        print("-" * 50)
        for data in data_mahasiswa:
            print(f"{data[0]} \t {data[1]} \t {data[2]} \t {data[3]}")
    else:
        print("Tidak ada data!")
    back_to_menu()


# Fungsi untuk memastikan input tidak kosong
def input_tidak_kosong(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong! Silakan coba lagi.")


# Membuat Data Mahasiswa dengan nomor urut otomatis
def create_mahasiswa():
    # Validasi File
    file_exists = os.path.exists(csv_filename)

    nomor_urut = 1
    if file_exists:
        with open(csv_filename, 'r', newline='') as csv_data:
            csv_reader = csv.reader(csv_data)
            data_list = list(csv_reader)
            if len(data_list) > 1:
                nomor_urut = len(data_list)

    with open(csv_filename, 'a', newline='') as csv_data:
        fieldnames = ['No', 'Nama', 'NIM', 'Email']
        writer = csv.DictWriter(csv_data, fieldnames=fieldnames)

        if not file_exists or os.stat(csv_filename).st_size == 0:
            writer.writeheader()

        nama = input_tidak_kosong('Nama  : ')
        nim = input_tidak_kosong('NIM   : ')
        email = input_tidak_kosong('Email : ')

        writer.writerow({'No': nomor_urut, 'Nama': nama, 'NIM': nim, 'Email': email})

    print("\nData berhasil ditambahkan!")
    back_to_menu()


# Menghapus Data Mahasiswa dan Memperbaiki Nomor Urut
def delete_mahasiswa():
    if not os.path.exists(csv_filename):
        print("Tidak ada data untuk dihapus!")
        back_to_menu()
        return

    data_mahasiswa = []

    # Validasi File
    if not os.path.exists(csv_filename):
        print("Tidak ada data!")
        back_to_menu()
        return

    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=",")

        for line in csv_reader:
            if len(line) == 4:  # Banyak Baris yang di proses
                data_mahasiswa.append(line)

    if len(data_mahasiswa) > 0:
        labels = data_mahasiswa.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t {labels[2]} \t {labels[3]}")
        print("-" * 50)
        for data in data_mahasiswa:
            print(f"{data[0]} \t {data[1]} \t {data[2]} \t {data[3]}")
    print("-" * 50)
    nomor_hapus = input_tidak_kosong("Masukkan No mahasiswa yang ingin dihapus: ")


    # Baca semua data dari CSV
    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data)
        data_mahasiswa = list(csv_reader)

    header = data_mahasiswa[0]
    data_mahasiswa = [row for row in data_mahasiswa[1:] if row[0] != nomor_hapus]  # Hapus data yang sesuai

    if len(data_mahasiswa) + 1 == len(header):
        print("Nomor mahasiswa tidak ditemukan!")
    else:
        # Perbaiki nomor urut
        for i, row in enumerate(data_mahasiswa, start=1):
            row[0] = str(i)


        with open(csv_filename, 'w', newline='') as csv_data:
            csv_writer = csv.writer(csv_data)
            csv_writer.writerow(header)
            csv_writer.writerows(data_mahasiswa)

        print("Data mahasiswa berhasil dihapus dan nomor urut diperbarui!")

    back_to_menu()

# Mengedit Data Mahasiswa Berdasarkan Nomor Urut
def edit_mahasiswa():
    if not os.path.exists(csv_filename):
        print("Tidak ada data untuk diedit!")
        back_to_menu()
        return

    data_mahasiswa = []

    # Validasi File
    if not os.path.exists(csv_filename):
        print("Tidak ada data!")
        back_to_menu()
        return

    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=",")

        for line in csv_reader:
            if len(line) == 4:  # Banyak Baris yang di proses
                data_mahasiswa.append(line)

    if len(data_mahasiswa) > 0:
        labels = data_mahasiswa.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t {labels[2]} \t {labels[3]}")
        print("-" * 50)
        for data in data_mahasiswa:
            print(f"{data[0]} \t {data[1]} \t {data[2]} \t {data[3]}")

    print("-"*30)
    nomor_edit = input_tidak_kosong("Masukkan No mahasiswa yang ingin diedit: ")


    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data)
        data_mahasiswa = list(csv_reader)

    header = data_mahasiswa[0]
    found = False

    for i in range(1, len(data_mahasiswa)):
        if data_mahasiswa[i][0] == nomor_edit:
            print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")

            new_nama = input(f"Nama ({data_mahasiswa[i][1]}): ").strip() or data_mahasiswa[i][1]
            new_nim = input(f"NIM ({data_mahasiswa[i][2]}): ").strip() or data_mahasiswa[i][2]
            new_email = input(f"Email ({data_mahasiswa[i][3]}): ").strip() or data_mahasiswa[i][3]

            data_mahasiswa[i] = [nomor_edit, new_nama, new_nim, new_email]
            found = True
            break

    if not found:
        print("Nomor mahasiswa tidak ditemukan!")
    else:
        with open(csv_filename, 'w', newline='') as csv_data:
            csv_writer = csv.writer(csv_data)
            csv_writer.writerow(header)  # Tulis header kembali
            csv_writer.writerows(data_mahasiswa)  # Tulis data yang diperbarui

        print("Data mahasiswa berhasil diperbarui!")

    back_to_menu()


import csv
import os

csv_filename = 'data_mahasiswa.csv'


# Pencarian Data Mahasiswa
def search_mahasiswa():
    if not os.path.exists(csv_filename):
        print("Tidak ada data untuk dicari!")
        back_to_menu()
        return

    print("\n=== Pencarian Data Mahasiswa ===")
    print("[1] Berdasarkan Keseluruhan Data (Nama/NIM/Email)")
    print("[2] Berdasarkan Sebagian Kata (Mengandung kata tertentu)")
    pilihan = input_tidak_kosong("Pilih jenis pencarian (1/2): ")

    keyword = input_tidak_kosong("Masukkan kata kunci pencarian: ").lower()

    data_mahasiswa = []

    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data)
        data_mahasiswa = list(csv_reader)

    header = data_mahasiswa[0]
    hasil_pencarian = []

    for row in data_mahasiswa[1:]:
        if pilihan == '1' and keyword in row:
            hasil_pencarian.append(row)
        elif pilihan == '2' and any(keyword in item.lower() for item in row):
            hasil_pencarian.append(row)

    if hasil_pencarian:
        print(f"\n{' | '.join(header)}")
        print("-" * 50)
        for data in hasil_pencarian:
            print(" | ".join(data))
    else:
        print("\nData tidak ditemukan!")

    back_to_menu()


#  Pengurutan Data Mahasiswa
def sort_mahasiswa():
    if not os.path.exists(csv_filename):
        print("Tidak ada data untuk diurutkan!")
        back_to_menu()
        return

    print("\n=== Pengurutan Data Mahasiswa ===")
    print("[1] Berdasarkan Nama (A-Z)")
    print("[2] Berdasarkan Nama (Z-A)")
    print("[3] Berdasarkan NIM (Kecil ke Besar)")
    print("[4] Berdasarkan NIM (Besar ke Kecil)")
    pilihan = input_tidak_kosong("Pilih metode pengurutan (1-4): ")

    data_mahasiswa = []
    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data)
        data_mahasiswa = list(csv_reader)

    header = data_mahasiswa[0]
    data_mahasiswa = data_mahasiswa[1:]

    if pilihan == '1':
        data_mahasiswa.sort(key=lambda x: x[1].lower())  # Nama A-Z
    elif pilihan == '2':
        data_mahasiswa.sort(key=lambda x: x[1].lower(), reverse=True)  # Nama Z-A
    elif pilihan == '3':
        data_mahasiswa.sort(key=lambda x: int(x[2]))  # NIM kecil ke besar
    elif pilihan == '4':
        data_mahasiswa.sort(key=lambda x: int(x[2]), reverse=True)  # NIM besar ke kecil
    else:
        print("Pilihan tidak valid!")
        back_to_menu()
        return

    print(f"\n{' | '.join(header)}")
    print("-" * 50)
    for data in data_mahasiswa:
        print(" | ".join(data))

    back_to_menu()


# Jalankan program
show_menu()
