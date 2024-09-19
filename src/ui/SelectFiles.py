from FileUpload import FileUpload
import tkinter as tk
from tkinter import *
from tkinter import ttk

class SelectFiles:
    def __init__(self, fileUpload):
        self.selectedFiles = []
        self.fileUpload = fileUpload
        self.fileList = self.fileUpload.getFileList()
        print("fileUpload in SelectFiles")
        self.root = tk.Tk()
        self.root.title("Select your Files")
        self.root.geometry("400x250")
        self.viewButton = tk.Button(self.root, text="View Files", command=self.viewFiles)
        self.viewButton.grid(row=0, column=0, pady=2)
        self.submitButton = tk.Button(self.root, text="Submit", command=self.completeSelection)
        self.errorMessage = tk.Label(self.root, text="Please Select a File", fg="#FF0000")
        self.root.mainloop()

    def viewFiles(self):
        self.viewButton.grid_forget()
        tk.Label(self.root, text="Select Files").grid(row=0, column=0, columnspan=2, padx=2, pady=2)
        for i in range(len(self.fileList)):
            button = ttk.Checkbutton(self.root, text=self.fileList[i][0], command=lambda f=self.fileList[i]: self.addToSelectedFiles(f))
            button.grid(row=i+1, column=0, columnspan=2, padx=2, pady=2)
            self.submitButton.grid(row=len(self.fileList)+1, column=0, padx=2, pady=2)

    def addToSelectedFiles(self, file):
        if file not in self.selectedFiles:
            self.selectedFiles.append(file)
            print(f"Added {file[0]} to selected files.")
        else:
            print(f"{file[0]} is already in the list.")
            self.selectedFiles.remove(file)

    def completeSelection(self):
        if(len(self.selectedFiles)>0):
            self.root.destroy()
        else:
            self.errorMessage.grid(row=len(self.fileList)+2, column=0)

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
    