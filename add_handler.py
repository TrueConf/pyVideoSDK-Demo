# coding=utf8
'''''
@author: zobov
'''

import pyVideoSDK
from pyVideoSDK.methods import Methods
from pyVideoSDK.consts import EVENT, METHOD_RESPONSE
import pyVideoSDK.consts as C
import config
import flask
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize    

sdk = pyVideoSDK.open_session(ip = config.IP, port = config.PORT, pin = config.PIN, debug = config.DEBUG)
methods = Methods(sdk)

# ==============================================================================
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 200))    

        self.btn1 = QPushButton('Call', self)
        self.btn1.clicked.connect(self.callClick)
        self.btn1.resize(100,32)
        self.btn1.move(50, 50)

        self.lbl_1 = QLabel('Label', self)
        self.lbl_1.resize(100,32)
        self.lbl_1.move(50, 150)

    def callClick(self):
        self.btn1.setText("Call")
        methods.call("echotest@trueconf.com")

    def on_all(self, response):
        self.lbl_1.setText(response["method"])

    def on_state_change(self, response):
        self.btn1.setText(str(response["appState"]))
# ===============================================================================


'''
@sdk.handler({})
def on_all(response):
    print(f'    @@@ {response}')
'''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()

    # Add event handlers
    sdk.add_handler({}, mainWin.on_all)
    sdk.add_handler(EVENT[C.EV_appStateChanged], mainWin.on_state_change)
    sdk.add_handler(METHOD_RESPONSE[C.M_getAppState], mainWin.on_state_change)
    #sdk.del_handler(mainWin.on_state_change)

    mainWin.show()
    sys.exit( app.exec_() )
