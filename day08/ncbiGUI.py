import tkinter as tk
from Bio import Entrez
import csv
from datetime import datetime
import os

# GUI ok button function with search and save functions applyed 
def btnOk_clicked():
    global database_chosen, search_term_chosen, number_items_chosen
    
    # getting the interface parameters
    database_chosen = clicked.get()
    search_term_chosen = search_term.get()
    number_items_chosen = int(spinNumber.get())  # converting into integer

    # printing out the search info
    print(f"Database: {database_chosen}, Term: {search_term_chosen}, Max Results: {number_items_chosen}")
    
    # starting the search
    data_search, id_data = data_search_function()
    download_and_save_data(id_data)
    save_in_csv(data_search)

    # closing the window
    window.destroy()


def btnCancel_clicked():
    window.destroy()

def data_search_function():
    Entrez.email = "dubovetskiy.artem@gmail.com"
    handle = Entrez.esearch(db=database_chosen, term=search_term_chosen, idtype='acc', retmax=number_items_chosen)
    data_search = Entrez.read(handle)
    id_data = data_search['IdList']
    handle.close()
    return data_search, id_data

def download_and_save_data(id_data):
    for i in range(len(id_data)):
        handle = Entrez.efetch(db=database_chosen, id=id_data[i], rettype="gb", retmode='text')
        data = handle.read()
        handle.close()
        filename = f"{id_data[i]}.data"
        print(f"Saving to file: {filename}")
        with open(filename, 'w') as fh:
            fh.write(data)

def save_in_csv(data_search):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    data_for_csv = [date_time, database_chosen, search_term_chosen, number_items_chosen, data_search['Count']]
    
    file_exists = os.path.exists('csv_data_file.csv')
    try:
        if file_exists:
            with open('csv_data_file.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data_for_csv)
        else:
            with open('csv_data_file.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['date time', 'database', 'term', 'max', 'total'])
                writer.writerow(data_for_csv)
    except PermissionError:
        print('!Please close your "csv_data_file.csv" file before starting this script!')
        exit()

# GUI setup
window = tk.Tk()
window.title('NCBI search')
window.geometry('350x300')
window.tk.call('tk', 'scaling', 2.0)

# Create the label frame for database selection
database_frame = tk.LabelFrame(window, text='Choose the database', padx=5, pady=5)
database_frame.pack(padx=10, pady=10)

# select database menu
clicked = tk.StringVar()
clicked.set('nucleotide')
drop_database = tk.OptionMenu(database_frame, clicked, 'nucleotide', 'gene', 'protein')
drop_database.grid(column=0, row=0)

# Search term entry
search_lbl = tk.Label(window, text="Choose the term for search")
search_lbl.pack()
search_term = tk.Entry(window)
search_term.pack()

# Spinbox for number of items to search (till 20)
number_lbl = tk.Label(window, text="Choose the maximum number of items")
number_lbl.pack()
spinNumber = tk.Spinbox(window, from_=1, to=20)
spinNumber.pack()

# Ok and cancel buttons
buttons_frame = tk.LabelFrame(window, padx=5, pady=5)
buttons_frame.pack(padx=10, pady=10)

btnOk = tk.Button(buttons_frame, text='Ok', command=btnOk_clicked)
btnOk.grid(column=0, row=0)
btnCancel = tk.Button(buttons_frame, text='Cancel', command=btnCancel_clicked)
btnCancel.grid(column=2, row=0)

window.mainloop()