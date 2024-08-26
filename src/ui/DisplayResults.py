import tkinter as tk



class DisplayResults:
    def __init__(self, performOperation):
        self.results = performOperation.getResults()
        self.operation = self.results[0]
        self.indVar = self.results[1]
        self.depVar = self.results[2]
        self.root = tk.Tk()
        self.root.geometry("400x250")
        # self.frame = tk.Frame(self.root)
        # self.frame.pack()
        self.root.title("Data Analysis Results")
        self.operationLabel = tk.Label(self.root, text="Performing " + self.operation)
        self.operationLabel.grid(row=0, column=0, pady=2)
        self.viewButton
        # self.uploadButton = tk.Button(self.root, text="Upload File", command=self.importFile)
        # self.uploadButton.pack(side=tk.TOP)
        # self.fileLabel = tk.Label(self.root, text = "Files uploaded:")
        # self.fileLabel.pack(side=tk.LEFT)
        # # print("created uploadButton")
        # self.completeButton = tk.Button(self.root, text="Complete Upload", command=self.completeUpload)
        self.root.mainloop()
    

    def display(self):
        if(self.operation == "Multiple Regression"):
            pVals = self.results[3]
            indVarLabel = tk.Label(self.root, text="Independent Variables:")
            indVarLabel.grid(row=1, column=0, pady=2)
            for i in range(len(self.indVar)):
                tk.Label(self.root, text=self.indVar[i]).grid(row=i+1, column=0, pady=2)
            depVarLabel = tk.Label(self.root, text="Dependent Variable: " + self.depVar)
            depVarLabel.grid(row=len(self.indVar)+1, column=0, pady=2)
            self.viewButton = tk.Button(self.root, text = "View Results", command=lambda p=pVals: self.multiReg(p))
            self.viewButton.grid(row = len(self.indVar) + 3, column=0, pady=2)
            # self.multiReg(pVals)
        elif(self.operation == "Simple Regression"):
            pVal = self.results[3]
            indVarLabel = tk.Label(self.root, text="Independent Variable: " + self.indVar)
            indVarLabel.grid(row=1, column=0, pady=2)
            depVarLabel = tk.Label(self.root, text="Dependent Variable: " + self.depVar)
            depVarLabel.grid(row=2, column=0, pady=2)
            viewButton = tk.Button(self.root, text = "View Results", command=lambda p=pVal: self.simpleReg(p))
            viewButton.grid(row = 4, column=0, pady=2)
            # self.simpleReg(pVal)
        elif(self.operation == "Logistic Regression"):
            pVal = self.results[3]
            indVarLabel = tk.Label(self.root, text="Independent Variable: " + self.indVar)
            indVarLabel.grid(row=1, column=0, pady=2)
            depVarLabel = tk.Label(self.root, text="Dependent Variable: " + self.depVar)
            depVarLabel.grid(row=2, column=0, pady=2)
            viewButton = tk.Button(self.root, text = "View Results", command=lambda p=pVal: self.logReg(p))
            viewButton.grid(row = 4, column=0, pady=2)
            # self.logReg(pVal)
        elif(self.operation == "One-Tail T-Test" or self.operation == "Two-Tail T-Test"):
            pVal = self.results[3]
            conf = self.results[4]
            indVarLabel = tk.Label(self.root, text="Independent Variable: " + self.indVar)
            indVarLabel.grid(row=1, column=0, pady=2)
            depVarLabel = tk.Label(self.root, text="Dependent Variable: " + self.depVar)
            depVarLabel.grid(row=2, column=0, pady=2)
            viewButton = tk.Button(self.root, text = "View Results", command=lambda p=pVal, c=conf: self.TTest(p, c))
            viewButton.grid(row = 4, column=0, pady=2)
            # self.TTest(pVal, conf)
        elif(self.operation == "ANOVA"):
            fVal = self.results[3]
            fCrit = self.results[4]
            indVarLabel = tk.Label(self.root, text="Independent Variable: " + self.indVar)
            indVarLabel.grid(row=1, column=0, pady=2)
            depVarLabel = tk.Label(self.root, text="Dependent Variables: ")
            depVarLabel.grid(row=2, column=0, pady=2)
            for i in range(len(self.depVar)):
                tk.Label(self.root, text=self.depVar[i]).grid(row=i+2, column=0, pady=2)
            viewButton = tk.Button(self.root, text = "View Results", command=lambda fV = fVal, fC=fCrit: self.ANOVA(fV, fC))
            viewButton.grid(row = len(self.depVar) + 4, column=0, pady=2)
            # self.TTest(fVal, fCrit)
        # elif(self.operation == "MANOVA"):
        else:
            corr = self.results[3]
            indVarLabel = tk.Label(self.root, text="Independent Variable: " + self.indVar)
            indVarLabel.grid(row=1, column=0, pady=2)
            depVarLabel = tk.Label(self.root, text="Dependent Variable: " + self.depVar)
            depVarLabel.grid(row=2, column=0, pady=2)
            viewButton = tk.Button(self.root, text = "View Results", command=lambda c=corr: self.correlation(c))
            viewButton.grid(row = 4, column=0, pady=2)
            # self.correlation(corr)
    
    def multiReg(self, pVals):
        self.viewButton.pack_forget()
        dep = self.depVar
        for i in range(len(self.indVar)):
            var = self.indVar[i]
            prob = pVals[i]
            label = tk.Label(self.root, text = "As " + var + " increases by 1, " + dep + " increases by " + prob)
            label.grid(row = len(self.indVar) + 5 + i, column=0, pady=2)
    
    def simpleReg(self, pVal):
        self.viewButton.pack_forget()
        label = tk.Label(self.root, text = "As " + self.indVar + " increases by 1, " + self.depVar + " increases by " + pVal)
        label.grid(row = 6, column=0, pady=2)

    def logReg(self, pVal):
        self.viewButton.pack_forget()
        label = tk.Label(self.root, text = "As " + self.indVar + " increases by 1, " + self.depVar + " increases by " + pVal)
        label.grid(row = 6, column=0, pady=2)
    
    def TTest(self, pVal, conf):
        self.viewButton.pack_forget()
        nullLabel = tk.Label(self.root, text="Null Hypothesis: Average " + self.indVar + " is the same as average " + self.depVar)
        nullLabel.grid(row=6, column=0, pady=2)
        if(pVal<conf):
            label = tk.Label(self.root, text = "Reject Null Hypothesis: there is a significant difference between average " + self.indVar + " and average " + self.depVar)
        else:
            label = tk.Label(self.root, text = "Do not reject Null Hypothesis: no proof of a significant difference between average " + self.indVar + " and average " + self.depVar)
        label.grid(row = 8, column=0, pady=2)
    
    def ANOVA(self, fVal, fCrit):
        self.viewButton.pack_forget()
        preLabelText = "average "
        for i in range(len(self.depVar)):
            if(i!=len(self.depVar)-1):
                preLabelText = preLabelText + self.depVar[i] + ", "
            else:
                preLabelText = preLabelText + "and " + self.depVar[i]
        nullLabel = tk.Label(self.root, text="Null Hypothesis: " + preLabelText +  + " are equal for given " + self.indVar)
        nullLabel.grid(row = len(self.indVar) + 6, column = 0, pady=2)
        if(fVal>fCrit):
            label = tk.Label(self.root, text= "Reject Null Hypothesis: " + preLabelText + " are different for given " + self.indVar)
        else:
            label = tk.Label(self.root, text= "Do not reject Null Hypothesis: no proof of significant difference in " + preLabelText + " for given " + self.indVar)
        label.grid(row = len(self.indVar) + 8, column = 0, pady=2)
        # print("ANOVA")
    
    def correlation(self, corr):
        self.viewButton.pack_forget()
        label = tk.Label(self.root, text = "The Pearson correlation coefficient for " + self.indVar + " and " + self.depVar + " is " + str(corr))
        label.grid(row = 6, column=0, pady=2)

