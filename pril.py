from PyQt5 import QtWidgets,QtCore
from PyQt5.Qt import*
from okno import Ui_Form
from class_fish import Fish
from class_shark import Shark
from matplotlib import pyplot as plt
from  matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from MplForWidget import MyMplCanavas

class MyWindow(QtWidgets.QWidget,Ui_Form):
    def __init__ (self,obj):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.timer=QTimer(self)
        self.timer.setInterval(2000)
        self.i=0
        self.i2=1                   # для графика
        self.obj=obj
        self.timer.timeout.connect(self.kik)
        self.timer.start()
        self.all_fish=[]
        self.all_shark=[]
        self.all_max_shark=[]          # считаем количество рыб за ход
        self.all_i=[]               # считаем количество шагов
        self.all_max_fish=[]        # считаем количество рыб за ход
        self.fig,self.axes=plt.subplots(nrows=1,ncols=1,figsize=(4,4))    
        self.axes.grid(True,c='lightgrey',alpha=0.5)
        #self.axes.set_title('spectr')
        
        #self.axes.plot(x,y,color='blue')
        #self.axes.plot(x2,y,color='green')
        #self.axes.plot(x3,y,color='green')
        #self.axes.plot(x4,y,color='red')
        self.companovka_for_mpl = QtWidgets.QVBoxLayout(self.widget)
        self.canavas=MyMplCanavas(self.fig)
        self.companovka_for_mpl.addWidget(self.canavas)
        self.toolbar=NavigationToolbar(self.canavas,self)
        self.companovka_for_mpl.addWidget(self.toolbar)
        


        
    def kik(self):
        """ Удаляем очищаем старую позицию """
        if self.obj.old_position[1]!=None:
            self.c1=QtWidgets.QTableWidgetItem (None)
            self.tableWidget.setItem(self.obj.old_position[1],self.obj.old_position[0],self.c1)
        
        
        """ Создаем новую  позицию и отмечаем новый ход """
        self.z=str(self.obj)
        #print(self.z)
        self.i+=1
        self.i2+=1
        self.all_i.append(self.i2)
        self.b=str(self.i)
        self.pushButton.setText("Ход"+" "+ self.b)  
        self.c=QtWidgets.QTableWidgetItem ('*')
        self.c.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(self.obj.position[1],self.obj.position[0],self.c)  
        self.obj.move()

    
        """ Добавляем новую рыбку"""
        #if self.i%2==0:
        if self.i%7 == 0 or 2:
            print('tut')
            self.fish=Fish()
            print(self.fish)
            self.all_fish.append(self.fish)
            """ Спавн акул"""
        if self.i%3==0 or 2:
            self.shark=Shark()
            self.all_shark.append(self.shark)
            del self.shark
        
        """ Стираем старую позицию новых рыбок"""
        if self.all_fish!=[]:
            for self.v in self.all_fish: 
                if self.v.old_position[1] !=None:
                    self.c1=QtWidgets.QTableWidgetItem (None)
                    self.tableWidget.setItem(self.v.old_position[1],self.v.old_position[0],self.c1)
                    
            """ Движение новых рыбок"""    
            for self.v  in self.all_fish:
                self.c=QtWidgets.QTableWidgetItem ('*')
                self.c.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.v.position[1],self.v.position[0],self.c)  
                self.v.move()
        
        """ Стираем старую позицию новыx акул"""
        if self.all_shark!=[]:
            for self.v in self.all_shark: 
                if self.v.old_position[1] !=None:
                    self.c1=QtWidgets.QTableWidgetItem (None)
                    self.tableWidget.setItem(self.v.old_position[1],self.v.old_position[0],self.c1)
                    
            """ Движение новых акул"""
            for self.v  in self.all_shark:
                self.c=QtWidgets.QTableWidgetItem ('+')
                self.c.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.v.position[1],self.v.position[0],self.c)  
                self.v.move()
            """ А вот тут самый экшон"""
            
            self.dead=True
            while self.dead==True and self.all_shark!=[]:       
                for self.v in  range (len(self.all_shark)):
                    for self.x1 in range(len(self.all_fish)):
                        if self.all_shark[self.v].position[1]==self.all_fish[self.x1].position[1] and self.all_shark[self.v].position[0]==self.all_fish[self.x1].position[0]:
                            self.all_shark[self.v].hunger=8
                            self.x2=QtWidgets.QTableWidgetItem (None)
                            self.tableWidget.setItem(self.all_fish[self.x1].old_position[1],self.all_fish[self.x1].old_position[0],self.x2)
                            del self.all_fish[self.x1]
                            
                            break

                for self.z in range(len(self.all_shark)):
                    
                    if self.all_shark[self.z].hunger==0:
                        self.x1=QtWidgets.QTableWidgetItem (None)
                        self.tableWidget.setItem(self.all_shark[self.z].old_position[1],self.all_shark[self.z].old_position[0],self.x1)
                        
                        del self.all_shark[self.z]
                        break
                    else: self.dead=None
        print('количество акул',len(self.all_shark))   
        print('количество рыб',len(self.all_fish))
        self.all_max_fish.append(len(self.all_fish))
        self.all_max_shark.append(len(self.all_shark))
        
        self.axes.clear()
        self.axes.grid(True,c='lightgrey',alpha=0.5)
        print('rab')
        print(len(self.all_i))
        print(len(self.all_max_fish))
        
        self.axes.plot(self.all_i,self.all_max_fish,color='blue')
        self.axes.plot(self.all_i,self.all_max_shark,color='red')
        self.fig.canvas.draw()

       
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
