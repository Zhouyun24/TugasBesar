import csv
import os

csv_filename = 'data_mahasiswa22.csv'

#Manampilkan Menu Utama
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

#Kemablai Ke Menu Utama
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

#Membuat Agar Input Tidak Boleh Kososng
def input_tidak_kosong(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong! Silakan coba lagi.")


#Menampilkan Data Mahasiswa
def show_mahasiswa():
    if not os.path.exists(csv_filename):
        print("Tidak ada data!")
        back_to_menu()
        return

    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=",")
        data_mahasiswa = list(csv_reader)

    if len(data_mahasiswa) > 0:
        header = ["No", "Nama", "Email"]
        print(f"{header[0]} \t {header[1]} \t {header[2]}")
        print("-" * 50)

        for idx, data in enumerate(data_mahasiswa[1:], 1):
            print(f"{idx} \t {data[0]} \t {data[1]}")

    else:
        print("Tidak ada data!")
    print("-" * 50)
    back_to_menu()


#Membuat Data Mahasiswa Baru
def create_mahasiswa():
    validasi = input("Ingin Melanjutkan Membuat Data? (Y/T): ").upper()
    if validasi == 'T':
        show_menu()

    nama = input_tidak_kosong('Nama  : ')
    email = input_tidak_kosong('Email : ')

    with open(csv_filename, 'a', newline='') as csv_data:
        writer = csv.writer(csv_data)
        if not os.path.exists(csv_filename) or os.stat(csv_filename).st_size == 0:
            writer.writerow(['Nama', 'Email'])
        writer.writerow([nama, email])

    print("\nData berhasil ditambahkan!")
    back_to_menu()


#Menghapus Data Mahasiswa
def delete_mahasiswa():
    if not os.path.exists(csv_filename):
        print("Tidak ada data untuk dihapus!")
        back_to_menu()
        return

    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=",")
        data_mahasiswa = list(csv_reader)

    if len(data_mahasiswa) > 0:
        header = ["No", "Nama", "Email"]
        print(f"{header[0]} \t {header[1]} \t {header[2]}")
        print("-" * 50)

        for idx, data in enumerate(data_mahasiswa[1:], 1):
            print(f"{idx} \t {data[0]} \t {data[1]}")

    print("-" * 50)
    nomor_hapus = int(input_tidak_kosong("Masukkan No mahasiswa yang ingin dihapus (Masukan 0 Jika Tidak Mau Hapus): "))

    with open(csv_filename, 'r', newline='') as csv_data:
        data_mahasiswa = list(csv.reader(csv_data))

    if nomor_hapus < 0 or nomor_hapus >= len(data_mahasiswa):
        print("Nomor mahasiswa tidak valid!")
        ulang = input("Ingin Mengulang?(Y/T)").upper()
        if (ulang == "Y"):
            delete_mahasiswa()
        else:
            show_menu()
    elif (nomor_hapus == 0):
        show_menu()
    else:
        data_mahasiswa.pop(nomor_hapus)

        with open(csv_filename, 'w', newline='') as csv_data:
            csv_writer = csv.writer(csv_data)
            csv_writer.writerows(data_mahasiswa)

        print("Data mahasiswa berhasil dihapus!")

    back_to_menu()


#Mengubah Data Mahasiwa
def edit_mahasiswa():
    if not os.path.exists(csv_filename):
        print("Tidak ada data untuk diedit!")
        back_to_menu()
        return

    with open(csv_filename, 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=",")
        data_mahasiswa = list(csv_reader)

    if len(data_mahasiswa) > 0:
        header = ["No", "Nama", "Email"]
        print(f"{header[0]} \t {header[1]} \t {header[2]}")
        print("-" * 50)

        for idx, data in enumerate(data_mahasiswa[1:], 1):
            print(f"{idx} \t {data[0]} \t {data[1]}")

    print("-" * 50)

    nomor_edit = int(input_tidak_kosong("Masukkan No mahasiswa yang ingin diedit (Masukan 0 Jika Tidak Mau Edit): "))

    with open(csv_filename, 'r', newline='') as csv_data:
        data_mahasiswa = list(csv.reader(csv_data))

    if nomor_edit < 0 or nomor_edit >= len(data_mahasiswa):
        print("Nomor mahasiswa tidak valid!")
    elif (nomor_edit == 0):
        show_menu()
    else:
        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
        new_nama = input(f"Nama ({data_mahasiswa[nomor_edit][0]}): ").strip() or data_mahasiswa[nomor_edit][0]
        new_email = input(f"Email ({data_mahasiswa[nomor_edit][1]}): ").strip() or data_mahasiswa[nomor_edit][1]

        data_mahasiswa[nomor_edit] = [new_nama, new_email]

        with open(csv_filename, 'w', newline='') as csv_data:
            csv_writer = csv.writer(csv_data)
            csv_writer.writerows(data_mahasiswa)

        print("Data mahasiswa berhasil diperbarui!")

    back_to_menu()


#Mencari Data Mahasiswa (berdasarkan Nama/Email)
def search_mahasiswa():
    if not os.path.exists(csv_filename):
        print("Tidak ada data untuk dicari!")
        back_to_menu()
        return

    print("\n=== Pencarian Data Mahasiswa ===")
    print("[1] Berdasarkan Keseluruhan Data (Nama/Email)")
    print("[2] Berdasarkan Sebagian Kata (Mengandung kata tertentu)")
    pilihan = input_tidak_kosong("Pilih jenis pencarian (1/2): ")

    keyword = input_tidak_kosong("Masukkan kata kunci pencarian: ").lower()

    with open(csv_filename, 'r', newline='') as csv_data:
        data_mahasiswa = list(csv.reader(csv_data))

    header = ["No", "Nama", "Email"]
    hasil_pencarian = []

    for idx, row in enumerate(data_mahasiswa[1:], 1):
        if pilihan == '1' and keyword in ' '.join(row).lower():
            hasil_pencarian.append((idx, row))
        elif pilihan == '2' and any(keyword in item.lower() for item in row):
            hasil_pencarian.append((idx, row))

    if hasil_pencarian:
        print(f"\n{' | '.join(header)}")
        print("-" * 50)
        for idx, data in hasil_pencarian:
            print(f"{idx} | {data[0]} | {data[1]}")
    else:
        print("\nData tidak ditemukan!")

    back_to_menu()


#Mengurutkan Data Mahasiswa
def sort_mahasiswa():
    if not os.path.exists(csv_filename):
        print("Tidak ada data untuk diurutkan!")
        back_to_menu()
        return

    print("\n=== Pengurutan Data Mahasiswa ===")
    print("[1] Berdasarkan Nama (A-Z)")
    print("[2] Berdasarkan Nama (Z-A)")
    print("[3] Berdasarkan Email (A-Z)")
    print("[4] Berdasarkan Email (Z-A)")
    pilihan = input_tidak_kosong("Pilih metode pengurutan (1-4): ")

    with open(csv_filename, 'r', newline='') as csv_data:
        data_mahasiswa = list(csv.reader(csv_data))

    header = data_mahasiswa[0]
    data = data_mahasiswa[1:]

    if pilihan == '1':
        data.sort(key=lambda x: x[0].lower())  # Nama A-Z
    elif pilihan == '2':
        data.sort(key=lambda x: x[0].lower(), reverse=True)  # Nama Z-A
    elif pilihan == '3':
        data.sort(key=lambda x: x[1].lower())  # Email A-Z
    elif pilihan == '4':
        data.sort(key=lambda x: x[1].lower(), reverse=True)  # Email Z-A
    else:
        print("Pilihan tidak valid!")
        back_to_menu()
        return

    print("\nNo | Nama | Email")
    print("-" * 50)
    for idx, row in enumerate(data, 1):
        print(f"{idx} | {row[0]} | {row[1]}")

    back_to_menu()


if __name__ == "__main__":
    show_menu()