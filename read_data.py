import csv

with open('data_mahasiswa22.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data_list = list(csv_reader)
    data_len = len(data_list)

print(data_len)