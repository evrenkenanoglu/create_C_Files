import tkinter as tk
from tkinter import messagebox
import datetime  

date = datetime.date.today().strftime("%d/%m/%Y")
yearNow = datetime.date.today().year
tempCFile = "_createFile_c"
tempHFile = "_createFile_h"

windowWidth = 300
windowHeigth = 250
incrementHeight = 30
firstElementPositionHeight = 25
elementHeightPosition = firstElementPositionHeight

root= tk.Tk()
root.title("Create C File")
canvas1 = tk.Canvas(root, width = windowWidth, height = windowHeigth)
canvas1.pack()

# messageBox = tk.messagebox()

######## FUNCTION DEFITIONS #######

def createSourceFile(fileName,authorName,about):
    sourceFile = open(fileName + '.c', 'a')
    tempFile = open(tempCFile, 'r').read()

    data = tempFile
    data = data.replace("%FILENAMELC%", fileName.lower())
    data = data.replace("%FILENAMEUC%", fileName.upper())
    data = data.replace("%AUTHOR%", authorName)
    data = data.replace("%DATE%", date)
    data = data.replace("%YEAR%", str(yearNow))
    data = data.replace("%BRIEF%", about)
    
    sourceFile.write(data)
    sourceFile.close()
    

def createHeaderFile(fileName,authorName,about):
    sourceFile = open(fileName + '.h', 'a')
    tempFile = open(tempHFile, 'r').read()

    data = tempFile
    data = data.replace("%FILENAMELC%", fileName.lower())
    data = data.replace("%FILENAMEUC%", fileName.upper())
    data = data.replace("%AUTHOR%", authorName)
    data = data.replace("%DATE%", date)
    data = data.replace("%YEAR%", str(yearNow))
    data = data.replace("%BRIEF%", about)
    
    sourceFile.write(data)
    sourceFile.close()


def createFiles():
    fileName = entryFileName.get()
    authorName = entryAuthor.get()
    about = entryFileAbout.get()
    if len(fileName)<3:
        messagebox.showerror("Error","File name error!")
    else if :
        
    else:
        createSourceFile(fileName, authorName, about)
        createHeaderFile(fileName, authorName, about)
        # canvas1.create_window(windowWidth/2, elementHeightPosition, window=labelAuthor)
        root.withdraw()
        messagebox.showinfo("Info","Files Created!")
        entryFileName.delete(0, tk.END)
        entryFileAbout.delete(0, tk.END)
        root.deiconify()

        

labelFileName = tk.Label(root, text="Enter File Name!")
canvas1.create_window(windowWidth/2, firstElementPositionHeight, window=labelFileName)

entryFileName = tk.Entry (root, width = 40)
elementHeightPosition = elementHeightPosition + incrementHeight
canvas1.create_window(windowWidth/2, elementHeightPosition, window=entryFileName)

labelFileAbout = tk.Label(root, text="What is it about?")
elementHeightPosition = elementHeightPosition + incrementHeight
canvas1.create_window(windowWidth/2, elementHeightPosition, window=labelFileAbout)

entryFileAbout = tk.Entry (root, width=40)
elementHeightPosition = elementHeightPosition + incrementHeight
canvas1.create_window(windowWidth/2, elementHeightPosition, window=entryFileAbout)

labelAuthor = tk.Label(root, text="Enter Author Name!")
elementHeightPosition = elementHeightPosition + incrementHeight
canvas1.create_window(windowWidth/2, elementHeightPosition, window=labelAuthor)

entryAuthor = tk.Entry (root, width=40) 
elementHeightPosition = elementHeightPosition + incrementHeight
canvas1.create_window(windowWidth/2, elementHeightPosition, window=entryAuthor)

buttonCreate = tk.Button(text='Create Files', command = createFiles)
elementHeightPosition = elementHeightPosition + incrementHeight
canvas1.create_window(windowWidth/2, elementHeightPosition, window=buttonCreate)

labelAuthor = tk.Label(root, text="Enter Author Name!")
elementHeightPosition = elementHeightPosition + incrementHeight

root.mainloop()

