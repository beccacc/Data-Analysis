from FileUpload import FileUpload
from SelectFiles import SelectFiles
from Operations import Operations
from ChooseVariables import ChooseVariables


class GraphicalUserInterface:
    def __init__(self):
        print("init0")
        self.fileUpload = FileUpload()
        print("init1")
        self.GraphicalUI()
        print("init2")


    def GraphicalUI(self):
        print("file upload available")
        self.fileUpload.uploadFile()
        print("files selected")
        self.selectFiles = SelectFiles(self.fileUpload)
        self.operation = Operations()
        self.operation.operations()
        self.chooseVariables = ChooseVariables(self, self.selectFiles, self.operation)
        self.chooseVariables.chooseVars(self)