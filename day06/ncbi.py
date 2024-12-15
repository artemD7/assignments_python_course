import argparse
from Bio import Entrez
import csv
from datetime import datetime
import os

# Taking variables from the terminal
def arg_parse_function():
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', type=str, default='nucleotide', help="database type (default = nucleotide)")
    parser.add_argument('--term',help='Term', required =True, type=str)
    parser.add_argument('--number', type=int, default=10, help="max number (default = 10)")
    args = parser.parse_args()
    return args

# Searching in the database
def data_search(args):
    Entrez.email = "dubovetskiy.artem@gmail.com"
    handle = Entrez.esearch(db = args.database, term = args.term, idtype = 'acc', retmax = args.number) 
    data_search = Entrez.read(handle)
    id_data = data_search['IdList']
    handle.close()
    return data_search,id_data

# Downloading from the database and saving into the files
def download_and_save_data(args, id_data):
    for i in range(len(id_data)):
            handle = Entrez.efetch(db = args.database, id = id_data[i], rettype = "gb", retmode = 'text' )
            data = handle.read()
            handle.close()
            filename = f"{id_data[i]}.data"
            print(f"{id_data[i]}.data")
            with open(filename, 'w') as fh:
                    fh.write(data)

# Saving in csv file
def save_in_csv(args, data_search):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    data_for_csv = [date_time, args.database, args.term, args.number, data_search['Count']]
    file_exists = os.path.exists('csv_data_file.csv')
    try:
        if file_exists:
            with open ('csv_data_file.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(data_for_csv)
        else: 
            with open ('csv_data_file.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['date time', 'database', 'term', 'max', 'total'])
                writer.writerow(data_for_csv)
    except PermissionError:
          print('!Please close your "csv_data_file.csv" file before starting this script!')
          exit()

args = arg_parse_function()
data_search, id_data = data_search(args)
download_and_save_data(args, id_data)
save_in_csv(args, data_search)