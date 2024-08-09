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
        
        self.ANOVAButton = tk.Button(self.root, text="ANOVA", command=lambda o="ANOVA": self.setOperation(o))
        self.ANOVAButton.pack()

        self.MANOVAButton = tk.Button(self.root, text="MANOVA", command=lambda o="MANOVA": self.setOperation(o))
        self.MANOVAButton.pack()
        
        self.correlationButton = tk.Button(self.root, text="Correlation", command=lambda o="Correlation": self.setOperation(o))
        self.correlationButton.pack()

        self.TTest1Button = tk.Button(self.root, text="One-tail T-Test", command=self.TTest1)
        self.TTest1Button.pack()

        self.TTest2Button = tk.Button(self.root, text="Two-tail T-Test", command=self.TTest2)
        self.TTest2Button.pack()

        self.root.mainloop()


    def TTest1(self):
        self.operation = "One-tail T-Test"
        self.multiRegButton['state'] = tk.DISABLED
        self.simpleRegButton['state'] = tk.DISABLED
        self.logRegButton['state'] = tk.DISABLED
        self.ANOVAButton['state'] = tk.DISABLED
        self.correlationButton['state'] = tk.DISABLED
        self.MANOVAButton['state'] = tk.DISABLED
        self.TTest2Button['state'] = tk.DISABLED

        button1 = tk.Button(self.root, text = "0.0005", command=lambda conf=0.0005: self.setConfidence(conf))
        button2 = tk.Button(self.root, text = "0.001", command=lambda conf=0.001: self.setConfidence(conf))
        button3 = tk.Button(self.root, text = "0.005", command=lambda conf=0.005: self.setConfidence(conf))
        button4 = tk.Button(self.root, text = "0.01", command=lambda conf=0.01: self.setConfidence(conf))
        button5 = tk.Button(self.root, text = "0.025", command=lambda conf=0.025: self.setConfidence(conf))
        button6 = tk.Button(self.root, text = "0.05", command=lambda conf=0.05: self.setConfidence(conf))
        button7 = tk.Button(self.root, text = "0.10", command=lambda conf=0.1: self.setConfidence(conf))
        button8 = tk.Button(self.root, text = "0.15", command=lambda conf=0.15: self.setConfidence(conf))
        button9 = tk.Button(self.root, text = "0.20", command=lambda conf=0.20: self.setConfidence(conf))
        button10 = tk.Button(self.root, text = "0.25", command=lambda conf=0.25: self.setConfidence(conf))
        button11 = tk.Button(self.root, text = "0.50", command=lambda conf=0.50: self.setConfidence(conf))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()
        button8.pack()
        button9.pack()
        button10.pack()
        button11.pack()

    def TTest2(self):
        self.operation = "Two-tail T-Test"
        self.multiRegButton['state'] = tk.DISABLED
        self.simpleRegButton['state'] = tk.DISABLED
        self.logRegButton['state'] = tk.DISABLED
        self.ANOVAButton['state'] = tk.DISABLED
        self.correlationButton['state'] = tk.DISABLED
        self.MANOVAButton['state'] = tk.DISABLED
        self.TTest1Button['state'] = tk.DISABLED

        button1 = tk.Button(self.root, text = "0.001", command=lambda conf=0.001: self.setConfidence(conf))
        button2 = tk.Button(self.root, text = "0.002", command=lambda conf=0.002: self.setConfidence(conf))
        button3 = tk.Button(self.root, text = "0.01", command=lambda conf=0.01: self.setConfidence(conf))
        button4 = tk.Button(self.root, text = "0.02", command=lambda conf=0.02: self.setConfidence(conf))
        button5 = tk.Button(self.root, text = "0.05", command=lambda conf=0.05: self.setConfidence(conf))
        button6 = tk.Button(self.root, text = "0.10", command=lambda conf=0.10: self.setConfidence(conf))
        button7 = tk.Button(self.root, text = "0.20", command=lambda conf=0.20: self.setConfidence(conf))
        button8 = tk.Button(self.root, text = "0.30", command=lambda conf=0.30: self.setConfidence(conf))
        button9 = tk.Button(self.root, text = "0.40", command=lambda conf=0.40: self.setConfidence(conf))
        button10 = tk.Button(self.root, text = "0.50", command=lambda conf=0.50: self.setConfidence(conf))
        button11 = tk.Button(self.root, text = "1.00", command=lambda conf=1.00: self.setConfidence(conf))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()
        button8.pack()
        button9.pack()
        button10.pack()
        button11.pack()

        


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
    

    
    