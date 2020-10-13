#! python3

from tkinter import filedialog
from PyPDF2 import PdfFileMerger

files = []

while True:
    file = filedialog.askopenfilename(title='PDF auswählen',
                                      filetypes=[('PDF-Dateien', '*.pdf')])
    if file:
        files.append(file)
    else:
        break

destination = filedialog.asksaveasfilename(title='Speicherort auswählen',
                                           filetypes=[('PDF-Dateien', '*.pdf')])
if not destination.endswith('.pdf'):
    destination += '.pdf'

merger = PdfFileMerger()

for file in files:
    merger.append(file)

merger.write(destination)
merger.close()
