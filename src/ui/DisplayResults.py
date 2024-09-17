import tkinter as tk



class DisplayResultsMulti:
    def __init__(self, performOperation):
        self.results = performOperation.getResults()
        print("  ********RESULTS******: ")
        print(self.results)
        self.str = ""
        self.operation = self.results[0]
        self.indVar = self.results[1]
        self.depVar = self.results[2]
        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        self.root.title("Data Analysis Results")
        self.operationLabel = tk.Label(self.root, text="Performing " + self.operation)
        self.operationLabel.grid(row=0, column=0, pady=2)
        self.explainResultsButton = tk.Button(self.root, text="Explain Results", command=self.explainResults)
        self.display()

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
            viewButton = tk.Button(self.root, text = "View Results", command=lambda p=pVals: self.multiReg(p))
            viewButton.grid(row = len(self.indVar) + 3, column=0, pady=2)
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
            conf = float(self.results[4])
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
        for w in self.root.winfo_children():
            if isinstance(w, tk.Button):
               w.grid_forget()
        dep = self.depVar
        for i in range(len(self.indVar)):
            var = self.indVar[i]
            prob = pVals[i]
            label = tk.Label(self.root, text = "As " + var + " increases by 1, " + dep + " increases by " + prob)
            label.grid(row = len(self.indVar) + 5 + i, column=0, pady=2)
    
    def simpleReg(self, pVal):
        for w in self.root.winfo_children():
            if isinstance(w, tk.Button):
               w.grid_forget()
        label = tk.Label(self.root, text = "As " + self.indVar + " increases by 1, " + self.depVar + " increases by " + pVal)
        label.grid(row = 6, column=0, pady=2)

    def logReg(self, pVal):
        for w in self.root.winfo_children():
            if isinstance(w, tk.Button):
               w.grid_forget()
        label = tk.Label(self.root, text = "As " + self.indVar + " increases by 1, " + self.depVar + " increases by " + pVal)
        label.grid(row = 6, column=0, pady=2)
    
    def TTest(self, pVal, conf):
        for w in self.root.winfo_children():
            if isinstance(w, tk.Button):
               w.grid_forget()
        nullLabel = tk.Label(self.root, text="Null Hypothesis: Average " + self.indVar + " is the same as average " + self.depVar)
        nullLabel.grid(row=6, column=0, pady=2)
        print(type(pVal))
        print(type(conf))
        if(pVal<conf):
            label = tk.Label(self.root, text = "Reject Null Hypothesis: there is a significant difference between average " + self.indVar + " and average " + self.depVar)
            self.txt = "Because our pValue(" + str(pVal) + ") is less than our confidence(" + str(conf) + "), we reject our Null Hypothesis.\n"
            self.txt = self.txt + "Our data shows that there is a significant difference between average " + self.indVar + " and average " + self.depVar
        else:
            label = tk.Label(self.root, text = "Do not reject Null Hypothesis: no proof of a significant difference between average " + self.indVar + " and average " + self.depVar)
            self.txt = "Because our pValue(" + str(pVal) + ") is greater than our confidence(" + str(conf) + "), we cannot reject our Null Hypothesis.\n"
            self.txt = self.txt + "Our data does not show a significant difference between average " + self.indVar + " and average " + self.depVar + "\n"
            self.txt = self.txt + "However, there is not enough information to prove that the averages are equal."
        label.grid(row = 8, column=0, pady=2)
        self.explainResultsButton.grid(row=9, column=0, pady=2)
    
    def ANOVA(self, fVal, fCrit):
        for w in self.root.winfo_children():
            if isinstance(w, tk.Button):
               w.grid_forget()
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
            self.txt = "Because our fValue(" + str(fVal) + ") is greater than our fCritical(" + str(fCrit) + "), we reject our Null Hypothesis.\n"
            self.txt = self.txt + "Our data shows that there is a significant difference between " + preLabelText + " for given " + self.indVar
        else:
            label = tk.Label(self.root, text= "Do not reject Null Hypothesis: no proof of significant difference in " + preLabelText + " for given " + self.indVar)
            self.txt = "Because our fValue(" + str(fVal) + ") is less than our fCritical(" + str(fCrit) + "), we cannot reject our Null Hypothesis.\n"
            self.txt = self.txt + "Our data does not show a significant difference between " + preLabelText + " for given " + self.indVar + "\n"
            self.txt = self.txt + "However, there is not enough information to prove that the averages are equal for given " + self.indVar
        label.grid(row = len(self.indVar) + 8, column = 0, pady=2)
        self.explainResultsButton.grid(row = len(self.indVar) + 9, column = 0, pady=2)
        # print("ANOVA")
    
    def correlation(self, corr):
        for w in self.root.winfo_children():
            if isinstance(w, tk.Button):
               w.grid_forget()
        label = tk.Label(self.root, text = "The Pearson correlation coefficient for " + self.indVar + " and " + self.depVar + " is " + str(corr))
        label.grid(row = 6, column=0, pady=2)


    def explainResults(self):
        for w in self.root.winfo_children():
            w.grid_forget()
        if(self.operation == "One-Tail T-Test" or self.operation == "Two-Tail T-Test"):
            tk.Label(self.root, text="Null Hypothesis: Average " + self.indVar + " is the same as average " + self.depVar).grid(row=0, column=0, padx=2, pady=2)
            tk.Label(self.root, text=self.txt).grid(row = len(self.indVar) + 9, column = 0, pady=2)
        elif(self.operation == "ANOVA"):
            labelText = "Null Hypothesis: Average "
            for i in range(len(self.depVar)):
                if(i!=len(self.depVar)-1):
                    labelText = labelText + self.depVar[i] + ", "
                else:
                    labelText = labelText + "and " + self.depVar[i] + " are equal for given " + self.indVar
            tk.Label(self.root, text=labelText).grid(row = 0, column = 0, pady=2)
            tk.Label(self.root, text=self.txt).grid(row = 1, column = 0, pady=2)
            


class DisplayResultsOne:
    def __init__(self, performOperation):
        self.results = performOperation.getResults()
        
        self.operation = performOperation.getOperation()
        self.filter = performOperation.getFilter()
        self.filterValue = performOperation.getFilterValue()

        self.varName = performOperation.getVarName()
        self.filterVarName = performOperation.getFilterVarName()
        self.variable = performOperation.getVarData()
        self.filterVariable = performOperation.getFilterData()


        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        self.root.title("Data Analysis Results")
        self.operationLabel = tk.Label(self.root, text= performOperation.getString())
        self.operationLabel.grid(row=0, column=0, pady=2)

        self.viewButton = tk.Button(self.root, text = "View Results", command=self.showResults)
        self.viewButton.grid(row = 1, column=0, pady=2)

        self.root.mainloop()

    

    def showResults(self):
        self.operationLabel.grid_forget()
        self.viewButton.grid_forget()
        if(self.operation!="SELECT"):
            txt="The " + self.operation + " value of " + self.varName
            if(self.filterVarName!="None"):
                 txt = txt + " where " + self.filterVarName + " " + self.filter + " " + str(self.filterValue)
            txt = txt + " is " + str(self.results)
            tk.Label(self.root, text=txt).grid(row=0, column=0, padx=2, pady=2)
        else:
            txt="Showing all instances of " + self.varName + " where " + self.filterVarName + " " + self.filter + " " + str(self.filterValue) + ":"
            tk.Label(self.root, text=txt).grid(row=0, column=0, padx=2, pady=2)
            resultsList = tk.Listbox(self.root)
            for r in self.results:
                resultsList.insert(tk.END, r)
            resultsList.grid(row=1, column=0, padx=2, pady=2)
            # scrollbar = tk.Scrollbar(self.root)
            # scrollbar.grid(row=1, column=1, padx=2, pady=2)
            # resultsList.config(yscrollcommand = scrollbar.set)
            # scrollbar.config(command = resultsList.yview)
        
    