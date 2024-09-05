import tkinter as tk
from tkinter import ttk
from tkinter import *
import numpy as np

class MultiFileOperations:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.root.title("Choose an Operation")
        self.ops = ["Simple Regression", "Logistic Regression", "Multiple Regression", "One-Tail T-Test",
                    "Two-Tail T-Test", "ANOVA", "MANOVA", "Correlation"]
        self.operationOptions = ttk.Combobox(self.root, values=self.ops)
        self.operationOptions.set("Choose an Operation")
        self.operationOptions.grid(row=0, column=0, padx=2, pady=2)
        self.submitButton1 = tk.Button(self.root, text="Submit", command=self.retrieveOperation)
        self.submitButton1.grid(row=1, column=0, padx=2, pady=2)
        self.submitButton2 = tk.Button(self.root, text="Submit", command=self.retrieveConfidence)
        self.operation=""
        self.confidence=0
        self.confs = [0.0005, 0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5]            
        self.confidenceOptions=ttk.Combobox(self.root, values=self.confs)
        self.confidenceOptions.set("Choose a Confidence Level")
        self.completeButton = tk.Button(self.root, text="Complete Selection", command=self.completeSelection)
        self.changeButton = tk.Button(self.root, text="Change Selection", command=self.changeSelection)
        self.root.mainloop()


    
    def retrieveOperation(self):
        self.operation = self.operationOptions.get()
        self.operationOptions.grid_forget()
        self.submitButton1.grid_forget()
        tk.Label(self.root, text="Selected Operation: " + self.operation).grid(row=0, column=0, padx=2, pady=2)
        confOps = ["One-Tail T-Test", "Two-Tail T-Test", "ANOVA", "MANOVA"]
        if(self.operation in confOps):
            self.confidenceOptions.grid(row=1, column=0, padx=2, pady=2)
            self.submitButton2.grid(row=2, column=0, padx=2, pady=2)
        else:
            self.completeButton.grid(row=1, column=0, padx=2, pady=2)
            self.changeButton.grid(row=1, column=1, padx=2, pady=2)
            
    def retrieveConfidence(self):
        self.confidence = self.confidenceOptions.get()
        self.confidenceOptions.grid_forget()
        self.submitButton2.grid_forget()
        tk.Label(self.root, text="Selected Confidence: " + self.confidence).grid(row=1, column=0, padx=2, pady=2)
        self.completeButton.grid(row=2, column=0, padx=2, pady=2)
        self.changeButton.grid(row=2, column=1, padx=2, pady=2)

    def changeSelection(self):
        for w in self.root.grid_slaves(column=0):
            w.grid_forget()
        self.operationOptions.grid(row=0, column=0, padx=2, pady=2)
        self.submitButton1.grid(row=1, column=0, padx=2, pady=2)
        

    def completeSelection(self):
        self.root.destroy()

    def getOperation(self):
        return self.operation

    def getConfidence(self):
        return self.confidence

class SingleFileOperations:
    def __init__(self, chooseVariables, selectFile):
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.root.title("Choose an Operation")
        self.varName = chooseVariables.getVar()
        self.filterVarName = chooseVariables.getFilterVar()
        self.file = selectFile.getFile()
        self.data = chooseVariables.getData()
        self.variable = self.data[self.varName]
        if(self.filterVarName != "None"):
            self.filterVar = self.data[self.filterVarName]
        
        self.operation = ""
        self.filter = ""
        self.filterValue = ""

        self.operations = ["MAX", "MIN", "MEAN", "MEDIAN", "MODE", "STDev", "SELECT"]

        self.whereNum = [">", ">=", "=", "<=", "<", "!="]
        self.whereCat = ["=", "!="]

        self.operationOps = ttk.Combobox(self.root, values=self.operations)
        self.operationOps.set("Choose a Query")
        self.operationOps.grid(row=0, column=0, padx=2, pady=2)
        self.submitButton = tk.Button(self.root, text="Submit", command=self.complete)

        if(self.filterVarName != "None"):
            self.queryVarLabel = tk.Label(self.root, text = self.varName + " WHERE " + self.filterVarName)
            self.queryVarLabel.grid(row=0, column=1, padx=2, pady=2)
            if isinstance(self.variable.iloc[1], (int, float, np.integer)):
                self.filterOperations = ttk.Combobox(self.root, values=self.whereNum)
                self.filterValues = tk.Text(self.root, height = 1, width = 5)
                self.filterValues.insert(tk.END, "Input a Value")

            else:
                self.filterOperations = ttk.Combobox(self.root, values=self.whereCat)
                self.filterValueOptions = set(self.filterVar)
                self.filterValues = ttk.Combobox(self.root, values=self.filterValueOptions)
                self.filterValues.set("Choose a Value")
            self.filterOperations.set("Choose a Filter")
            self.filterOperations.grid(row=0, column=2, padx=2, pady=2)
            self.filterValues.grid(row=0, column=3, padx=2, pady=2)
        else:
            self.queryVarLabel = tk.Label(self.root, text = self.varName)
            self.queryVarLabel.grid(row=0, column=1, padx=2, pady=2)




    def complete(self):
        self.operation = self.operationOps.get()
        if(self.filterVarName != "None"):
            self.filter = self.filterOperations.get()
            if isinstance(self.variable.iloc[1], (int, float, np.integer)):
                self.filterValue = self.filterValues.get("1.0",tk.END)
            else:
                self.filterValue = self.filterValues.get()
        self.root.destroy()
        
    def getOperation(self):
        return self.operation

    def getFilter(self):
        return self.filter
    
    def getFilterValue(self):
        return self.filterValue

    def getFilterData(self):
        return self.filterVar
    
    def getVarData(self):
        return self.variable

    def getVarName(self):
        return self.varName
    
    def getFilterVarName(self):
        return self.filterVarName

    def getString(self):
        if(self.filterVarName != "None"):
            text = self.operation + " " + self.varName + " WHERE " + self.filterVarName + " " + self.filter + " " + self.filterValue
        else:
            text = self.operation + " " + self.varName
        return text