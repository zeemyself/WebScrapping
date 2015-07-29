 #!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)

win = QWidget()

win.resize(320, 240)
win.setWindowTitle("Hello, World!")
layout = QVBoxLayout()
win.setLayout(layout)

label = QLabel("Hello World")
label2 = QLabel("5555")
label3 = QLabel("eiei")

button = QPushButton("Click Me")
layout.addWidget(label)
layout.addWidget(label2)
layout.addWidget(label3)
layout.addWidget(button)

win.show()

app.exec_()
