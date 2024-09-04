from FileUpload import FileUpload
from SelectFiles import SelectFiles
from Operations import Operations
from ChooseVariables import ChooseVariables
from DisplayResults import DisplayResults
from ChooseUsage import ChooseUsage
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from model.PerformOperation import PerformOperation




def main():
    fileUpload = FileUpload()
    selectFiles = SelectFiles(fileUpload)
    # chooseUsage = ChooseUsage()
    operation = Operations()
    chooseVariables = ChooseVariables(selectFiles, operation)
    performOperation = PerformOperation(chooseVariables, operation)
    displayResults = DisplayResults(performOperation)
    displayResults.display()
 
    # chooseVariables.chooseVars()
    




if __name__ == '__main__':
    main()