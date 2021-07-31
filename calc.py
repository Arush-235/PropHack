from PyQt5 import QtCore, QtGui, QtWidgets
import math

def countInscribed(R1, R2):

    if (R2 > R1):
        return 0
    angle = 0
    ratio = 0
    number_of_circles = 0
    ratio = R2 / (R1 - R2)
    if (R1 < 2 * R2):
        number_of_circles = 1
    else:
        angle = (abs(math.asin(ratio) * 180) / 3.14159265)
        number_of_circles = (360 / (2 * math.floor(angle)))
    return number_of_circles

def sumFloor(n):
    s=0
    for i in range(n):
        s+=i
    return s


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 731)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 211, 61))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 350, 631, 25))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate_everything)
        self.density = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.density.setGeometry(QtCore.QRect(340, 120, 141, 31))
        self.density.setObjectName("density")
        self.P = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.P.setGeometry(QtCore.QRect(340, 150, 141, 31))
        self.P.setObjectName("P")
        self.h = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.h.setGeometry(QtCore.QRect(340, 180, 141, 31))
        self.h.setObjectName("h")
        self.w = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.w.setGeometry(QtCore.QRect(340, 270, 141, 31))
        self.w.setObjectName("w")
        self.N = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.N.setGeometry(QtCore.QRect(340, 210, 141, 31))
        self.N.setObjectName("N")
        self.l = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.l.setGeometry(QtCore.QRect(340, 240, 141, 31))
        self.l.setObjectName("l")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 231, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 160, 241, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 90, 201, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 190, 231, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 220, 231, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 250, 231, 20))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 280, 231, 20))
        self.label_9.setObjectName("label_9")
        self.SolarCellRequired = QtWidgets.QComboBox(self.centralwidget)
        self.SolarCellRequired.setGeometry(QtCore.QRect(510, 120, 191, 31))
        self.SolarCellRequired.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SolarCellRequired.setObjectName("SolarCellRequired")
        self.SolarCellRequired.addItem("")
        self.SolarCellRequired.addItem("")
        self.roofMountOnly = QtWidgets.QComboBox(self.centralwidget)
        self.roofMountOnly.setGeometry(QtCore.QRect(510, 200, 191, 31))
        self.roofMountOnly.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.roofMountOnly.setObjectName("roofMountOnly")
        self.roofMountOnly.addItem("")
        self.roofMountOnly.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(510, 170, 201, 20))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(510, 250, 231, 20))
        self.label_10.setObjectName("label_10")
        self.FOCdia = QtWidgets.QComboBox(self.centralwidget)
        self.FOCdia.setGeometry(QtCore.QRect(510, 280, 191, 31))
        self.FOCdia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FOCdia.setObjectName("FOCdia")
        self.FOCdia.addItem("")
        self.FOCdia.addItem("")
        self.circlesInside = QtWidgets.QLabel(self.centralwidget)
        self.circlesInside.setGeometry(QtCore.QRect(70, 410, 271, 17))
        self.circlesInside.setObjectName("circlesInside")
        self.areaLSC = QtWidgets.QLabel(self.centralwidget)
        self.areaLSC.setGeometry(QtCore.QRect(70, 450, 281, 17))
        self.areaLSC.setObjectName("areaLSC")
        self.FOClength = QtWidgets.QLabel(self.centralwidget)
        self.FOClength.setGeometry(QtCore.QRect(70, 490, 261, 17))
        self.FOClength.setObjectName("FOClength")
        self.FOCcost = QtWidgets.QLabel(self.centralwidget)
        self.FOCcost.setGeometry(QtCore.QRect(70, 530, 261, 17))
        self.FOCcost.setObjectName("FOCcost")
        self.equipCost = QtWidgets.QLabel(self.centralwidget)
        self.equipCost.setGeometry(QtCore.QRect(70, 570, 281, 17))
        self.equipCost.setObjectName("equipCost")
        self.SolarCellCost = QtWidgets.QLabel(self.centralwidget)
        self.SolarCellCost.setGeometry(QtCore.QRect(70, 610, 271, 17))
        self.SolarCellCost.setObjectName("SolarCellCost")
        self.breakeven = QtWidgets.QLabel(self.centralwidget)
        self.breakeven.setGeometry(QtCore.QRect(400, 610, 321, 17))
        self.breakeven.setObjectName("breakeven")
        self.LSCcost = QtWidgets.QLabel(self.centralwidget)
        self.LSCcost.setGeometry(QtCore.QRect(400, 410, 301, 17))
        self.LSCcost.setObjectName("LSCcost")
        self.MoneySaved = QtWidgets.QLabel(self.centralwidget)
        self.MoneySaved.setGeometry(QtCore.QRect(400, 530, 321, 17))
        self.MoneySaved.setObjectName("MoneySaved")
        self.TotalCost = QtWidgets.QLabel(self.centralwidget)
        self.TotalCost.setGeometry(QtCore.QRect(400, 450, 301, 17))
        self.TotalCost.setObjectName("TotalCost")
        self.EnergySaved = QtWidgets.QLabel(self.centralwidget)
        self.EnergySaved.setGeometry(QtCore.QRect(400, 490, 351, 17))
        self.EnergySaved.setObjectName("EnergySaved")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
        self.menubar.setObjectName("menubar")
        self.menuArush_loves_sunlight = QtWidgets.QMenu(self.menubar)
        self.menuArush_loves_sunlight.setObjectName("menuArush_loves_sunlight")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArush_loves_sunlight.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def FOCBundle(self):
        if self.FOCdia.currentIndex() ==0:
            r = 3.5
        else:
            r = 4.2
        return countInscribed(70,r)
 
    def LSC_exposed_area(self):
        return float(self.N) * float(self.l) * float(self.w) * float(self.density) * float(self.P) / 1360

    def TotalFOCLength(self):
        return (self.N*self.h) + self.N * (self.l + self.w*self.l/(math.sqrt(1/self.density)))
    def FOC_cost(self):
        return float(self.TotalFOCLength()) * 1.9
    
    def Solar_cost(self):
        if self.SolarCellRequired.currentIndex()==0:
            return (self.density*self.N*self.w*self.l*self.P)/400 * 200
        elif self.SolarCellRequired.currentIndex()==1:
            return 0

    def LSC_cost(self):
        return 10*float(self.LSC_exposed_area())

    def equipmentCost(self):
        return 24*(self.N+1) + 2.8*self.N*self.w*self.l*self.density/3 + 20*self.N 

    def totalCost(self):
        return self.equipmentCost() + self.LSC_cost() + self.Solar_cost() + self.FOC_cost()
    
    def energySave(self):
        return self.density*self.N*self.w*self.l*365*24
    
    def moneySave(self):
        return self.density*self.N*self.w*self.l*365*24/1000 * 0.11

    def calculate_everything(self):
        self.N = float(str(self.N.toPlainText()))
        self.P = float(str(self.P.toPlainText()))
        self.w = float(str(self.w.toPlainText()))
        self.l = float(str(self.l.toPlainText()))
        self.density = float(str(self.density.toPlainText()))
        self.h = float(str(self.h.toPlainText()))
        self.circlesInside.setText(f"FOCs per bundle =  {self.FOCBundle()}")
        self.areaLSC.setText(f"Exposed Area on LSC = {self.LSC_exposed_area()} m")
        self.FOClength.setText(f"Total FOC Length =  {self.TotalFOCLength()} m" )
        self.FOCcost.setText(f"Cost of FOC = $ {self.FOC_cost()}")
        self.equipCost.setText(f"Cost of Rest Equipment = $ {self.equipmentCost()}")
        self.SolarCellCost.setText(f"Cost of Solar Cell System = $ {self.Solar_cost()}" )
        self.LSCcost.setText(f"Cost of LSC = $ {self.LSC_cost()}")
        self.TotalCost.setText(f"Total Cost = $ {self.totalCost()}")
        self.EnergySaved.setText(f"Energy Saved / annum = {self.energySave()/1000} KWh")
        self.MoneySaved.setText(f"Money Saved / annum = $ {self.moneySave()}")
        self.breakeven.setText(f"Breakeven duration : {int(self.totalCost() / self.moneySave())} years")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NaturaLight System Calculator"))
        self.pushButton.setText(_translate("MainWindow", "Calculate Parameters"))
        self.density.setPlainText(_translate("MainWindow", "0.125"))
        self.P.setPlainText(_translate("MainWindow", "9"))
        self.h.setPlainText(_translate("MainWindow", "5.5"))
        self.w.setPlainText(_translate("MainWindow", "30"))
        self.N.setPlainText(_translate("MainWindow", "4"))
        self.l.setPlainText(_translate("MainWindow", "35"))
        self.label_2.setText(_translate("MainWindow", "Number of light outlets / m^2"))
        self.label_3.setText(_translate("MainWindow", "Max. Power per spot luminaire (W)"))
        self.label_4.setText(_translate("MainWindow", "Solar Cell Backup Required?"))
        self.label_5.setText(_translate("MainWindow", "Ceiling height / floor (m)"))
        self.label_6.setText(_translate("MainWindow", "Number of floors"))
        self.label_7.setText(_translate("MainWindow", "Length of floor (m)"))
        self.label_9.setText(_translate("MainWindow", "Width of floor (m)"))
        self.SolarCellRequired.setItemText(0, _translate("MainWindow", "Yes"))
        self.SolarCellRequired.setItemText(1, _translate("MainWindow", "Nope"))
        self.roofMountOnly.setItemText(0, _translate("MainWindow", "Nope"))
        self.roofMountOnly.setItemText(1, _translate("MainWindow", "Yes"))
        self.label_8.setText(_translate("MainWindow", "Sideways Mounting?"))
        self.label_10.setText(_translate("MainWindow", "Diameter of Fibre Optic Cable"))
        self.FOCdia.setItemText(0, _translate("MainWindow", "5 mm"))
        self.FOCdia.setItemText(1, _translate("MainWindow", "6 mm"))
        self.circlesInside.setText(_translate("MainWindow", "FOCs per bundle"))
        self.areaLSC.setText(_translate("MainWindow", "Exposed Area on LSC (m^2)"))
        self.FOClength.setText(_translate("MainWindow", "Total FOC Length (m)"))
        self.FOCcost.setText(_translate("MainWindow", "Cost of FOC ($)"))
        self.equipCost.setText(_translate("MainWindow", "Cost of Rest Equipment ($)"))
        self.SolarCellCost.setText(_translate("MainWindow", "Cost of Solar Cell System ($)"))
        self.breakeven.setText(_translate("MainWindow", "Breakeven duration (years)"))
        self.LSCcost.setText(_translate("MainWindow", "Cost of LSC ($)"))
        self.MoneySaved.setText(_translate("MainWindow", "Money saved / m^2 / annum ($)"))
        self.TotalCost.setText(_translate("MainWindow", "Total Cost ($)"))
        self.EnergySaved.setText(_translate("MainWindow", "Energy Saved / m^2 / annum (W)"))
        self.menuArush_loves_sunlight.setTitle(_translate("MainWindow", "Arush loves sunlight"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

