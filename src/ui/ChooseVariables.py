import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
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
        self.root.geometry("400x250")
        self.indVarOptionsList = ttk.Combobox(self.root, values=self.indVarOptions)
        self.indVarOptionsList.set("Choose an Independent Variable")
        self.depVarOptionsList = ttk.Combobox(self.root, values=self.depVarOptions)
        self.depVarOptionsList.set("Choose a Dependent Variable")

        self.indSubmitButton = tk.Button(self.root, text="Submit", command=self.setInd)
        self.depSubmitButton = tk.Button(self.root, text="Submit", command=self.setDep)


        # tk.Label(self.root, text="Independent Variable Options: ").grid(row=0, column=0,sticky = W, pady = 2)
        # tk.Label(self.root, text="Dependent Variable Options: ").grid(row=0, column=1,sticky = W, pady = 2)
        
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
        if(self.operation == "Multiple Regression" or self.operation == "MANOVA"):
            tk.Label(self.root, text="Choose Independent Variables").grid(row=0, column=0, padx=2, pady=2)
            for i in range(len(self.indVarOptions)):
                button = ttk.Checkbutton(self.root, text=self.indVarOptions[i], command=lambda v=self.indVarOptions[i]: self.setIndVars(v))
                button.grid(row=i+1, column=0, padx=2, pady=2)
            self.indSubmitButton.grid(row=len(self.indVarOptions)+1, column=0, padx=2, pady=2)
        else:
            self.indVarOptionsList.grid(row=0, column=0, padx=2, pady=2)
            self.indSubmitButton.grid(row=3, column=0, padx=2, pady=2)
        if(self.operation == "MANOVA" or self.operation == "ANOVA"):
            tk.Label(self.root, text="Choose Dependent Variables").grid(row=0, column=1, padx=2, pady=2)
            for i in range(len(self.depVarOptions)):
                button = ttk.Checkbutton(self.root, text=self.depVarOptions[i], command=lambda v=self.depVarOptions[i]: self.setDepVars(v))
                button.grid(row=i+1, column=1, padx=2, pady=2)
                self.depSubmitButton.grid(row=len(self.depVarOptions)+1, column=0, padx=2, pady=2)
        else:
            self.depVarOptionsList.grid(row=1, column=1, padx=2, pady=2)
            self.depSubmitButton.grid(row=3, column=1, padx=2, pady=2)

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
            


    # def setInd(self):
    #     if(self.operation == "Multiple Regression" or self.operation == "MANOVA"):
    #         for w in self.root.winfo_children():
    #             if isinstance(w, ttk.Checkbutton):
    #                 if()
    #         self.indVars.append(i)
    #         tk.Button(self.left, text="Complete Selection", command=lambda : self.completeSelection("ind")).grid(row=len(self.indVarOptions), column=0, sticky=W, pady=2)
    #         for button in self.left.winfo_children():
    #             if(button.cget('text') in self.indVar):
    #                 print(button.cget('text') + " disabled *******")
    #                 button['state'] = DISABLED
    #     else:
    #         self.indVar = i
    #         for button in self.left.winfo_children():
    #             button['state'] = DISABLED
    #         self.indCompleted = True
    #     if(self.indCompleted == True and self.depCompleted == True):
    #         self.left.pack_forget()
    #         self.right.pack_forget()
    #         # self.completeBut.pack()
        
    
    # def setDep(self, d):
    #     if(self.operation == "MANOVA" or self.operation == "ANOVA"):
    #         self.depVars.append(d)
    #         tk.Button(self.right, text="Complete Selection", command=lambda : self.completeSelection("dep")).grid(row=len(self.depVarOptions), column=0, sticky=W, pady=2)
    #         for button in self.right.winfo_children():
    #             if(button.cget('text') in self.depVar):
    #                 button['state'] = DISABLED
    #     else:
    #         self.depVar = d
    #         for button in self.right.winfo_children():
    #             button['state'] = DISABLED
    #         self.depCompleted = True
    #     if(self.indCompleted == True and self.depCompleted == True):
    #         self.left.pack_forget()
    #         self.right.pack_forget()
    #         # self.completeBut.pack()
    
    # def completeSelection(self, type):
    #     if(type == "ind"):
    #         for button in self.left.winfo_children():
    #             button.grid_forget()
    #         self.indCompleted = True
    #         print()
    #         Label(self.left, text="Selected Independent Variable(s): ").grid(row=0, column=0, sticky=W, pady=2)
    #         for i in range(len(self.indVars)):
    #             Label(self.left, text = self.indVars[i]).grid(row=i+1, column=0, sticky=W, pady=2)
    #     elif(type == "dep"):
    #         for button in self.right.winfo_children():
    #             button.grid_forget()
    #         if(self.indCompleted != True):
    #             self.depCompleted = True
    #         Label(self.right, text="Selected Dependent Variable(s): ").grid(row=0, column=0, sticky=W, pady=2)
    #         for i in range(len(self.depVars)):
    #             Label(self.right, text = self.depVars[i]).grid(row=i+1, column=0, sticky=W, pady=2)

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


