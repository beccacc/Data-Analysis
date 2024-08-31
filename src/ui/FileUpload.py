import tkinter as tk
from tkinter import filedialog
import os



class FileUpload:
    def __init__(self):
        self.fileList = []
        self.completed = False
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.root.title("Upload File")
        self.uploadButton = tk.Button(self.root, text="Upload File", command=self.importFile)
        self.uploadButton.grid(row=0, column=0, pady=2)
        self.fileLabel = tk.Label(self.root, text = "Files uploaded:")
        self.fileLabel.grid(row=1, column=0, pady=2)
        # print("created uploadButton")
        self.completeButton = tk.Button(self.root, text="Complete Upload", command=self.completeUpload)
        self.errorMessage1 = tk.Label(self.root, text="File already exists\n Please choose a new file or complete upload", bg="#FF0000", fg="#FFFFFF")
        self.errorMessage2 = tk.Label(self.root, text="File already exists under another name\n Please choose a new file or complete upload", bg="#FF0000", fg="#FFFFFF")
        self.errorMessage3 = tk.Label(self.root, text="A different file already exists under the same name", bg="#FF0000", fg="#FFFFFF")

        self.replaceButton = tk.Button(self.root, text="Replace Existing File", command=self.replaceFile)
        self.renameButton = tk.Button(self.root, text="Change File Name", command=self.renameFile)
        self.existingFile=()
        self.currentFile=()

        self.textBox = tk.Text(self.root, height = 1, width = 20)
        self.submitButton = tk.Button(self.root, text="Submit", command=self.changeFileName)

        self.root.mainloop()

    def importFile(self):
        self.resetDisplay()
        filePath = filedialog.askopenfilename(title="Select a file", filetypes=[("CSV files", "*.csv")])
        if filePath:
            fileName = os.path.basename(filePath).replace('.csv', '')
            file = (fileName, filePath)
            self.currentFile = file
            if(self.fileCheck(file)):
                self.fileList.append(file)
                label = tk.Label(self.root, text = file[0])
                label.grid(row=len(self.fileList)+1, column=0, pady=2)
            # label.grid(row=len(self.fileList), column=0, padx=10, pady=10)
            # label.pack(side=tk.LEFT, pady=10)
        if(len(self.fileList) > 0):
            self.completeButton.grid(row=0, column=2, pady=5)

    def completeUpload(self):
        print("complete button pressed")
        self.root.destroy()

    def getFileList(self):
        return self.fileList
    
    def fileCheck(self, file):
        if(self.fileList.__contains__(file)):
            #Error 1: file has already been uploaded, do not add to fileList
            self.errorMessage1.grid(row=len(self.fileList)+2, column=0, padx=2, pady=2)
            self.setTextRed(file[0])
            return False
        else:
            for f in self.fileList:
                if(f[1] == file[1]):
                    #Error 2: file has already been uploaded under a different name, do not add to fileList
                    self.errorMessage2.grid(row=len(self.fileList)+2, column=0, padx=2, pady=2)
                    self.setTextRed(f[0])
                    return False
                if(f[0] == file[0]):
                    #Error 3: different file has already been uploaded with the same name, do not add to fileList
                    self.errorMessage3.grid(row=len(self.fileList)+2, column=0, padx=2, pady=2)
                    #set existingFile to spot in list of existing file
                    self.existingFile = f
                    self.changeFile()
                    return False
        # No Error: add to fileList
        return True
    
    def resetDisplay(self):
        for w in self.root.winfo_children():
            if isinstance(w, tk.Label):
                w.config(fg="#000000")
        self.errorMessage1.grid_forget()
        self.errorMessage2.grid_forget()
        self.errorMessage3.grid_forget()

    def setTextRed(self, text):
        for w in self.root.winfo_children():
            if isinstance(w, tk.Label):
                if(w.cget("text")==text):
                    w.config(fg="#FF0000")
    
    def changeFile(self):
        #disable buttons temporarily
        self.uploadButton['state'] = tk.DISABLED
        self.completeButton['state'] = tk.DISABLED
        # self.replaceButton.grid(row=5, column=0, padx=2, pady=2)
        # self.renameButton.grid(row=5, column=1, padx=2, pady=2)
        self.replaceButton.grid(row=len(self.fileList)+4, column=0, padx=2, pady=2)
        self.renameButton.grid(row=len(self.fileList)+4, column=1, padx=2, pady=2)
    
    def renameFile(self):
        self.renameButton.grid_forget()
        self.replaceButton.grid_forget()
        self.textBox.grid(row=len(self.fileList)+4, column=0, padx=2, pady=2)
        self.submitButton.grid(row=len(self.fileList)+4, column=1, padx=2, pady=2)
        #enable upload/complete buttons after error is addressed

    
    def changeFileName(self):
        txt = self.textBox.get("1.0",tk.END)
        filePath = self.currentFile[1]
        self.currentFile = (txt, filePath)
        self.fileList.append(self.currentFile)
        label = tk.Label(self.root, text = txt)
        label.grid(row=len(self.fileList)+1, column=0, pady=2)
        self.uploadButton['state'] = tk.NORMAL
        self.completeButton['state'] = tk.NORMAL
        self.textBox.grid_forget()
        self.submitButton.grid_forget()
        self.resetDisplay()


    def replaceFile(self):
        self.fileList.remove(self.existingFile)
        self.fileList.append(self.currentFile)
        #enable upload/complete buttons after error is addressed
        self.uploadButton['state'] = tk.NORMAL
        self.completeButton['state'] = tk.NORMAL
        self.renameButton.grid_forget()
        self.replaceButton.grid_forget()
        self.resetDisplay()
        
    def uploadFile(self):
        self.root.mainloop()