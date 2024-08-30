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
        self.errorMessage = tk.Label(self.root, text="File already exists\n Please choose a new file or complete upload", bg="#FF0000", fg="#FFFFFF")
        self.root.mainloop()

    def importFile(self):
        self.reset()
        filePath = filedialog.askopenfilename(title="Select a file", filetypes=[("CSV files", "*.csv")])
        if filePath:
            fileName = os.path.basename(filePath).replace('.csv', '')
            file = (fileName, filePath)
            self.fileDisplay(file)
            # label.grid(row=len(self.fileList), column=0, padx=10, pady=10)
            # label.pack(side=tk.LEFT, pady=10)
        if(len(self.fileList) > 0):
            self.completeButton.grid(row=0, column=2, pady=5)

    def completeUpload(self):
        print("complete button pressed")
        self.root.destroy()

    def getFileList(self):
        return self.fileList
    
    def fileDisplay(self, file):
        if(self.fileList.__contains__(file)):
            self.errorMessage.grid(row=len(self.fileList)+2, column=0, padx=2, pady=2)
            for w in self.root.winfo_children():
                if isinstance(w, tk.Label):
                    if(w.cget("text")==file[0]):
                        w.config(fg="#FF0000")
        else:
            self.errorMessage.grid_forget()
            self.fileList.append(file)
            label = tk.Label(self.root, text = file[0])
            label.grid(row=len(self.fileList)+1, column=0, pady=2)
    
    def reset(self):
        for w in self.root.winfo_children():
            if isinstance(w, tk.Label):
                w.config(fg="#000000")
        self.errorMessage.grid_forget()
        
    def uploadFile(self):
        self.root.mainloop()