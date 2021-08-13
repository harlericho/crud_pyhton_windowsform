from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

import sys
import persons

# functions
def list():
    windows.tableData.setRowCount(0)
    indice =0
    data = persons.get_list()
    for i in data:
        windows.tableData.setRowCount(indice + 1)
        windows.tableData.setItem(indice,0,QTableWidgetItem(str(i[0])))
        windows.tableData.setItem(indice,1,QTableWidgetItem(str(i[1])))
        windows.tableData.setItem(indice,2,QTableWidgetItem(str(i[2])))
        indice +=1

def edit():
    id = windows.tableData.selectedIndexes()[0].data()
    names = windows.tableData.selectedIndexes()[1].data()
    email = windows.tableData.selectedIndexes()[2].data()
    windows.txtID.setText(id)
    windows.txtNames.setText(names)
    windows.txtEmail.setText(email)

def save():
    id = windows.txtID.text()
    names = windows.txtNames.text()
    email = windows.txtEmail.text()
    if validations(names, email):
        return False
    if id == "":
        persons.save_data(names, email)
        alert =QMessageBox()
        alert.setText("Saved data")
        alert.setIcon(QMessageBox.Information)
        alert.exec()
    else:
        update(names,email,id)
        alert =QMessageBox()
        alert.setText("Updating data")
        alert.setIcon(QMessageBox.Information)
        alert.exec()
    list()
    clean()

def update(names,email,id):
    persons.update_data(names, email,id)

def delete():
    id = windows.txtID.text()
    if id != "":
        persons.delete_data(id)
        alert =QMessageBox()
        alert.setText("Deleting data")
        alert.setIcon(QMessageBox.Information)
        alert.exec()
    else:
        persons.delete_data(id)
        alert =QMessageBox()
        alert.setText("Choose a data to delete")
        alert.setIcon(QMessageBox.Critical)
        alert.exec()
    clean()
    list()

# validations
def clean():
    windows.txtID.setText("")
    windows.txtNames.setText("")
    windows.txtEmail.setText("")

def validations(names, email):
    if names == "" or email == "" :
        alert =QMessageBox()
        alert.setText("Null data is not accepted")
        alert.setIcon(QMessageBox.Warning)
        alert.exec()
        return True


# views router - designer windows gt_Designer
app = QtWidgets.QApplication([])
windows = uic.loadUi("./windows.ui")
windows.show()

# views table with data
list()

# table configuration
windows.tableData.setHorizontalHeaderLabels(['#','Names','Email'])
windows.tableData.setEditTriggers(QTableWidget.NoEditTriggers)
windows.tableData.setSelectionBehavior(QTableWidget.SelectRows)

# select table indice id
windows.tableData.cellClicked.connect(edit)

# button configuration
windows.btnSave.clicked.connect(save)
# windows.btnUpdate.clicked.connect(update)
windows.btnDelete.clicked.connect(delete)
windows.btnNew.clicked.connect(clean)


sys.exit(app.exec_())