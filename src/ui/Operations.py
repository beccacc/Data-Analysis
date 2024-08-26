import tkinter as tk
from tkinter import *
import os

operationSelected = False
operation = ""
confidence = -1

class Operations:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.root.title("Choose an Operation")
        self.multiRegButton = tk.Button(self.root, text="Multiple Regression", command=lambda o="Multiple Regression": self.setOperation(o))
        self.multiRegButton.grid(row=0, column=0, padx=2, pady=2)
        
        self.simpleRegButton = tk.Button(self.root, text="Simple Regression", command=lambda o="Simple Regression": self.setOperation(o))
        self.simpleRegButton.grid(row=1, column=0, padx=2, pady=2)

        self.logRegButton = tk.Button(self.root, text="Logistic Regression", command=lambda o="Logistic Regression": self.setOperation(o))
        self.logRegButton.grid(row=2, column=0, padx=2, pady=2)

        self.TTest1Button = tk.Button(self.root, text="One-tail T-Test", command=self.TTest1)
        self.TTest1Button.grid(row=3, column=0, padx=2, pady=2)

        self.TTest2Button = tk.Button(self.root, text="Two-tail T-Test", command=self.TTest2)
        self.TTest2Button.grid(row=4, column=0, padx=2, pady=2)

        self.ANOVAButton = tk.Button(self.root, text="ANOVA", command=self.ANOVA)
        self.ANOVAButton.grid(row=5, column=0, padx=2, pady=2)

        self.MANOVAButton = tk.Button(self.root, text="MANOVA", command=lambda o="MANOVA": self.setOperation(o))
        self.MANOVAButton.grid(row=6, column=0, padx=2, pady=2)
        
        self.correlationButton = tk.Button(self.root, text="Correlation", command=lambda o="Correlation": self.setOperation(o))
        self.correlationButton.grid(row=7, column=0, padx=2, pady=2)
        
        self.completeButton = Button(self.root, text="Complete Selection", command=self.completeSelection)
        self.changeButton = Button(self.root, text="Change Selection", command=self.changeSelection)

        self.root.mainloop()

    def ANOVA(self):
        self.operation = "ANOVA"
        self.operationDisplay()
        Label(self.root, text="Choose Confidence Level:").grid(row=0, column=1, padx=2, pady=2)
        ANOVA = [0.0005, 0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5]
        for i in range(len(ANOVA)):
            conf= ANOVA[i]
            button = Button(self.root, text = str(conf), command =lambda c=conf: self.setConfidence(c))
            button.grid(row=i+1, column=1, padx=2, pady=2)

    def MANOVA(self):
        self.operation = "MANOVA"
        self.operationDisplay()
        Label(self.root, text="Choose Confidence Level:").grid(row=0, column=1, padx=2, pady=2)
        MANOVA = [0.0005, 0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5]
        for i in range(len(MANOVA)):
            conf= MANOVA[i]
            button = Button(self.root, text = str(conf), command =lambda c=conf: self.setConfidence(c))
            button.grid(row=i+1, column=1, padx=2, pady=2)

    def TTest1(self):
        self.operation = "One-tail T-Test"
        self.operationDisplay()
        Label(self.root, text="Choose Confidence Level:").grid(row=0, column=1, padx=2, pady=2)
        ttest1 = [0.0005, 0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5]
        for i in range(len(ttest1)):
            conf= ttest1[i]
            button = Button(self.root, text = str(conf), command =lambda c=conf: self.setConfidence(c))
            button.grid(row=i+1, column=1, padx=2, pady=2)


    def TTest2(self):
        self.operation = "Two-tail T-Test"
        self.operationDisplay()
        Label(self.root, text="Choose Confidence Level:").grid(row=0, column=1, padx=2, pady=2)
        ttest2 = [0.001, 0.002, 0.01, 0.02, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 1.00]
        for i in range(len(ttest2)):
            conf= ttest2[i]
            button = Button(self.root, text = str(conf), command =lambda c=conf: self.setConfidence(c))
            button.grid(row=i+1, column=1, padx=2, pady=2)


    def setOperation(self, op):
        self.operation = op
        self.operationDisplay()
        self.completeButton.grid(row=0, column=1, padx=2, pady=0)
        self.changeButton.grid(row=1, column=1, padx=2, pady=0)
    
    def getOperation(self):
        return self.operation
    
    def setConfidence(self, conf):
        self.confidence = conf
        Label(self.root, text="Confidence Level: " + str(conf)).grid(row=1, column=0, padx=2, pady=2)
        for button in self.root.grid_slaves(column=1):
            button.grid_forget()
        self.completeButton.grid(row=0, column=1, padx=2, pady=0)
        self.changeButton.grid(row=1, column=1, padx=2, pady=0)
    
    def getConfidence(self):
        return self.confidence
    
    def operationDisplay(self):
        self.multiRegButton.grid_forget()
        self.simpleRegButton.grid_forget()
        self.logRegButton.grid_forget()
        self.TTest1Button.grid_forget()
        self.TTest2Button.grid_forget()
        self.correlationButton.grid_forget()
        self.ANOVAButton.grid_forget()
        self.MANOVAButton.grid_forget()
        Label(self.root, text="Chosen Operation: " + self.operation).grid(row=0, column=0, padx=2, pady=2)
    
    def changeSelection(self):
        self.changeButton.grid_forget()
        self.completeButton.grid_forget()
        for w in self.root.grid_slaves(column=0):
            w.grid_forget()
        self.multiRegButton.grid(row=0, column=0, padx=2, pady=2)
        self.simpleRegButton.grid(row=1, column=0, padx=2, pady=2)
        self.logRegButton.grid(row=2, column=0, padx=2, pady=2)
        self.TTest1Button.grid(row=3, column=0, padx=2, pady=2)
        self.TTest2Button.grid(row=4, column=0, padx=2, pady=2)
        self.ANOVAButton.grid(row=5, column=0, padx=2, pady=2)
        self.MANOVAButton.grid(row=6, column=0, padx=2, pady=2)
        self.correlationButton.grid(row=7, column=0, padx=2, pady=2)
        

    def completeSelection(self):
        self.root.destroy()


        
    

    
    
    