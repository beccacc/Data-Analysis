import tkinter as tk
from tkinter import filedialog
import os



class FileUpload:
    def __init__(self):
        self.fileList = []
        self.completed = False
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.root.title("Upload File")
        self.uploadButton = tk.Button(self.root, text="Upload File", command=self.importFile)
        self.uploadButton.pack(side=tk.TOP)
        self.fileLabel = tk.Label(self.root, text = "Files uploaded:")
        self.fileLabel.pack(side=tk.LEFT)
        # print("created uploadButton")
        self.completeButton = tk.Button(self.root, text="Complete Upload", command=self.completeUpload)
        self.root.mainloop()

    def importFile(self):
        filePath = filedialog.askopenfilename(title="Select a file", filetypes=[("CSV files", "*.csv")])
        if filePath:
            fileName = os.path.basename(filePath).replace('.csv', '')
            self.fileList.append((fileName, filePath))
            label = tk.Label(self.root, text = fileName)
            # label.grid(row=len(self.fileList), column=0, padx=10, pady=10)
            label.pack(side=tk.LEFT, pady=10)
        if(len(self.fileList) > 0):
            self.completeButton.pack(side=tk.BOTTOM)
    def completeUpload(self):
        print("complete button pressed")
        self.root.destroy()

    def getFileList(self):
        return self.fileList

    def uploadFile(self):
        self.root.mainloop()