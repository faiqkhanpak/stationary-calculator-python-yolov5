
# importing various libraries
import sys
from PyQt5.QtWidgets import QLCDNumber,QComboBox,QDialog, QApplication, QPushButton, QVBoxLayout,QLineEdit,QWidget,QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont, QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw, ImageQt
import glob

# All files and directories ending with .txt and that don't begin with a dot:


# main window
# which inherits QDialog
class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.pencil = QSpinBox(self)
        self.pencil.setRange(0, 100)
        self.scale = QSpinBox(self)
        self.scale.setRange(0, 100)
        self.eraser = QSpinBox(self)
        self.eraser.setRange(0, 100)
        self.sharpner = QSpinBox(self)
        self.sharpner.setRange(0, 100)
        names=glob.glob(r"G:\Study Material 2\testimages\*.jpg") 
        self.names1=[i.split('testimages')[1:][0][1:] for i in names]
        self.lcd = QLCDNumber(self)
        self.combobox1 = QComboBox(self)
        self.combobox1.addItems(self.names1)
        self.figure = plt.figure(figsize=(8,10))
        self.setWindowTitle("Annotation Assignment")  
		# this is the Canvas Widget that
		# displays the 'figure'it takes the
		# 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

		# this is the Navigation widget
		# it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        self.button0 = QPushButton('Read File')
		
		# adding action to the button
        self.button0.clicked.connect(self.readimage)
		# Just some button connected to 'plot' method
        self.button = QPushButton('Display Original image')
		
		# adding action to the button
        self.button.clicked.connect(self.plot1)
        
        self.button1 = QPushButton('Generate bill')
		
		# adding action to the button
        self.button1.clicked.connect(self.plot2)
		# creating a Vertical Box layout
        layout = QVBoxLayout()

		# adding tool bar to the layout
        layout.addWidget(self.toolbar)
		
		# adding canvas to the layout
        layout.addWidget(self.canvas)
   
        labelnames = QLabel(("Name of the file"))
        labelp = QLabel(("Pencil price: "))
        labels = QLabel(("Scale price: "))
        labelsh = QLabel(("Sharpner price: "))
        labele = QLabel(("Eraser price: "))
		# adding push button to the layout
        layout.addWidget(labelnames)
        layout.addWidget(self.combobox1)
        layout.addWidget(self.button0)
        layout.addWidget(self.button)

        layout.addWidget(labelp)
        layout.addWidget(self.pencil)
        layout.addWidget(labels)
        layout.addWidget(self.scale)
        layout.addWidget(labelsh)
        layout.addWidget(self.sharpner)
        layout.addWidget(labele)
        layout.addWidget(self.eraser)
        layout.addWidget(self.button1)
        layout.addWidget(self.lcd)

		
		# setting layout to the main window
        self.setLayout(layout)
    
	# action called by thte push button
    def plot1(self):
        self.figure.clear()
       
        ax = self.figure.add_subplot()
        ax.imshow(self.im)
        ax.set_title("Image")
		# refresh canvas
        self.canvas.draw()
        
    def plot2(self):
        
        #self.lcd.setGeometry(3, 120, 150, 30)
        palette = self.lcd.palette()
        # foreground color
        palette.setColor(palette.WindowText, QtGui.QColor(85, 85, 255))
# background color
        palette.setColor(palette.Background, QtGui.QColor(0, 170, 255))
# "light" border
        palette.setColor(palette.Light, QtGui.QColor(255, 0, 0))
# "dark" border
        palette.setColor(palette.Dark, QtGui.QColor(0, 255, 0))
        self.lcd.setPalette(palette)
        self.lcd.setDigitCount(6)
        a1,a2,a3,a4=1,2,3,4
        total=a1*self.pencil.value()+a2*self.eraser.value()+a3*self.sharpner.value()+a4*self.scale.value()
        self.lcd.display(total)
		
    def readimage(self):
        self.img=self.combobox1.currentText().split(".")[0]

        #image = cv2.imread(r'G:\Study Material 2\dataset\images\001.jpg', 0)
        self.im = Image.open(r'testimages\\'+self.img+'.jpg')
        self.f = open(r"testimages\\"+self.combobox1.currentText(), "r")
        

# driver code
if __name__ == '__main__':
	
	# creating apyqt5 application
	app = QApplication(sys.argv)

	# creating a window object
	main = Window()
	
	# showing the window
	main.show()

	# loop
	sys.exit(app.exec_())
