# Main program
# Import basic modules
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
                            QVBoxLayout, QGridLayout, QHBoxLayout,  QLabel, QScrollArea,
                            QFileDialog, QDialog, QMessageBox, QTableWidget, QTableWidgetItem, QTextEdit)
from PyQt5.QtGui import (QPixmap, QFont)

class MainProgram(QWidget):

    def __init__(self):
        super().__init__()

        # Membuat properti class
        self.top = 130
        self.left = 130
        self.windowTitle = "Testing Tampilan Desktop"

        # self.setGeometry(self.top, self.left, self.width, self.height)
        # self.setMaximumSize(self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        self.initUI()

    def initUI(self):
        # Mengambil data gambar untuk cover
        self.gridLayout = QGridLayout()
        
        textEdit1 = QTextEdit('Text Edit 1')
        textEdit2 = QTextEdit('Text Edit 2')
        textEdit3 = QTextEdit('Text Edit 3')
        textEdit4 = QTextEdit('Text Edit 4')
        textEdit5 = QTextEdit('Text Edit 5')
        textEdit6 = QTextEdit('Text Edit 6')
        
        self.gridLayout.addWidget(textEdit1, 0, 0)
        self.gridLayout.addWidget(textEdit2, 0, 1, 2, 2)
        self.gridLayout.addWidget(textEdit3, 0, 3)
        self.gridLayout.addWidget(textEdit4, 1, 0)
        self.gridLayout.addWidget(textEdit5, 2, 1)
        self.gridLayout.addWidget(textEdit6, 2, 2)

        self.setLayout(self.gridLayout)
        self.show()

if __name__ == '__main__':
    apps = QApplication(sys.argv)
    mainPogram = MainProgram()
    sys.exit(apps.exec_())