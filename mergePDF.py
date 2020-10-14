#! /usr/bin/python3
#Drucken: Erst ungerade Seiten drucken. Seiten so herausnehmen, dass man die
#unbedruckte Seite vor sich sieht, oben aber oben bleibt. Dann um 180° nach
#rechts drehen. Dann gerade Seiten drucken. Oder gleich an langer Kante
#spiegeln, falls möglich.

from tkinter import filedialog, messagebox, Tk
from PyPDF2 import PdfFileMerger
import os

def get_pdfs():
    files = []

    while True:
        file = filedialog.askopenfilename(title='PDF auswählen',
                                          filetypes=[('PDF-Dateien', '*.pdf')])
        if file:
            files.append(file)
        else:
            break
    return files

def get_destination():
    destination = filedialog.asksaveasfilename(
        title='Speicherort auswählen',
        filetypes=[('PDF-Dateien', '*.pdf')])
    if not destination:
        messagebox.showwarning(
            title='Warnung',
            message='Da kein Dateiname festgelegt wurde, wird'\
                    ' result.pdf genommen.')
        destination = os.path.join(os.getcwd(), 'result.pdf')

    elif not destination.endswith('.pdf'):
        destination += '.pdf'
    return destination

def merge(files, destination):
    merger = PdfFileMerger()

    for file in files:
        merger.append(file)

    merger.write(destination)
    merger.close()

if __name__ == '__main__':
    root = Tk()
    files = get_pdfs()
    if files:
        destination = get_destination()
        merge(files, destination)
    root.destroy()
