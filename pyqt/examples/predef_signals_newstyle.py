#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Luis Pérez

Ejemplo de conexión de señales y slots de qt por defecto que se pasan parámetros
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DefaultSignalsExample(QDialog):

    def __init__(self, parent=None):
        super(DefaultSignalsExample, self).__init__(parent)

        dial = QDial()
        spinner = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinner)
        self.setLayout(layout)

        dial.valueChanged.connect(spinner.setValue)
        spinner.valueChanged.connect(dial.setValue)

        self.setWindowTitle("Using default signals")
        self.resize(300, 200)

app = QApplication(sys.argv)
dialog = DefaultSignalsExample()
dialog.show()
sys.exit(app.exec_())
