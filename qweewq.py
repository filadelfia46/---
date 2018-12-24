import sys
from random import choice
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('���������')
        
        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("������")
        self.button_1.clicked.connect(self.run)  
        self.show()
 
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()
 
    def drawFlag(self,qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(30, 30, 120, 30)
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(30, 60, 120, 30)
        qp.setBrush(QColor(0, 0, 255))
        qp.drawRect(30, 90, 120, 30)
    def run(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_1.setStyleSheet(
                   "background-color: {}".format(color.name())
               )    
        
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())