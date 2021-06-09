# Importing All Python Library
from tkinter import*
import PyPDF2
import pyttsx3
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as Pdf
# Initializing tk
root = Tk()
root.title('PDF VIEWER & READER')
# Set the width and height of our root window.
root.geometry("550x750")
# welcome banner
Label(root, text="Welcome to PDF Viewer and Reader", font="comicsansms 13 bold").pack()



# open our pdf files


def open_pdf():
    # creating object of ShowPdf from tkPDFViewer.
    v1 = Pdf.ShowPdf()

    # Adding pdf location and width and height.
    v2 = v1.pdf_view(root,
                     pdf_location=filedialog.askopenfilename(
                         title="Open PDF File",
                         filetypes=(
                             ("PDF Files", "*.pdf"),
                             ("All Files", "*.*"))),
                     width=80, height=100)
    v2.pack()




# reader for pdf


def run_pdf():
    openpdf = filedialog.askopenfilename(
        title="Open PDF File",
        filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")))
    pdf_file = PyPDF2.PdfFileReader(openpdf)
    for n in range(pdf_file.getNumPages()):
        page = pdf_file.getPage(n)
        page_contain = page.extractText()
        speaker = pyttsx3.init()
        speaker.say(page_contain)
        speaker.runAndWait()


# create a menu

my_menu = Menu(root)
root.config(menu=my_menu)
# add some dropdown menus
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Run", command=run_pdf)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)



root.mainloop()
