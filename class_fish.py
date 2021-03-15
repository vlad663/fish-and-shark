import random
class  Fish():
    def __init__(self,parent=None):
        self.life=1
        self.x = 10#random.randrange(0,18,1)
        self.y = 0#random.randrange(0,15,1)
        self.position = [self.x,self.y]
        self.old_position=[None,None]
        self.step=0
    def move(self):
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
