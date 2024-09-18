import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.multivariate.manova import MANOVA
from sklearn import linear_model as lm
# from sklearn.metrics import classification_report, confusion_matrix

class PerformAnalysis:
    def __init__(self, chooseVariables, operation):
        self.indVar = chooseVariables.getIndVar()
        self.depVar = chooseVariables.getDepVar()
        self.operation = operation.getOperation()
        self.data = chooseVariables.getDataset()
        if(self.operation == "One-Tail T-Test" or self.operation == "ANOVA" or self.operation == "MANOVA"):
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
        elif(self.operation == "MANOVA"):
            #TODO:
            self.MANOVA()
        else:
            self.correlation()
        
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

    # def MANOVA(self):
    #     independents = pd.DataFrame(self.data.loc[:, self.indVar[0]])
    #     for i in range(len(self.indVar)):
    #         if(i!=0):
    #             data = pd.DataFrame(self.data.loc[:, self.indVar[i]])
    #             independents = independents.join(data, how = "inner")
    #     dependents = pd.DataFrame(self.data.loc[:, self.depVar[0]])
    #     for i in range(len(self.depVar)):
    #         if(i!=0):
    #             data = pd.DataFrame(self.data.loc[:, self.depVar[i]])
    #             dependents = dependents.join(data, how = "inner")
    #     manova = MANOVA(endog=independents, exog=dependents).fit()
    #     result = manova.mv_test()

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
        # for i in range(len(self.indVar)):
        #     outputString = outputString + "/n As " + self.indVar[i] + " increases by 1, " + dependent + " increases by " + pVal[i]
        # print(outputString)

    def correlation(self):
        independent = self.data.loc[:,self.indVar]
        dependent = self.data.loc[:, self.depVar]
        if(len(independent) > len(dependent)):
            extra = len(independent) - len(dependent)
            independent.drop(independent.tail(extra).index, inplace = True)
        else:
            extra = len(dependent) - len(independent)
            dependent.drop(dependent.tail(extra).index, inplace = True)
        corr = stats.pearsonr(independent, dependent).statistic
        self.results = [self.operation, self.indVar, self.depVar, corr]
    
    def getResults(self):
        return self.results

class PerformOperation:
    def __init__(self, operations):
        self.operation = operations.getOperation()
        self.string = operations.getString()
        self.filter = operations.getFilter()
        self.varName = operations.getVarName()
        self.filterVarName = operations.getFilterVarName()
        if(self.filterVarName!="None"):
            self.filterValue = int(operations.getFilterValue())
        if(self.operation == "SELECT"):
            self.results = pd.DataFrame()
        else:
            self.results = float(0.0)

        self.variable = operations.getVarData()
        self.filterVariable = operations.getFilterData()
        if(self.filterVarName=="None"):
            self.df = self.variable.to_frame(name=self.varName)
        else:
            self.df=pd.concat({self.varName: self.variable,self.filterVarName: self.filterVariable},axis=1)
            self.df.dropna()
        self.performFilter()


    def performFilter(self):
        if(self.filterVarName=="None"):
            self.performOperation(self.df[self.varName])
        else:
            filtered = []
            if(self.filter==">"):
                for i in range(len(self.df)):
                    if(self.filterVariable[i] > self.filterValue):
                        filtered.append(self.variable[i])
            elif(self.filter==">="):
                for i in range(len(self.df)):
                    if(self.filterVariable[i] >= self.filterValue):
                        filtered.append(self.variable[i])
            elif(self.filter=="="):
                for i in range(len(self.df)):
                    if(self.filterVariable[i] == self.filterValue):
                        filtered.append(self.variable[i])
            elif(self.filter=="<="):
                for i in range(len(self.df)):
                    if(self.filterVariable[i] <= self.filterValue):
                        filtered.append(self.variable[i])
            elif(self.filter=="<"):
                for i in range(len(self.df)):
                    if(self.filterVariable[i] < self.filterValue):
                        filtered.append(self.variable[i])
            elif(self.filter==">="):
                for i in range(len(self.df)):
                    if(self.filterVariable[i] >= self.filterValue):
                        filtered.append(self.variable[i])
            else:
                for i in range(len(self.df)):
                    if(self.filterVariable[i] != self.filterValue):
                        filtered.append(self.variable[i])
            self.performOperation(filtered)


    def performOperation(self, filtered):
        # print(filtered)
        data = filtered
        print(type(data))
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
        if(self.filterVarName!="None"):
            return self.filter

    def getFilterValue(self):
        if(self.filterVarName!="None"):
            return self.filterValue

    def getVarName(self):
        return self.varName
    
    def getFilterVarName(self):
        return self.filterVarName

    def getVarData(self):
        return self.variable
    
    def getFilterData(self):
        if(self.filterVarName!="None"):
            return self.filterVariable
    
    def getString(self):
        return self.string