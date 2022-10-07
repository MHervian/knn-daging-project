# Main program
# Import basic modules
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
                            QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import (QPixmap, QFont)

# Import modul - modul program lain
import ResizeImage, KnnInterface

class MainProgram(QWidget):

    def __init__(self):
        super().__init__()

        # Membuat properti class
        self.top = 180
        self.left = 180
        self.width = 300
        self.height = 200
        self.windowTitle = "Aplikasi Menentukan Daging Menggunakan"

        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        self.initUI()

    def initUI(self):
        # Mengambil data gambar untuk cover
        imgFilepath = os.getcwd() + "/resources/beef_cover.jpg"
        self.imageCover = QPixmap(imgFilepath)

        # Membuat label gambar untuk menampung gambar cover
        self.coverImageLabel = QLabel()
        self.coverImageLabel.setPixmap(self.imageCover)
        self.coverImageLabel.setFixedHeight(170)

        # Membuat 2 button
        self.bttnImgManipWindow = QPushButton("Image Processing")
        self.bttnKnnWindow = QPushButton("KNN Processing")

        self.bttnImgManipWindow.setFont(QFont('Sans', 13))
        self.bttnKnnWindow.setFont(QFont('Sans', 13))

        self.bttnImgManipWindow.clicked.connect(self.activateImageProgram)
        self.bttnKnnWindow.clicked.connect(self.activateKnnInterface)

        # Membuat layout horizontal
        self.HMainWindow = QHBoxLayout()
        self.HMainWindow.addStretch(1)
        self.HMainWindow.addWidget(self.bttnImgManipWindow)
        self.HMainWindow.addWidget(self.bttnKnnWindow)

        # Membuat layout vertikal
        self.VMainWindow = QVBoxLayout()
        self.VMainWindow.addWidget(self.coverImageLabel)
        self.VMainWindow.addLayout(self.HMainWindow)

        self.setLayout(self.VMainWindow)
        
        # Jendela program ini tampil
        self.show()

    # Method untuk event click buka pada tombol 'bttnImgManipWindow'
    def activateImageProgram(self):
        self.imageProgram = ResizeImage.ImageResizeProgram()
        self.imageProgram.show()
        self.hide()

    def activateKnnInterface(self):
        self.knnProgram = KnnInterface.KnnProgram()
        self.knnProgram.show()
        self.hide()


if __name__ == '__main__':
    apps = QApplication(sys.argv)
    mainPogram = MainProgram()
    sys.exit(apps.exec_())