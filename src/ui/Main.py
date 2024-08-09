from FileUpload import FileUpload
from SelectFiles import SelectFiles
from Operations import Operations
from ChooseVariables import ChooseVariables
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
# from PerformOperation import PerformOperation



def main():
    fileUpload = FileUpload()
    selectFiles = SelectFiles(fileUpload)
    operation = Operations()
    chooseVariables = ChooseVariables(selectFiles, operation)
    # chooseVariables.chooseVars()
    




if __name__ == '__main__':
    main()
        