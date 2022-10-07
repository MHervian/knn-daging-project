# Modul program untuk mengecilkan gambar/resize image
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
                            QVBoxLayout, QGridLayout, QHBoxLayout,  QLabel, QScrollArea,
                            QFileDialog, QDialog, QMessageBox, QTableWidget, QTableWidgetItem)
from PyQt5.QtGui import (QPixmap, QFont, QImage)

# Mysql connector
import mysql.connector
from mysql.connector import Error

# Import OpenCV dan yang bersangkutan
import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Import library matematika
import numpy as np
import math
import operator

# Import modul
import app

class KnnProgram(QWidget):
    
    def __init__(self):
        super().__init__()

        self.top = 70
        self.left = 70
        self.width = 950
        self.height = 620
        self.windowTitle = "KNN Processing"

        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.setWindowTitle(self.windowTitle)

        # Memulai mengisi elemen2 di program ini 
        self.initUI()

    def initUI(self):
        self.basicLayout = QGridLayout()

        self.setLayout(self.basicLayout)

        tombolBack = QPushButton('Back')
        
        backMenuLayout = QHBoxLayout()
        backMenuLayout.addWidget(tombolBack)
        backMenuLayout.addStretch(1)

        self.basicLayout.addLayout(backMenuLayout, 0, 0, 1, 6)

        # Menampilkan sampel data gambar daging
        tombolBukaGambar = QPushButton('Buka Sampel')
        tombolResetGambar = QPushButton('Hapus Sampel')
        tombolSimpanHasilKNN = QPushButton('Simpan Hasil')

        verticalMenuLayout = QVBoxLayout()
        verticalMenuLayout.addWidget(tombolBukaGambar)
        verticalMenuLayout.addWidget(tombolResetGambar)
        # verticalMenuLayout.addWidget(tombolSimpanHasilKNN)
        verticalMenuLayout.addStretch(1)

        self.basicLayout.addLayout(verticalMenuLayout, 1, 0, 4, 1)

        sampelData = QLabel()
        sampelData.setScaledContents(True)
        
        self.scrollAreaSampelData = QScrollArea()
        self.scrollAreaSampelData.setWidget(sampelData)

        sampelGambarLayout = QVBoxLayout()
        sampelGambarLayout.addWidget(self.scrollAreaSampelData)

        self.basicLayout.addLayout(sampelGambarLayout, 1, 1, 2, 3)

        # Menghitung nilai RGB
        tombolHitungRGB = QPushButton('Hitung RGB')
        labelHasilRGB = QLabel('Nilai RGB')
        self.tableRGB = QTableWidget()
        self.tableRGB.setRowCount(3)
        self.tableRGB.setColumnCount(3)

        self.tableRGB.setItem(0, 0, QTableWidgetItem('RED'))
        self.tableRGB.setItem(0, 1, QTableWidgetItem(':'))
        self.tableRGB.setItem(0, 2, QTableWidgetItem('0'))

        self.tableRGB.setItem(1, 0, QTableWidgetItem('GREEN'))
        self.tableRGB.setItem(1, 1, QTableWidgetItem(':'))
        self.tableRGB.setItem(1, 2, QTableWidgetItem('0'))

        self.tableRGB.setItem(2, 0, QTableWidgetItem('BLUE'))
        self.tableRGB.setItem(2, 1, QTableWidgetItem(':'))
        self.tableRGB.setItem(2, 2, QTableWidgetItem('0'))

        tombolProsesKNN = QPushButton('Proses KNN')

        verticalSampelInfo = QVBoxLayout()
        verticalSampelInfo.addWidget(tombolHitungRGB)
        verticalSampelInfo.addWidget(labelHasilRGB)
        verticalSampelInfo.addWidget(self.tableRGB)
        verticalSampelInfo.addWidget(tombolProsesKNN)
        verticalSampelInfo.addStretch(1)

        self.basicLayout.addLayout(verticalSampelInfo, 1, 4, 2, 2)

        # Menampilkan tabel data training
        self.displayDataTraining()

        # Event click connection
        tombolBack.clicked.connect(self.closeThisProgram)
        tombolBukaGambar.clicked.connect(self.bukaFileGambar)
        tombolResetGambar.clicked.connect(self.resetSampelGambar)
        # tombolSimpanHasilKNN.clicked.connect(self.prosesSimpanHasilKNN)
        tombolHitungRGB.clicked.connect(self.hitungRGBSampel)
        tombolProsesKNN.clicked.connect(self.knn_process)

    def closeThisProgram(self):
        self.mainProgram = app.MainProgram()
        self.mainProgram.show()
        self.hide()

    def bukaFileGambar(self):
        self.resetSampelGambar()
        fname = QFileDialog.getOpenFileName(self, 'Open file','H:\'', "Image files (*.jpg *.png)")
        
        # Mengambilkan alamat filepath gambar tersebut
        self.imagePath = fname[0]
        # Membuat elemen gambar dengan QPixmap
        filePixmapGambar = QPixmap(self.imagePath)
        
        sampelGambar = QLabel()
        sampelGambar.setPixmap(filePixmapGambar)
        sampelGambar.resize(filePixmapGambar.width(), filePixmapGambar.height())

        self.scrollAreaSampelData.setWidget(sampelGambar)

    def resetSampelGambar(self):
        sampelGambar = QLabel()
        sampelGambar.setPixmap(QPixmap())
        sampelGambar.resize(1,1)
        self.imagePath = ''

        self.scrollAreaSampelData.setWidget(sampelGambar)

        # Reset variable mean pada channel RGB dan tabel
        self.meanRed = self.meanGreen = self.meanBlue = 0

        self.tableRGB.setItem(0, 0, QTableWidgetItem('RED'))
        self.tableRGB.setItem(0, 1, QTableWidgetItem(':'))
        self.tableRGB.setItem(0, 2, QTableWidgetItem('0'))

        self.tableRGB.setItem(1, 0, QTableWidgetItem('GREEN'))
        self.tableRGB.setItem(1, 1, QTableWidgetItem(':'))
        self.tableRGB.setItem(1, 2, QTableWidgetItem('0'))

        self.tableRGB.setItem(2, 0, QTableWidgetItem('BLUE'))
        self.tableRGB.setItem(2, 1, QTableWidgetItem(':'))
        self.tableRGB.setItem(2, 2, QTableWidgetItem('0'))

    def hitungRGBSampel(self):
        # self.bukaFileGambar()

        sampelCitra = cv2.imread(self.imagePath, cv2.IMREAD_UNCHANGED)
        sampelCitra = cv2.cvtColor(sampelCitra, cv2.COLOR_BGR2RGB)

        # Hitung masing2 nilai rata2 channel BGR tersebut
        # blue = np.mean(sampelCitra[:,:,0], axis=0)
        # self.meanBlue = round(np.mean(blue, axis=0), 2)

        # green = np.mean(sampelCitra[:,:,1], axis=0)
        # self.meanGreen = round(np.mean(green, axis=0), 2)

        # red = np.mean(sampelCitra[:,:,2], axis=0)
        # self.meanRed = round(np.mean(red, axis=0), 2)
        red = np.mean(sampelCitra[:,:,0], axis=0)
        self.meanRed = round(np.mean(red, axis=0), 2)

        green = np.mean(sampelCitra[:,:,1], axis=0)
        self.meanGreen = round(np.mean(green, axis=0), 2)

        blue = np.mean(sampelCitra[:,:,2], axis=0)
        self.meanBlue = round(np.mean(blue, axis=0), 2)

        self.tableRGB.setItem(0, 2, QTableWidgetItem(f'{self.meanRed}'))
        self.tableRGB.setItem(1, 2, QTableWidgetItem(f'{self.meanGreen}'))
        self.tableRGB.setItem(2, 2, QTableWidgetItem(f'{self.meanBlue}'))

    
    def displayDataTraining(self):
        # Melakukan query data 
        try:
            connection = mysql.connector.connect(host = 'localhost',
                                                 database = 'knn_daging', 
                                                 user = 'root', 
                                                 password = '')

            cursor = connection.cursor()
            cursor.execute("SELECT \
	                data_mentah.no_data AS no_data, \
                    data_mentah.red_mean AS red_mean, \
                    data_mentah.green_mean AS green_mean, \
                    data_mentah.blue_mean AS blue_mean, \
                    cate.nama_cat AS nama_cat \
                        FROM (SELECT \
	                        hasil_knn.no_data AS no_data, \
                            kategori.nama_cat AS nama_cat \
                            FROM hasil_knn \
    	                    INNER JOIN kategori ON kategori.no_kategori = hasil_knn.no_kategori) cate \
                        RIGHT JOIN data_mentah ON data_mentah.no_data = cate.no_data")
            
            self.recordData = cursor.fetchall()
            recordLength = len(self.recordData)

        except Error as e:
            print("Error while connecting to MySQL ", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
            
            self.tableDataTraining = QTableWidget()
            self.tableDataTraining.setRowCount(1 + recordLength)
            self.tableDataTraining.setColumnCount(5)

            self.tableDataTraining.setItem(0, 0, QTableWidgetItem('Status Data'))
            self.tableDataTraining.setItem(0, 1, QTableWidgetItem('Red Mean'))
            self.tableDataTraining.setItem(0, 2, QTableWidgetItem('Green Mean'))
            self.tableDataTraining.setItem(0, 3, QTableWidgetItem('Blue Mean'))
            self.tableDataTraining.setItem(0, 4, QTableWidgetItem('Kategori Daging'))

            statusData = ''

            for iteration in range(recordLength):
                dList = list(self.recordData[iteration])

                if dList[4] is None:
                    statusData = 'Data Sampel'
                else:
                    statusData = 'Data Training'

                self.tableDataTraining.setItem(iteration + 1, 0, QTableWidgetItem(f'{statusData}'))
                self.tableDataTraining.setItem(iteration + 1, 1, QTableWidgetItem(f'{dList[1]}'))
                self.tableDataTraining.setItem(iteration + 1, 2, QTableWidgetItem(f'{dList[2]}'))
                self.tableDataTraining.setItem(iteration + 1, 3, QTableWidgetItem(f'{dList[3]}'))
                self.tableDataTraining.setItem(iteration + 1, 4, QTableWidgetItem(f'{dList[4]}'))

            self.basicLayout.addWidget(self.tableDataTraining, 3, 1, 2, 3)

    # Method untuk Rumus Euclidean Distance
    def euclideanDistance(self, dataSampel, dataTraining, length):
        distance = 0.0
        for x in range(length):
            distance += np.square(dataSampel[x] - dataTraining[x])
        return round(np.sqrt(distance), 2)

    def itemGetterOperator(self, iterate):
        return iterate[0]

    # Method untuk Algoritma KNN
    def knn_process(self):
        distances = []
        sorted_d = []

        # Persiapan data sampel
        dataSampel = [self.meanRed, self.meanGreen, self.meanBlue]

        # Query data baru
        try:
            connection = mysql.connector.connect(host = 'localhost',
                                                 database = 'knn_daging', 
                                                 user = 'root', 
                                                 password = '')

            cursor = connection.cursor()
            cursor.execute("SELECT \
	                data_mentah.no_data AS no_data, \
                    data_mentah.red_mean AS red_mean, \
                    data_mentah.green_mean AS green_mean, \
                    data_mentah.blue_mean AS blue_mean, \
                    cate.nama_cat AS nama_cat \
                        FROM (SELECT \
	                        hasil_knn.no_data AS no_data, \
                            kategori.nama_cat AS nama_cat \
                            FROM hasil_knn \
    	                    INNER JOIN kategori ON kategori.no_kategori = hasil_knn.no_kategori) cate \
                        INNER JOIN data_mentah ON data_mentah.no_data = cate.no_data")
            
            recordDataBaru = cursor.fetchall()

        except Error as e:
            print("Error while connecting to MySQL ", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        # Menghitung Distance pada data sampel terhadap data - data training
        for x in range(len(recordDataBaru)):
            dataTraining = list(recordDataBaru[x])

            dist = self.euclideanDistance(dataSampel, dataTraining[1:4], len(dataTraining[1:4]))
            distances.append((dist, dataTraining[4]))

        # Melakukan pengurutan data dari terkecil hingga terbesar
        sorted_d = sorted(distances, key=operator.itemgetter(0))

        # Menampilkan perkiraan berdasarkan nilai K-n
        k_1 = 1
        k_3 = 3
        k_5 = 5
        k_1Arr = []
        k_3Arr = []
        k_5Arr = []

        resultFrequence = []

        # Menyiapkan tabel
        self.tableHasilKNN = QTableWidget()
        self.tableHasilKNN.setRowCount(20)
        self.tableHasilKNN.setColumnCount(3)

        self.tableHasilKNN.setItem(0, 0, QTableWidgetItem('Data Sampel'))
        self.tableHasilKNN.setItem(1, 0, QTableWidgetItem(f'{dataSampel[0]}'))
        self.tableHasilKNN.setItem(1, 1, QTableWidgetItem(f'{dataSampel[1]}'))
        self.tableHasilKNN.setItem(1, 2, QTableWidgetItem(f'{dataSampel[2]}'))

        # Menampilkan data dengan K = 1
        self.tableHasilKNN.setItem(3, 0, QTableWidgetItem('K = 1'))
        for x in range(k_1):
            k_1Arr.append(list(sorted_d[x])[1])
            tmp_data = list(sorted_d[x])
            self.tableHasilKNN.setItem(4, 0, QTableWidgetItem(f'{tmp_data[0]}'))
            self.tableHasilKNN.setItem(4, 1, QTableWidgetItem(f'{tmp_data[1]}'))

        frequence_found = self.frekuensi_muncul(k_1Arr)
        resultFrequence.append(frequence_found)     
        self.tableHasilKNN.setItem(5, 0, QTableWidgetItem(f'Frekuensi muncul: {frequence_found}'))

        # Menampilkan data dengan K = 3
        pos = 8
        self.tableHasilKNN.setItem(7, 0, QTableWidgetItem('K = 3'))
        for x in range(k_3):
            k_3Arr.append(list(sorted_d[x])[1])
            tmp_data = list(sorted_d[x])
            self.tableHasilKNN.setItem((pos + x), 0, QTableWidgetItem(f'{tmp_data[0]}'))
            self.tableHasilKNN.setItem((pos + x), 1, QTableWidgetItem(f'{tmp_data[1]}'))

        frequence_found = self.frekuensi_muncul(k_3Arr)
        resultFrequence.append(frequence_found)
        self.tableHasilKNN.setItem(11, 0, QTableWidgetItem(f'Frekuensi muncul: {frequence_found}'))

        # Menampilkan data dengan K = 5
        pos = 14
        self.tableHasilKNN.setItem(13, 0, QTableWidgetItem('K = 5'))
        for x in range(k_5):
            k_5Arr.append(list(sorted_d[x])[1])
            tmp_data = list(sorted_d[x])
            self.tableHasilKNN.setItem((pos + x), 0, QTableWidgetItem(f'{tmp_data[0]}'))
            self.tableHasilKNN.setItem((pos + x), 1, QTableWidgetItem(f'{tmp_data[1]}'))

        frequence_found = self.frekuensi_muncul(k_5Arr)
        resultFrequence.append(frequence_found)
        self.tableHasilKNN.setItem(19, 0, QTableWidgetItem(f'Frekuensi muncul: {frequence_found}'))

        self.basicLayout.addWidget(self.tableHasilKNN, 3, 4, 1, 2)

        # Menampilkan kesimpulan hasil training
        self.resultFrequence = self.frekuensi_muncul(resultFrequence)
        layoutKesimpulan = QVBoxLayout()

        labelKesimpulan1 = QLabel("Kesimpulan:")
        labelKesimpulan2 = QLabel(f'Data sampel daging ini adalah {self.resultFrequence}')
        btnSimpanHasilKNN = QPushButton('Simpan Hasil KNN')

        layoutKesimpulan.addWidget(labelKesimpulan1)
        layoutKesimpulan.addWidget(labelKesimpulan2)
        layoutKesimpulan.addWidget(btnSimpanHasilKNN)

        btnSimpanHasilKNN.clicked.connect(self.prosesSimpanHasilKNN)

        self.basicLayout.addLayout(layoutKesimpulan, 4, 4, 1, 2)

    # Method buat menghitung kemunculan data daging hasil perhitungan distance
    def frekuensi_muncul(self, lst):
        occurence_count = Counter(lst)
        return occurence_count.most_common(1)[0][0]

    def prosesSimpanHasilKNN(self):
        # Buat koneksi
        try:
            connection = mysql.connector.connect(host = 'localhost',
                                                 database = 'knn_daging', 
                                                 user = 'root', 
                                                 password = '')

        except Error as e:
            print("Error while connecting to MySQL ", e)
        finally:
            cursor = connection.cursor()
        
        # Dapatkan no_kategori dari tabel kategori berdasarkan nama_cat
        sql = f"SELECT no_kategori FROM kategori WHERE nama_cat = '{self.resultFrequence}'"
        cursor.execute(sql)

        kategori = cursor.fetchall()
        dataKategori = list(kategori[0])
        idKategori = dataKategori[0]

        # Insert data baru ke data_mentah
        sql = "INSERT INTO data_mentah(red_mean, green_mean, blue_mean) VALUES(%s, %s, %s)"
        val = (float(self.meanRed), float(self.meanGreen), float(self.meanBlue))
        cursor.execute(sql, val)

        connection.commit()

        no_data_terakhir = cursor.lastrowid

        # Update data
        sql = f"INSERT INTO hasil_knn(no_data, no_kategori) VALUES({no_data_terakhir},{idKategori})"
        cursor.execute(sql)

        connection.commit()

        if connection.is_connected():
            cursor.close()
            connection.close()

        # Menampilkan dialog untu hasil perhitungan BGR
        windowDialog = QDialog(self)

        vBoxResult = QVBoxLayout()

        textBerhasilInput = QLabel('Data hasil training KNN baru telah berhasil diinput ke basis data training')

        vBoxResult.addWidget(textBerhasilInput)

        windowDialog.setLayout(vBoxResult)
        windowDialog.show()