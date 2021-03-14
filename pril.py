from PyQt5 import QtWidgets,QtCore
from PyQt5.Qt import*
from okno import Ui_Form
from class_fish import Fish



class MyWindow(QtWidgets.QWidget,Ui_Form):
    def __init__ (self,obj):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.timer=QTimer(self)
        self.timer.setInterval(1200)
        self.i=0
        self.obj=obj
        self.timer.timeout.connect(self.kik)
        self.timer.start()
        self.all_fish=[]
        
    def kik(self):
        """ Удаляем очищаем старую позицию """
        if self.obj.old_position[1]!=None:
            self.c1=QtWidgets.QTableWidgetItem (None)
            self.tableWidget.setItem(self.obj.old_position[1],self.obj.old_position[0],self.c1)
        
        
        """ Создаем новую  позицию и отмечаем новый ход """
        self.z=str(self.obj)
        #print(self.z)
        self.i+=1
        self.b=str(self.i)
        self.pushButton.setText("Ход"+" "+ self.b)  
        self.c=QtWidgets.QTableWidgetItem ('*')
        self.c.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(self.obj.position[1],self.obj.position[0],self.c)  
        self.obj.move()

    
        """ Добавляем новую рыбку"""
        if self.pushButton.text() == 'Ход 7':
            print('tut')
            self.fish=Fish()
            print(self.fish)
            self.all_fish.append(self.fish)
        """ Стираем старую позицию новой рыбки"""
        for self.v in self.all_fish:
            if self.v.old_position[1] !=None:
                self.c1=QtWidgets.QTableWidgetItem (None)
                self.tableWidget.setItem(self.v.old_position[1],self.v.old_position[0],self.c1)
                
        """ Движение новой рыбки"""
        if self.all_fish!=[]:
            for self.v  in self.all_fish:
                self.c=QtWidgets.QTableWidgetItem ('*')
                self.c.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.v.position[1],self.v.position[0],self.c)  
                self.v.move()
        


       
def new_life_fish():
        x=Fish()
        return(x)


all_fish=[]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    all_fish.append(new_life_fish())
    window = MyWindow(all_fish[0])
    window.show()                
    sys.exit(app.exec_())
    
'''
    def table_move(self,obj):    

        self.Z=QtWidgets.QTableWidgetItem ('1')
        """тут правил """
        
        self.tableWidget.setItem(self.obj.position[1],self.obj.position[0],self.Z)    
        
    def clear_old_position(self,obj):
        
        self.c1=QtWidgets.QTableWidgetItem (None)
        self.tableWidget.setItem(obj.old_position[1],obj.old_position[0],self.c1)



    '''
