import pyttsx3 as pt
import PyPDF2

pdf = open('Mastering-Python.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf)
pages = reader.numPages
print("Total numbers of pages: ", pages)
speak = pt.init()
for txt in range(72, pages):
    words = reader.getPage(72)
    text = words.extractText()
    speak.say(text)
    speak.runAndWait()

