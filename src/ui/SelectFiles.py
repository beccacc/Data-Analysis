from FileUpload import FileUpload
import tkinter as tk
from tkinter import *
from tkinter import ttk
from operator import itemgetter


fileSelected = False
fileUpload = FileUpload()

class SelectFiles:
    def __init__(self, fileUpload):
        self.selectedFiles = []
        self.fileUpload = fileUpload
        print("fileUpload in SelectFiles")
        self.root = tk.Tk()
        self.root.title("Select your Files")
        self.root.geometry("400x250")
        # print("root created")
        self.viewButton = tk.Button(self.root, text="View Files", command=self.viewFiles)
        self.viewButton.grid(row=0, column=0, pady=2)
        # print("viewButton created")
        self.root.mainloop()

    def viewFiles(self):
        self.viewButton.grid_forget()
        fileList = self.fileUpload.getFileList()
        # numFiles = len(fileList)
        viewLabel = tk.Label(self.root, text="Choose files: ")
        viewLabel.grid(row=0, column=0, padx=2, pady=2)
        for i in range(len(fileList)):
            button = Button(self.root, text=fileList[i][0], command=lambda f=fileList[i]: self.addToSelectedFiles(f))
            button.grid(row=i+1, column=0, pady=2)
        selectedFilesLabel = tk.Label(self.root, text="Selected Files:")
        selectedFilesLabel.grid(row=0, column=3, padx=2, pady=2)



    def addToSelectedFiles(self, file):
        if file not in self.selectedFiles:
            self.selectedFiles.append(file)
            print(f"Added {file[0]} to selected files.")
            fileLabel = tk.Label(self.root, text = file[0])
            fileLabel.grid(row=len(self.selectedFiles), column=3, pady=2, padx=2)
        else:
            print(f"{file[0]} is already in the list.")
        if(len(self.selectedFiles)>0):
            completeButton = tk.Button(self.root, text="Complete Selection", command=self.completeSelection)
            completeButton.grid(row=0, column=4, pady=2, padx=2)

    def completeSelection(self):
        self.root.destroy()

    def getSelected(self):
        return fileSelected

    def getSelection(self):
        return self.selectedFiles
    
class SelectFile:
    def __init__(self, fileUpload):
        self.selectedFile = ("", "")
        self.fileList = fileUpload.getFileList()
        self.fileNames = []
        for i in range(len(self.fileList)):
            self.fileNames.append(self.fileList[i][0])
        self.root = tk.Tk()
        self.root.title("Select your File")
        self.root.geometry("400x250")
        self.chooseFile = ttk.Combobox(self.root, values=self.fileNames)
        self.viewButton = tk.Button(self.root, text="View Files", command=self.viewFiles)
        self.viewButton.grid(row=0, column=0, pady=2)
        self.submitButton = tk.Button(self.root, text="Submit", command=self.setFile)
        self.errorMessage = tk.Label(self.root, text="Please Select a File", fg="#FF0000")
        self.root.mainloop()

    def viewFiles(self):
        self.viewButton.grid_forget()
        self.chooseFile.set("Choose a File")
        self.chooseFile.grid(row=0, column=0, padx=2, pady=2)
        self.submitButton.grid(row=0, column=1, padx=2, pady=2)

    def setFile(self):
        if(self.chooseFile.get()=="Choose a File"):
            self.errorMessage.grid(row=1, column=0, padx=2, pady=2)
        else:
            fileName = self.chooseFile.get()
            for file in self.fileList:
                if(file[0] == fileName):
                    self.selectedFile = file
            self.root.destroy()

    def getFile(self):
        return self.selectedFile
    