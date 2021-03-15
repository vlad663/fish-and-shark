import random
class  Shark():
    def __init__(self,parent=None):
        self.life=1
        self.x = random.randrange(0,18,1)
        self.y = random.randrange(0,15,1)
        self.position = [self.x,self.y]
        self.old_position=[None,None]
        self.step=0
        self.hunger=9
    def move(self):
        self.hunger-=1
        self.h=random.randrange(1,5,1)


        if self.position[0] != None and self.position[1] != None:
            self.old_position[0]=self.position[0]
            self.old_position[1]=self.position[1]
            #print('очистил',self.old_position[0])
            #print('очистил',self.old_position[1])
            
        if self.h==1 and self.position[0]>0:
            self.position[0] = self.position[0]+(-1)
    
    
        elif self.h==2 and self.position[1]<20:
            self.position[1] = self.position[1]+(1)
            
        elif self.h==3 and self.position[0]<18:
            self.position[0] = self.position[0]+(1)

        elif self.h==4 and self.position[1]>0:
            self.position[1] = self.position[1]+(-1)

        self.step+=1
        
        if self.h==1 and self.position[0]==0:
            self.position[0]=17
        elif self.h ==3 and self.position[0]==18:
            self.position[0]=0
        
        if self.h == 4 and self.position[1]==0:
            self.position[1]=20
        elif self.h == 2 and self.position[1]==20:
            self.position[1]=0
        
            
    def __del__(self):
        class_name = self.__class__.__name__  
        print('{} уничтожен'.format(class_name))


"""        
all_shark=[]
x=Shark()
y=Shark()
all_shark.append(x)
#all_shark.append(y)
print(len(all_shark))
for i in range (9):
    x.move()

"""
