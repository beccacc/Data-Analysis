import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.multivariate.manova import MANOVA
from sklearn import linear_model as lm

# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
# from ChooseVariables import ChooseVariables


class PerformOperation:
    def __init__(self, chooseVariables, operation):
        self.indVar = chooseVariables.getIndVar()
        self.depVar = chooseVariables.getDepVar()
        self.operation = operation.getOperation()
        self.data = chooseVariables.getDataSet()
        if(self.operation == "Two-tail T-Test" or self.operation == "One-tail T-Test" or
            self.operation == "ANOVA" or self.operation == "MANOVA"):
            self.confidence = operation.getConfidence()
        self.results = []

    def performOperation(self):
        if(self.operation == "Multiple Regression"):
            self.multiReg()
        elif(self.operation == "Simple Regression"):
            self.simpleReg()
        elif(self.operation == "Logistic Regression"):
            self.logReg()
        elif(self.operation == "One-tail T-Test" or self.operation == "Two-tail T-Test"):
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
        i = indVariance^2 / indNum
        d = depVariance^2 / depNum
        dofNum = (i + d)^2
        dofDenom = (i^2)/(indNum - 1) + (d^2)/(depNum - 1)
        dof = dofNum / dofDenom
        pVal = stats.t.sf(abs(tVal), dof)
        self.results = [self.operation, self.indVar, self.depVar, pVal, self.confidence]
        # if(pVal < self.confidence):
        #     print("reject null: significant difference")
        # else:
        #     print("do not reject null: no significant difference")



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
            SSB = SSB + size*(sampleMean-overallMean)^2
            for val in depData:
                SSE = SSE + (val - sampleMean)^2
        # SST = SSB + SSE
        df1 = len(self.depVar) - 1
        df2 = sampleSize - len(self.depVar)
        MSB = SSB/df1
        MSE = SSE/df2
        fVal = MSB/MSE
        fCrit = stats.f.ppf(self.confidence, df1, df2)
        self.results = [self.operation, self.indVar, self.depVar, fVal, fCrit]
        # if(fVal>fCrit):
        #     print("reject null: significant difference")
        # else:
        #     print("do not reject null: no significant difference")

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
        independent = self.data.loc[:,self.indVar]
        dependent = self.data.loc[:, self.depVar]
        logr = lm.LogisticRegression()
        logr.fit(independent, dependent)
        pVal = np.exp(logr.coef_)
        self.results = [self.operation, self.indVar, self.depVar, pVal]
        # print("As " + independent + " increases by 1, " + dependent + " increases by " + str(pVal))

    def simpleReg(self):
        independent = self.data.loc[:,self.indVar]
        dependent = self.data.loc[:, self.depVar]
        simpleR = lm.LinearRegression()
        simpleR.fit(independent, dependent)
        pVal = simpleR.coef_
        self.results = [self.operation, self.indVar, self.depVar, pVal]
        # print("As " + independent + " increases by 1, " + dependent + " increases by " + str(pVal))
            
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
        # outputString = ""
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
        # print("The Pearson correlation coefficient for " + independent + " and " + dependent + " is " + str(corr))
    
    def getResults(self):
        return self.results