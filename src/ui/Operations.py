import tkinter as tk
from tkinter import ttk
from tkinter import *
import numpy as np
import pandas as pd

class MultiFileOperations:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.root.title("Choose an Operation")
        self.ops = ["Simple Regression", "Logistic Regression", "Multiple Regression", "One-Tail T-Test",
                    "Two-Tail T-Test", "ANOVA"]
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
        self.errorMessage1 = tk.Label(self.root, text="Please select an operation", fg="#FF0000")
        self.errorMessage2 = tk.Label(self.root, text="Please select a confidence level", fg="#FF0000")
        self.root.mainloop()

    def retrieveOperation(self):
        if(self.operationOptions.get()=="Choose an Operation"):
            self.errorMessage1.grid(row=2, column=0, padx=2, pady=2)
        else:
            self.errorMessage1.grid_forget()
            self.operation = self.operationOptions.get()
            self.operationOptions.grid_forget()
            self.submitButton1.grid_forget()
            tk.Label(self.root, text="Selected Operation: " + self.operation).grid(row=0, column=0, padx=2, pady=2)
            confOps = ["One-Tail T-Test", "Two-Tail T-Test", "ANOVA"]
            if(self.operation in confOps):
                self.confidenceOptions.grid(row=1, column=0, padx=2, pady=2)
                self.submitButton2.grid(row=2, column=0, padx=2, pady=2)
            else:
                self.completeButton.grid(row=1, column=0, padx=2, pady=2)
                self.changeButton.grid(row=1, column=1, padx=2, pady=2)
            
    def retrieveConfidence(self):
        if(self.confidenceOptions.get()=="Choose a Confidence Level"):
            self.errorMessage2.grid(row=3, column=0, padx=2, pady=2)
        else:
            self.confidence = self.confidenceOptions.get()
            self.confidenceOptions.grid_forget()
            self.submitButton2.grid_forget()
            tk.Label(self.root, text="Selected Confidence: " + self.confidence).grid(row=1, column=0, padx=2, pady=2)
            self.completeButton.grid(row=2, column=0, padx=2, pady=2)
            self.changeButton.grid(row=2, column=1, padx=2, pady=2)

    def changeSelection(self):
        for w in self.root.grid_slaves(column=0):
            w.grid_forget()
        self.changeButton.grid_forget()
        self.operationOptions.set("Choose an Operation")
        self.confidenceOptions.set("Choose a Confidence Level")
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
        self.filterVarNames = chooseVariables.getFilterVar()
        self.file = selectFile.getFile()
        self.data = chooseVariables.getData()
        self.varData = self.data[self.varName]

        self.operation = ""
        self.filters = []
        self.filterVals = []

        if(self.filterVarNames[0] != "None"):
            self.df = pd.DataFrame(data=self.data[self.filterVarNames[0]], columns=[self.filterVarNames[0]])
            for i in range(len(self.filterVarNames)):
                if(i!=0):
                    d = pd.DataFrame(data = self.data[self.filterVarNames[i]], columns=[self.filterVarNames[i]])
                    self.df = self.df.join(d, on=None)

        self.numOperations = ["MAX", "MIN", "MEAN", "MEDIAN", "MODE", "STDev", "SELECT"]
        self.catOperations = ["MODE", "SELECT"]
        self.whereNum = [">", ">=", "=", "<=", "<", "!="]
        self.whereCat = ["=", "!="]

        if(self.filterVarNames[0]=="None"):
            self.numOperations.remove("SELECT")
            self.catOperations.remove("SELECT")
        if(isinstance(self.varData, str)):
            self.operationOps = ttk.Combobox(self.root, values=self.catOperations)
        else:
            self.operationOps = ttk.Combobox(self.root, values=self.numOperations)
        self.operationOps.set("Choose a Query")
        
        self.submitButton1 = tk.Button(self.root, text="Submit", command=self.submit1)
        self.submitButton2 = tk.Button(self.root, text="Submit", command=self.submit2)
        self.submitButton3 = tk.Button(self.root, text="Submit", command=self.submit3)

        self.errorMessage1 = tk.Label(self.root, text="Please select an operation", fg="#FF0000")
        self.errorMessage2 = tk.Label(self.root, text="Please select a filter", fg="#FF0000")
        self.errorMessage3 = tk.Label(self.root, text="Please select a filter value", fg="#FF0000")
        self.errorMessage4 = tk.Label(self.root, text="Please input a number", fg="#FF0000")
        
        if(self.filterVarNames != "None"):
            self.queryVarLabel = tk.Label(self.root, text = self.operation + " " + self.varName + " WHERE " + self.filterVarNames[0])
            self.catFilterValues = ttk.Combobox(self.root, values=[])
            self.catFilterValues.set("Choose a Value")
            self.numFilterValues = tk.Text(self.root, height = 1, width = 5)
            self.numFilterValues.insert(tk.END, "Input a Value")
            if isinstance(self.varData.iloc[1], str):
                self.filterOperations = ttk.Combobox(self.root, values=self.whereCat)
            else:
                self.filterOperations = ttk.Combobox(self.root, values=self.whereNum)
            self.filterOperations.set("Choose a Filter")
        else:
            self.queryVarLabel = tk.Label(self.root, text = self.varName)
        self.completeButton = tk.Button(self.root, text="Complete Selection", command=self.complete)
        self.display()

    def display(self):
        self.operationOps.grid(row=0, column=0, padx=2, pady=2)
        self.submitButton1.grid(row=1, column=0, padx=2, pady=2)
        self.queryVarLabel.grid(row=0, column=1, padx=2, pady=2)
        self.root.mainloop()

    def submit1(self):
        if(self.operationOps.get()=="Choose a Query"):
            self.errorMessage1.grid(row=2, column=0, padx=2, pady=2)
        else:
            self.errorMessage1.grid_forget()
            self.operation = self.operationOps.get()
            self.queryVarLabel['text'] = self.operation + " " + self.queryVarLabel['text']
            self.queryVarLabel.grid_forget()
            self.queryVarLabel.grid(row=0, column=0, padx=0, pady=0)
            self.operationOps.grid_forget()
            self.submitButton1.grid_forget()
            if(self.filterVarNames[0] == "None"):
                self.root.destroy()
            else:
                self.filterOperations.grid(row=1, column=0, padx=2, pady=2)
                if isinstance(self.df[self.filterVarNames[len(self.filters)]][0], (int, float, np.integer)):
                    self.filterOperations['values'] = self.whereNum
                else:
                    self.filterOperations['values'] = self.whereCat
                self.submitButton2.grid(row=2, column=0, padx=2, pady=2)         
            
    def submit2(self):
        if(self.filterOperations.get()=="Choose a Filter"):
            self.errorMessage2.grid(row=3, column=0, padx=2, pady=2)
        else:
            self.errorMessage2.grid_forget()
            self.filters.append(self.filterOperations.get())
            self.filterOperations.grid_forget()
            self.queryVarLabel['text'] = self.queryVarLabel['text'] + " " +  self.filters[-1]
            self.submitButton2.grid_forget()
            currentFilterVar = self.filterVarNames[len(self.filters)-1]
            if isinstance(self.df[currentFilterVar][0], str):
                self.catFilterValues['values'] = set(self.df[currentFilterVar])
                self.catFilterValues.set("Choose a Value")
                self.catFilterValues.grid(row=1, column=0, padx=2, pady=2)
            else:
                self.numFilterValues.insert(tk.END, "Input a Value")
                self.numFilterValues.grid(row=1, column=0, padx=2, pady=2)
            self.submitButton3.grid(row=2, column=0, padx=2, pady=2)

    def submit3(self):
        if isinstance(self.df[self.filterVarNames[len(self.filters)-1]][0], (int, float, np.integer)):
            try:
                self.filterVals.append(int(self.numFilterValues.get("1.0",tk.END)))
            except:
                self.numFilterValues.insert(tk.END, "Input a Value")
                self.errorMessage4.grid(row=3, column=0, padx=2, pady=2)
            self.errorMessage4.grid_forget()
            self.numFilterValues.grid_forget()
            self.catFilterValues.grid_forget()
            self.submitButton3.grid_forget()
            if(len(self.filters)!= len(self.filterVarNames)):
                self.queryVarLabel['text'] = self.queryVarLabel['text'] + " " +  str(self.filterVals) + " and " + self.filterVarNames[len(self.filters)]
                if isinstance(self.df[self.filterVarNames[len(self.filters)]][0], (int, float, np.integer)):
                    self.filterOperations['values'] = self.whereNum
                else:
                    self.filterOperations['values'] = self.whereCat
                self.filterOperations.grid(row=1, column=0, padx=2, pady=2)
                self.submitButton2.grid(row=2, column=0, padx=2, pady=2)
            else:
                self.queryVarLabel['text'] = self.queryVarLabel['text'] + " " +  str(self.filterVals)
                self.completeButton.grid(row=2, column=0, padx=2, pady=2)
        else:
            if(self.catFilterValues.get()=="Choose a Value"):
                self.errorMessage3.grid(row=4, column=0, padx=2, pady=2)
            else:
                self.filterVals.append(self.catFilterValues.get())
                self.errorMessage3.grid_forget()
                self.numFilterValues.grid_forget()
                self.catFilterValues.grid_forget()
                self.submitButton3.grid_forget()
                if(len(self.filters)!= len(self.filterVarNames)):
                    self.queryVarLabel['text'] = self.queryVarLabel['text'] + " " +  str(self.filterVals) + " and "
                    if isinstance(self.df[self.filterVarNames[len(self.filters)]][0], (int, float, np.integer)):
                        self.filterOperations['values'] = self.whereNum
                    else:
                        self.filterOperations['values'] = self.whereCat
                    self.filterOperations.set("Choose a Filter")
                    self.filterOperations.grid(row=1, column=0, padx=2, pady=2)
                    self.submitButton2.grid(row=2, column=0, padx=2, pady=2)
                else:
                    self.queryVarLabel['text'] = self.queryVarLabel['text'] + " " +  str(self.filterVals)
                    self.completeButton.grid(row=2, column=0, padx=2, pady=2)

    def complete(self):
        self.root.destroy()
        
    def getOperation(self):
        return self.operation

    def getFilters(self):
        if(self.filterVarNames[0] != "None"):
            return self.filters
        return ""
    
    def getFilterValues(self):
        if(self.filterVarNames[0] != "None"):
            return self.filterVals
        return ""

    def getFilterData(self):
        if(self.filterVarNames[0] != "None"):
            return self.df
        return ""
    
    def getVarData(self):
        return self.varData

    def getVarName(self):
        return self.varName
    
    def getFilterVarNames(self):
        return self.filterVarNames

    def getString(self):
        if(self.filterVarNames[0] == "None"):
            text = self.operation + " " + self.varName
        else:
            text = self.operation + " " + self.varName + " WHERE "
            for i in range(len(self.filterVarNames)):
                if(self.filterVarNames[i]!= self.filterVarNames[-1]):
                    text = text + self.filterVarNames[i] + " " + self.filters[i] + " " + str(self.filterVals[i]) + " and "
                else:
                    text = text + self.filterVarNames[i] + " " + self.filters[i] + " " + str(self.filterVals[i])
        return text