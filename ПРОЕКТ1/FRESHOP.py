import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QLCDNumber, QLineEdit
from PyQt5.QtGui import QPixmap

class Example(QWidget):


    def __init__(self):
        self.hub=0
        self.g=0
        self.jk=str(self.g)
        super().__init__()
        self.initUI()

    def initUI(self): 
        self.setGeometry(400, 400, 400, 400)
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("as.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(100, 100)
        self.setWindowTitle('????')
  
        self.button_1 = QPushButton(self)
        self.button_1.move(300, 200)
        self.button_1.setText("Choose your language")
        self.button_1.clicked.connect(self.run)   
        self.button_2R = QPushButton(self)
        self.button_2R.move(-1000, -1000)
        self.button_2R.setText("100 eur")
        self.button_2E = QPushButton(self)
        self.button_2E.clicked.connect(self.ran2)
        self.button_2E.move(-1000, -1000)
        self.button_2E.setText("100 eur")
        self.button_2E.clicked.connect(self.ran2)
        self.button_3E = QPushButton(self)
        self.button_3E.move(-1000, -1000)
        self.button_3E.setText("200 eur")
        self.button_3E.clicked.connect(self.ran3)
        self.button_3R = QPushButton(self)
        self.button_3R.move(-1000, -1000)
        self.button_3R.setText("200 eur")
        self.button_3R.clicked.connect(self.ran3)  
        self.button_4R = QPushButton(self)
        self.button_4R.move(-1000, -1000)
        self.button_4R.setText("300 руб")
        self.button_4R.clicked.connect(self.ran4)            
        self.button_4E = QPushButton(self)
        self.button_4E.move(-1000, -1000)
        self.button_4E.setText("300 eur")
        self.button_4E.clicked.connect(self.ran4)  
        self.button_5R = QPushButton(self)
        self.button_5R.move(-1000, -1000)
        self.button_5R.setText("400 руб")
        self.button_5R.clicked.connect(self.ran5)           
        self.button_5E = QPushButton(self)
        self.button_5E.move(-1000, -1000)
        self.button_5E.setText("400 eur")
        self.button_5E.clicked.connect(self.ran5) 
        self.label = QLabel(self)
        self.label.setText(self.jk)
        self.label.move(-1000,-1000)        
        self.show()

    def run(self): 
            i, okBtnPressed = QInputDialog.getItem(self, "Choose","Сhoose your language",("Русский", "English"), 1,False)
            if okBtnPressed and i=="English":
                i, okBtnPressed = QInputDialog.getItem(self, "Winter or summer shoes?","choose the right shoes",("Summer shoes", "Winter shoes"), 1,False)
                self.button_1.move(-1000, -1000)
                self.button_2E.move(200, 50)
                self.button_3E.move(200, 100)
                self.button_4E.move(200, 150)
                self.button_5E.move(200, 200)                
                if i == "Summer shoes":
                    self.button_1.move(-1000, -1000)
                    self.button_2E.setText(str(200)+' eur')
                    self.button_3E.setText(str(400)+' eur')
                    self.button_4E.setText(str(600)+' eur')
                    self.button_5E.setText(str(800)+' eur')
                if i == "Summer shoes":
                    self.hub=2
                else:
                    self.hub=1
     
            elif okBtnPressed and i=="Русский":
                i, okBtnPressed = QInputDialog.getItem(self, "Зимняя или летняя обувь?","Выберете нужную обувь",("Летняя обувь", "Зимняя обувь"), 1,False)
                self.button_1.move(-1000, -1000)
                self.button_2R.move(200, 50)
                self.button_3R.move(200, 100)
                self.button_4R.move(200, 150)
                self.button_5R.move(200, 200)                
                if i == "Летняя обувь":
                    self.button_1.move(-1000, -1000)
                    self.button_2R.setText(str(200)+' руб')
                    self.button_3R.setText(str(400)+' руб')
                    self.button_4R.setText(str(600)+' руб')
                    self.button_5R.setText(str(800)+' руб')

                if i == "Летняя обувь":
                    self.hub=2
                else:
                    self.hub=1                
                
    def ran2(self):
        self.label.move(150,300)
        i, okBtnPressed = QInputDialog.getItem(self, "Buy","Buy",("No", "Yes"), 1,False)
        if i=='Yes':
            self.g += 100 * self.hub
            self.label.setText(str(self.g))
        
    def ran3(self):
        self.label.move(150,300)
        i, okBtnPressed = QInputDialog.getItem(self, "Buy","Buy",("No", "Yes"), 1,False)   
        if i=='Yes':
            self.g +=200 * self.hub
            self.label.setText(str(self.g))
    def ran4(self):
        self.label.move(150,300)
        i, okBtnPressed = QInputDialog.getItem(self, "Buy","Buy",("No", "Yes"), 1,False)   
        if i=='Yes':
            self.g +=300 * self.hub
            self.label.setText(str(self.g))
            
    def ran5(self):
        self.label.move(150,300)
        i, okBtnPressed = QInputDialog.getItem(self, "Buy","Buy",("No", "Yes"), 1,False)   
        if i=='Yes':
            self.g +=400 * self.hub
            self.label.setText(str(self.g))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())