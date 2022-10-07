# Program image processing
# Import framework PyQt5
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
                            QVBoxLayout, QGridLayout, QHBoxLayout,  QLabel, QScrollArea,
                            QFileDialog)
from PyQt5.QtGui import (QPixmap, QFont, QImage)

# Import OpenCV dan yang bersangkutan
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Import modul
import apps

class ImageProcessingProgram(QWidget):
    def __init__(self):
        super().__init__()

        self.top = 200
        self.left = 200
        self.width = 800
        self.height = 800
        self.windowTitle = "Image Processing - Threshold dan Segmentasi"

        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        # Memulai mengisi elemen2 di program ini 
        self.initUI()

    def initUI(self):
        # Membuat layout horizontal
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout2 = QHBoxLayout()

        # Membuat 4 button
        self.bttnOpenImage = QPushButton("Open Image")
        self.bttnClearImage = QPushButton("Clear Image")
        self.bttnThresSegment = QPushButton("Thresholding && Segmentasi")
        self.bttnSaveImage = QPushButton("Save Image")
        self.bttnHitungRGB = QPushButton("Calculate RGB")
        self.bttnBack = QPushButton("Back to Main")

        self.bttnOpenImage.setFont(QFont('Sans', 13))
        self.bttnClearImage.setFont(QFont('Sans', 13))
        self.bttnThresSegment.setFont(QFont('Sans', 13))
        self.bttnSaveImage.setFont(QFont('Sans', 13))
        self.bttnHitungRGB.setFont(QFont('Sans', 13))
        self.bttnBack.setFont(QFont('Sans', 13))

        # Menyambungkan dengan event klik
        self.bttnBack.clicked.connect(self.backToMain)
        self.bttnOpenImage.clicked.connect(self.getImage)
        self.bttnClearImage.clicked.connect(self.clearImage)
        self.bttnThresSegment.clicked.connect(self.prosesManipulasiGambar)
        self.bttnSaveImage.clicked.connect(self.saveImage)
        self.bttnHitungRGB.clicked.connect(self.calculateRGBMean)

        self.hBoxLayout.addWidget(self.bttnOpenImage)
        self.hBoxLayout.addWidget(self.bttnClearImage)
        self.hBoxLayout.addWidget(self.bttnThresSegment)
        self.hBoxLayout.addWidget(self.bttnSaveImage)
        self.hBoxLayout.addWidget(self.bttnHitungRGB)
        self.hBoxLayout.addStretch(1)

        self.hBoxLayout2.addWidget(self.bttnBack)
        self.hBoxLayout2.addStretch(1)

        # Membuat elemen gambar
        self.sampelGambar = QLabel()
        self.sampelGambar.setScaledContents(True)

        # Elemen gambar diberi elemen scrolling
        self.scrollAreaPicture = QScrollArea()
        self.scrollAreaPicture.setWidget(self.sampelGambar)
        self.scrollAreaPicture.setWidgetResizable(False)

        # Membuat layout model vertikal
        self.vBox = QVBoxLayout()
        self.vBox.addLayout(self.hBoxLayout2)
        self.vBox.addLayout(self.hBoxLayout)
        self.vBox.addWidget(self.scrollAreaPicture)

        # Pasang layout vertikal tadi ke widget
        self.setLayout(self.vBox)

    # Method untuk mengambil data gambar dari komputer
    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','H:\'', "Image files (*.jpg *.png)")
        
        # Mengambilkan alamat filepath gambar tersebut
        self.imagePath = fname[0]
        # Membuat elemen gambar dengan QPixmap
        self.fileGambar = QPixmap(self.imagePath)
        self.sampelGambar.setPixmap(self.fileGambar)
        self.sampelGambar.resize(self.fileGambar.width(), self.fileGambar.height())
    
    # Method untuk menghapus gambar yang muncul di window
    def clearImage(self):
        self.sampelGambar.setPixmap(QPixmap())
        self.sampelGambar.resize(1,1)
        self.imagePath = ''

    # Method untuk tombol kembali ke program utama
    def backToMain(self):
        self.mainProgram = apps.MainProgram()
        self.mainProgram.show()
        self.hide()

    # Proses thresholding dan segmentasi gambar daging
    def prosesManipulasiGambar(self):
        # Membaca gambar yang ingin diproses
        self.sampelCitra = cv2.imread(self.imagePath, cv2.IMREAD_UNCHANGED)

        # Konversi warna gambar, BGR (Blue, Green, Red) ke HSV (Hue, Saturation, Value)
        hsv = cv2.cvtColor(self.sampelCitra, cv2.COLOR_BGR2HSV)

        # Ambil channel Saturasi dari gambar hsv tersebut
        saturasi = hsv[:,:,1]

        # Menentukan area biner dengan threshold metode Otsu
        ambang, hasilThres = cv2.threshold(saturasi, 128, 255, cv2.THRESH_OTSU)

        # Ubah sampel gambar berwarna menjadi keabu-abuan
        grayImage = cv2.cvtColor(self.sampelCitra, cv2.COLOR_BGR2GRAY)

        # Pisahkan objek dengan background pada gambar abu2 tersebut
        self.sampelCitraAkhir = np.bitwise_and(grayImage, hasilThres)

        # Ubah kembali gambar akhir menjadi berwarna
        self.sampelCitraAkhir2 = cv2.cvtColor(self.sampelCitraAkhir, cv2.COLOR_GRAY2BGR)

        # Menggunakan subplot dari matplotlib, untuk menampilkan perbandingan setiap gambar

        # rgbCitra = cv2.cvtColor(self.sampelCitra, cv2.COLOR_BGR2RGB)
        # hasilThresColor = cv2.cvtColor(hasilThres, cv2.COLOR_GRAY2RGB)
        # rgbCitra2 = cv2.cvtColor(self.sampelCitraAkhir, cv2.COLOR_BGR2RGB)

        # plt.subplot(1, 4, 1)
        # plt.imshow(rgbCitra)
        # plt.xticks([]), plt.yticks([])
        # plt.title('Citra Mentah')

        # plt.subplot(1, 4, 2)
        # plt.imshow(hasilThresColor)
        # plt.xticks([]), plt.yticks([])
        # plt.title('Citra Thresholding')

        # plt.subplot(1, 4, 3)
        # plt.imshow(rgbCitra2)
        # plt.xticks([]), plt.yticks([])
        # plt.title('Hasil Akhir Thresholding Citra')

        # plt.show()

        # # print(self.sampelCitraAkhir[208:300,210:260,2])

        # # Ambil data ukuran gambar
        # height, width, color = rgbCitra2.shape[:]
        # bytesPerLine = 3 * width

        # # Konversi hasil citra akhir tadi ke object QImage dengan format 24 bit (RGB888 = 8-8-8)
        # img = QImage(rgbCitra2, width, height, bytesPerLine, QImage.Format_RGB888)
        # pixmap = QPixmap.fromImage(img)

        # # Tampilkan 
        # self.sampelGambar.setPixmap(pixmap)
        # self.sampelGambar.setScaledContents(True)
        # self.sampelGambar.resize(pixmap.width(), pixmap.height())

    # Method simpan gambar
    def saveImage(self):
        pass

    # Method menghitung kalkulasi rata2 RGB
    def calculateRGBMean(self):
        # Split BGR channel
        blue = self.sampelCitraAkhir[:,:,0]
        print(blue)
        green = self.sampelCitraAkhir[:,:,1]
        red = self.sampelCitraAkhir[:,:,2]

        # Hitung semua nilai rata2 channel
        avgBlue = np.average(blue, axis=0)
        # totalBlue = np.average(avgBlue, axis=0)

        avgGreen = np.average(green, axis=0)
        # totalGreen = np.average(avgGreen, axis=0)

        avgRed = np.average(red, axis=0)
        # totalRed = np.average(avgRed, axis=0)

        print('Rata2 Blue', avgBlue)
        # print('Rata2 Green', avgGreen)
        # print('Rata2 Red', avgRed)