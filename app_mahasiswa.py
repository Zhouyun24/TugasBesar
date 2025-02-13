import csv

csv_filename = 'data_mahasiswa.csv'

#Menampilkan Menu(Fitur-fiturnya)
def show_menu():
    print('==== Aplikasi Mahasiswa ====')
    print('[1] Lihat Daftar Mahasiswa')
    print('[2] Buat Data Mahasiswa Baru')
    print('[3] Edit Data Mahasiswa')
    print('[4] Hapus Data Mahasiswa')
    print('[0] Exit')
    print('-'*30)
    select_menu = input('Pilih Menu (Dalam Bentuk Angka) : ')

    if(select_menu == '1'):
        show_mahasiswa()
    elif(select_menu == '2'):
        create_mahasiswa()
    elif(select_menu == '0'):
        exit()
    else:
        print('Menu Tidak Ada')
        back_to_menu()


#Kembali Ke Menu
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


#Menampilkan Data Mahasiswa
def show_mahasiswa():
    data_mahasiswa=[]
    with open(csv_filename , 'r', newline='') as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=",")

        for line in csv_reader:
            if len(line) == 3:  # Pastikan hanya baris dengan 3 elemen yang diproses
                data_mahasiswa.append(line)

    if (len(data_mahasiswa) > 0):
        labels = data_mahasiswa.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
        print("-"*34)
        for data in data_mahasiswa:
            print(f'{data[0]} \t {data[1]} \t {data[2]}')
    else:
        print("Tidak ada data!")
    back_to_menu()


# Fungsi untuk memastikan input tidak kosong
def input_tidak_kosong(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
        print("Input tidak boleh kosong! Silakan coba lagi.")

# Membuat Data Mahasiswa
def create_mahasiswa():
    with open(csv_filename, 'a', newline='') as csv_data:
        data_mahasiswa = ['Nama', 'NIM', 'Email']
        writer = csv.DictWriter(csv_data, fieldnames=data_mahasiswa)

        nama = input_tidak_kosong('Nama  : ')
        nim = input_tidak_kosong('NIM   : ')
        email = input_tidak_kosong('Email : ')

        writer.writerow({'Nama': nama, 'NIM': nim, 'Email': email})

    back_to_menu()

show_menu()