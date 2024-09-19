import tkinter as tk

class ChooseUsage:
    def __init__(self):
        self.usage = ""
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.root.title("Choose Usage")
        self.oneFileButton = tk.Button(self.root, text="Data Analysis on a Single File", command=self.oneFile)
        self.oneFileButton.grid(row=0, column=0, pady=2)
        self.multiFileButton = tk.Button(self.root, text = "Data Analysis on Multiple Files", command=self.multiFile)
        self.multiFileButton.grid(row=1, column=0, pady=2)
        self.root.mainloop()

    def oneFile(self):
        self.usage = "oneFile"
        self.root.destroy()
    
    def multiFile(self):
        self.usage = "multiFile"
        self.root.destroy()
    
    def getUsage(self):
        return self.usage
    
