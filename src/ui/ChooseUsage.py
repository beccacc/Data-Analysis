import tkinter as tk

class ChooseUsage:
    def __init__(self):
        self.usage = ""
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.root.title("Choose Usage")
        self.oneFileButton = tk.Button(self.root, text="Querying Data", command=self.queryData)
        self.oneFileButton.grid(row=0, column=0, pady=2)
        self.multiFileButton = tk.Button(self.root, text = "Data Analysis", command=self.dataAnalysis)
        self.multiFileButton.grid(row=1, column=0, pady=2)
        self.root.mainloop()

    def queryData(self):
        self.usage = "queryData"
        self.root.destroy()
    
    def dataAnalysis(self):
        self.usage = "dataAnalysis"
        self.root.destroy()
    
    def getUsage(self):
        return self.usage
    
