from FileUpload import FileUpload
import tkinter as tk
from tkinter import *

fileSelected = False
fileUpload = FileUpload()

class SelectFiles:
    def __init__(self, fileUpload):
        self.selectedFiles = []
        self.fileUpload = fileUpload
        print("fileUpload in SelectFiles")
        self.root = tk.Tk()
        self.root.title("Select your File")
        self.root.geometry("400x250")
        print("root created")
        self.viewButton = tk.Button(self.root, text="View Files", command=self.viewFiles)
        self.viewButton.pack()
        print("viewButton created")
        self.root.mainloop()

    def viewFiles(self):
        self.viewButton.destroy()
        fileList = self.fileUpload.getFileList()
        # numFiles = len(fileList)
        for file in fileList:
            button = Button(self.root, text=file[0], command=lambda f=file: self.addToSelectedFiles(f))
            button.pack(side = tk.LEFT)
        selectedFilesLabel = tk.Label(self.root, text="Selected Files:")
        selectedFilesLabel.pack(side = tk.RIGHT)



    def addToSelectedFiles(self, file):
        if file not in self.selectedFiles:
            self.selectedFiles.append(file)
            print(f"Added {file[0]} to selected files.")
            fileLabel = tk.Label(self.root, text = file[0])
            fileLabel.pack(side = tk.RIGHT)
        else:
            print(f"{file[0]} is already in the list.")
        if(len(self.selectedFiles)>0):
            completeButton = tk.Button(self.root, text="Complete Selection", command=self.completeSelection)
            completeButton.pack(side = tk.BOTTOM)

    def completeSelection(self):
        self.root.destroy()

    def getSelected(self):
        return fileSelected

    def getSelection(self):
        return self.selectedFiles
    