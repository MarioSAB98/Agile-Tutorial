import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize
from moduleConfgFrames import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtCore import pyqtSlot
from Gui.logger.logController import LogController


#the class contain the buttons and functions to perform the requiered opreations 

class StandardItem(QStandardItem):#realted to the gui
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class AppConfigWindow(QMainWindow):
    __instance = None  # Singleton Instance

    windowFrame = Ui_MainWindow()



    def __init__(self, toolName, toolIcon):

        super(AppConfigWindow, self).__init__()

        self.windowFrame = Ui_MainWindow()
        self.windowFrame.setupUi(self)

        self.setWindowTitle(toolName)
        self.setWindowIcon(QtGui.QIcon(toolIcon))



        
        # self.parametersAndReferences.setGeometry(500, 70, 850, 500)
        self.parametersAndReferencesRows = QFormLayout()
        self.logger = LogController(self.windowFrame.log)
        self.logger.add_text("Fori_tool Logger")
        self.toolIcon = toolIcon

     
        self.showToolBar()

    @staticmethod
    def getInstance(toolName=None, toolIcon=None):
        if AppConfigWindow.__instance is None:
            AppConfigWindow.__instance = AppConfigWindow(toolName, toolIcon)
        return AppConfigWindow.__instance

    
    

    def showToolBar(self):
# adding the $ options button 
        self.addToolBarItem = QAction("o1", self)
        self.addToolBarItem.setIcon(QtGui.QIcon('Images/plus.png'))
        self.windowFrame.toolBar.addAction(self.addToolBarItem)
        self.addToolBarItem.triggered.connect(self.o1)


        self.generateToolBarItem = QAction(" o4", self)
        self.generateToolBarItem.setIcon(QtGui.QIcon('Images/generate.png'))
        self.windowFrame.toolBar.addAction(self.generateToolBarItem)
        self.generateToolBarItem.triggered.connect(self.o4)



    def clickme(self):
        ok=1
        if self.nametext.text()=="":
            self.logger.add_warning("item name cannot be empty")
            ok=0
        if self.quantitytext.text()=="":
            self.logger.add_warning("qunatity cannot be empty")
            ok=0
            
        if self.pricetext.text()=="":
            self.logger.add_warning("price cannot be empty")
            ok=0
        if ok==1:           
            self.logger.add_success("added"+self.quantitytext.text()+" units of"+self.nametext.text()+" each for price "+self.pricetext.text()+" LE")


    def clickme2(self):
        self.logger.add_text("function 2 check the stock  ")

  

 #layouts for each button 
    def o1(self):
       self.logger.add_text("fill all the fields then click add ")
       self.namel = QLabel("Item name ")
       self.nametext = QLineEdit("")
       self.quantityl = QLabel("quantity")
       self.quantitytext = QLineEdit("")
       self.pricel = QLabel("Price/unit")
       self.pricetext = QLineEdit("")
       self.button = QPushButton("add", self)
       self.button.clicked.connect(self.clickme)
       self.fbox = QFormLayout()
       self.fbox.addRow(self.namel,self.nametext)
       self.fbox.addRow(self.quantityl,self.quantitytext)
       self.fbox.addRow(self.pricel,self.pricetext)
       self.fbox.addRow(self.button)
       self.win = QWidget()
       self.win.setLayout(self.fbox)
       self.setCentralWidget(self.win)
     

    def o4(self):
       
       self.logger.add_text("2 ")
       self.nm = QLineEdit("")
       self.button = QPushButton("check", self)
       self.button.clicked.connect(self.clickme)
       self.fbox = QFormLayout()
       self.fbox.addRow(self.nm)
       self.fbox.addRow(self.button)
       self.win = QWidget()
       self.win.setLayout(self.fbox)
       self.setCentralWidget(self.win)        


   


