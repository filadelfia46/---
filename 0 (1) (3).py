from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QCheckBox,QPlainTextEdit,QLineEdit
from PyQt5.QtGui import QPixmap

import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        #каталог магазина
        self.menu = {"ТУФЛИ ДЛЯ ТАНГО (39-43)": 3590, "ТУФЛИ-ПЕРЧАТКИ (41)": 7700, 
                     "ОКСФОРДЫ (все размеры)": 15300, "ДЕРБИ (38-43)": 3444, 
                     "БРОГИ (все размеры)": 6800, "МОНКИ (37-39)": 2230, "ЛОФЕРЫ (37-40)": 7800,
                     "ДЕЗЕРТЫ (39, 40)": 9600, "ЧАККА (42)": 3800}
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 500, 400, 500)
        self.setWindowTitle('оптовый обувной интернет-магазин')

        self.check_b = []
        self.input_count = []

        k = 0
      #Вывод QCheckBox и поля для ввода количества товаров
        for i in self.menu.keys():
            tmp = QCheckBox(self)
            tmp.setText(i)
            tmp.move(10,20*k)
            tmp.stateChanged.connect(self.select_count)
            self.check_b.append(tmp)

            input_tmp = QLineEdit('',self)
            input_tmp.move(230, 20 * k)
            input_tmp.resize(30,20)
            input_tmp.setEnabled(False)
            input_tmp.setText('0')
            self.input_count.append(input_tmp)
            k+=1

        # Кнопка заказа
        self.btn = QPushButton('Заказать', self)
        self.btn.clicked.connect(self.run)
        self.btn.move(10, 20 * (len(self.check_b) + 1)) # 1111
       
        ## Отображаем заказ на экране
        self.result = QPlainTextEdit(self)
        self.result.setEnabled(False)
        self.result.move(10,20*(len(self.check_b)+3))
        self.setStyleSheet("background-color: #FFDAB9; color: #aaaa; font-family: Times;")
     # Если товар выбран, то становится доступен ввод количества
   
    def select_count(self,state):
        if state==2:
            self.input_count[self.check_b.index(self.sender())].setText('1')
            self.input_count[self.check_b.index(self.sender())].setEnabled(True)
        else:
            self.input_count[self.check_b.index(self.sender())].setText('0')
            self.input_count[self.check_b.index(self.sender())].setEnabled(False)

    def run(self):
        self.result.clear()
       # Чек
        data = [(self.check_b[self.input_count.index(i)].text(),i.text(),self.menu[self.check_b[self.input_count.index(i)].text()]*int(i.text())) for i in self.input_count if i.text()!='0']
        result = ["{}-----{}-----{}".format(*i) for i in data]
        print(result)
        result.insert(0,"Ваши покупки:\n")
        self.result.appendPlainText("\n".join(result))
        self.result.appendPlainText("\nС вас: {}".format(sum(i[2] for i in data)))
        self.result.appendPlainText(" \n Хорошего дня (;")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
