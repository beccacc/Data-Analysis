import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import *
# from Operations import MultiFileOperations
# from SelectFiles import SelectFiles
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
# from model import ReadFile

# selectFiles = SelectFiles()
# operations = Operations()

class ChooseVariables:
    def __init__(self, selectFiles, operations):
        self.fileList = list(selectFiles.getSelection())
        self.data = self.getData()
        self.varList = self.getVarList()
        self.operation = operations.getOperation()
        # print("operation: " + self.operation)
        self.confidence = 0
        self.indVarOptions = []
        self.depVarOptions = []
        #set indVar and depVar options
        self.setVars()
        self.indVar = ""
        self.depVar = ""
        self.indVars = []
        self.depVars = []

        self.indCompleted = False
        self.depCompleted = False
        
        self.root = tk.Tk()
        self.root.title("Select Variables")
        self.root.geometry("500x250")
        self.indVarOptionsList = ttk.Combobox(self.root, values=self.indVarOptions, width=22)
        self.indVarOptionsList.set("Choose an Independent Variable")
        self.depVarOptionsList = ttk.Combobox(self.root, values=self.depVarOptions, width=20)
        self.depVarOptionsList.set("Choose a Dependent Variable")

        self.indSubmitButton = tk.Button(self.root, text="Submit", command=self.setInd)
        self.depSubmitButton = tk.Button(self.root, text="Submit", command=self.setDep)
        
        self.display()
        self.root.mainloop()


    def getData(self):
        data = pd.read_csv(self.fileList[0][1])
        for i in range(len(self.fileList)):
            if(i!=0):
                filePath = self.fileList[i][1]
                fileData = pd.read_csv(filePath)
                data = data.join(fileData, how="inner")
        return data
    
    def getVarList(self):
        return self.data.columns
        

    def getConfidence(self):
        if(self.operation == "One-tail T-Test" or self.operation == "Two-tail T-Test"):
            self.confidence = self.operations.getConfidence()
    
    def ANOVA(self):
        for var in self.varList:
            if isinstance(self.data[var].iloc[1], (int, float, np.integer)):
                self.depVarOptions.append(var)
            else:
                self.indVarOptions.append(var)

    def Correlation(self):
        for var in self.varList:
            if isinstance(self.data[var].iloc[1], (int, float, np.integer)):
                self.indVarOptions.append(var)
                self.depVarOptions.append(var)

    def MANOVA(self):
        for var in self.varList:
            if isinstance(self.data[var].iloc[1], (int, float, np.integer)):
                self.depVarOptions.append(var)
            else:
                self.indVarOptions.append(var)

    def multiReg(self):
        for var in self.varList:
            if isinstance(self.data[var].iloc[1], (int, float, np.integer)):
                self.indVarOptions.append(var)
                self.depVarOptions.append(var)
     
    def simpleReg(self):
        for var in self.varList:
            if isinstance(self.data[var].iloc[1], (int, float, np.integer)):
                self.indVarOptions.append(var)
                self.depVarOptions.append(var)

    def logReg(self):
        for var in self.varList:
            if isinstance(self.data[var].iloc[1], (int, float, np.integer)):
                self.indVarOptions.append(var)
            else:
                self.depVarOptions.append(var)
    
    def TTest(self):
        for var in self.varList:
            if isinstance(self.data[var].iloc[1], (int, float, np.integer)):
                self.depVarOptions.append(var)
                self.indVarOptions.append(var)
                

    def display(self):
        if(self.operation == "Multiple Regression" or self.operation == "MANOVA"):
            tk.Label(self.root, text="Choose Independent Variables").grid(row=0, column=0, columnspan=2, padx=2, pady=2)
            for i in range(len(self.indVarOptions)):
                button = ttk.Checkbutton(self.root, text=self.indVarOptions[i], command=lambda v=self.indVarOptions[i]: self.setIndVars(v))
                button.grid(row=i+1, column=0, columnspan=2, padx=2, pady=2)
            self.indSubmitButton.grid(row=len(self.indVarOptions)+1, column=0, padx=2, pady=2)
        else:
            self.indVarOptionsList.grid(row=0, column=0, columnspan=2, padx=2, pady=2)
            self.indSubmitButton.grid(row=1, column=0, padx=2, pady=2)
        if(self.operation == "MANOVA" or self.operation == "ANOVA"):
            tk.Label(self.root, text="Choose Dependent Variables").grid(row=0, column=2, columnspan=2, padx=2, pady=2)
            for i in range(len(self.depVarOptions)):
                button = ttk.Checkbutton(self.root, text=self.depVarOptions[i], command=lambda v=self.depVarOptions[i]: self.setDepVars(v))
                button.grid(row=i+1, column=2, columnspan=2, padx=2, pady=2)
                self.depSubmitButton.grid(row=len(self.depVarOptions)+1, column=2, padx=2, pady=2)
        else:
            self.depVarOptionsList.grid(row=0, column=2, columnspan=2, padx=2, pady=2)
            self.depSubmitButton.grid(row=1, column=2, padx=2, pady=2)

    def setVars(self):
        if(self.operation == "One-tail T-Test" or self.operation == "Two-tail T-Test"):
            self.TTest()
        elif(self.operation == "ANOVA"):
            self.ANOVA()
        elif(self.operation == "MANOVA"):
            self.MANOVA()
        elif(self.operation == "Multiple Regression"):
            self.multiReg()
        elif(self.operation == "Simple Regression"):
            self.simpleReg()
        elif(self.operation == "Logistic Regression"):
            self.logReg()
        else:
            self.Correlation()


    def setIndVars(self, var):
        if(var in self.indVars):
            self.indVars.remove(var)
        else:
            self.indVars.append(var)
    
    def setDepVars(self, var):
        if(var in self.depVars):
            self.depVars.remove(var)
        else:
            self.depVars.append(var)

    def setInd(self):
        self.indCompleted = True
        if(self.operation != "MANOVA" and self.operation != "Multiple Regression"):
            self.indVar = self.indVarOptionsList.get()
            self.indVarOptionsList.grid_forget()
        else:
            for w in self.root.winfo_children():
                if w.grid_info()['column']==0:
                    w.grid_forget()
        if(self.indCompleted and self.depCompleted):
            self.root.destroy()


    def setDep(self):
        self.depCompleted = True
        if(self.operation != "MANOVA" and self.operation != "ANOVA"):
            self.depVar = self.depVarOptionsList.get()
            self.depVarOptionsList.grid_forget()
        else:
            for w in self.root.winfo_children():
                if w.grid_info()['column']==1:
                    w.grid_forget()
        if(self.indCompleted and self.depCompleted):
            self.root.destroy()

    def getIndVar(self):
        if(self.operation == "Multiple Regression" or self.operation == "MANOVA"):
            return self.indVars
        return self.indVar
    
    def getDepVar(self):
        if(self.operation == "MANOVA" or self.operation == "ANOVA"):
            return self.depVars
        return self.depVar

    def getDataset(self):
        return self.data

class ChooseVariable:
    def __init__(self, selectFile):
        self.file = selectFile.getFile()
        self.data = self.setData()
        self.varList = self.setVarList()
        self.variable = ""
        self.filterVar = ""
        # self.str=""
        
        self.root = tk.Tk()
        self.root.title("Select Variables")
        self.root.geometry("500x250")
        self.varOptions = ttk.Combobox(self.root, values=self.varList, width=22)
        self.varOptions.set("Choose a Variable to Query")
        self.varOptions.grid(row=0, column=0, padx=2, pady=2)
        self.submitButton1 = tk.Button(self.root, text="Submit", command=self.setVar)
        self.submitButton1.grid(row=1, column=0, padx=2, pady=2)

        self.depVarOptions = ttk.Combobox(self.root, width=20)
        self.depVarOptions.set("Choose a Filter Variable")
        self.submitButton2 = tk.Button(self.root, text="Submit", command=self.setFilterVar)
        # self.submitButton3 = tk.Button(self.root, text="Submit", command=self.setNewFilterVar)


        # self.addNewButton = tk.Button(self.root, text="Add Filter", command=self.newFilter)
        self.completeButton = tk.Button(self.root, text="Complete Selection", command=self.completeSelection)
        self.changeButton = tk.Button(self.root, text="Change Selection", command=self.changeSelection)

        self.errorMessage1 = tk.Label(self.root, text="Please choose a variable to query", fg="#FF0000")
        self.errorMessage2 = tk.Label(self.root, text="Please choose a filter variable", fg="#FF0000")
        
        self.root.mainloop()

    def setData(self):
        data = pd.read_csv(self.file[1])
        return data
    
    def setVarList(self):
        varList = sorted(list(self.data.columns))
        return varList
    
    def setVar(self):
        if(self.varOptions.get()=="Choose a Variable to Query"):
            self.errorMessage1.grid(row=2, column=0, padx=2, pady=2)
        else:
            self.errorMessage1.grid_forget()
            self.variable = self.varOptions.get()
            self.varOptions.grid_forget()
            self.submitButton1.grid_forget()
            tk.Label(self.root, text="Querying " + self.variable).grid(row=0, column=0, padx=2, pady=2)
        
            depVarOptionsList = self.varList.copy()
            depVarOptionsList.insert(0,"None")
            depVarOptionsList.remove(self.variable)
            self.depVarOptions['values'] = depVarOptionsList
            self.depVarOptions.grid(row=1, column=0, padx=2, pady=2)
            self.submitButton2.grid(row=2, column=0, padx=2, pady=2)
    
    def setFilterVar(self):
        if(self.depVarOptions.get()=="Choose a Filter Variable"):
            self.errorMessage2.grid(row=3, column=0, padx=2, pady=2)
        else:
            self.errorMessage2.grid_forget()
            self.filterVar = self.depVarOptions.get()
            self.depVarOptions.grid_forget()
            self.submitButton2.grid_forget()
            tk.Label(self.root, text="based on " + self.filterVar[0]).grid(row=1, column=0, padx=2, pady=2)
            # self.addNewButton.grid(row=2, column=0, padx=2, pady=2)
            self.completeButton.grid(row=2, column=1, padx=2, pady=2)
            self.changeButton.grid(row=2, column=2, padx=2, pady=2)

    # def newFilter(self):
    #     for w in self.root.winfo_children():
    #         w.grid_forget()
    #     self.str = "Querying " + self.variable + " based on "
    #     depVarOptionsList = self.varList.copy()
    #     depVarOptionsList.insert(0,"None")
    #     depVarOptionsList.remove(self.variable)
    #     for var in self.filterVar:
    #         self.str = self.str + var + " and "
    #     tk.Label(self.root, text=self.str).grid(row=0, column=0, padx=2, pady=2)
    #     self.depVarOptions['values'] = depVarOptionsList
    #     self.depVarOptions.set("Choose a Filter Variable")
    #     self.depVarOptions.grid(row=1, column=0, padx=2, pady=2)
    #     self.submitButton3.grid(row=2, column=0, padx=2, pady=2)
    
    # def setNewFilterVar(self):
    #     if(self.depVarOptions.get()=="Choose New Filter Variable"):
    #         self.errorMessage2.grid(row=3, column=0, padx=2, pady=2)
    #     else:
    #         for w in self.root.winfo_children():
    #             w.grid_forget()
    #         self.filterVar.append(self.depVarOptions.get())
    #         tk.Label(self.root, text= self.str + self.depVarOptions.get()).grid(row=0, column=0, padx=2, pady=2)
    #         self.addNewButton.grid(row=1, column=0, padx=2, pady=2)
    #         self.completeButton.grid(row=1, column=1, padx=2, pady=2)
    #         self.changeButton.grid(row=1, column=2, padx=2, pady=2)

    def changeSelection(self):
        for w in self.root.winfo_children():
            w.grid_forget()
        self.varOptions.grid(row=0, column=0, padx=2, pady=2)
        self.submitButton1.grid(row=1, column=0, padx=2, pady=2)
    
    def completeSelection(self):
        self.root.destroy()
    
    def getVar(self):
        return self.variable

    def getFilterVar(self):
        return self.filterVar

    def getData(self):
        return self.data