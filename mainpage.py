import sys
import os
from PySide2 import *
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from qt_material import *
import psutil
import PySide2extn
#UI FILE CONVERTED FROM .ui to python file ui.py

from final import *

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		apply_stylesheet(app, theme='dark_blue.xml')
		win=self.ui.centralwidget
		self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

		'''self.setWindowFlags(QtCore.Qt.FramelessWindowHint)'''
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		#self.setAttribute(QtCore.Qt.WA_NoSystemBackground)
		
		
		
		
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(50)
		self.shadow.setXOffset(3)
		self.shadow.setYOffset(3)
		self.shadow.setColor(QtGui.QColor(0,92,157,550))

		win.setGraphicsEffect(self.shadow)

		self.setWindowIcon(QtGui.QIcon(":/Black/Icons/white/airplay.svg"))

		self.setWindowTitle("HEATSINK")
		QSizeGrip(self.ui.size_grip)      
		#minimize window
		self.ui.Minimize_window_button.clicked.connect(lambda:self.showMinimized())

		#close window
		self.ui.Close_window_button.clicked.connect(lambda:self.close())

		#restore/maximize window
		self.ui.Restore_window_button.clicked.connect(lambda: self.resize_win())
		
		#Navigation#################################
		self.ui.CPU_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_and_bat))
		self.ui.RAM_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.memory))
		self.ui.Disk_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.rom))
		self.ui.Wifi_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.network))
		self.ui.GPU_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.gpu))
		self.ui.System_info.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_info))
		self.ui.act_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activity))
		self.ui.sensor_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensor))
		self.ui.battery_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battery))
		
		#move bar
		def moveWindow(e):
			if self.isMaximized()==False:
				if e.buttons() == Qt.LeftButton:
					self.move(self.pos() + e.globalPos() - self.clickPosition)
					self.clickPosition=e.globalPos()
					e.accept()

		self.ui.Header_frame.mouseMoveEvent = moveWindow		

		self.ui.menu.clicked.connect(lambda: self.slideLeftMenu())	


		self.show()




		self.battery()




	#all functions below
	#left slide
	def slideLeftMenu(self):

		# Get current left menu width

		width = self.ui.Left_menu_cont_frame.width()

		# If minimized

		if width== 110:

		# Expand menu

			newWidth= 300

		# If maximized

		else:

		# Restore menu

			newWidth = 110

		# Animate the transition

		self.animation = QPropertyAnimation (self.ui.Left_menu_cont_frame, b"minimumWidth") #Animate minimumwidht
		self.animation.setDuration(250)
		self.animation.setStartValue(width) #Start value is the current menu width
		self.animation.setEndValue(newWidth) #end value is the new menu width
		self.animation.setEasingCurve (QtCore.QEasingCurve.InOutQuart)
		self.animation.start()

	#mouse events
	def mousePressEvent(self,event):
		self.clickPosition=event.globalPos()
	#minimized
	def resize_win(self):
		if self.isMaximized():
			self.showNormal()
			self.ui.Restore_window_button.setIcon(QtGui.QIcon(u":/Black/Icons/white/plus-square.svg"))
		else:
			self.showMaximized()
			self.ui.Restore_window_button.setIcon(QtGui.QIcon(u":/Black/Icons/white/minus-square.svg"))

	#cpu and ram info
	def cpu_ram(self):
		totalRam = 1.0
		totalRam = psutil.virtual_memory()[0] 
	
	
	#a function to convert seconds to hours
	def secs2hours(self,secs);
		mm, ss = divmod(secs, 60)
		hh, mm = divmod(mm, 60)
		return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)

	#battery info
	def battery(self):
		batt=psutil.sensors_battery()

		if not hasattr(psutil, "sensors_battery"):
			self.ui.battery_status.setText("Platform not supported")
		
		if batt is None:
			self.ui.battery_status.setText("No battery installed")

		if batt.power_plugged:
			self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
			self.ui.battery_time_left.setText("N/A")
			if batt.percent < 100:
				self.ui.battery_status.setText("Charging")
			else:
				self.ui.battery_status.setText("Fully Charged")
			self.ui.battery_plugged.setText("Yes")
		
		else:
			self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
			self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))
			if batt.percent < 100:
				self.ui.battery_status.setText("Discharging")
			else:
				self.ui.battery_status.setText("Fully Charged")
			self.ui.battery_plugged.setText("No")
	#battery power indicator
		self.ui.battery_usage.rpb_setaaMaximum(100)
		self.ui.battery_usage.rpb_setValue(batt.percent)
		self.ui.battery_usage.rpb_setBarStyle('Hybrid2')
		self.ui.battery_usage.rpb_setLineColor((255, 30, 99))
		self.ui.battery_usage.rpb_setPieColor((45, 74, 83))
		self.ui.battery_usage.rpb_setTextColor((255, 255, 255))
		self.ui.battery_usage.rpb_setInitialPos('West')
		self.ui.battery_usage.rpb_setTextFormat('Percentage')
		self.ui.battery_usage.rpb_setLineWidth(15)
		self.ui.battery_usage.rpb_setPathWidth(15)
		self.ui.battery_usage.rpb_setLineCap('RoundCap')










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())