import sys
import os
import pandas as pd
import numpy as np
import scipy.stats as stats
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
# from ChooseVariables import ChooseVariables


class PerformOperation:
    def __init__(self, chooseVariables, operation):
        self.indVar = chooseVariables.getIndVar()
        self.depVar = chooseVariables.getDepVar()
        self.operation = operation.getOperation()
        self.data = chooseVariables.getData()
        if(self.operation == "Two-tail T-Test" or self.operation == "One-tail T-Test"):
            self.confidence = operation.getConfidence()

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
            self.MANOVA()
        else:
            self.correlation()
        
    def TTest(self):
        independent = self.data.lo[:,self.indVar]
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
        if(pVal < self.confidence):
            print("reject null: significant difference")
        else:
            print("")




        

