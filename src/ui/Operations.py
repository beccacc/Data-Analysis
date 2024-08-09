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
        self.multiRegButton.pack()
        
        self.simpleRegButton = tk.Button(self.root, text="Simple Regression", command=lambda o="Simple Regression": self.setOperation(o))
        self.simpleRegButton.pack()

        self.logRegButton = tk.Button(self.root, text="Logistic Regression", command=lambda o="Logistic Regression": self.setOperation(o))
        self.logRegButton.pack()

        self.TTest1Button = tk.Button(self.root, text="One-tail T-Test", command=self.TTest1)
        self.TTest1Button.pack()

        self.TTest2Button = tk.Button(self.root, text="Two-tail T-Test", command=self.TTest2)
        self.TTest2Button.pack()

        self.MANOVAButton = tk.Button(self.root, text="MANOVA", command=lambda o="MANOVA": self.setOperation(o))
        self.MANOVAButton.pack()
        
        self.correlationButton = tk.Button(self.root, text="Correlation", command=lambda o="Correlation": self.setOperation(o))
        self.correlationButton.pack()
        
        self.ANOVAButton = tk.Button(self.root, text="ANOVA", command=self.ANOVA)
        self.ANOVAButton.pack()

        



        self.root.mainloop()

    def ANOVA(self):
        self.operation = "ANOVA"
        self.multiRegButton.pack_forget()
        self.simpleRegButton.pack_forget()
        self.logRegButton.pack_forget()
        self.TTest1Button.pack_forget()
        self.correlationButton.pack_forget()
        self.MANOVAButton.pack_forget()
        self.TTest2Button.pack_forget()
        ANOVA = [0.0005, 0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5]
        for conf in ANOVA:
            button = tk.Button(self.root, text = str(conf), command = self.setConfidence(conf))
            button.pack()

    def MANOVA(self):
        self.operation = "ANOVA"
        self.multiRegButton.pack_forget()
        self.simpleRegButton.pack_forget()
        self.logRegButton.pack_forget()
        self.TTest1Button.pack_forget()
        self.correlationButton.pack_forget()
        self.MANOVAButton.pack_forget()
        self.TTest2Button.pack_forget()
        MANOVA = [0.0005, 0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5]
        for conf in MANOVA:
            button = tk.Button(self.root, text = str(conf), command = self.setConfidence(conf))
            button.pack()

    def TTest1(self):
        self.operation = "One-tail T-Test"
        self.multiRegButton.pack_forget()
        self.simpleRegButton.pack_forget()
        self.logRegButton.pack_forget()
        self.ANOVAButton.pack_forget()
        self.correlationButton.pack_forget()
        self.MANOVAButton.pack_forget()
        self.TTest2Button.pack_forget()

        ttest1 = [0.0005, 0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5]
        for conf in ttest1:
            button = tk.Button(self.root, text = str(conf), command = self.setConfidence(conf))
            button.pack()

    def TTest2(self):
        self.operation = "Two-tail T-Test"
        self.multiRegButton.pack_forget()
        self.simpleRegButton.pack_forget()
        self.logRegButton.pack_forget()
        self.ANOVAButton.pack_forget()
        self.correlationButton.pack_forget()
        self.MANOVAButton.pack_forget()
        self.TTest1Button.pack_forget()

        ttest2 = [0.001, 0.002, 0.01, 0.02, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 1.00]
        for conf in ttest2:
            button = tk.Button(self.root, text = str(conf), command = self.setConfidence(conf))
            button.pack()
        # show buttons for options for significance


    def setOperation(self, op):
        self.operation = op
        self.root.destroy()
    
    def getOperation(self):
        return self.operation
    
    def setConfidence(self, conf):
        self.confidence = conf
        self.root.destroy()
    
    def getConfidence(self):
        return self.confidence
    

    
    