from mainwindow import Ui_Hamming
from PyQt5 import QtWidgets
import Hamming
import re
import conversion

class MyWindow(Ui_Hamming):
    def __init__(self):
        super().__init__()


    def onLoad(self):
        self.hammingTable.resizeRowsToContents()
        self.hammingTable.resizeColumnsToContents()
        self.repairTable.resizeRowsToContents()
        self.repairTable.resizeColumnsToContents()
        self.convertBtn.clicked.connect(self.convert)
        self.checkBtn.clicked.connect(self.check)
        self.radioPar.setChecked(True)
        self.copyBtn.clicked.connect(self.copyResult)

    def fillHammingTable(self, result):
        self.hammingTable.clearContents()
        data = [2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16]
        p1 = [0,2,4,6,8,10,12,14,16]
        p2 = [1,2,5,6,9,10,13,14]
        p4 = [3,4,5,6,11,12,13,14]
        p8 = [7,8,9,10,11,12,13,14]
        p16 = [15,16]
        full = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        rows = [data, p1, p2, p4, p8, p16, full]

        rowNumber = 0
        for row in rows:
            for column in row:
                self.hammingTable.setItem(rowNumber, column, QtWidgets.QTableWidgetItem(result[column]))
            rowNumber+=1

        self.hammingTable.repaint()





    def fillRepairTable(self, result):
        self.fillReceiveData(result[0])
        if(len(result) > 2):
            self.errorLabel.setText("Error en el bit " + str(result[2]))
            for parity in range(1, 6):
                if parity in result[3]:
                    self.repairTable.setItem(parity, 17, QtWidgets.QTableWidgetItem("Error"))
                else:
                    self.repairTable.setItem(parity, 17, QtWidgets.QTableWidgetItem("Correcto"))
        else:
            for parity in range(1, 6):
                self.repairTable.setItem(parity, 17, QtWidgets.QTableWidgetItem("Correcto"))
                self.errorLabel.setText("No hay errores")


        self.repairTable.repaint()


    def convert(self):
        regex = r'[0+1]{12}'
        input = self.input.text()
        if(re.fullmatch(regex, input)):
            self.hexaLabel.setText(conversion.binahexa(input))
            decimal = conversion.binarioDeci(input)
            self.decimalLabel.setText(str(decimal))
            self.bcdLabel.setText(conversion.deciBCD(decimal))

            result = Hamming.calcular_hamming(input, self.radioPar.isChecked())
            self.fillHammingTable(result)
            strResult = ""
            for char in result:
                strResult += char
            self.hammingResult.setText(strResult)
            self.hammingResult.repaint()

        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Entrada inválida")
            msg.setInformativeText("La entrada debe ser un número binario de 12 bits")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def check(self):

        regex = r'[0+1]{17}'
        input = self.input.text()
        inputList = list(input)
        if(re.fullmatch(regex, input)):
            try:
                result = Hamming.arreglar_hamming(inputList, self.radioPar.isChecked())
                self.fillRepairTable(result)
            except:
                self.errorLabel.setText("Existen 2 o mas errores")
                self.fillReceiveData(inputList)
                self.repairTable.repaint()



        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Entrada inválida")
            msg.setInformativeText("La entrada debe ser un número binario de 17 bits")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def fillReceiveData(self, result):
        self.repairTable.clearContents()
        p1 = [0, 2, 4, 6, 8, 10, 12, 14, 16]
        p2 = [1, 2, 5, 6, 9, 10, 13, 14]
        p4 = [3, 4, 5, 6, 11, 12, 13, 14]
        p8 = [7, 8, 9, 10, 11, 12, 13, 14]
        p16 = [15, 16]
        full = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        rows = [full, p1, p2, p4, p8, p16]

        rowNumber = 0
        for row in rows:
            for column in row:
                self.repairTable.setItem(rowNumber, column, QtWidgets.QTableWidgetItem(result[column]))
            rowNumber += 1

    def copyResult(self):
        self.input.setText(self.hammingResult.text())
        self.input.repaint()
