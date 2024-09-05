import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.multivariate.manova import MANOVA
from sklearn import linear_model as lm

# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
# from ChooseVariables import ChooseVariables


class PerformAnalysis:
    def __init__(self, operations):
        self.operation = operations.getOperation()
        self.filter = operations.getFilter()
        self.filterValue = operations.getFilterValue()
        self.varName = operations.getVarName()
        self.filterVarName = operations.getFilterVarName()
        if(self.operation == "SELECT"):
            self.results = pd.DataFrame()
        else:
            self.results=0


        self.variable = operations.getVarData()
        self.filterVariable = operations.getFilterData()
        if(self.filter=="None"):
            self.df = pd.DataFrame(list(self.variable), columns=['x'], )
        else:
            self.df = pd.DataFrame(list(zip(self.variable, self.filterVariable)), columns=['x', 'y'])
            self.df.dropna()


    def performFilter(self):
        if(self.filter=="None"):
            self.performOperation("None")
        elif(self.filter==">"):
            filtered = self.df.query('y > @self.filterValue')
        elif(self.filter==">="):
            filtered = self.df.query('y >= @self.filterValue')
        elif(self.filter=="="):
            filtered = self.df.query('y == @self.filterValue')
        elif(self.filter=="<="):
            filtered = self.df.query('y <= @self.filterValue')
        elif(self.filter=="<"):
           filtered = self.df.query('y < @self.filterValue')
        elif(self.filter=="!="):
            filtered = self.df.query('y >= @self.filterValue')
        self.performOperation(filtered)


    def performOperation(self, filtered):
        if(filtered== "None"):
            data = self.df['x']
        else:
            data = filtered['x']

        if(self.operation=="MAX"):
            for i in len(data):
                if(data[i]>max):
                    max=data[i]
            self.results = max
        elif(self.operation=="MIN"):
            min=data[0]
            for i in len(data):
                if(data[i]<min):
                    min=data[i]
            self.results = min
        elif(self.operation=="MEAN"):
            mean=np.mean(data)
            self.results = mean
        elif(self.operation=="MEDIAN"):
            median=np.median(data)
            self.results = median
        elif(self.operation=="MODE"):
            mode = data.mode()
            self.results = mode
        elif(self.operation=="STDev"):
            stdev = np.std(data)
            self.results = stdev
        elif(self.operation=="SELECT"):
            self.results = filtered
    
    def getResults(self):
        return self.results