import pandas as pd
import numpy as np
import scipy.stats as stats
from sklearn import linear_model as lm

class PerformAnalysis:
    def __init__(self, chooseVariables, operation):
        self.indVar = chooseVariables.getIndVar()
        self.depVar = chooseVariables.getDepVar()
        self.operation = operation.getOperation()
        self.data = chooseVariables.getDataset()
        if(self.operation == "One-Tail T-Test" or self.operation == "ANOVA"):
            self.confidence = operation.getConfidence()
        if(self.operation == "Two-Tail T-Test"):
            self.confidence = operation.getConfidence()*2
        self.results = []
        self.performOperation()

    def performOperation(self):
        if(self.operation == "Multiple Regression"):
            self.multiReg()
        elif(self.operation == "Simple Regression"):
            self.simpleReg()
        elif(self.operation == "Logistic Regression"):
            self.logReg()
        elif(self.operation == "One-Tail T-Test" or self.operation == "Two-Tail T-Test"):
            self.TTest()
        elif(self.operation == "ANOVA"):
            self.ANOVA()
        else:
            print("*****ERROR: NO VALID OPERATION*****")
        
    def TTest(self):
        independent = self.data.loc[:,self.indVar]
        dependent = self.data.loc[:, self.depVar]
        indVariance = np.var(independent)
        depVariance = np.var(dependent)
        indMean = np.mean(independent)
        depMean = np.mean(dependent)
        indNum = len(independent)
        depNum = len(dependent)
        tVal = (indMean-depMean)/np.sqrt((indVariance/indNum) + (depVariance/depNum))
        i = (indVariance**2) / indNum
        d = (depVariance**2) / depNum
        dofNum = (i + d)**2
        dofDenom = (i**2)/(indNum - 1) + (d**2)/(depNum - 1)
        dof = dofNum / dofDenom
        pVal = stats.t.sf(abs(tVal), dof)
        self.results = [self.operation, self.indVar, self.depVar, pVal, self.confidence]

    def ANOVA(self):
        independent = self.data.loc[:, self.indVar]
        dependents = pd.DataFrame(self.data.loc[:, self.depVar[0]])
        for i in range(len(self.depVar)):
            if(i!=0):
                data = pd.DataFrame(self.data.loc[:, self.depVar[i]])
                dependents = dependents.join(data, how = "inner")
        overallMean = np.mean(dependents)
        SSB=0
        SSE = 0
        sampleSize = 0
        for dep in self.depVar:
            depData = self.data.loc[:, dep]
            size = len(depData)
            sampleSize = sampleSize + size
            sampleMean = np.mean(depData)
            SSB = SSB + size*(sampleMean-overallMean)**2
            for val in depData:
                SSE = SSE + (val - sampleMean)**2
        df1 = len(self.depVar) - 1
        df2 = sampleSize - len(self.depVar)
        MSB = SSB/df1
        MSE = SSE/df2
        fVal = MSB/MSE
        fCrit = stats.f.ppf(float(self.confidence), df1, df2)
        self.results = [self.operation, self.indVar, self.depVar, fVal, fCrit]

    def logReg(self):
        #TODO: FIGURE OUT OUTPUT OF .COEF_
        independent = self.data.loc[:,self.indVar]
        dependent = np.array(self.data.loc[:, self.depVar])
        ind = np.array(independent).reshape(-1,1)
        logR = lm.LogisticRegression(solver='liblinear', random_state=0)
        logR.fit(ind, dependent)
        pVal = logR.coef_
        self.results = [self.operation, self.indVar, self.depVar, pVal]

    def simpleReg(self):
        independent = self.data.loc[:,self.indVar]
        dependent = np.array(self.data.loc[:, self.depVar])
        ind = np.array(independent).reshape(-1,1)
        simpleR = lm.LinearRegression()
        simpleR.fit(ind, dependent)
        pVal = simpleR.coef_
        self.results = [self.operation, self.indVar, self.depVar, pVal]
            
    def multiReg(self):
        independents = pd.DataFrame(self.data.loc[:, self.indVar[0]])
        for i in range(len(self.indVar)):
            if(i!=0):
                data = pd.DataFrame(self.data.loc[:, self.indVar[i]])
                independents = independents.join(data, how = "inner")
        dependent = self.data.loc[:, self.depVar]
        multiR = lm.LinearRegression()
        multiR.fit(independents, dependent)
        pVals = multiR.coef_
        self.results = [self.operation, self.indVar, self.depVar, pVals]
    
    def getResults(self):
        return self.results

class PerformOperation:
    def __init__(self, operations):
        self.operation = operations.getOperation()
        self.string = operations.getString()
        self.filters = operations.getFilters()
        self.varName = operations.getVarName()
        self.filterVarNames = operations.getFilterVarNames()
        if(self.filterVarNames[0]!="None"):
            self.filterValues = operations.getFilterValues()
        if(self.operation == "SELECT"):
            self.results = pd.DataFrame()
        else:
            self.results = float(0.0)

        self.varData = operations.getVarData()
        self.filterData = operations.getFilterData()
        if(self.filterVarNames=="None"):
            self.df = self.varData.to_frame(name=self.varName)
        else:
            self.df = self.filterData.copy()
            d = pd.DataFrame(data = self.varData, columns=[self.varName])
            self.df = self.df.join(d, on=None)
            self.df.dropna()
        self.performFilter()

    def performFilter(self):
        if(self.filterVarNames[0]=="None"):
            self.performOperation(self.df[self.varName])
        elif(len(self.filterVarNames)<=1):
            filtered = []
            data = self.filterData[0]
            filter = self.filters[0]
            filterValue = self.filterValues[0]
            if(filter==">"):
                for i in range(len(self.df)):
                    if(data[i] > filterValue):
                        filtered.append(self.varData[i])
            elif(filter==">="):
                for i in range(len(self.df)):
                    if(data[i] >= filterValue):
                        filtered.append(self.varData[i])
            elif(filter=="="):
                for i in range(len(self.df)):
                    if(data[i] == filterValue):
                        filtered.append(self.varData[i])
            elif(filter=="<="):
                for i in range(len(self.df)):
                    if(data[i] <= filterValue):
                        filtered.append(self.varData[i])
            elif(filter=="<"):
                for i in range(len(self.df)):
                    if(data[i] < filterValue):
                        filtered.append(self.varData[i])
            elif(filter==">="):
                for i in range(len(self.df)):
                    if(data[i] >= filterValue):
                        filtered.append(self.varData[i])
            else:
                for i in range(len(self.df)):
                    if(data[i] != filterValue):
                        filtered.append(self.varData[i])
            self.performOperation(filtered)
        else:
            filtered = []
            for i in range(len(self.df)):
                keep = True
                for f in range(len(self.filterVarNames)):
                    filterData = self.filterData[self.filterVarNames[f]]
                    filter = self.filters[f]
                    filterValue = self.filterValues[f]
                    if(filter==">"):
                        if(filterData[i] <= filterValue):
                            keep = False
                    elif(filter == ">="):
                        if(filterData[i] < filterValue):
                            keep = False
                    elif(filter == "<"):
                        if(filterData[i] >= filterValue):
                            keep = False
                    elif(filter == "<="):
                        if(filterData[i] > filterValue):
                            keep = False
                    elif(filter == "="):
                        if(filterData[i] == filterValue):
                            keep = False
                    else:
                        if(filterData[i] != filterValue):
                            keep = False
                if(keep):
                    filtered.append(self.varData[i])
        self.performOperation(filtered)
                
    def performOperation(self, filtered):
        data = filtered
        if(self.operation=="MAX"):
            max=data[0]
            for i in range(len(data)):
                if(data[i]>max):
                    max=data[i]
            self.results = float(max)
        elif(self.operation=="MIN"):
            min=data[0]
            for i in range(len(data)):
                if(data[i]<min):
                    min=data[i]
            self.results = float(min)
        elif(self.operation=="MEAN"):
            self.results = float(np.mean(data))
        elif(self.operation=="MEDIAN"):
            self.results = float(np.median(data))
        elif(self.operation=="MODE"):
            data=pd.DataFrame(filtered)
            mode = data.mode()
            self.results=float(mode.iloc[0])
        elif(self.operation=="STDev"):
            self.results = float(np.std(data))
        elif(self.operation=="SELECT"):
            self.results = filtered
    
    def getResults(self):
        return self.results

    def getOperation(self):
        return self.operation
    
    def getFilter(self):
        if(self.filterVarNames!="None"):
            return self.filters

    def getFilterValue(self):
        if(self.filterVarNames!="None"):
            return self.filterValues

    def getVarName(self):
        return self.varName
    
    def getFilterVarName(self):
        return self.filterVarNames

    def getVarData(self):
        return self.varData
    
    def getFilterData(self):
        if(self.filterVarNames!="None"):
            return self.filterData
    
    def getString(self):
        return self.string