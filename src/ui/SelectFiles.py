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
        # print("root created")
        self.viewButton = tk.Button(self.root, text="View Files", command=self.viewFiles)
        self.viewButton.grid(row=0, column=0, pady=2)
        # print("viewButton created")
        self.root.mainloop()

    def viewFiles(self):
        self.viewButton.destroy()
        fileList = self.fileUpload.getFileList()
        # numFiles = len(fileList)
        for i in range(len(fileList)):
            button = Button(self.root, text=fileList[i][0], command=lambda f=fileList[i]: self.addToSelectedFiles(f))
            button.grid(row=i+1, column=0, pady=2)
        selectedFilesLabel = tk.Label(self.root, text="Selected Files:")
        selectedFilesLabel.grid(button.grid(row=0, column=1, pady=2, padx=2))



    def addToSelectedFiles(self, file):
        if file not in self.selectedFiles:
            self.selectedFiles.append(file)
            print(f"Added {file[0]} to selected files.")
            fileLabel = tk.Label(self.root, text = file[0])
            fileLabel.grid(row=len(self.selectedFiles), column=1, pady=2, padx=2)
        else:
            print(f"{file[0]} is already in the list.")
        if(len(self.selectedFiles)>0):
            completeButton = tk.Button(self.root, text="Complete Selection", command=self.completeSelection)
            completeButton.grid(row=0, column=2, pady=2, padx=2)

    def completeSelection(self):
        self.root.destroy()

    def getSelected(self):
        return fileSelected

    def getSelection(self):
        return self.selectedFiles
    