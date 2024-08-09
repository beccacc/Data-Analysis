import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *
from Operations import Operations
from SelectFiles import SelectFiles
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
        # print(self.varList)
        self.operation = operations.getOperation()
        print("operation: " + self.operation)
        self.confidence = -1
        self.indVarOptions = []
        self.depVarOptions = []
        self.indVar = ""
        self.depVar = ""
        self.indCompleted = False
        self.depCompleted = False
        self.indVars = []
        self.depVars = []
        
        self.root = tk.Tk()
        self.root.title("Select Variables")
        self.root.geometry("400x250")
        self.left = Frame(self.root)
        self.left.pack(side = tk.LEFT)
        self.right = Frame(self.root)
        self.right.pack(side = tk.RIGHT)
        tk.Label(self.left, text="Independent Variable Options: ").grid(row=0, column=0,sticky = W, pady = 2)
        tk.Label(self.right, text="Dependent Variable Options: ").grid(row=0, column=0,sticky = W, pady = 2)
        # self.completeBut = Button(self.root, text = "Perform " + self.operation, operation=self.complete())
        
        self.setVars()
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
                self.depVarOptions.append(var)
    
    def TTest(self):
        for var in self.varList:
            if isinstance(self.data[var].iloc[1], (int, float, np.integer)):
                self.depVarOptions.append(var)
                self.indVarOptions.append(var)
                

    def display(self):
        # print("independent variable options")
        # print(self.indVarOptions)
        for i in range(len(self.indVarOptions)):
            button = tk.Button(self.left, text = self.indVarOptions[i], command=lambda i = self.indVarOptions[i]: self.setInd(i))
            button.grid(row=i+1, column=0,sticky = W, pady = 2)
        for i in range(len(self.depVarOptions)):
            button = tk.Button(self.right, text = self.depVarOptions[i], command=lambda d = self.depVarOptions[i]: self.setDep(d))
            button.grid(row=i+1, column=0,sticky = W, pady = 2)
        
        
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
    
    def setInd(self, i):
        if(self.operation == "Multiple Regression" or self.operation == "MANOVA"):
            self.indVars.append(i)
            tk.Button(self.left, text="Complete Selection", command=lambda : self.completeSelection("ind")).grid(row=len(self.indVarOptions), column=0, sticky=W, pady=2)
            for button in self.left.winfo_children():
                if(button.cget('text') in self.indVar):
                    print(button.cget('text') + " disabled *******")
                    button['state'] = DISABLED
        else:
            self.indVar = i
            for button in self.left.winfo_children():
                button['state'] = DISABLED
            self.indCompleted = True
        if(self.indCompleted == True and self.depCompleted == True):
            self.left.pack_forget()
            self.right.pack_forget()
            # self.completeBut.pack()
        
    
    def setDep(self, d):
        if(self.operation == "MANOVA" or self.operation == "ANOVA"):
            self.depVars.append(d)
            tk.Button(self.right, text="Complete Selection", command=lambda : self.completeSelection("dep")).grid(row=len(self.depVarOptions), column=0, sticky=W, pady=2)
            for button in self.right.winfo_children():
                if(button.cget('text') in self.depVar):
                    button['state'] = DISABLED
        else:
            self.depVar = d
            for button in self.right.winfo_children():
                button['state'] = DISABLED
            self.depCompleted = True
        if(self.indCompleted == True and self.depCompleted == True):
            self.left.pack_forget()
            self.right.pack_forget()
            # self.completeBut.pack()
    
    def completeSelection(self, type):
        if(type == "ind"):
            for button in self.left.winfo_children():
                button.grid_forget()
            self.indCompleted = True
            print()
            Label(self.left, text="Selected Independent Variable(s): ").grid(row=0, column=0, sticky=W, pady=2)
            for i in range(len(self.indVars)):
                Label(self.left, text = self.indVars[i]).grid(row=i+1, column=0, sticky=W, pady=2)
        elif(type == "dep"):
            for button in self.right.winfo_children():
                button.grid_forget()
            if(self.indCompleted != True):
                self.depCompleted = True
            Label(self.right, text="Selected Dependent Variable(s): ").grid(row=0, column=0, sticky=W, pady=2)
            for i in range(len(self.depVars)):
                Label(self.right, text = self.depVars[i]).grid(row=i+1, column=0, sticky=W, pady=2)
    
    def chooseVars(self):
        self.setVars()
        self.display()
    
    def complete(self):
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