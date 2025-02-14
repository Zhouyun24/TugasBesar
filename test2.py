import csv

data = [['Ayu'], ['Budi'], ['Citra'],['Jono'],['budi']]

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Menulis header
    writer.writerow(['No', 'Nama'])

    # Menulis data dengan nomor otomatis
    for i, row in enumerate(data, start=1):
        writer.writerow([i] + row)
