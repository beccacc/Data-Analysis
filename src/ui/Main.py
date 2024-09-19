from FileUpload import FileUpload
from SelectFiles import SelectFiles, SelectFile
from Operations import MultiFileOperations, SingleFileOperations
from ChooseVariables import ChooseVariables, ChooseVariable
from DisplayResults import DisplayResultsMulti, DisplayResultsOne
from ChooseUsage import ChooseUsage
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from model.PerformOperation import PerformAnalysis, PerformOperation




def main():
    fileUpload = FileUpload()
    chooseUsage = ChooseUsage()
    if(chooseUsage.getUsage()=="multiFile"):
        selectFiles = SelectFiles(fileUpload)
        operation = MultiFileOperations()
        chooseVariables = ChooseVariables(selectFiles, operation)
        performOperation = PerformAnalysis(chooseVariables, operation)
        displayResults = DisplayResultsMulti(performOperation)
        displayResults.display()
    else:
        selectFile = SelectFile(fileUpload)
        chooseVariable = ChooseVariable(selectFile)
        operation = SingleFileOperations(chooseVariable, selectFile)
        performOperation = PerformOperation(operation)
        # ops = ["MAX", "MIN", "MEAN", "MEDIAN", "MODE", "STDev", "SELECT"]
        displayResults = DisplayResultsOne(performOperation)
    




if __name__ == '__main__':
    main()