# Modul program untuk mengecilkan gambar/resize image
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
                            QVBoxLayout, QGridLayout, QHBoxLayout,  QLabel, QScrollArea,
                            QFileDialog, QDialog, QMessageBox)
from PyQt5.QtGui import (QPixmap, QFont, QImage)
import mysql.connector
from mysql.connector import Error

# Import OpenCV dan yang bersangkutan
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Import modul
import app

class ImageResizeProgram(QWidget):
    
    def __init__(self):
        super().__init__()

        self.top = 90
        self.left = 90
        self.width = 950
        self.height = 660
        self.windowTitle = "Image Processing - Threshold dan Segmentasi"

        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        # Memulai mengisi elemen2 di program ini 
        self.initUI()

    def initUI(self):
        # Membuat dan memasangkan layout dasar window ini
        basicLayout = QVBoxLayout()

        self.setLayout(basicLayout)

        # Menambahkan tombol button back
        tombolBack = QPushButton('Kembali')

        backMenuLayout = QHBoxLayout()
        backMenuLayout.addWidget(tombolBack)
        backMenuLayout.addStretch(1)

        basicLayout.addLayout(backMenuLayout)

        # Menambahkan tombol menampilkan file gambar
        tombolBukaGambar = QPushButton('Open Image')
        tombolResetGambar = QPushButton('Clear Image')

        imageOpsLayout = QHBoxLayout()
        imageOpsLayout.addWidget(tombolBukaGambar)
        imageOpsLayout.addWidget(tombolResetGambar)
        imageOpsLayout.addStretch(1)

        basicLayout.addLayout(imageOpsLayout)

        # Membuat bagian workspace untuk manipulasi gambar
        # #1 Display gambar
        sampelGambar = QLabel()
        sampelGambar.setScaledContents(True)
        tombolResize = QPushButton('Resize Gambar')

        self.gambar1ScrollArea = QScrollArea()
        self.gambar1ScrollArea.setWidget(sampelGambar)

        gambar1VerticalLayout = QVBoxLayout()
        gambar1VerticalLayout.addWidget(self.gambar1ScrollArea)
        gambar1VerticalLayout.addWidget(tombolResize)

        # #2 Hasil gambar
        hasilGambar = QLabel()
        hasilGambar.setScaledContents(True)
        tombolSimpanGambar = QPushButton('Simpan Gambar')
        tombolHitungRGB = QPushButton('Hitung Nilai RGB')

        self.gambar2ScrollArea = QScrollArea()
        self.gambar2ScrollArea.setWidget(hasilGambar)

        menuOperasiHasilGambarLayout = QHBoxLayout()
        menuOperasiHasilGambarLayout.addWidget(tombolSimpanGambar)
        menuOperasiHasilGambarLayout.addWidget(tombolHitungRGB)

        gambar2VerticalLayout = QVBoxLayout()
        gambar2VerticalLayout.addWidget(self.gambar2ScrollArea)
        gambar2VerticalLayout.addLayout(menuOperasiHasilGambarLayout)

        # Menggabungkan dua bagian display gambar tersebut
        displayDuaGambarLayout = QHBoxLayout()
        displayDuaGambarLayout.addLayout(gambar1VerticalLayout)
        displayDuaGambarLayout.addLayout(gambar2VerticalLayout)

        basicLayout.addLayout(displayDuaGambarLayout)

        # Styling button font 
        tombolBack.setFont(QFont('Sans', 13))
        tombolBukaGambar.setFont(QFont('Sans', 13))
        tombolResetGambar.setFont(QFont('Sans', 13))
        tombolHitungRGB.setFont(QFont('Sans', 13))
        tombolResize.setFont(QFont('Sans', 13))
        tombolSimpanGambar.setFont(QFont('Sans', 13))

        # Pasang event click pada setiap button
        tombolBack.clicked.connect(self.closeThisProgram)
        tombolBukaGambar.clicked.connect(self.bukaFileGambar)
        tombolResetGambar.clicked.connect(self.resetGambar)
        tombolResize.clicked.connect(self.resizeGambar)
        tombolSimpanGambar.clicked.connect(self.simpanGambar)
        tombolHitungRGB.clicked.connect(self.hitungRGB)

    def closeThisProgram(self):
        self.mainProgram = app.MainProgram()
        self.mainProgram.show()
        self.hide()

    def bukaFileGambar(self):
        
        # Bersihkan semua workspace gambar
        self.resetGambar()

        fname = QFileDialog.getOpenFileName(self, 'Open file','H:\'', "Image files (*.jpg *.png)")
        
        # Mengambilkan alamat filepath gambar tersebut
        self.imagePath = fname[0]
        # Membuat elemen gambar dengan QPixmap
        filePixmapGambar = QPixmap(self.imagePath)
        
        sampelGambar = QLabel()
        sampelGambar.setPixmap(filePixmapGambar)
        sampelGambar.resize(filePixmapGambar.width(), filePixmapGambar.height())

        self.gambar1ScrollArea.setWidget(sampelGambar)

    def resetGambar(self):
        sampelGambar = QLabel()
        sampelGambar.setPixmap(QPixmap())
        sampelGambar.resize(1,1)
        self.imagePath = ''

        self.gambar1ScrollArea.setWidget(sampelGambar)
        self.gambar2ScrollArea.setWidget(sampelGambar)

    def resizeGambar(self):
        citra = cv2.imread(self.imagePath, cv2.IMREAD_UNCHANGED)

        # Melakukan pengecilan gambar dengan method resize()
        jumBaris, jumKolom = citra.shape[:2]

        self.citraResized = cv2.resize(citra, (int(0.1 * jumKolom), int(0.15 * jumBaris)))

        # Menampilkan di Container sebelah gambar
        height, width = self.citraResized.shape[:2]
        bytesPerLine = 3 * width

        citraTampil = cv2.cvtColor(self.citraResized, cv2.COLOR_BGR2RGB)

        # Konversi hasil citra akhir tadi ke object QImage dengan format 24 bit (RGB888 = 8-8-8)
        img = QImage(citraTampil, width, height, bytesPerLine, QImage.Format_RGB888)
        hasilCitraPixmap = QPixmap.fromImage(img)

        # Tampilkan 
        sampelGambar = QLabel()
        sampelGambar.setPixmap(hasilCitraPixmap)
        sampelGambar.setScaledContents(True)
        sampelGambar.resize(hasilCitraPixmap.width(), hasilCitraPixmap.height())

        self.gambar2ScrollArea.setWidget(sampelGambar)

    def simpanGambar(self):
        height, width = self.citraResized.shape[:2]
        bytesPerLine = 3 * width
        citraTampil = cv2.cvtColor(self.citraResized, cv2.COLOR_BGR2RGB)
        img = QImage(citraTampil, width, height, bytesPerLine, QImage.Format_RGB888)

        # selecting file path 
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", 
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ") 
  
        # if file path is blank return back 
        if filePath == "": 
            return
          
        # saving canvas at desired path 
        img.save(filePath)

    def hitungRGB(self):
        
        # Hitung masing2 nilai rata2 channel BGR tersebut
        blue = np.mean(self.citraResized[:,:,0], axis=0)
        avgBlue = round(np.mean(blue, axis=0), 2)

        green = np.mean(self.citraResized[:,:,1], axis=0)
        avgGreen = round(np.mean(green, axis=0), 2)

        red = np.mean(self.citraResized[:,:,2], axis=0)
        avgRed = round(np.mean(red, axis=0), 2)

        # Menampilkan dialog untu hasil perhitungan BGR
        windowDialog = QDialog(self)

        vBoxResult = QVBoxLayout()

        # konversi nilai int menjadi string
        avgBlue = str(avgBlue)
        avgGreen = str(avgGreen)
        avgRed = str(avgRed)

        textBlue = QLabel('Blue : ' + avgBlue)
        textGreen = QLabel('Green : ' + avgGreen)
        textRed = QLabel('Red : ' + avgRed)

        vBoxResult.addWidget(textBlue)
        vBoxResult.addWidget(textGreen)
        vBoxResult.addWidget(textRed)

        windowDialog.setLayout(vBoxResult)
        windowDialog.show()