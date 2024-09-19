import pandas as pd

class ReadFile:
    def __init__(self, selectFiles):
        self.varList = []
        self.data = []
        self.files = selectFiles.getSelection()
        self.readCSVFile(self, self.files)
    
    def readCSVFile(self, file):
        filePath = file[1]
        self.data = pd.read_csv(filePath)
        self.varList = self.data.columns()
    
    def getData(self):
        return self.data
    
    def getVarList(self):
        return self.varList
        