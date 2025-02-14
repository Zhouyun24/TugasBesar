import csv

# Data contoh
data = [
    ["Nama", "NIM", "Email"],
    ["Andi Saputra", "2301001", "andi.saputra@email.com"],
    ["Budi Santoso", "2301002", "budi.santoso@email.com"],
    ["Citra Lestari", "2301003", "citra.lestari@email.com"],
    ["Dewi Anggraini", "2301004", "dewi.anggraini@email.com"],
    ["Eko Prasetyo", "2301005", "eko.prasetyo@email.com"],
    ["Farah Maulida", "2301006", "farah.maulida@email.com"],
    ["Gilang Ramadhan", "2301007", "gilang.ramadhan@email.com"],
    ["Hani Salsabila", "2301008", "hani.salsabila@email.com"],
    ["Indra Kusuma", "2301009", "indra.kusuma@email.com"],
    ["Joko Widodo", "2301010", "joko.widodo@email.com"],
]

# Nama file CSV
file_path = "data_mahasiswa22.csv"

# Menulis data ke file CSV
with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

