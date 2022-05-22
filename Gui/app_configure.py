import sys
import csv
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
            self.logger.add_success(" added "+self.quantitytext.text()+" units of "+self.nametext.text()+" each for price "+self.pricetext.text()+" LE")


    def clickme2(self):
        if self.fbox.rowCount() > 1:
            self.fbox.removeRow(1)
        skipfirst=1
        rc=0
        names=[]
        quan=[]
        price=[]
        try:
            with open('stock.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    rc=rc+1
                    if skipfirst==1:
                        skipfirst=0
                    else: 
                     print(row)
                     names.append(row[0])
                     quan.append(row[1])
                     price.append(row[2])
            print(rc)
            self.tableWidget = QTableWidget()
            print(names)
            # set row count
            self.tableWidget.setRowCount(rc)

            # set column count
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
            self.tableWidget.setItem(0, 1, QTableWidgetItem("Quantity"))
            self.tableWidget.setItem(0, 2, QTableWidgetItem("Price"))
            l=0
            for i in names:
                self.tableWidget.setItem(l+1, 0, QTableWidgetItem(names[l]))
                self.tableWidget.setItem(l+1, 1, QTableWidgetItem(quan[l]))
                self.tableWidget.setItem(l+1, 2, QTableWidgetItem(price[l]))
                l=l+1

            self.tableWidget.verticalHeader().setVisible(False)  # remove table index for each column
            self.tableWidget.horizontalHeader().setVisible(False)  # remove table index for each row
            self.fbox.addRow(self.tableWidget)
            self.logger.add_success("dispalyed the stock ")
        except:
            self.logger.add_error("could not display ")
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
       
       self.logger.add_text("checking")
       self.button = QPushButton("stock", self)
       self.button.clicked.connect(self.clickme2)
       self.fbox = QFormLayout()
       self.fbox.addRow(self.button)
       self.win = QWidget()
       self.win.setLayout(self.fbox)
       self.setCentralWidget(self.win)        


   


