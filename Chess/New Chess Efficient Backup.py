import pygame
pygame.init()
from pygame.locals import *
class bishopw(object):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            while jk==False:
                yposition=1+yposition
                xposition=1+xposition

                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            while jk==True:
                yposition=yposition-1
                xposition=xposition-1

                if yposition>-1 and xposition>-1 and  yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]==""  :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if yposition>-1 and xposition>-1 and yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==False:
                xposition=1+xposition
                yposition=yposition-1

                if xposition<8 and yposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if xposition<8 and yposition>-1  and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==True:
                xposition=xposition-1
                yposition=yposition+1

                if xposition>-1 and yposition<8  and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if xposition>-1 and yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=False
                    
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])
            
            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])
            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])    
    def position(self,coords,coords2,bwmx,bwmy,number):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        tg=0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                gh=roomx%60
                roomx=(roomx-gh)+30
                gh=roomy%60
                roomy=(roomy-gh)+30
                if roomx==self.coords2[0][0] and roomy==self.coords2[0][1]:
                    piece=""
                    fv=1
                    tg=1
                else:
                    for k1 in range (0, len(self.coords)):
                        roomx,roomy=pygame.mouse.get_pos()
                        gh=roomx%60
                        roomx=(roomx-gh)+30
                        gh=roomy%60
                        roomy=(roomy-gh)+30

                        if roomx==self.coords[k1][0] and roomy==self.coords[k1][1]:
                                piece=""
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)
                                self.bwmx=self.bwmx//60
                                self.bwmy=converty(self.bwmy)
                                self.bwmy=self.bwmy//60
                                yposition=list_searchy(Board,self.number)
                                xposition=list_searchx(Board,self.number)
                                firstposition1=Board[yposition][xposition][0]
                                firstposition2=Board[yposition][xposition][1]
                                Board[yposition][xposition][0]=""
                                Board[yposition][xposition][1]=""
                                Board[self.bwmy][self.bwmx][0]=""
                                Board[self.bwmy][self.bwmx][1]=""
                                Board[self.bwmy][self.bwmx][0]=firstposition1
                                Board[self.bwmy][self.bwmx][1]=firstposition2
                                tg=2
                if fv==0:
                    tg=3
                    return tg

                if fv==1:
                    self.coords=[]
                    self.coords2=[]
                    return tg
                elif fv==2:
                    self.coords=[]
                    self.coords2=[]
                    return tg
                
        else:
            return tg
                    
class rookw(bishopw):

    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:        
            while jk==False:
                yposition=1+yposition
                if yposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==True:
                yposition=yposition-1
                if yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and yposition>-1:
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if yposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==False:
                xposition=1+xposition
                if xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==True:
                xposition=xposition-1
                if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=False
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])

            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])
            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]]) 
class knightw(bishopw):
    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        
        if xposition!=9:
            yposition=2+yposition
            xposition=1+xposition
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                self.coords.append([xposition*60+30,yposition*60+30])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition*60+30,yposition*60+30])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=2+yposition
            xposition=xposition-1
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                self.coords.append([xposition*60+30,yposition*60+30])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition*60+30,yposition*60+30])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition-2
            xposition=1+xposition

            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                self.coords.append([xposition*60+30,yposition*60+30])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition*60+30,yposition*60+30])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition-2
            xposition=xposition-1

            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                self.coords.append([xposition*60+30,yposition*60+30])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition*60+30,yposition*60+30])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition-1
            xposition=xposition-2

            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :

                self.coords.append([xposition*60+30,yposition*60+30])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition*60+30,yposition*60+30])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition+1
            xposition=xposition-2

            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                self.coords.append([xposition*60+30,yposition*60+30])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition*60+30,yposition*60+30])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition+1
            xposition=xposition+2
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                
                
                self.coords.append([xposition*60+30,yposition*60+30])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition*60+30,yposition*60+30])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)


            yposition=yposition-1
            xposition=xposition+2
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                self.coords.append([xposition*60+30,yposition*60+30])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                    self.coords.append([xposition*60+30,yposition*60+30])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])

            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])
            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]]) 
class queenw(bishopw):

    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            while jk==False:
                yposition=1+yposition
                xposition=1+xposition
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==True:

                yposition=yposition-1
                xposition=xposition-1
                if yposition>-1 and xposition>-1 and yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]==""  :
                    self.coords.append([xposition*60+30,yposition*60+30])

                else:
                    if yposition>-1 and xposition>-1 and yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==False:
                xposition=1+xposition
                yposition=yposition-1
                if xposition<8 and yposition>-1 and yposition<8 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if xposition<8 and yposition>-1  and xposition<8 and yposition>-1 and yposition<8 and xposition>-1 and yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==True:
                xposition=xposition-1
                yposition=yposition+1
                if xposition>-1 and yposition<8  and  xposition<8 and yposition>-1 and yposition<8 and xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if xposition>-1 and yposition<8 and xposition<8 and yposition>-1 and yposition<8 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=False

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            while jk==False:
                yposition=1+yposition
                if yposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=True
                    
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==True:
                yposition=yposition-1
                if  yposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if yposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==False:
                xposition=1+xposition
                if xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            
            while jk==True:
                xposition=xposition-1
                if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    self.coords.append([xposition*60+30,yposition*60+30])
                else:
                    if xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour:
                        self.coords.append([xposition*60+30,yposition*60+30])
                    jk=False
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])

            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])
            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]]) 
class kingw(bishopw):
    def possible_moves(self,coords,coords2,colour):
        self.colour=colour
        
        if vc=="k1b":
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            if xposition!=9:

                yposition=1+yposition
                xposition=1+xposition
                
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                
                xposition2=xposition2+30
                yposition2=yposition2+30
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])
                        
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                yposition=yposition-1
                xposition=xposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True  :
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                xposition=1+xposition
                yposition=yposition-1
                xposition2=xposition*60
                yposition2=yposition*60

                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if xposition<8 and yposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition<8 and yposition>-1  and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                self.coords2.append([xposition4,yposition4])
                
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                xposition=xposition-1
                yposition=yposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if xposition>-1 and yposition<8  and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition>-1 and yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                yposition=1+yposition
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False        
                xposition2=xposition2+30
                yposition2=yposition2+30        
                if yposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]==""  and fc==True:
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                yposition=yposition-1
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                
                if yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and yposition>-1 and fc==True:
                    self.coords.append([xposition2,yposition2])
                else:
                    if yposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                
                xposition=1+xposition
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                xposition=xposition-1
                xposition2=xposition*60
                yposition2=yposition*60
                fc=True
                for i in range (0,len(all_white)):
                    if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                        fc=False
                xposition2=xposition2+30
                yposition2=yposition2+30
                if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                    
                    self.coords.append([xposition2,yposition2])
                else:
                    if xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                        self.coords.append([xposition2,yposition2])

                if moves2kb==0 and moves2r1b==0:
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    xposition=xposition-1
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_white)):
                        if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                            fc=False
                    if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and yposition==7 and yposition==7 and xposition==3:
                        xposition=list_searchx(Board,vc)
                        xposition=list_searchx(Board,vc)
                        xposition=xposition-2
                        xposition2=xposition*60
                        yposition2=yposition*60
                        fc=True
                        for i in range (0,len(all_white)):
                            if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                                fc=False
                        if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and Board[yposition][xposition-1][0]=="":
                            xposition=list_searchx(Board,"r1b")
                            yposition=list_searchy(Board,"r1b")
                            if xposition==0 and yposition==7:
                                xposition2=xposition2+30
                                yposition2=yposition2+30
                                self.coords.append([xposition2,yposition2])
                if  moves2kb==0 and moves2r2b==0:          
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    xposition=xposition+1
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_white)):
                        if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                            fc=False
                    if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and yposition==7 and yposition==7 and xposition==5:
                        xposition=list_searchx(Board,vc)
                        xposition=list_searchx(Board,vc)
                        xposition=xposition+2
                        xposition2=xposition*60
                        yposition2=yposition*60
                        fc=True
                        for i in range (0,len(all_white)):
                            if xposition2==all_white[i][0] and yposition2==all_white[i][1]:
                                fc=False
                        if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                            xposition=list_searchx(Board,"r2b")
                            yposition=list_searchy(Board,"r2b")

                            if xposition==7 and yposition==7:
                                xposition2=xposition2+30
                                yposition2=yposition2+30
                                self.coords.append([xposition2,yposition2])
                        
        if vc=="k1w":
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            if xposition!=9:
                    yposition=1+yposition
                    xposition=1+xposition
                    
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        
                        
                        self.coords.append([xposition2,yposition2])
                    else:
                        if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])
                            
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=yposition-1
                    xposition=xposition-1
                    xposition2=xposition*60
                    yposition2=yposition*60
                    
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True  :
                        self.coords.append([xposition2,yposition2])
                    else:
                        if yposition>-1 and xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    
                    xposition=1+xposition
                    yposition=yposition-1
                    xposition2=xposition*60
                    yposition2=yposition*60

                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if xposition<8 and yposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        
                        self.coords.append([xposition2,yposition2])
                    else:
                        if xposition<8 and yposition>-1  and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    
                    xposition4=xposition*60+30
                    yposition4=yposition*60+30
                    self.coords2.append([xposition4,yposition4])
                    
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)

                    xposition=xposition-1
                    yposition=yposition+1
                    
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if xposition>-1 and yposition<8  and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        
                        self.coords.append([xposition2,yposition2])
                        
                    else:
                        if xposition>-1 and yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=1+yposition
                    xposition2=xposition*60
                    yposition2=yposition*60
                    
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False        
                    xposition2=xposition2+30
                    yposition2=yposition2+30        
                    if yposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]==""  and fc==True:
                        self.coords.append([xposition2,yposition2])
                    else:
                        if yposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                            
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=yposition-1
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    
                    if yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and yposition>-1 and fc==True:
                        self.coords.append([xposition2,yposition2])
                    else:
                        if yposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    
                    xposition=1+xposition
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        
                        self.coords.append([xposition2,yposition2])
                    else:
                        if xposition<8 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])

                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    xposition=xposition-1
                    xposition2=xposition*60
                    yposition2=yposition*60
                    fc=True
                    for i in range (0,len(all_black)):
                        if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                            fc=False
                    xposition2=xposition2+30
                    yposition2=yposition2+30
                    if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                        self.coords.append([xposition2,yposition2])
                    else:
                        if xposition>-1 and  yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][1]==self.colour and fc==True:
                            self.coords.append([xposition2,yposition2])
                    if  moves2kw==0 and moves2r1w==0: 
                        yposition=list_searchy(Board,vc)
                        xposition=list_searchx(Board,vc)
                        xposition=xposition-1
                        xposition2=xposition*60
                        yposition2=yposition*60
                        fc=True
                        for i in range (0,len(all_black)):
                            if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                                fc=False
                        if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and yposition==0 and xposition==3:
                            xposition=list_searchx(Board,vc)
                            xposition=list_searchx(Board,vc)
                            xposition=xposition-2
                            xposition2=xposition*60
                            yposition2=yposition*60
                            fc=True
                            for i in range (0,len(all_black)):
                                if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                                    fc=False
                            if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and fc==True and Board[yposition][xposition-1][0]=="":
                                xposition=list_searchx(Board,"r1w")
                                yposition=list_searchy(Board,"r1w")
                                if xposition==0 and yposition==0:
                                    xposition2=xposition2+30
                                    yposition2=yposition2+30
                                    self.coords.append([xposition2,yposition2])

                    if moves2kw==0 and moves2r2w==0:             
                        yposition=list_searchy(Board,vc)
                        xposition=list_searchx(Board,vc)
                        xposition=xposition+1
                        xposition2=xposition*60
                        yposition2=yposition*60
                        fc=True
                        for i in range (0,len(all_black)):
                            if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                                fc=False
                        if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True and yposition==0 and xposition==5:
                            xposition=list_searchx(Board,vc)
                            xposition=list_searchx(Board,vc)
                            xposition=xposition+2
                            xposition2=xposition*60
                            yposition2=yposition*60
                            fc=True
                            for i in range (0,len(all_black)):
                                if xposition2==all_black[i][0] and yposition2==all_black[i][1]:
                                    fc=False
                            if xposition>-1 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" and fc==True:
                                xposition=list_searchx(Board,"r2w")
                                yposition=list_searchy(Board,"r2w")
                                if xposition==7 and yposition==0:
                                    xposition2=xposition2+30
                                    yposition2=yposition2+30
                                    self.coords.append([xposition2,yposition2])


    def position(self,coords,coords2,bwmx,bwmy,number):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        tg=0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                gh=roomx%60
                roomx=(roomx-gh)+30
                gh=roomy%60
                roomy=(roomy-gh)+30
                if roomx==self.coords2[0][0] and roomy==self.coords2[0][1]:
                    piece=("")
                    fv=1
                    tg=1
                else:
                    for k1 in range (0, len(self.coords)):
                        roomx,roomy=pygame.mouse.get_pos()
                        gh=roomx%60
                        roomx=(roomx-gh)+30
                        gh=roomy%60
                        roomy=(roomy-gh)+30

                        if roomx==self.coords[k1][0] and roomy==self.coords[k1][1]:
                                if self.coords[k1][0]==150 and self.coords[k1][1]==450 and moves2kb==0 and moves2r1b==0:
                                    Board[7][0][0]=""
                                    Board[7][0][1]=""
                                    Board[7][3][0]="r1b"
                                    Board[7][3][1]="b"
                                if self.coords[k1][0]==390 and self.coords[k1][1]==450 and moves2kb==0 and moves2r2b==0:
                                    Board[7][7][0]=""
                                    Board[7][7][1]=""
                                    Board[7][5][0]="r2b"
                                    Board[7][5][1]="b"
                                if self.coords[k1][0]==150 and self.coords[k1][1]==30 and moves2kw==0 and moves2r1w==0:
                                    Board[0][0][0]=""
                                    Board[0][0][1]=""
                                    Board[0][3][0]="r1w"
                                    Board[0][3][1]="w"
                                if self.coords[k1][0]==390 and self.coords[k1][1]==30 and moves2kw==0 and moves2r2w==0:
                                    Board[0][7][0]=""
                                    Board[0][7][1]=""
                                    Board[0][5][0]="r2w"
                                    Board[0][5][1]="w"
                                piece=("")
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)
                                self.bwmx=self.bwmx//60
                                self.bwmy=converty(self.bwmy)
                                self.bwmy=self.bwmy//60
                                yposition=list_searchy(Board,self.number)
                                xposition=list_searchx(Board,self.number)
                                firstposition1=Board[yposition][xposition][0]
                                firstposition2=Board[yposition][xposition][1]
                                Board[yposition][xposition][0]=""
                                Board[yposition][xposition][1]=""
                                Board[self.bwmy][self.bwmx][0]=""
                                Board[self.bwmy][self.bwmx][1]=""
                                Board[self.bwmy][self.bwmx][0]=firstposition1
                                Board[self.bwmy][self.bwmx][1]=firstposition2
                                tg=2
                if fv==0:
                    tg=3
                    return tg

                if fv==1:
                    self.coords=[]
                    self.coords2=[]
                    return tg
                elif fv==2:
                    self.coords=[]
                    self.coords2=[]
                    return tg
                
        else:
            return tg

                    
class pawnw(bishopw):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour,moves2):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
        self.moves2=moves2
        
    def possible_moves(self,coords,coords2,colour,moves2):
        self.colour=colour
        self.moves2=moves2
        
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9:
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            self.coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=1+yposition
            xposition=xposition-1
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            if yposition<8 and xposition<8 and Board[yposition][xposition][1]=="b":
                self.coords.append([xposition2,yposition2])

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            yposition=1+yposition
            xposition=xposition+1
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            if yposition<8 and xposition<8 and Board[yposition][xposition][1]=="b" :
                self.coords.append([xposition2,yposition2])
            if self.moves2==0:
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                
                self.coords2.append([xposition4,yposition4])
                
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                yposition=yposition+1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=2+yposition
                    xposition2=xposition*60+30
                    yposition2=yposition*60+30
                    
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                        
                        self.coords.append([xposition2,yposition2])
            else:
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                self.coords2.append([xposition4,yposition4])
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                yposition=1+yposition
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    
                    self.coords.append([xposition2,yposition2])
            if white_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])


            if self.colour=="b":
                if two_protectors==False:                          
                    coords4=[]
                    remove=[]
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if white_protector[i][1]+30==self.coords[a][0] and white_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(white_protector)):
                        if white_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]]) 
                            
    def position(self,coords,coords2,bwmx,bwmy,number):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        tg=0
        global rookw_moves
        global bishopw_moves
        global queenw_moves
        global knightw_moves
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                gh=roomx%60
                roomx=(roomx-gh)+30
                gh=roomy%60
                roomy=(roomy-gh)+30
                if roomx==self.coords2[0][0] and roomy==self.coords2[0][1]:
                    piece=("")
                    fv=1
                    tg=1
                    if fv==0:
                        tg=3
                        return tg

                    if fv==1:
                        self.coords=[]
                        self.coords2=[]
                        return tg
                    elif fv==2:
                        self.coords=[]
                        self.coords2=[]
                        return tg
                else:
                    for k1 in range (0, len(self.coords)):
                        roomx,roomy=pygame.mouse.get_pos()
                        gh=roomx%60
                        roomx=(roomx-gh)+30
                        gh=roomy%60
                        roomy=(roomy-gh)+30
                        if roomx==self.coords[k1][0] and roomy==self.coords[k1][1]:
                            if roomy==450:
                                event2=wait()
                                if event2.type==pygame.KEYDOWN and event2.key==pygame.K_q:
                                    if queenw_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q2w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        queenw_moves=queenw_moves+1
                                        fv=2
                                        tg=2
                                    elif queenw_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        queenw_moves=queenw_moves+1
                                        fv=2
                                        tg=2
                                    elif queenw_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        queenw_moves=queenw_moves+1
                                        fv=2
                                        tg=2
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_r:
                                    if rookw_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        rookw_moves=rookw_moves+1
                                    elif rookw_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        rookw_moves=rookw_moves+1
                                    elif rookw_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r5w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        rookw_moves=rookw_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_b:
                                    if bishopw_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        bishopw_moves=bishopw_moves+1
                                    elif bishopw_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        bishopw_moves=bishopw_moves+1
                                    elif bishopw_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b5w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        bishopw_moves=bishopw_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_k:
                                    if knightw_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn3w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        knightw_moves=knightw_moves+1
                                    elif knightw_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn4w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        knightw_moves=knightw_moves+1
                                    elif knightw_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn5w"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="w"
                                        fv=2
                                        tg=2
                                        knightw_moves=knightw_moves+1
                                        
                            else:
                                piece=("")
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)
                                self.bwmx=self.bwmx//60
                                self.bwmy=converty(self.bwmy)
                                self.bwmy=self.bwmy//60
                                yposition=list_searchy(Board,self.number)
                                xposition=list_searchx(Board,self.number)
                                firstposition1=Board[yposition][xposition][0]
                                firstposition2=Board[yposition][xposition][1]
                                Board[yposition][xposition][0]=""
                                Board[yposition][xposition][1]=""
                                Board[self.bwmy][self.bwmx][0]=""
                                Board[self.bwmy][self.bwmx][1]=""
                                Board[self.bwmy][self.bwmx][0]=firstposition1
                                Board[self.bwmy][self.bwmx][1]=firstposition2
                                tg=2
                            if fv==0:
                                tg=3
                                return tg

                            if fv==1:
                                self.coords=[]
                                self.coords2=[]
                                return tg
                            elif fv==2:
                                self.coords=[]
                                self.coords2=[]
                                return tg
                    
        else:
            return tg

class pawnb(bishopw):
    def __init__(self,coords,coords2,bwmx,bwmy,number,colour,moves2):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        self.colour=colour
        self.moves2=moves2
        
    def possible_moves(self,coords,coords2,colour,moves2):
        self.colour=colour
        self.moves2=moves2
       
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if xposition!=9: 
            xposition4=xposition*60+30
            yposition4=yposition*60+30
            coords2.append([xposition4,yposition4])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)

            yposition=yposition-1
            xposition=xposition-1
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            if yposition<8 and xposition<8 and Board[yposition][xposition][1]=="w" :
                coords.append([xposition2,yposition2])
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            yposition=yposition-1
            xposition=xposition+1
            xposition2=xposition*60+30
            yposition2=yposition*60+30
            if yposition<8 and xposition<8 and Board[yposition][xposition][1]=="w" :
                coords.append([xposition2,yposition2])
            if self.moves2==0:
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                coords2.append([xposition4,yposition4])
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                yposition=yposition-1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30

                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    
                    self.coords.append([xposition2,yposition2])
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=yposition-2
                    xposition2=xposition*60+30
                    yposition2=yposition*60+30
                    
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                        
                        self.coords.append([xposition2,yposition2])

            else:
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)
                xposition4=xposition*60+30
                yposition4=yposition*60+30
                coords2.append([xposition4,yposition4])
                yposition=list_searchy(Board,vc)
                xposition=list_searchx(Board,vc)

                yposition=yposition-1
                
                xposition2=xposition*60+30
                yposition2=yposition*60+30
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and  yposition<8 and xposition<8  and Board[yposition][xposition][0]=="" :
                    coords.append([xposition2,yposition2])
            if black_check==True:
                coords3=[]
                if len(attack)>1:
                    for i in range(0,len(self.coords)):
                        self.coords.pop()
                else:
                    attack_positions2=[]
                    for a in range (0,len(attack_positions)):
                        attack_positions2.append([attack_positions[a][0]+30,attack_positions[a][1]+30])
                    for i in range(0,len(coords)):
                        coords3.append(self.coords[i])   
                    for i in range(0,len(coords3)):
                        self.coords.pop()
                    for a in range(len(attack_positions2)):
                        for i in range (len(coords3)):
                            if coords3[i]==attack_positions2[a]:
                                self.coords.append(coords3[i])
                    for i in range (0,len(coords3)):
                        if coords3[i][0]==list_searchx(Board,attack[0][0])*60+30 and coords3[i][1]==list_searchy(Board,attack[0][0])*60+30:
                            self.coords.append([list_searchx(Board,attack[0][0])*60+30,list_searchy(Board,attack[0][0])*60+30])
            if self.colour=="w":
                if two_protectors==False:                    
                    coords4=[]
                    remove=[]
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for a in range(0,len(self.coords)):
                                if black_protector[i][1]+30==self.coords[a][0] and black_protector[i][2]+30==self.coords[a][1]:
                                    coords4.append([self.coords[a][0],self.coords[a][1]])
                    for i in range (0,len(black_protector)):
                        if black_protector[i][0]==vc:
                            for i in range(0,len(self.coords)):
                                self.coords.pop()
                            for i in range (0,len(coords4)):
                                self.coords.append([coords4[i][0],coords4[i][1]])

    def position(self,coords,coords2,bwmx,bwmy,number):
        self.coords=coords
        self.coords2=coords2
        self.bwmx=bwmx
        self.bwmy=bwmy
        self.number=number
        tg=0
        global rookb_moves
        global bishopb_moves
        global queenb_moves
        global knightb_moves
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fv=0
                roomx,roomy=pygame.mouse.get_pos()
                gh=roomx%60
                roomx=(roomx-gh)+30
                gh=roomy%60
                roomy=(roomy-gh)+30
                if roomx==self.coords2[0][0] and roomy==self.coords2[0][1]:
                    piece=("")
                    fv=1
                    tg=1
                    if fv==0:
                        tg=3
                        return tg

                    if fv==1:
                        self.coords=[]
                        self.coords2=[]
                        return tg
                    elif fv==2:
                        self.coords=[]
                        self.coords2=[]
                        return tg
                else:
                    for k1 in range (0, len(self.coords)):
                        roomx,roomy=pygame.mouse.get_pos()
                        gh=roomx%60
                        roomx=(roomx-gh)+30
                        gh=roomy%60
                        roomy=(roomy-gh)+30
                        if roomx==self.coords[k1][0] and roomy==self.coords[k1][1]:
                            if roomy==30:
                                event2=wait()
                                if event2.type==pygame.KEYDOWN and event2.key==pygame.K_q:
                                    if queenb_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q2b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        queenb_moves=queenb_moves+1
                                        fv=2
                                        tg=2
                                    elif queenb_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        queenb_moves=queenb_moves+1
                                        fv=2
                                        tg=2
                                    elif queenb_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="q4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        queenb_moves=queenb_moves+1
                                        fv=2
                                        tg=2
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_r:
                                    if rookb_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        rookb_moves=rookb_moves+1
                                    elif rookb_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        rookb_moves=rookb_moves+1
                                    elif rookb_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="r5b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        rookb_moves=rookb_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_b:
                                    if bishopb_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        bishopb_moves=bishopb_moves+1
                                    elif bishopb_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        bishopb_moves=bishopb_moves+1
                                    elif bishopb_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="b5b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        bishopb_moves=bishopb_moves+1
                                elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_k:
                                    if knightb_moves==0:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn3b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        knightb_moves=knightb_moves+1
                                    elif knightb_moves==1:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn4b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        knightb_moves=knightb_moves+1
                                    elif knightb_moves==2:
                                        yposition=list_searchy(Board,self.number)
                                        xposition=list_searchx(Board,self.number)
                                        Board[yposition][xposition][0]=""
                                        Board[yposition][xposition][1]=""                                        
                                        yposition=(roomy-30)//60
                                        xposition=(roomx-30)//60
                                        Board[(roomy-30)//60][(roomx-30)//60][0]="kn5b"
                                        Board[(roomy-30)//60][(roomx-30)//60][1]="b"
                                        fv=2
                                        tg=2
                                        knightb_moves=knightb_moves+1
                            else:
                                piece=("")
                                self.bwmx,self.bwmy=pygame.mouse.get_pos()
                                fv=2
                                self.bwmx=convertx(self.bwmx)
                                self.bwmx=self.bwmx//60
                                self.bwmy=converty(self.bwmy)
                                self.bwmy=self.bwmy//60
                                yposition=list_searchy(Board,self.number)
                                xposition=list_searchx(Board,self.number)
                                firstposition1=Board[yposition][xposition][0]
                                firstposition2=Board[yposition][xposition][1]
                                Board[yposition][xposition][0]=""
                                Board[yposition][xposition][1]=""
                                Board[self.bwmy][self.bwmx][0]=""
                                Board[self.bwmy][self.bwmx][1]=""
                                Board[self.bwmy][self.bwmx][0]=firstposition1
                                Board[self.bwmy][self.bwmx][1]=firstposition2
                                tg=2
                            if fv==0:
                                tg=3
                                return tg

                            if fv==1:
                                self.coords=[]
                                self.coords2=[]
                                return tg
                            elif fv==2:
                                self.coords=[]
                                self.coords2=[]
                                return tg
                    
        else:
            return tg
def wait():
    fgh=False
    pygame.event.clear()
    while fgh==False:
        event2=pygame.event.wait()
        if event2.type==pygame.KEYDOWN and event2.key==pygame.K_q:
            fgh=True
        elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_r:
            fgh=True
        elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_k:
            fgh=True
        elif event2.type==pygame.KEYDOWN and event2.key==pygame.K_b:
            fgh=True
    return event2
def wait2():
    fgh=False
    pygame.event.clear()
    while fgh==False:
        event3=pygame.event.wait()
        if event3.type==pygame.MOUSEBUTTONDOWN:
            fgh=True
    return event3
class bishop1(object):
    def __init__(self,b11,b12,b13,b14,black_protector,vc,king,colour,colour2):
        self.b11=b11
        self.b12=b12
        self.b13=b13
        self.b14=b14
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
    def check(self,b11,b12,b13,b14,black_protector,vc,king,colour,colour2):
        self.b11=b11
        self.b12=b12
        self.b13=b13
        self.b14=b14
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
        global two_protectors
        pos_spaces=[]
        jk=False
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=1+yposition
                xposition=1+xposition
                xposition2=xposition*60
                yposition2=yposition*60
        
                if yposition<8 and xposition<8 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.b11.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.b11.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                            yposition=1+yposition
                            xposition=1+xposition
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.b11.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
            
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition-1
                xposition=xposition-1
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.b12.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.b12.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:
                            yposition=yposition-1
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                 
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.b12.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=1+xposition
                yposition=yposition-1
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.b13.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.b13.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                            xposition=1+xposition
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                 
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.b13.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                yposition=yposition+1
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.b14.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.b14.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition+1
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                 
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.b14.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False

class queen1(object):
    def __init__(self,q11,q12,q13,q14,q15,q16,q17,q18,black_protector,vc,king,colour,colour2):
        self.q11=q11
        self.q12=q12
        self.q13=q13
        self.q14=q14
        self.q15=q15
        self.q16=q16
        self.q17=q17
        self.q18=q18
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
    def check(self,q11,q12,q13,q14,q15,q16,q17,q18,black_protector,vc,king,colour,colour2):
        self.q11=q11
        self.q12=q12
        self.q13=q13
        self.q14=q14
        self.q15=q15
        self.q16=q16
        self.q17=q17
        self.q18=q18
        self.vc=vc
        global two_protectors
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
        jk=False
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=1+yposition
                xposition=1+xposition
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.q11.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q11.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                            
                            yposition=1+yposition
                            xposition=1+xposition
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True     
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q11.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                yposition=yposition-1
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.q12.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q12.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition-1
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        self.q12.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=1+xposition
                yposition=yposition-1
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.q13.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q13.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                            xposition=1+xposition
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q13.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                yposition=yposition+1
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.q14.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q14.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition+1
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q14.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition+1
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.q15.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q15.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:                                
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=False                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q15.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
                    
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q16.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q16.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q16.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.q17.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q17.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                    
                            xposition=xposition+1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q17.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            
            pos_spaces=[]
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.q18.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.q18.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.q18.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            

class knight1(object):
    def __init__(self,kn1,black_protector,vc,king,colour,colour2):
        self.kn1=kn1
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
    def check(self,kn1,black_protector,vc,king,colour,colour2):
        self.kn1=kn1
        self.vc=vc
        self.king=king
        global two_protectors
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector

        jk=False
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            yposition=2+yposition
            xposition=1+xposition
            xposition2=xposition*60
            yposition2=yposition*60

            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            yposition=2+yposition
            xposition=xposition-1
            
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

            yposition=yposition-2
            xposition=1+xposition
            
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition-2
            xposition=xposition-1
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
    
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition-1
            xposition=xposition-2
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition+1
            xposition=xposition-2
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :          
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
                                    
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition+1
            xposition=xposition+2 
            xposition2=xposition*60
            yposition2=yposition*60                    
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition-1
            xposition=xposition+2
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                self.kn1.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.kn1.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.kn1.append([xposition2,yposition2])
                
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)

class rook1(object):
    def __init__(self,r11,r12,r13,r14,black_protector,vc,king,colour,colour2):
        self.r11=r11
        self.r12=r12
        self.r13=r13
        self.r14=r14
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
    def check(self,r11,r12,r13,r14,black_protector,vc,king,colour,colour2):
        self.r11=r11
        self.r12=r12
        self.r13=r13
        global two_protectors
        self.r14=r14
        self.vc=vc
        self.king=king
        self.colour=colour
        self.colour2=colour2
        self.black_protector=black_protector
        jk=False
        yposition=list_searchy(Board,vc)
        xposition=list_searchx(Board,vc)
        if yposition!=9 or xposition!=9:
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    self.r11.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.r11.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                    
                            yposition=yposition+1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.r11.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True

            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            pos_spaces=[]
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                yposition=yposition-1
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.r12.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.r12.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            yposition=yposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.r12.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            pos_spaces=[]
            while jk==False:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition+1
                
                xposition2=xposition*60
                yposition2=yposition*60
                if yposition<8 and xposition<8 and  yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.r13.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.r13.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==False:
                    
                            xposition=xposition+1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=True
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=True
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.r13.append([xposition2,yposition2])
                        jk=True
                    else:
                        jk=True
            yposition=list_searchy(Board,vc)
            xposition=list_searchx(Board,vc)
            pos_spaces=[]
            
            while jk==True:
                pos_spaces.append([xposition*60,yposition*60])
                xposition=xposition-1
                
                xposition2=xposition*60
                yposition2=yposition*60
                
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1  and Board[yposition][xposition][0]=="" :
                    pos_spaces.append([xposition*60,yposition*60])
                    
                    self.r14.append([xposition2,yposition2])
                else:
                    if yposition<8 and xposition<8  and yposition>-1 and xposition>-1 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                        self.r14.append([xposition2,yposition2])
                        piece2=Board[yposition][xposition][0]
                        while jk==True:                                
                            xposition=xposition-1
                            pos_spaces.append([xposition*60,yposition*60])
                            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1:
                                if Board[yposition][xposition][0]==self.king:
                                    for i in range(0,len(pos_spaces)):
                                        black_protector.append([piece2,pos_spaces[i][0],pos_spaces[i][1]])
                                        jk=False
                                elif Board[yposition][xposition][1]==self.colour:
                                    two_protectors=True                                      
                            else:
                                jk=False
                    elif yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                        
                        self.r14.append([xposition2,yposition2])
                        jk=False
                    else:
                        jk=False


class king1(object):
    def __init__(self,k1w,vc,colour,colour2):
        self.k1w=k1w
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
    def check(self,k1w,vc,colour,colour2):
        self.k1w=k1w
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
        global two_protectors
        jk=False
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            yposition=1+yposition
            xposition=1+xposition
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][0]=="" :
                self.k1w.append([xposition2,yposition2])
            else:
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition-1
            xposition=xposition-1
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition>-1 and xposition>-1 and  Board[yposition][xposition][0]==""  :
                self.k1w.append([xposition2,yposition2])
            else:
                if yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            xposition=1+xposition
            yposition=yposition-1
            xposition2=xposition*60
            yposition2=yposition*60
            if xposition<8 and yposition>-1 and Board[yposition][xposition][0]=="" :
               
                self.k1w.append([xposition2,yposition2])
            else:
                if xposition<8 and yposition>-1  and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            xposition=xposition-1
            yposition=yposition+1
            xposition2=xposition*60
            yposition2=yposition*60
            
            if xposition>-1 and yposition<8  and Board[yposition][xposition][0]=="" :
                self.k1w.append([xposition2,yposition2])
            else:
                if xposition>-1 and yposition<8 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])

            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=1+yposition
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and Board[yposition][xposition][0]=="" :
                self.k1w.append([xposition2,yposition2])
            else:
                if yposition<8 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
                    
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition-1
            xposition2=xposition*60
            yposition2=yposition*60

            if Board[yposition][xposition][0]=="" and yposition>-1:
                self.k1w.append([xposition2,yposition2])
            else:
                if yposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            xposition=1+xposition
            xposition2=xposition*60
            yposition2=yposition*60
            if xposition<8 and Board[yposition][xposition][0]=="" :
                self.k1w.append([xposition2,yposition2])
            else:
                if xposition<8 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            xposition=xposition-1
            xposition2=xposition*60
            yposition2=yposition*60
            if xposition>-1 and Board[yposition][xposition][0]=="" :
                self.k1w.append([xposition2,yposition2])
            else:
                if xposition>-1 and Board[yposition][xposition][1]==self.colour:
                    self.k1w.append([xposition2,yposition2])
                if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2:
                    self.k1w.append([xposition2,yposition2])

class pawn1w(object):
    def __init__(self,p1,vc,colour,colour2):
        self.p1=p1
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
    def check(self,p1,vc,colour,colour2):
        self.p1=p1
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
        global two_protectors
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            yposition=1+yposition
            xposition=xposition-1
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]=="" :
                self.p1.append([xposition2,yposition2])            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour :
                self.p1.append([xposition2,yposition2])
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2 :
                self.p1.append([xposition2,yposition2])
        
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)                
        if yposition!=9 or xposition!=9:
            yposition=1+yposition
            xposition=xposition+1
            xposition2=xposition*60
            yposition2=yposition*60
            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]=="" :
                self.p1.append([xposition2,yposition2])            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour :
                self.p1.append([xposition2,yposition2])
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2 :
                self.p1.append([xposition2,yposition2])

class pawn1b(object):
    def __init__(self,p1b,vc,colour,colour2):
        self.p1b=p1b
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
    def check(self,p1,vc,colour,colour2):
        self.p1b=p1b
        self.vc=vc
        self.colour=colour
        self.colour2=colour2
        global two_protectors
        yposition=list_searchy(Board,self.vc)
        xposition=list_searchx(Board,self.vc)
        if yposition!=9 or xposition!=9:
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition-1
            xposition=xposition-1
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]=="" :
                self.p1b.append([xposition2,yposition2])            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour :
                self.p1b.append([xposition2,yposition2])
                
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2 :
                self.p1b.append([xposition2,yposition2])
            yposition=list_searchy(Board,self.vc)
            xposition=list_searchx(Board,self.vc)
            yposition=yposition-1
            xposition=xposition+1
            xposition2=xposition*60
            yposition2=yposition*60
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]=="" :
                self.p1b.append([xposition2,yposition2])            
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour :
                self.p1b.append([xposition2,yposition2])
            if yposition<8 and xposition<8 and yposition>-1 and xposition>-1 and Board[yposition][xposition][1]==self.colour2 :
                self.p1b.append([xposition2,yposition2])
class Status(object):
    def __init__(self,vc,pawn_black1_status):
        self.vc=vc
        self.pawn_black1_status=pawn_black1_status
    def Status2(self,vc,pawn_black1_status):
        xposition=list_searchx(Board,self.vc)        
        if xposition==9:
            self.pawn_black1_status="dead"
class Status1(object):
    def __init__(self,vc,queen_black4_status,queen4b_spawn,q4bmx,q4bmy):
        self.vc=vc
        self.queen_black4_status=queen_black4_status
        self.queen4b_spawn=queen4b_spawn
        self.q4bmx=q4bmx
        self.q4bmy=q4bmy
    def Status21(self,vc,queen_black4_status,queen4b_spawn,q4bmx,q4bmy):
        xposition=list_searchx(Board,self.vc)
        yposition=list_searchy(Board,self.vc)
        if self.queen4b_spawn==0:
            if xposition<9:
                self.q4bmx=xposition*60
                self.q4bmy=yposition*60
                self.queen_black4_status="alive"
                self.queen4b_spawn=1

class attack_class_and_all_white(object):
    def __init__(self,vc,attack_piece,black_check,attack,attack_positions,all_white):
        self.vc=vc
        self.attack_piece=attack_piece
        self.black_check=black_check
        self.attack=attack
        self.attack_positions=attack_positions
        self.all_white=all_white
    def attack_class1(self,vc,attack_piece,black_check,attack,attack_positions,all_white):
        if vc[2]=="b":            
            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
        else:
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
        xposition=60*xposition
        yposition=60*yposition
        for ju in range (0,len(self.attack_piece)):
            if xposition==self.attack_piece[ju][0] and yposition==self.attack_piece[ju][1]:
                self.attack.append([self.vc])
                self.attack_positions=self.attack_piece
    def all_white_class1(self,vc,attack_piece,black_check,attack,attack_positions,all_white):
        yposition=list_searchy(Board,"k1b")
        xposition=list_searchx(Board,"k1b")
        xposition=60*xposition
        yposition=60*yposition
        for i in range (0,len(self.attack_piece)):
            if self.attack_piece!=[]:
                self.all_white.append(self.attack_piece[i])
                if self.attack_piece[len(self.attack_piece)-1][0]==xposition and self.attack_piece[len(self.attack_piece)-1][1]==yposition:
                    yposition1=list_searchy(Board,self.vc)*60
                    xposition1=list_searchx(Board,self.vc)*60
                    x_addition=self.attack_piece[0][0]-xposition1
                    y_addition=self.attack_piece[0][1]-yposition1
                    r122=(self.attack_piece[(len(self.attack_piece))-1][0])
                    r123=(self.attack_piece[(len(self.attack_piece))-1][1])                
                    r121=[r122+x_addition,r123+y_addition]
                    self.all_white.append(r121)

class attack_class_and_all_black(object):
    def __init__(self,vc,attack_piece,black_check,attack,attack_positions,all_black):
        self.vc=vc
        self.attack_piece=attack_piece
        self.black_check=black_check
        self.attack=attack
        self.attack_positions=attack_positions
        self.all_black=all_black
    def attack_class1(self,vc,attack_piece,black_check,attack,attack_positions,all_black):
        if vc[2]=="b":            
            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
        else:
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
        xposition=60*xposition
        yposition=60*yposition
        for ju in range (0,len(self.attack_piece)):
            if xposition==self.attack_piece[ju][0] and yposition==self.attack_piece[ju][1]:
                self.attack.append([self.vc])
                self.attack_positions=self.attack_piece
    def all_black_class1(self,vc,attack_piece,black_check,attack,attack_positions,all_black):
        yposition=list_searchy(Board,"k1w")
        xposition=list_searchx(Board,"k1w")
        xposition=60*xposition
        yposition=60*yposition
        for i in range (0,len(self.attack_piece)):
            if self.attack_piece!=[]:
                self.all_black.append(self.attack_piece[i])
                if self.attack_piece[len(self.attack_piece)-1][0]==xposition and self.attack_piece[len(self.attack_piece)-1][1]==yposition:
                    yposition1=list_searchy(Board,self.vc)*60
                    xposition1=list_searchx(Board,self.vc)*60
                    x_addition=self.attack_piece[0][0]-xposition1
                    y_addition=self.attack_piece[0][1]-yposition1
                    r122=(self.attack_piece[(len(self.attack_piece))-1][0])
                    r123=(self.attack_piece[(len(self.attack_piece))-1][1])                
                    r121=[r122+x_addition,r123+y_addition]
                    self.all_black.append(r121)
class all_black_class(object):
    def __init__(self,all_black,piece_attack,piece):
        self.all_black=all_black
        self.piece_attack=piece_attack
        self.piece=piece
    def all_black_class1(self,all_black,piece_attack,piece):
        yposition=list_searchy(Board,"k1w")
        xposition=list_searchx(Board,"k1w")
        xposition=60*xposition
        yposition=60*yposition
        for i in range (0,len(self.piece_attack)):
            if self.piece_attack!=[]:
                self.all_black.append(self.piece_attack[i])
                if self.piece_attack[len(self.piece_attack)-1][0]==xposition and self.piece_attack[len(self.piece_attack)-1][1]==yposition:
                    yposition1=list_searchy(Board,self.piece)*60
                    xposition1=list_searchx(Board,self.piece)*60
                    x_addition=self.piece_attack[0][0]-xposition1
                    y_addition=self.piece_attack[0][1]-yposition1
                    r122=(self.piece_attack[(len(self.piece_attack))-1][0])
                    r123=(self.piece_attack[(len(self.piece_attack))-1][1])                
                    r121=[r122+x_addition,r123+y_addition]
                    self.all_black.append(r121)
def convertx(piecex):
    d=piecex%60
    piecex=piecex-d
    return piecex

def converty(piecey):
    d=piecey%60
    piecey=piecey-d
    return piecey

def board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy):
    r1wmx=convertx(r1wmx)
    r1wmy=converty(r1wmy)
    
    r2wmx=convertx(r2wmx)
    r2wmy=converty(r2wmy)

    r3wmx=convertx(r3wmx)
    r3wmy=converty(r3wmy)

    r4wmx=convertx(r4wmx)
    r4wmy=converty(r4wmy)

    r5wmx=convertx(r5wmx)
    r5wmy=converty(r5wmy)
    
    r2bmx=convertx(r2bmx)
    r2bmy=converty(r2bmy)

    r3bmx=convertx(r3bmx)
    r3bmy=converty(r3bmy)

    r4bmx=convertx(r4bmx)
    r4bmy=converty(r4bmy)

    r5bmx=convertx(r5bmx)
    r5bmy=converty(r5bmy)
    
    r1bmx=convertx(r1bmx)
    r1bmy=converty(r1bmy)
    
    b1wmx=convertx(b1wmx)
    b1wmy=converty(b1wmy)
    
    b2wmx=convertx(b2wmx)
    b2wmy=converty(b2wmy)

    b3wmx=convertx(b3wmx)
    b3wmy=converty(b3wmy)

    b4wmx=convertx(b4wmx)
    b4wmy=converty(b4wmy)

    b5wmx=convertx(b5wmx)
    b5wmy=converty(b5wmy)
    
    b1bmx=convertx(b1bmx)
    b1bmy=converty(b1bmy)

    b2bmx=convertx(b2bmx)
    b2bmy=converty(b2bmy)

    b3bmx=convertx(b3bmx)
    b3bmy=converty(b3bmy)

    b4bmx=convertx(b4bmx)
    b4bmy=converty(b4bmy)

    b5bmx=convertx(b5bmx)
    b5bmy=converty(b5bmy)
    
    kn1wmx=convertx(kn1wmx)
    kn1wmy=converty(kn1wmy)

    kn2wmx=convertx(kn2wmx)
    kn2wmy=converty(kn2wmy)

    kn3wmx=convertx(kn3wmx)
    kn3wmy=converty(kn3wmy)

    kn4wmx=convertx(kn4wmx)
    kn4wmy=converty(kn4wmy)

    kn5wmx=convertx(kn5wmx)
    kn5wmy=converty(kn5wmy)
    
    kn1bmx=convertx(kn1bmx)
    kn1bmy=converty(kn1bmy)

    kn2bmx=convertx(kn2bmx)
    kn2bmy=converty(kn2bmy)

    kn3bmx=convertx(kn3bmx)
    kn3bmy=converty(kn3bmy)

    kn4bmx=convertx(kn4bmx)
    kn4bmy=converty(kn4bmy)

    kn5bmx=convertx(kn5bmx)
    kn5bmy=converty(kn5bmy)
    
    q1wmx=convertx(q1wmx)
    q1wmy=converty(q1wmy)

    q2wmx=convertx(q2wmx)
    q2wmy=converty(q2wmy)

    q3wmx=convertx(q3wmx)
    q3wmy=converty(q3wmy)

    q4wmx=convertx(q4wmx)
    q4wmy=converty(q4wmy)
    
    q1bmx=convertx(q1bmx)
    q1bmy=converty(q1bmy)

    q2bmx=convertx(q2bmx)
    q2bmy=converty(q2bmy)

    q3bmx=convertx(q3bmx)
    q3bmy=converty(q3bmy)

    q4bmx=convertx(q4bmx)
    q4bmy=converty(q4bmy)
    
    k1wmx=convertx(k1wmx)
    k1wmy=converty(k1wmy)

    k1bmx=convertx(k1bmx)
    k1bmy=converty(k1bmy)

    p8wmx=convertx(p8wmx)
    p8wmy=converty(p8wmy)

    p7wmx=convertx(p7wmx)
    p7wmy=converty(p7wmy)

    p6wmx=convertx(p6wmx)
    p6wmy=converty(p6wmy)

    p5wmx=convertx(p5wmx)
    p5wmy=converty(p5wmy)

    p4wmx=convertx(p4wmx)
    p4wmy=converty(p4wmy)

    p3wmx=convertx(p3wmx)
    p3wmy=converty(p3wmy)

    p2wmx=convertx(p2wmx)
    p2wmy=converty(p2wmy)

    p1wmx=convertx(p1wmx)
    p1wmy=converty(p1wmy)

    p1bmx=convertx(p1bmx)
    p1bmy=converty(p1bmy)

    p2bmx=convertx(p2bmx)
    p2bmy=converty(p2bmy)

    p3bmx=convertx(p3bmx)
    p3bmy=converty(p3bmy)

    p4bmx=convertx(p4bmx)
    p4bmy=converty(p4bmy)

    p5bmx=convertx(p5bmx)
    p5bmy=converty(p5bmy)

    p6bmx=convertx(p6bmx)
    p6bmy=converty(p6bmy)

    p7bmx=convertx(p7bmx)
    p7bmy=converty(p7bmy)

    p8bmx=convertx(p8bmx)
    p8bmy=converty(p8bmy)
    
    win.blit(bg,(0,0))
    if king_black_status=="alive":
        gameDisplay.blit(king_black,(k1bmx,k1bmy))
    else:
        gameDisplay.blit(king_black,(481,481))
    if king_white_status=="alive":
        gameDisplay.blit(king_white,(k1wmx,k1wmy))
    else:
        gameDisplay.blit(king_white,(481,481))
    if queen_black_status=="alive":
        gameDisplay.blit(queen_black,(q1bmx,q1bmy))
    else:
        gameDisplay.blit(queen_black,(480,60))
    if queen_black2_status=="alive":
        gameDisplay.blit(queen_black2,(q2bmx,q2bmy))
    else:
        gameDisplay.blit(queen_black2,(481,481))
    if queen_black3_status=="alive":
        gameDisplay.blit(queen_black3,(q3bmx,q3bmy))
    else:
        gameDisplay.blit(queen_black3,(481,481))
    if queen_black4_status=="alive":
        gameDisplay.blit(queen_black4,(q4bmx,q4bmy))
    else:
        gameDisplay.blit(queen_black4,(481,481))
    if queen_white_status=="alive":
        gameDisplay.blit(queen_white,(q1wmx,q1wmy))
    else:
        gameDisplay.blit(queen_white,(480,300))
    if queen_white2_status=="alive":
        gameDisplay.blit(queen_white2,(q2wmx,q2wmy))
    else:
        gameDisplay.blit(queen_white2,(481,481))
    if queen_white3_status=="alive":
        gameDisplay.blit(queen_white3,(q3wmx,q3wmy))
    else:
        gameDisplay.blit(queen_white3,(481,481))
    if queen_white4_status=="alive":
        gameDisplay.blit(queen_white4,(q4wmx,q4wmy))
    else:
        gameDisplay.blit(queen_white4,(481,481))
    if rook_black1_status=="alive":
        gameDisplay.blit(rook_black1,(r1bmx,r1bmy))
    else:
        gameDisplay.blit(rook_black1,(540,60))
    if rook_black2_status=="alive":
        gameDisplay.blit(rook_black2,(r2bmx,r2bmy))
    else:
        gameDisplay.blit(rook_black2,(600,60))
    if rook_black3_status=="alive":
        gameDisplay.blit(rook_black3,(r3bmx,r3bmy))
    else:
        gameDisplay.blit(rook_black3,(481,481))
    if rook_black4_status=="alive":
        gameDisplay.blit(rook_black4,(r4bmx,r4bmy))
    else:
        gameDisplay.blit(rook_black4,(481,481))
    if rook_black5_status=="alive":
        gameDisplay.blit(rook_black5,(r5bmx,r5bmy))
    else:
        gameDisplay.blit(rook_black5,(481,481))                 
    if rook_white1_status=="alive":
        gameDisplay.blit(rook_white1,(r1wmx,r1wmy))
    else:
        gameDisplay.blit(rook_black1,(481,481)) 
    if rook_white2_status=="alive":
        gameDisplay.blit(rook_white2,(r2wmx,r2wmy))
    else:
        gameDisplay.blit(rook_white2,(481,481))
    if rook_white3_status=="alive":
        gameDisplay.blit(rook_white3,(r3wmx,r3wmy))
    else:
        gameDisplay.blit(rook_white3,(481,481))
    if rook_white4_status=="alive":
        gameDisplay.blit(rook_white4,(r4wmx,r4wmy))
    else:
        gameDisplay.blit(rook_white4,(481,481))
    if rook_white5_status=="alive":
        gameDisplay.blit(rook_white5,(r5wmx,r5wmy))
    else:
        gameDisplay.blit(rook_white5,(481,481))
    if knight_black1_status=="alive":
        gameDisplay.blit(knight_black1,(kn1bmx,kn1bmy))
    else:
        gameDisplay.blit(knight_black1,(660,60))
    if knight_black2_status=="alive":   
        gameDisplay.blit(knight_black2,(kn2bmx,kn2bmy))
    else:
        gameDisplay.blit(knight_black2,(720,60))
    if knight_black3_status=="alive":   
        gameDisplay.blit(knight_black3,(kn3bmx,kn3bmy))
    else:
        gameDisplay.blit(knight_black3,(481,481))
    if knight_black4_status=="alive":   
        gameDisplay.blit(knight_black4,(kn4bmx,kn4bmy))
    else:
        gameDisplay.blit(knight_black4,(481,481))
    if knight_black5_status=="alive":   
        gameDisplay.blit(knight_black5,(kn5bmx,kn5bmy))
    else:
        gameDisplay.blit(knight_black5,(481,481))
    if knight_white1_status=="alive":
        gameDisplay.blit(knight_white1,(kn1wmx,kn1wmy))
    else:
        gameDisplay.blit(knight_white1,(481,481))
    if knight_white2_status=="alive":
        gameDisplay.blit(knight_white2,(kn2wmx,kn2wmy))
    else:
        gameDisplay.blit(knight_white2,(481,481))
    if knight_white3_status=="alive":
        gameDisplay.blit(knight_white3,(kn3wmx,kn3wmy))
    else:
        gameDisplay.blit(knight_white3,(481,481))
    if knight_white4_status=="alive":
        gameDisplay.blit(knight_white4,(kn4wmx,kn4wmy))
    else:
        gameDisplay.blit(knight_white4,(481,481))
    if knight_white5_status=="alive":
        gameDisplay.blit(knight_white5,(kn5wmx,kn5wmy))
    else:
        gameDisplay.blit(knight_white5,(481,481))
    if bishop_black1_status=="alive":
        gameDisplay.blit(bishop_black1,(b1bmx,b1bmy))
    else:
        gameDisplay.blit(bishop_black1,(780,60))
    if bishop_black2_status=="alive":  
        gameDisplay.blit(bishop_black2,(b2bmx,b2bmy))
    else:
        gameDisplay.blit(bishop_black2,(840,60))
    if bishop_black3_status=="alive":  
        gameDisplay.blit(bishop_black3,(b3bmx,b3bmy))
    else:
        gameDisplay.blit(bishop_black3,(481,481))
    if bishop_black4_status=="alive":  
        gameDisplay.blit(bishop_black4,(b4bmx,b4bmy))
    else:
        gameDisplay.blit(bishop_black4,(481,481))
    if bishop_black5_status=="alive":  
        gameDisplay.blit(bishop_black5,(b5bmx,b5bmy))
    else:
        gameDisplay.blit(bishop_black5,(481,481))
    if bishop_white1_status=="alive":   
        gameDisplay.blit(bishop_white1,(b1wmx,b1wmy))
    else:
        gameDisplay.blit(bishop_white1,(481,481))
    if bishop_white2_status=="alive":     
        gameDisplay.blit(bishop_white2,(b2wmx,b2wmy))
    else:
        gameDisplay.blit(bishop_white2,(481,481))
    if bishop_white3_status=="alive":     
        gameDisplay.blit(bishop_white3,(b3wmx,b3wmy))
    else:
        gameDisplay.blit(bishop_white3,(481,481))
    if bishop_white4_status=="alive":     
        gameDisplay.blit(bishop_white4,(b4wmx,b4wmy))
    else:
        gameDisplay.blit(bishop_white4,(481,481))
    if bishop_white5_status=="alive":     
        gameDisplay.blit(bishop_white5,(b5wmx,b5wmy))
    else:
        gameDisplay.blit(bishop_white5,(481,481))
    if pawn_white1_status=="alive":   
        gameDisplay.blit(pawn_white1,(p1wmx,p1wmy))
    else:
        gameDisplay.blit(pawn_white1,(481,481))
    if pawn_white2_status=="alive":
        gameDisplay.blit(pawn_white2,(p2wmx,p2wmy))
    else:
        gameDisplay.blit(pawn_white2,(481,481))
    if pawn_white3_status=="alive":   
        gameDisplay.blit(pawn_white3,(p3wmx,p3wmy))
    else:
        gameDisplay.blit(pawn_white3,(481,481))
    if pawn_white4_status=="alive":    
        gameDisplay.blit(pawn_white4,(p4wmx,p4wmy))
    else:
        gameDisplay.blit(pawn_white4,(481,481))
    if pawn_white5_status=="alive":
        gameDisplay.blit(pawn_white5,(p5wmx,p5wmy))
    else:
        gameDisplay.blit(pawn_white5,(481,481))
    if pawn_white6_status=="alive":   
        gameDisplay.blit(pawn_white6,(p6wmx,p6wmy))
    else:
        gameDisplay.blit(pawn_white6,(481,481))
    if pawn_white7_status=="alive":  
        gameDisplay.blit(pawn_white7,(p7wmx,p7wmy))
    else:
        gameDisplay.blit(pawn_white7,(481,481))
    if pawn_white8_status=="alive": 
        gameDisplay.blit(pawn_white8,(p8wmx,p8wmy))
    else:
        gameDisplay.blit(pawn_white8,(481,481))
    if pawn_black1_status=="alive":
        gameDisplay.blit(pawn_black1,(p1bmx,p1bmy))
    else:
        gameDisplay.blit(pawn_black1,(900,60))
    if pawn_black2_status=="alive":    
        gameDisplay.blit(pawn_black2,(p2bmx,p2bmy))
    else:
        gameDisplay.blit(pawn_black2,(480,120))
    if pawn_black3_status=="alive":   
        gameDisplay.blit(pawn_black3,(p3bmx,p3bmy))
    else:
        gameDisplay.blit(pawn_black3,(481,481))
    if pawn_black4_status=="alive":
        gameDisplay.blit(pawn_black4,(p4bmx,p4bmy))
    else:
        gameDisplay.blit(pawn_black4,(481,481))
    if pawn_black5_status == "alive":
        gameDisplay.blit(pawn_black5,(p5bmx,p5bmy))
    else:
        gameDisplay.blit(pawn_black5,(481,481))             
    if pawn_black6_status== "alive" :                      
        gameDisplay.blit(pawn_black6,(p6bmx,p6bmy))
    else:
        gameDisplay.blit(pawn_black6,(481,481))
    if pawn_black7_status=="alive":                     
        gameDisplay.blit(pawn_black7,(p7bmx,p7bmy))
    else:
        gameDisplay.blit(pawn_black7,(481,481))
    if pawn_black8_status=="alive":
        gameDisplay.blit(pawn_black8,(p8bmx,p8bmy))
    else:
        gameDisplay.blit(pawn_black8,(481,481))
    
def list_searchy(Board, piece):
    f=9
    for i in range (0,8):
        for a in range (0,8):
            if Board[i][a][0]==piece:
                f=i
                return f
    return f       
def list_searchx(Board, piece):
    f=9
    for i in range (0,8):
        for a in range (0,8):
            if Board[i][a][0]==piece:
                f=a
                return f
    return f

blength=480
win =pygame.display.set_mode((480,blength))
pygame.display.set_caption("Chess")
gameDisplay=pygame.display.set_mode((480,blength))

rook_white1=pygame.image.load("rook_white.png")
rook_white2=pygame.image.load("rook_white.png")
rook_white3=pygame.image.load("rook_white.png")
rook_white4=pygame.image.load("rook_white.png")
rook_white5=pygame.image.load("rook_white.png")

rook_black1=pygame.image.load("rook_black.png")
rook_black2=pygame.image.load("rook_black.png")
rook_black3=pygame.image.load("rook_black.png")
rook_black4=pygame.image.load("rook_black.png")
rook_black5=pygame.image.load("rook_black.png")

knight_white1=pygame.image.load("knight_white.png")
knight_white2=pygame.image.load("knight_white.png")
knight_white3=pygame.image.load("knight_white.png")
knight_white4=pygame.image.load("knight_white.png")
knight_white5=pygame.image.load("knight_white.png")

knight_black1=pygame.image.load("knight_black.png")
knight_black2=pygame.image.load("knight_black.png")
knight_black3=pygame.image.load("knight_black.png")
knight_black4=pygame.image.load("knight_black.png")
knight_black5=pygame.image.load("knight_black.png")

pawn_white1=pygame.image.load("pawn_white.png")
pawn_white2=pygame.image.load("pawn_white.png")
pawn_white3=pygame.image.load("pawn_white.png")
pawn_white4=pygame.image.load("pawn_white.png")
pawn_white5=pygame.image.load("pawn_white.png")
pawn_white6=pygame.image.load("pawn_white.png")
pawn_white7=pygame.image.load("pawn_white.png")
pawn_white8=pygame.image.load("pawn_white.png")

pawn_black1=pygame.image.load("pawn_black.png")
pawn_black2=pygame.image.load("pawn_black.png")
pawn_black3=pygame.image.load("pawn_black.png")
pawn_black4=pygame.image.load("pawn_black.png")
pawn_black5=pygame.image.load("pawn_black.png")
pawn_black6=pygame.image.load("pawn_black.png")
pawn_black7=pygame.image.load("pawn_black.png")
pawn_black8=pygame.image.load("pawn_black.png")

queen_white=pygame.image.load("queen_white.png")
queen_black=pygame.image.load("queen_black.png")
queen_white2=pygame.image.load("queen_white.png")
queen_black2=pygame.image.load("queen_black.png")
queen_white3=pygame.image.load("queen_white.png")
queen_black3=pygame.image.load("queen_black.png")
queen_white4=pygame.image.load("queen_white.png")
queen_black4=pygame.image.load("queen_black.png")
king_white=pygame.image.load("king_white.png")
king_black=pygame.image.load("king_black.png")

bishop_white1=pygame.image.load("bishop_white.png")
bishop_white2=pygame.image.load("bishop_white.png")
bishop_white3=pygame.image.load("bishop_white.png")
bishop_white4=pygame.image.load("bishop_white.png")
bishop_white5=pygame.image.load("bishop_white.png")

bishop_black1=pygame.image.load("bishop_black.png")
bishop_black2=pygame.image.load("bishop_black.png")
bishop_black3=pygame.image.load("bishop_black.png")
bishop_black4=pygame.image.load("bishop_black.png")
bishop_black5=pygame.image.load("bishop_black.png")

checkmate=pygame.image.load("checkmate.png")
stalemate=pygame.image.load("stalemate.png")
bg=pygame.image.load("ChessBoard.png")

rook_white1_status="alive"
rook_white2_status="alive"
rook_white3_status="alive"
rook_white4_status="alive"
rook_white5_status="alive"

knight_white1_status="alive"
knight_white2_status="alive"
knight_white3_status="alive"
knight_white4_status="alive"
knight_white5_status="alive"


bishop_white1_status="alive"
bishop_white2_status="alive"
bishop_white3_status="alive"
bishop_white4_status="alive"
bishop_white5_status="alive"

king_white_status="alive"
queen_white_status="alive"

queen_white2_status="alive"
queen_white3_status="alive"
queen_white4_status="alive"

pawn_white1_status="alive"
pawn_white2_status="alive"
pawn_white3_status="alive"
pawn_white4_status="alive"
pawn_white5_status="alive"
pawn_white6_status="alive"
pawn_white7_status="alive"
pawn_white8_status="alive"

pawn_black1_status="alive"
pawn_black2_status="alive"
pawn_black3_status="alive"
pawn_black4_status="alive"
pawn_black5_status="alive"
pawn_black6_status="alive"
pawn_black7_status="alive"
pawn_black8_status="alive"

rook_black1_status="alive"
rook_black2_status="alive"
rook_black3_status="alive"
rook_black4_status="alive"
rook_black5_status="alive"

knight_black1_status="alive"
knight_black2_status="alive"
knight_black3_status="alive"
knight_black4_status="alive"
knight_black5_status="alive"

bishop_black1_status="alive"
bishop_black2_status="alive"
bishop_black3_status="alive"
bishop_black4_status="alive"
bishop_black5_status="alive"

king_black_status="alive"
queen_black_status="alive"

queen_black2_status="alive"
queen_black3_status="alive"
queen_black4_status="alive"

rookb_moves=0
bishopb_moves=0
queenb_moves=0
knightb_moves=0

rookw_moves=0
bishopw_moves=0
queenw_moves=0
knightw_moves=0

Board=[[["r1w","w"],["kn1w","w"],["b1w","w"],["q1w", "w"],["k1w", "w"],["b2w","w"],["kn2w","w"],["r2w","w"]],
       [["p1w","w"],["p2w", "w"],["p3w","w"],["p4w","w"],["p5w","w"],["p6w","w"],["p7w", "w"],["p8w","w"]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["",   ""],["",    ""],["",   ""],["",   ""],["",   ""],["",   ""],["",    ""],["",   ""]],
       [["p1b","b"],["p2b", "b"],["p3b","b"],["p4b","b"],["p5b","b"],["p6b","b"],["p7b", "b"],["p8b","b"]],
       [["r1b","b"],["kn1b","b"],["b1b","b"],["q1b", "b"],["k1b", "b"],["b2b","b"],["kn2b","b"],["r2b","b"]]]

attack=[]
r1wmx=0
r1wmy=0

r2wmx=420
r2wmy=0

r3wmx=481
r3wmy=481

r4wmx=481
r4wmy=481

r5wmx=481
r5wmy=481

r2bmx=420
r2bmy=420

r1bmx=0
r1bmy=420

r3bmx=481
r3bmy=481

r4bmx=481
r4bmy=481

r5bmx=481
r5bmy=481

b1wmx=120
b1wmy=0

b3wmx=481
b3wmy=481

b4wmx=481
b4wmy=481

b5wmx=481
b5wmy=481

b2wmx=300
b2wmy=0

b1bmx=120
b1bmy=420

b2bmx=300
b2bmy=420

b3bmx=481
b3bmy=481

b4bmx=481
b4bmy=481

b5bmx=481
b5bmy=481

kn1wmx=60
kn1wmy=0

kn2wmx=360
kn2wmy=0

kn3wmx=481
kn3wmy=481

kn4wmx=481
kn4wmy=481

kn5wmx=481
kn5wmy=481

kn1bmx=60
kn1bmy=420

kn2bmx=360
kn2bmy=420

kn3bmx=481
kn3bmy=481

kn4bmx=481
kn4bmy=481

kn5bmx=481
kn5bmy=481

q1wmx=180
q1wmy=0

q2wmx=481
q2wmy=481

q3wmx=481
q3wmy=481

q4wmx=481
q4wmy=481

q1bmx=180
q1bmy=420

q2bmx=481
q2bmy=481

q3bmx=481
q3bmy=481

q4bmx=481
q4bmy=481

q5bmx=481
q5bmy=481

k1wmx=240
k1wmy=0

k1bmx=240
k1bmy=420

p1wmx=0
p1wmy=60

p2wmx=60
p2wmy=60

p3wmx=120
p3wmy=60

p4wmx=180
p4wmy=60

p5wmx=240
p5wmy=60

p6wmx=300
p6wmy=60

p7wmx=360
p7wmy=60

p8wmx=420
p8wmy=60


p1bmx=0
p1bmy=360

p2bmx=60
p2bmy=360

p3bmx=120
p3bmy=360

p4bmx=180
p4bmy=360

p5bmx=240
p5bmy=360

p6bmx=300
p6bmy=360

p7bmx=360
p7bmy=360

p8bmx=420
p8bmy=360

moves=0
hb=0
hw=0
black=(255,0,0)
run=True
piece=""
board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
pygame.display.update()
coords=[]
coords2=[]

moves28=0
moves27=0
moves26=0
moves25=0
moves24=0
moves23=0
moves22=0
moves21=0

moves28b=0
moves27b=0
moves26b=0
moves25b=0
moves24b=0
moves23b=0
moves22b=0
moves21b=0

moves2kw=0
moves2kb=0
moves2r1w=0
moves2r2w=0
moves2r1b=0
moves2r2b=0

pos_spaces=[]

two_protectors=False

b11=[]
b12=[]
b13=[]
b14=[]

b21=[]
b22=[]
b23=[]
b24=[]

b31=[]
b32=[]
b33=[]
b34=[]

b41=[]
b42=[]
b43=[]
b44=[]

b51=[]
b52=[]
b53=[]
b54=[]

r11=[]
r12=[]
r13=[]
r14=[]

r21=[]
r22=[]
r23=[]
r24=[]

r31=[]
r32=[]
r33=[]
r34=[]

r41=[]
r42=[]
r43=[]
r44=[]

r51=[]
r52=[]
r53=[]
r54=[]

kn1=[]
kn2=[]

q11=[]
q12=[]
q13=[]
q14=[]
q15=[]
q16=[]
q17=[]
q18=[]

q21=[]
q22=[]
q23=[]
q24=[]
q25=[]
q26=[]
q27=[]
q28=[]

q31=[]
q32=[]
q33=[]
q34=[]
q35=[]
q36=[]
q37=[]
q38=[]

q41=[]
q42=[]
q43=[]
q44=[]
q45=[]
q46=[]
q47=[]
q48=[]

k1w=[]

p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
p6=[]
p7=[]
p8=[]

b11b=[]
b12b=[]
b13b=[]
b14b=[]

b21b=[]
b22b=[]
b23b=[]
b24b=[]

b31b=[]
b32b=[]
b33b=[]
b34b=[]

b41b=[]
b42b=[]
b43b=[]
b44b=[]

b51b=[]
b52b=[]
b53b=[]
b54b=[]

r11b=[]
r12b=[]
r13b=[]
r14b=[]

r21b=[]
r22b=[]
r23b=[]
r24b=[]

r31b=[]
r32b=[]
r33b=[]
r34b=[]

r41b=[]
r42b=[]
r43b=[]
r44b=[]

r51b=[]
r52b=[]
r53b=[]
r54b=[]

kn1b=[]
kn2b=[]
kn3b=[]
kn4b=[]
kn5b=[]

q11b=[]
q12b=[]
q13b=[]
q14b=[]
q15b=[]
q16b=[]
q17b=[]
q18b=[]

q21b=[]
q22b=[]
q23b=[]
q24b=[]
q25b=[]
q26b=[]
q27b=[]
q28b=[]

q31b=[]
q32b=[]
q33b=[]
q34b=[]
q35b=[]
q36b=[]
q37b=[]
q38b=[]

q41b=[]
q42b=[]
q43b=[]
q44b=[]
q45b=[]
q46b=[]
q47b=[]
q48b=[]

k1b=[]

p1b=[]
p2b=[]
p3b=[]
p4b=[]
p5b=[]
p6b=[]
p7b=[]
p8b=[]

jkl=0
jkb=0

attack_positions=[]
black_check=False
white_check=False
white_checkmate=False
black_checkmate=False
white_stalemate=False
black_stalemate=False
black_protector=[]
white_protector=[]

queen2w_spawn=0
queen3w_spawn=0
queen4w_spawn=0

queen2b_spawn=0
queen3b_spawn=0
queen4b_spawn=0

bishop3b_spawn=0
bishop4b_spawn=0
bishop5b_spawn=0

bishop3w_spawn=0
bishop4w_spawn=0
bishop5w_spawn=0

rook3w_spawn=0
rook4w_spawn=0
rook5w_spawn=0

rook3b_spawn=0
rook4b_spawn=0
rook5b_spawn=0

knight3w_spawn=0
knight4w_spawn=0
knight5w_spawn=0

knight3b_spawn=0
knight4b_spawn=0
knight5b_spawn=0

counter=0
event3=wait2()
rfv=0
Check_screen=False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False        
        b11=[]
        b12=[]
        b13=[]
        b14=[]

        b21=[]
        b22=[]
        b23=[]
        b24=[]

        b41=[]
        b42=[]
        b43=[]
        b44=[]

        b31=[]
        b32=[]
        b33=[]
        b34=[]

        b51=[]
        b52=[]
        b53=[]
        b54=[]
        
        r11=[]
        r12=[]
        r13=[]
        r14=[]

        r21=[]
        r22=[]
        r23=[]
        r24=[]

        r31=[]
        r32=[]
        r33=[]
        r34=[]

        r41=[]
        r42=[]
        r43=[]
        r44=[]

        r51=[]
        r52=[]
        r53=[]
        r54=[]
        
        kn1=[]
        kn2=[]
        kn3=[]
        kn4=[]
        kn5=[]
        
        q11=[]
        q12=[]
        q13=[]
        q14=[]
        q15=[]
        q16=[]
        q17=[]
        q18=[]

        q21=[]
        q22=[]
        q23=[]
        q24=[]
        q25=[]
        q26=[]
        q27=[]
        q28=[]

        q31=[]
        q32=[]
        q33=[]
        q34=[]
        q35=[]
        q36=[]
        q37=[]
        q38=[]

        q41=[]
        q42=[]
        q43=[]
        q44=[]
        q45=[]
        q46=[]
        q47=[]
        q48=[]
        
        k1w=[]

        p1=[]
        p2=[]
        p3=[]
        p4=[]
        p5=[]
        p6=[]
        p7=[]
        p8=[]

        b11b=[]
        b12b=[]
        b13b=[]
        b14b=[]

        b31b=[]
        b32b=[]
        b33b=[]
        b34b=[]

        b41b=[]
        b42b=[]
        b43b=[]
        b44b=[]

        b51b=[]
        b52b=[]
        b53b=[]
        b54b=[]
        
        b21b=[]
        b22b=[]
        b23b=[]
        b24b=[]

        r11b=[]
        r12b=[]
        r13b=[]
        r14b=[]

        r21b=[]
        r22b=[]
        r23b=[]
        r24b=[]

        r31b=[]
        r32b=[]
        r33b=[]
        r34b=[]

        r41b=[]
        r42b=[]
        r43b=[]
        r44b=[]

        r51b=[]
        r52b=[]
        r53b=[]
        r54b=[]
        
        kn1b=[]
        kn2b=[]
        kn3b=[]
        kn4b=[]
        kn5b=[]
        
        q11b=[]
        q12b=[]
        q13b=[]
        q14b=[]
        q15b=[]
        q16b=[]
        q17b=[]
        q18b=[]
        
        q21b=[]
        q22b=[]
        q23b=[]
        q24b=[]
        q25b=[]
        q26b=[]
        q27b=[]
        q28b=[]

        q31b=[]
        q32b=[]
        q33b=[]
        q34b=[]
        q35b=[]
        q36b=[]
        q37b=[]
        q38b=[]

        q41b=[]
        q42b=[]
        q43b=[]
        q44b=[]
        q45b=[]
        q46b=[]
        q47b=[]
        q48b=[]
        
        k1b=[]

        p1b=[]
        p2b=[]
        p3b=[]
        p4b=[]
        p5b=[]
        p6b=[]
        p7b=[]
        p8b=[]
        
        if hb==0:
            two_protectors=False
            black_protector=[]
            pos_spaces=[]
            all_white=[]
            Bishop1w2=bishop1(b11,b12,b13,b14,black_protector,"b1w","k1b","b","w")
            Bishop1w2.check(b11,b12,b13,b14,black_protector,"b1w","k1b","b","w")
                
            Bishop2w2=bishop1(b21,b22,b23,b24,black_protector,"b2w","k1b","b","w")
            Bishop2w2.check(b21,b22,b23,b24,black_protector,"b2w","k1b","b","w")

            Bishop3w3=bishop1(b31,b32,b33,b34,black_protector,"b3w","k1b","b","w")
            Bishop3w3.check(b31,b32,b33,b34,black_protector,"b3w","k1b","b","w")

            Bishop4w4=bishop1(b41,b42,b43,b44,black_protector,"b4w","k1b","b","w")
            Bishop4w4.check(b41,b42,b43,b44,black_protector,"b4w","k1b","b","w")

            Bishop5w5=bishop1(b51,b52,b53,b54,black_protector,"b5w","k1b","b","w")
            Bishop5w5.check(b51,b52,b53,b54,black_protector,"b5w","k1b","b","w")

            Queen1w2=queen1(q11,q12,q13,q14,q15,q16,q17,q18,black_protector,"q1w","k1b","b","w")
            Queen1w2.check(q11,q12,q13,q14,q15,q16,q17,q18,black_protector,"q1w","k1b","b","w")

            Queen2w2=queen1(q21,q22,q23,q24,q25,q26,q27,q28,black_protector,"q2w","k1b","b","w")
            Queen2w2.check(q21,q22,q23,q24,q25,q26,q27,q28,black_protector,"q2w","k1b","b","w")

            Queen4w4=queen1(q41,q42,q43,q44,q45,q46,q47,q48,black_protector,"q4w","k1b","b","w")
            Queen4w4.check(q41,q42,q43,q44,q45,q46,q47,q48,black_protector,"q4w","k1b","b","w")

            Queen3w3=queen1(q31,q32,q33,q34,q35,q36,q37,q38,black_protector,"q3w","k1b","b","w")
            Queen3w3.check(q31,q32,q33,q34,q35,q36,q37,q38,black_protector,"q3w","k1b","b","w")

            knight1w2=knight1(kn1,black_protector,"kn1w","k1b","b","w")
            knight1w2.check(kn1,black_protector,"kn1w","k1b","b","w")            

            knight2w2=knight1(kn1,black_protector,"kn2w","k1b","b","w")
            knight2w2.check(kn1,black_protector,"kn2w","k1b","b","w")

            knight3w3=knight1(kn3,black_protector,"kn3w","k1b","b","w")
            knight3w3.check(kn3,black_protector,"kn3w","k1b","b","w")

            knight4w4=knight1(kn4,black_protector,"kn4w","k1b","b","w")
            knight4w4.check(kn4,black_protector,"kn4w","k1b","b","w")

            knight5w2=knight1(kn5,black_protector,"kn5w","k1b","b","w")
            knight5w2.check(kn5,black_protector,"kn5w","k1b","b","w") 

            Rook1w2=rook1(r11,r12,r13,r14,black_protector,"r1w","k1b","b","w")
            Rook1w2.check(r11,r12,r13,r14,black_protector,"r1w","k1b","b","w")

            Rook2w2=rook1(r21,r22,r23,r24,black_protector,"r2w","k1b","b","w")
            Rook2w2.check(r21,r22,r23,r24,black_protector,"r2w","k1b","b","w")

            Rook3w2=rook1(r31,r32,r33,r34,black_protector,"r3w","k1b","b","w")
            Rook3w2.check(r31,r32,r33,r34,black_protector,"r3w","k1b","b","w")

            Rook4w2=rook1(r41,r42,r43,r44,black_protector,"r4w","k1b","b","w")
            Rook4w2.check(r41,r42,r43,r44,black_protector,"r4w","k1b","b","w")

            Rook5w2=rook1(r51,r52,r53,r54,black_protector,"r5w","k1b","b","w")
            Rook5w2.check(r51,r52,r53,r54,black_protector,"r5w","k1b","b","w")

            Pawn1w2=pawn1w(p1,"p1w","b","w")
            Pawn1w2.check(p1,"p1w","b","w")

            Pawn2w2=pawn1w(p2,"p2w","b","w")
            Pawn2w2.check(p2,"p2w","b","w")

            Pawn3w2=pawn1w(p3,"p3w","b","w")
            Pawn3w2.check(p3,"p3w","b","w")

            Pawn4w2=pawn1w(p4,"p4w","b","w")
            Pawn4w2.check(p4,"p4w","b","w")

            Pawn5w2=pawn1w(p5,"p5w","b","w")
            Pawn5w2.check(p5,"p5w","b","w")

            Pawn6w2=pawn1w(p6,"p6w","b","w")
            Pawn6w2.check(p6,"p6w","b","w")

            Pawn7w2=pawn1w(p7,"p7w","b","w")
            Pawn7w2.check(p7,"p7w","b","w")

            Pawn8w2=pawn1w(p8,"p8w","b","w")
            Pawn8w2.check(p8,"p8w","b","w")

            King1w2=king1(k1w,"k1w","b","w")
            King1w2.check(k1w,"k1w","b","w")

            attack_positions=[]
            attack=[]
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
            xposition=60*xposition
            yposition=60*yposition
            
            Rook11w_attack=attack_class_and_all_white("r1w",r11,black_check,attack,attack_positions,all_white)
            Rook11w_attack.attack_class1("r1w",r11,black_check,attack,attack_positions,all_white)
            Rook11w_attack.all_white_class1("r1w",r11,black_check,attack,attack_positions,all_white)
            attack_positions=Rook11w_attack.attack_positions
            attack=Rook11w_attack.attack
            
            Rook12w_attack=attack_class_and_all_white("r1w",r12,black_check,attack,attack_positions,all_white)
            Rook12w_attack.attack_class1("r1w",r12,black_check,attack,attack_positions,all_white)
            Rook12w_attack.all_white_class1("r1w",r12,black_check,attack,attack_positions,all_white)
            attack_positions=Rook12w_attack.attack_positions
            attack=Rook12w_attack.attack

            Rook13w_attack=attack_class_and_all_white("r1w",r13,black_check,attack,attack_positions,all_white)
            Rook13w_attack.attack_class1("r1w",r13,black_check,attack,attack_positions,all_white)
            Rook13w_attack.all_white_class1("r1w",r13,black_check,attack,attack_positions,all_white)
            attack_positions=Rook13w_attack.attack_positions
            attack=Rook13w_attack.attack
            
            Rook14w_attack=attack_class_and_all_white("r1w",r14,black_check,attack,attack_positions,all_white)
            Rook14w_attack.attack_class1("r1w",r14,black_check,attack,attack_positions,all_white)
            Rook14w_attack.all_white_class1("r1w",r14,black_check,attack,attack_positions,all_white)
            attack_positions=Rook14w_attack.attack_positions
            attack=Rook14w_attack.attack
                    
            Rook21w_attack=attack_class_and_all_white("r2w",r21,black_check,attack,attack_positions,all_white)
            Rook21w_attack.attack_class1("r2w",r21,black_check,attack,attack_positions,all_white)
            Rook21w_attack.all_white_class1("r2w",r21,black_check,attack,attack_positions,all_white)
            attack_positions=Rook21w_attack.attack_positions
            attack=Rook21w_attack.attack
            
            Rook22w_attack=attack_class_and_all_white("r2w",r22,black_check,attack,attack_positions,all_white)
            Rook22w_attack.attack_class1("r2w",r22,black_check,attack,attack_positions,all_white)
            Rook22w_attack.all_white_class1("r2w",r22,black_check,attack,attack_positions,all_white)
            attack_positions=Rook22w_attack.attack_positions
            attack=Rook22w_attack.attack

            Rook23w_attack=attack_class_and_all_white("r2w",r23,black_check,attack,attack_positions,all_white)
            Rook23w_attack.attack_class1("r2w",r23,black_check,attack,attack_positions,all_white)
            Rook23w_attack.all_white_class1("r2w",r23,black_check,attack,attack_positions,all_white)
            attack_positions=Rook23w_attack.attack_positions
            attack=Rook23w_attack.attack
            
            Rook24w_attack=attack_class_and_all_white("r2w",r24,black_check,attack,attack_positions,all_white)
            Rook24w_attack.attack_class1("r2w",r24,black_check,attack,attack_positions,all_white)
            Rook24w_attack.all_white_class1("r2w",r24,black_check,attack,attack_positions,all_white)
            attack_positions=Rook24w_attack.attack_positions
            attack=Rook24w_attack.attack

            Rook31w_attack=attack_class_and_all_white("r3w",r31,black_check,attack,attack_positions,all_white)
            Rook31w_attack.attack_class1("r3w",r31,black_check,attack,attack_positions,all_white)
            Rook31w_attack.all_white_class1("r3w",r31,black_check,attack,attack_positions,all_white)
            attack_positions=Rook31w_attack.attack_positions
            attack=Rook31w_attack.attack
            
            Rook32w_attack=attack_class_and_all_white("r3w",r32,black_check,attack,attack_positions,all_white)
            Rook32w_attack.attack_class1("r3w",r32,black_check,attack,attack_positions,all_white)
            Rook32w_attack.all_white_class1("r3w",r32,black_check,attack,attack_positions,all_white)
            attack_positions=Rook32w_attack.attack_positions
            attack=Rook32w_attack.attack

            Rook33w_attack=attack_class_and_all_white("r3w",r33,black_check,attack,attack_positions,all_white)
            Rook33w_attack.attack_class1("r3w",r33,black_check,attack,attack_positions,all_white)
            Rook33w_attack.all_white_class1("r3w",r33,black_check,attack,attack_positions,all_white)
            attack_positions=Rook33w_attack.attack_positions
            attack=Rook33w_attack.attack
            
            Rook34w_attack=attack_class_and_all_white("r3w",r34,black_check,attack,attack_positions,all_white)
            Rook34w_attack.attack_class1("r3w",r34,black_check,attack,attack_positions,all_white)
            Rook34w_attack.all_white_class1("r3w",r34,black_check,attack,attack_positions,all_white)
            attack_positions=Rook34w_attack.attack_positions
            attack=Rook34w_attack.attack
            
            Rook41w_attack=attack_class_and_all_white("r4w",r41,black_check,attack,attack_positions,all_white)
            Rook41w_attack.attack_class1("r4w",r41,black_check,attack,attack_positions,all_white)
            Rook41w_attack.all_white_class1("r4w",r41,black_check,attack,attack_positions,all_white)
            attack_positions=Rook41w_attack.attack_positions
            attack=Rook41w_attack.attack
            
            Rook42w_attack=attack_class_and_all_white("r4w",r42,black_check,attack,attack_positions,all_white)
            Rook42w_attack.attack_class1("r4w",r42,black_check,attack,attack_positions,all_white)
            Rook42w_attack.all_white_class1("r4w",r42,black_check,attack,attack_positions,all_white)
            attack_positions=Rook42w_attack.attack_positions
            attack=Rook42w_attack.attack

            Rook43w_attack=attack_class_and_all_white("r4w",r43,black_check,attack,attack_positions,all_white)
            Rook43w_attack.attack_class1("r4w",r43,black_check,attack,attack_positions,all_white)
            Rook43w_attack.all_white_class1("r4w",r43,black_check,attack,attack_positions,all_white)
            attack_positions=Rook43w_attack.attack_positions
            attack=Rook43w_attack.attack
            
            Rook44w_attack=attack_class_and_all_white("r4w",r44,black_check,attack,attack_positions,all_white)
            Rook44w_attack.attack_class1("r4w",r44,black_check,attack,attack_positions,all_white)
            Rook44w_attack.all_white_class1("r4w",r44,black_check,attack,attack_positions,all_white)
            attack_positions=Rook44w_attack.attack_positions
            attack=Rook44w_attack.attack

            Rook51w_attack=attack_class_and_all_white("r5w",r51,black_check,attack,attack_positions,all_white)
            Rook51w_attack.attack_class1("r5w",r51,black_check,attack,attack_positions,all_white)
            Rook51w_attack.all_white_class1("r5w",r51,black_check,attack,attack_positions,all_white)
            attack_positions=Rook51w_attack.attack_positions
            attack=Rook51w_attack.attack
            
            Rook52w_attack=attack_class_and_all_white("r5w",r52,black_check,attack,attack_positions,all_white)
            Rook52w_attack.attack_class1("r5w",r52,black_check,attack,attack_positions,all_white)
            Rook52w_attack.all_white_class1("r5w",r52,black_check,attack,attack_positions,all_white)
            attack_positions=Rook52w_attack.attack_positions
            attack=Rook52w_attack.attack

            Rook53w_attack=attack_class_and_all_white("r5w",r53,black_check,attack,attack_positions,all_white)
            Rook53w_attack.attack_class1("r5w",r53,black_check,attack,attack_positions,all_white)
            Rook53w_attack.all_white_class1("r5w",r53,black_check,attack,attack_positions,all_white)
            attack_positions=Rook53w_attack.attack_positions
            attack=Rook53w_attack.attack
            
            Rook54w_attack=attack_class_and_all_white("r5w",r54,black_check,attack,attack_positions,all_white)
            Rook54w_attack.attack_class1("r5w",r54,black_check,attack,attack_positions,all_white)
            Rook54w_attack.all_white_class1("r5w",r54,black_check,attack,attack_positions,all_white)
            attack_positions=Rook54w_attack.attack_positions
            attack=Rook54w_attack.attack
                    
            Bishop11w_attack=attack_class_and_all_white("b1w",b11,black_check,attack,attack_positions,all_white)
            Bishop11w_attack.attack_class1("b1w",b11,black_check,attack,attack_positions,all_white)
            Bishop11w_attack.all_white_class1("b1w",b11,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop11w_attack.attack_positions
            attack=Bishop11w_attack.attack
            
            Bishop12w_attack=attack_class_and_all_white("b1w",b12,black_check,attack,attack_positions,all_white)
            Bishop12w_attack.attack_class1("b1w",b12,black_check,attack,attack_positions,all_white)
            Bishop12w_attack.all_white_class1("b1w",b12,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop12w_attack.attack_positions
            attack=Bishop12w_attack.attack

            Bishop13w_attack=attack_class_and_all_white("b1w",b13,black_check,attack,attack_positions,all_white)
            Bishop13w_attack.attack_class1("b1w",b13,black_check,attack,attack_positions,all_white)
            Bishop13w_attack.all_white_class1("b1w",b13,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop13w_attack.attack_positions
            attack=Bishop13w_attack.attack
            
            Bishop14w_attack=attack_class_and_all_white("b1w",b14,black_check,attack,attack_positions,all_white)
            Bishop14w_attack.attack_class1("b1w",b14,black_check,attack,attack_positions,all_white)
            Bishop14w_attack.all_white_class1("b1w",b14,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop14w_attack.attack_positions
            attack=Bishop14w_attack.attack
                    
            Bishop21w_attack=attack_class_and_all_white("b2w",b21,black_check,attack,attack_positions,all_white)
            Bishop21w_attack.attack_class1("b2w",b21,black_check,attack,attack_positions,all_white)
            Bishop21w_attack.all_white_class1("b2w",b21,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop21w_attack.attack_positions
            attack=Bishop21w_attack.attack
            
            Bishop22w_attack=attack_class_and_all_white("b2w",b22,black_check,attack,attack_positions,all_white)
            Bishop22w_attack.attack_class1("b2w",b22,black_check,attack,attack_positions,all_white)
            Bishop22w_attack.all_white_class1("b2w",b22,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop22w_attack.attack_positions
            attack=Bishop22w_attack.attack

            Bishop23w_attack=attack_class_and_all_white("b2w",b23,black_check,attack,attack_positions,all_white)
            Bishop23w_attack.attack_class1("b2w",b23,black_check,attack,attack_positions,all_white)
            Bishop23w_attack.all_white_class1("b2w",b23,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop23w_attack.attack_positions
            attack=Bishop23w_attack.attack
            
            Bishop24w_attack=attack_class_and_all_white("b2w",b24,black_check,attack,attack_positions,all_white)
            Bishop24w_attack.attack_class1("b2w",b24,black_check,attack,attack_positions,all_white)
            Bishop24w_attack.all_white_class1("b2w",b24,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop24w_attack.attack_positions
            attack=Bishop24w_attack.attack

            Bishop31w_attack=attack_class_and_all_white("b3w",b31,black_check,attack,attack_positions,all_white)
            Bishop31w_attack.attack_class1("b3w",b31,black_check,attack,attack_positions,all_white)
            Bishop31w_attack.all_white_class1("b3w",b31,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop31w_attack.attack_positions
            attack=Bishop31w_attack.attack
            
            Bishop32w_attack=attack_class_and_all_white("b3w",b32,black_check,attack,attack_positions,all_white)
            Bishop32w_attack.attack_class1("b3w",b32,black_check,attack,attack_positions,all_white)
            Bishop32w_attack.all_white_class1("b3w",b32,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop32w_attack.attack_positions
            attack=Bishop32w_attack.attack

            Bishop33w_attack=attack_class_and_all_white("b3w",b33,black_check,attack,attack_positions,all_white)
            Bishop33w_attack.attack_class1("b3w",b33,black_check,attack,attack_positions,all_white)
            Bishop33w_attack.all_white_class1("b3w",b33,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop33w_attack.attack_positions
            attack=Bishop33w_attack.attack
            
            Bishop34w_attack=attack_class_and_all_white("b3w",b34,black_check,attack,attack_positions,all_white)
            Bishop34w_attack.attack_class1("b3w",b34,black_check,attack,attack_positions,all_white)
            Bishop34w_attack.all_white_class1("b3w",b34,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop34w_attack.attack_positions
            attack=Bishop34w_attack.attack
            
            Bishop41w_attack=attack_class_and_all_white("b4w",b41,black_check,attack,attack_positions,all_white)
            Bishop41w_attack.attack_class1("b4w",b41,black_check,attack,attack_positions,all_white)
            Bishop41w_attack.all_white_class1("b4w",b41,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop41w_attack.attack_positions
            attack=Bishop41w_attack.attack
            
            Bishop42w_attack=attack_class_and_all_white("b4w",b42,black_check,attack,attack_positions,all_white)
            Bishop42w_attack.attack_class1("b4w",b42,black_check,attack,attack_positions,all_white)
            Bishop42w_attack.all_white_class1("b4w",b42,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop42w_attack.attack_positions
            attack=Bishop42w_attack.attack

            Bishop43w_attack=attack_class_and_all_white("b4w",b43,black_check,attack,attack_positions,all_white)
            Bishop43w_attack.attack_class1("b4w",b43,black_check,attack,attack_positions,all_white)
            Bishop43w_attack.all_white_class1("b4w",b43,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop43w_attack.attack_positions
            attack=Bishop43w_attack.attack
            
            Bishop44w_attack=attack_class_and_all_white("b4w",b44,black_check,attack,attack_positions,all_white)
            Bishop44w_attack.attack_class1("b4w",b44,black_check,attack,attack_positions,all_white)
            Bishop44w_attack.all_white_class1("b4w",b44,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop44w_attack.attack_positions
            attack=Bishop44w_attack.attack

            Bishop51w_attack=attack_class_and_all_white("b5w",b51,black_check,attack,attack_positions,all_white)
            Bishop51w_attack.attack_class1("b5w",b51,black_check,attack,attack_positions,all_white)
            Bishop51w_attack.all_white_class1("b5w",b51,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop51w_attack.attack_positions
            attack=Bishop51w_attack.attack
            
            Bishop52w_attack=attack_class_and_all_white("b5w",b52,black_check,attack,attack_positions,all_white)
            Bishop52w_attack.attack_class1("b5w",b52,black_check,attack,attack_positions,all_white)
            Bishop52w_attack.all_white_class1("b5w",b52,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop52w_attack.attack_positions
            attack=Bishop52w_attack.attack

            Bishop53w_attack=attack_class_and_all_white("b5w",b53,black_check,attack,attack_positions,all_white)
            Bishop53w_attack.attack_class1("b5w",b53,black_check,attack,attack_positions,all_white)
            Bishop53w_attack.all_white_class1("b5w",b53,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop53w_attack.attack_positions
            attack=Bishop53w_attack.attack
            
            Bishop54w_attack=attack_class_and_all_white("b5w",b54,black_check,attack,attack_positions,all_white)
            Bishop54w_attack.attack_class1("b5w",b54,black_check,attack,attack_positions,all_white)
            Bishop54w_attack.all_white_class1("b5w",b54,black_check,attack,attack_positions,all_white)
            attack_positions=Bishop54w_attack.attack_positions
            attack=Bishop54w_attack.attack

            Queen11w_attack=attack_class_and_all_white("q1w",q11,black_check,attack,attack_positions,all_white)
            Queen11w_attack.attack_class1("q1w",q11,black_check,attack,attack_positions,all_white)
            Queen11w_attack.all_white_class1("q1w",q11,black_check,attack,attack_positions,all_white)
            attack_positions=Queen11w_attack.attack_positions
            attack=Queen11w_attack.attack
            
            Queen12w_attack=attack_class_and_all_white("q1w",q12,black_check,attack,attack_positions,all_white)
            Queen12w_attack.attack_class1("q1w",q12,black_check,attack,attack_positions,all_white)
            Queen12w_attack.all_white_class1("q1w",q12,black_check,attack,attack_positions,all_white)
            attack_positions=Queen12w_attack.attack_positions
            attack=Queen12w_attack.attack

            Queen13w_attack=attack_class_and_all_white("q1w",q13,black_check,attack,attack_positions,all_white)
            Queen13w_attack.attack_class1("q1w",q13,black_check,attack,attack_positions,all_white)
            Queen13w_attack.all_white_class1("q1w",q13,black_check,attack,attack_positions,all_white)
            attack_positions=Queen13w_attack.attack_positions
            attack=Queen13w_attack.attack
            
            Queen14w_attack=attack_class_and_all_white("q1w",q14,black_check,attack,attack_positions,all_white)
            Queen14w_attack.attack_class1("q1w",q14,black_check,attack,attack_positions,all_white)
            Queen14w_attack.all_white_class1("q1w",q14,black_check,attack,attack_positions,all_white)
            attack_positions=Queen14w_attack.attack_positions
            attack=Queen14w_attack.attack

            Queen15w_attack=attack_class_and_all_white("q1w",q15,black_check,attack,attack_positions,all_white)
            Queen15w_attack.attack_class1("q1w",q15,black_check,attack,attack_positions,all_white)
            Queen15w_attack.all_white_class1("q1w",q15,black_check,attack,attack_positions,all_white)
            attack_positions=Queen15w_attack.attack_positions
            attack=Queen15w_attack.attack
            
            Queen16w_attack=attack_class_and_all_white("q1w",q16,black_check,attack,attack_positions,all_white)
            Queen16w_attack.attack_class1("q1w",q16,black_check,attack,attack_positions,all_white)
            Queen16w_attack.all_white_class1("q1w",q16,black_check,attack,attack_positions,all_white)
            attack_positions=Queen16w_attack.attack_positions
            attack=Queen16w_attack.attack
            
            Queen17w_attack=attack_class_and_all_white("q1w",q17,black_check,attack,attack_positions,all_white)
            Queen17w_attack.attack_class1("q1w",q17,black_check,attack,attack_positions,all_white)
            Queen17w_attack.all_white_class1("q1w",q17,black_check,attack,attack_positions,all_white)
            attack_positions=Queen17w_attack.attack_positions
            attack=Queen17w_attack.attack
            
            Queen18w_attack=attack_class_and_all_white("q1w",q18,black_check,attack,attack_positions,all_white)
            Queen18w_attack.attack_class1("q1w",q18,black_check,attack,attack_positions,all_white)
            Queen18w_attack.all_white_class1("q1w",q18,black_check,attack,attack_positions,all_white)
            attack_positions=Queen18w_attack.attack_positions
            attack=Queen18w_attack.attack
            
            Queen21w_attack=attack_class_and_all_white("q2w",q21,black_check,attack,attack_positions,all_white)
            Queen21w_attack.attack_class1("q2w",q21,black_check,attack,attack_positions,all_white)
            Queen21w_attack.all_white_class1("q2w",q21,black_check,attack,attack_positions,all_white)
            attack_positions=Queen21w_attack.attack_positions
            attack=Queen21w_attack.attack
            
            Queen22w_attack=attack_class_and_all_white("q2w",q22,black_check,attack,attack_positions,all_white)
            Queen22w_attack.attack_class1("q2w",q22,black_check,attack,attack_positions,all_white)
            Queen22w_attack.all_white_class1("q2w",q22,black_check,attack,attack_positions,all_white)
            attack_positions=Queen22w_attack.attack_positions
            attack=Queen22w_attack.attack

            Queen23w_attack=attack_class_and_all_white("q2w",q23,black_check,attack,attack_positions,all_white)
            Queen23w_attack.attack_class1("q2w",q23,black_check,attack,attack_positions,all_white)
            Queen23w_attack.all_white_class1("q2w",q23,black_check,attack,attack_positions,all_white)
            attack_positions=Queen23w_attack.attack_positions
            attack=Queen23w_attack.attack
            
            Queen24w_attack=attack_class_and_all_white("q2w",q24,black_check,attack,attack_positions,all_white)
            Queen24w_attack.attack_class1("q2w",q24,black_check,attack,attack_positions,all_white)
            Queen24w_attack.all_white_class1("q2w",q24,black_check,attack,attack_positions,all_white)
            attack_positions=Queen24w_attack.attack_positions
            attack=Queen24w_attack.attack

            Queen25w_attack=attack_class_and_all_white("q2w",q25,black_check,attack,attack_positions,all_white)
            Queen25w_attack.attack_class1("q2w",q25,black_check,attack,attack_positions,all_white)
            Queen25w_attack.all_white_class1("q2w",q25,black_check,attack,attack_positions,all_white)
            attack_positions=Queen25w_attack.attack_positions
            attack=Queen25w_attack.attack
            
            Queen26w_attack=attack_class_and_all_white("q2w",q26,black_check,attack,attack_positions,all_white)
            Queen26w_attack.attack_class1("q2w",q26,black_check,attack,attack_positions,all_white)
            Queen26w_attack.all_white_class1("q2w",q26,black_check,attack,attack_positions,all_white)
            attack_positions=Queen26w_attack.attack_positions
            attack=Queen26w_attack.attack
            
            Queen27w_attack=attack_class_and_all_white("q2w",q27,black_check,attack,attack_positions,all_white)
            Queen27w_attack.attack_class1("q2w",q27,black_check,attack,attack_positions,all_white)
            Queen27w_attack.all_white_class1("q2w",q27,black_check,attack,attack_positions,all_white)
            attack_positions=Queen27w_attack.attack_positions
            attack=Queen27w_attack.attack
            
            Queen28w_attack=attack_class_and_all_white("q2w",q28,black_check,attack,attack_positions,all_white)
            Queen28w_attack.attack_class1("q2w",q28,black_check,attack,attack_positions,all_white)
            Queen28w_attack.all_white_class1("q2w",q28,black_check,attack,attack_positions,all_white)
            attack_positions=Queen28w_attack.attack_positions
            attack=Queen28w_attack.attack
            
            Queen31w_attack=attack_class_and_all_white("q3w",q31,black_check,attack,attack_positions,all_white)
            Queen31w_attack.attack_class1("q3w",q31,black_check,attack,attack_positions,all_white)
            Queen31w_attack.all_white_class1("q3w",q31,black_check,attack,attack_positions,all_white)
            attack_positions=Queen31w_attack.attack_positions
            attack=Queen31w_attack.attack
            
            Queen32w_attack=attack_class_and_all_white("q3w",q32,black_check,attack,attack_positions,all_white)
            Queen32w_attack.attack_class1("q3w",q32,black_check,attack,attack_positions,all_white)
            Queen32w_attack.all_white_class1("q3w",q32,black_check,attack,attack_positions,all_white)
            attack_positions=Queen32w_attack.attack_positions
            attack=Queen32w_attack.attack

            Queen33w_attack=attack_class_and_all_white("q3w",q33,black_check,attack,attack_positions,all_white)
            Queen33w_attack.attack_class1("q3w",q33,black_check,attack,attack_positions,all_white)
            Queen33w_attack.all_white_class1("q3w",q33,black_check,attack,attack_positions,all_white)
            attack_positions=Queen33w_attack.attack_positions
            attack=Queen33w_attack.attack
            
            Queen34w_attack=attack_class_and_all_white("q3w",q34,black_check,attack,attack_positions,all_white)
            Queen34w_attack.attack_class1("q3w",q34,black_check,attack,attack_positions,all_white)
            Queen34w_attack.all_white_class1("q3w",q34,black_check,attack,attack_positions,all_white)
            attack_positions=Queen34w_attack.attack_positions
            attack=Queen34w_attack.attack

            Queen35w_attack=attack_class_and_all_white("q3w",q35,black_check,attack,attack_positions,all_white)
            Queen35w_attack.attack_class1("q3w",q35,black_check,attack,attack_positions,all_white)
            Queen35w_attack.all_white_class1("q3w",q35,black_check,attack,attack_positions,all_white)
            attack_positions=Queen35w_attack.attack_positions
            attack=Queen35w_attack.attack
            
            Queen36w_attack=attack_class_and_all_white("q3w",q36,black_check,attack,attack_positions,all_white)
            Queen36w_attack.attack_class1("q3w",q36,black_check,attack,attack_positions,all_white)
            Queen36w_attack.all_white_class1("q3w",q36,black_check,attack,attack_positions,all_white)
            attack_positions=Queen36w_attack.attack_positions
            attack=Queen36w_attack.attack
            
            Queen37w_attack=attack_class_and_all_white("q3w",q37,black_check,attack,attack_positions,all_white)
            Queen37w_attack.attack_class1("q3w",q37,black_check,attack,attack_positions,all_white)
            Queen37w_attack.all_white_class1("q3w",q37,black_check,attack,attack_positions,all_white)
            attack_positions=Queen37w_attack.attack_positions
            attack=Queen37w_attack.attack
            
            Queen38w_attack=attack_class_and_all_white("q3w",q38,black_check,attack,attack_positions,all_white)
            Queen38w_attack.attack_class1("q3w",q38,black_check,attack,attack_positions,all_white)
            Queen38w_attack.all_white_class1("q3w",q38,black_check,attack,attack_positions,all_white)
            attack_positions=Queen38w_attack.attack_positions
            attack=Queen38w_attack.attack
            
            Queen41w_attack=attack_class_and_all_white("q3w",q41,black_check,attack,attack_positions,all_white)
            Queen41w_attack.attack_class1("q3w",q41,black_check,attack,attack_positions,all_white)
            Queen41w_attack.all_white_class1("q3w",q41,black_check,attack,attack_positions,all_white)
            attack_positions=Queen41w_attack.attack_positions
            attack=Queen41w_attack.attack
            
            Queen42w_attack=attack_class_and_all_white("q3w",q42,black_check,attack,attack_positions,all_white)
            Queen42w_attack.attack_class1("q3w",q42,black_check,attack,attack_positions,all_white)
            Queen42w_attack.all_white_class1("q3w",q42,black_check,attack,attack_positions,all_white)
            attack_positions=Queen42w_attack.attack_positions
            attack=Queen42w_attack.attack

            Queen43w_attack=attack_class_and_all_white("q3w",q43,black_check,attack,attack_positions,all_white)
            Queen43w_attack.attack_class1("q3w",q43,black_check,attack,attack_positions,all_white)
            Queen43w_attack.all_white_class1("q3w",q43,black_check,attack,attack_positions,all_white)
            attack_positions=Queen43w_attack.attack_positions
            attack=Queen43w_attack.attack
            
            Queen44w_attack=attack_class_and_all_white("q3w",q44,black_check,attack,attack_positions,all_white)
            Queen44w_attack.attack_class1("q3w",q44,black_check,attack,attack_positions,all_white)
            Queen44w_attack.all_white_class1("q3w",q44,black_check,attack,attack_positions,all_white)
            attack_positions=Queen44w_attack.attack_positions
            attack=Queen44w_attack.attack

            Queen45w_attack=attack_class_and_all_white("q3w",q45,black_check,attack,attack_positions,all_white)
            Queen45w_attack.attack_class1("q3w",q45,black_check,attack,attack_positions,all_white)
            Queen45w_attack.all_white_class1("q3w",q45,black_check,attack,attack_positions,all_white)
            attack_positions=Queen45w_attack.attack_positions
            attack=Queen45w_attack.attack
            
            Queen46w_attack=attack_class_and_all_white("q3w",q46,black_check,attack,attack_positions,all_white)
            Queen46w_attack.attack_class1("q3w",q46,black_check,attack,attack_positions,all_white)
            Queen46w_attack.all_white_class1("q3w",q46,black_check,attack,attack_positions,all_white)
            attack_positions=Queen46w_attack.attack_positions
            attack=Queen46w_attack.attack
            
            Queen47w_attack=attack_class_and_all_white("q3w",q47,black_check,attack,attack_positions,all_white)
            Queen47w_attack.attack_class1("q3w",q47,black_check,attack,attack_positions,all_white)
            Queen47w_attack.all_white_class1("q3w",q47,black_check,attack,attack_positions,all_white)
            attack_positions=Queen47w_attack.attack_positions
            attack=Queen47w_attack.attack
            
            Queen48w_attack=attack_class_and_all_white("q3w",q48,black_check,attack,attack_positions,all_white)
            Queen48w_attack.attack_class1("q3w",q48,black_check,attack,attack_positions,all_white)
            Queen48w_attack.all_white_class1("q3w",q48,black_check,attack,attack_positions,all_white)
            attack_positions=Queen48w_attack.attack_positions
            attack=Queen48w_attack.attack
            
            for ju in range (0,len(kn1)):
                if xposition==kn1[ju][0] and yposition==kn1[ju][1]:
                    attack.append(["kn1w"])

            for ju in range (0,len(kn2)):
                if xposition==kn2[ju][0] and yposition==kn2[ju][1]:
                    attack.append(["kn2w"])

            for ju in range (0,len(kn3)):
                if xposition==kn3[ju][0] and yposition==kn3[ju][1]:
                    attack.append(["kn3w"])

            for ju in range (0,len(kn4)):
                if xposition==kn4[ju][0] and yposition==kn4[ju][1]:
                    attack.append(["kn4w"])

            for ju in range (0,len(kn5)):
                if xposition==kn5[ju][0] and yposition==kn5[ju][1]:
                    attack.append(["kn5w"])
                    
            for ju in range (0,len(p1)):
                if xposition==p1[ju][0] and yposition==p1[ju][1]:
                    attack.append(["p1w"])
                    
            for ju in range (0,len(p2)):
                if xposition==p2[ju][0] and yposition==p2[ju][1]:
                    attack.append(["p2w"])
                    
            for ju in range (0,len(p3)):
                if xposition==p3[ju][0] and yposition==p3[ju][1]:
                    attack.append(["p3w"])
                    
            for ju in range (0,len(p4)):
                if xposition==p4[ju][0] and yposition==p4[ju][1]:
                    attack.append(["p4w"])
                    
            for ju in range (0,len(p5)):
                if xposition==p5[ju][0] and yposition==p5[ju][1]:
                    attack.append(["p5w"])
                    
            for ju in range (0,len(p6)):
                if xposition==p6[ju][0] and yposition==p6[ju][1]:
                    attack.append(["p6w"])
                    
            for ju in range (0,len(p7)):
                if xposition==p7[ju][0] and yposition==p7[ju][1]:
                    attack.append(["p7w"])
                    
            for ju in range (0,len(p8)):               
                if xposition==p8[ju][0] and yposition==p8[ju][1]:
                    attack.append(["p8w"])
            if attack!=[]:
                black_check=True
                    
            for i in range (0,len(kn1)):
                if kn1!=[]:
                    all_white.append(kn1[i])
                    
            for i in range (0,len(kn2)):
                if kn2!=[]:
                    all_white.append(kn2[i])

            for i in range (0,len(kn3)):
                if kn3!=[]:
                    all_white.append(kn3[i])

            for i in range (0,len(kn4)):
                if kn4!=[]:
                    all_white.append(kn4[i])

            for i in range (0,len(kn5)):
                if kn5!=[]:
                    all_white.append(kn5[i])
                    
            for i in range (0,len(p1)):
                if p1!=[]:
                    all_white.append(p1[i])
            for i in range (0,len(p2)):
                if p2!=[]:
                    all_white.append(p2[i])
            for i in range (0,len(p3)):
                if p3!=[]:
                    all_white.append(p3[i])
            for i in range (0,len(p4)):
                if p4!=[]:
                    all_white.append(p4[i])
            for i in range (0,len(p5)):
                if p5!=[]:
                    all_white.append(p5[i])
            for i in range (0,len(p6)):
                if p6!=[]:
                    all_white.append(p6[i])
            for i in range (0,len(p7)):
                if p7!=[]:
                    all_white.append(p7[i])
            for i in range (0,len(p8)):
                if p8!=[]:
                    all_white.append(p8[i])
            for i in range (0,len(k1w)):
                if k1w!=[]:
                    all_white.append(k1w[i])                
            hb=1
            
        if hw==0:
            two_protectors=False
            white_protector=[]
            pos_spaces=[]
            all_black=[]
            Bishop1b2=bishop1(b11b,b12b,b13b,b14b,white_protector,"b1b","k1w","w","b")
            Bishop1b2.check(b11b,b12b,b13b,b14b,white_protector,"b1b","k1w","w","b")
                
            Bishop2b2=bishop1(b21b,b22b,b23b,b24b,white_protector,"b2b","k1w","w","b")
            Bishop2b2.check(b21b,b22b,b23b,b24b,white_protector,"b2b","k1w","w","b")

            Bishop3b3=bishop1(b31b,b32b,b33b,b34b,white_protector,"b3b","k1w","w","b")
            Bishop3b3.check(b31b,b32b,b33b,b34b,white_protector,"b3b","k1w","w","b")

            Bishop4b4=bishop1(b41b,b42b,b43b,b44b,white_protector,"b4b","k1w","w","b")
            Bishop4b4.check(b41b,b42b,b43b,b44b,white_protector,"b4b","k1w","w","b")

            Bishop5b5=bishop1(b51b,b52b,b53b,b54b,white_protector,"b5b","k1w","w","b")
            Bishop5b5.check(b51b,b52b,b53b,b54b,white_protector,"b5b","k1w","w","b")

            Queen1b2=queen1(q11b,q12b,q13b,q14b,q15b,q16b,q17b,q18b,white_protector,"q1b","k1w","w","b")
            Queen1b2.check(q11b,q12b,q13b,q14b,q15b,q16b,q17b,q18b,white_protector,"q1b","k1w","w","b")

            Queen2b2=queen1(q21b,q22b,q23b,q24b,q25b,q26b,q27b,q28b,white_protector,"q2b","k1w","w","b")
            Queen2b2.check(q21b,q22b,q23b,q24b,q25b,q26b,q27b,q28b,white_protector,"q2b","k1w","w","b")

            Queen4b4=queen1(q41b,q42b,q43b,q44b,q45b,q46b,q47b,q48b,white_protector,"q4b","k1w","w","b")
            Queen4b4.check(q41b,q42b,q43b,q44b,q45b,q46b,q47b,q48b,white_protector,"q4b","k1w","w","b")

            Queen3b3=queen1(q31b,q32b,q33b,q34b,q35b,q36b,q37b,q38b,white_protector,"q3b","k1w","w","b")
            Queen3b3.check(q31b,q32b,q33b,q34b,q35b,q36b,q37b,q38b,white_protector,"q3b","k1w","w","b")

            knight1b2=knight1(kn1b,white_protector,"kn1b","k1w","w","b")
            knight1b2.check(kn1b,white_protector,"kn1b","k1w","w","b")            

            knight2b2=knight1(kn1b,white_protector,"kn2b","k1w","w","b")
            knight2b2.check(kn1b,white_protector,"kn2b","k1w","w","b")

            knight3b3=knight1(kn3b,white_protector,"kn3b","k1w","w","b")
            knight3b3.check(kn3b,white_protector,"kn3b","k1w","w","b")

            knight4b4=knight1(kn4b,white_protector,"kn4b","k1w","w","b")
            knight4b4.check(kn4b,white_protector,"kn4b","k1w","w","b")

            knight5b2=knight1(kn5b,white_protector,"kn5b","k1w","w","b")
            knight5b2.check(kn5b,white_protector,"kn5b","k1w","w","b") 

            Rook1b2=rook1(r11b,r12b,r13b,r14b,white_protector,"r1b","k1w","w","b")
            Rook1b2.check(r11b,r12b,r13b,r14b,white_protector,"r1b","k1w","w","b")

            Rook2b2=rook1(r21b,r22b,r23b,r24b,white_protector,"r2b","k1w","w","b")
            Rook2b2.check(r21b,r22b,r23b,r24b,white_protector,"r2b","k1w","w","b")

            Rook3b2=rook1(r31b,r32b,r33b,r34b,white_protector,"r3b","k1w","w","b")
            Rook3b2.check(r31b,r32b,r33b,r34b,white_protector,"r3b","k1w","w","b")

            Rook4b2=rook1(r41b,r42b,r43b,r44b,white_protector,"r4b","k1w","w","b")
            Rook4b2.check(r41b,r42b,r43b,r44b,white_protector,"r4b","k1w","w","b")

            Rook5b2=rook1(r51b,r52b,r53b,r54b,white_protector,"r5b","k1w","w","b")
            Rook5b2.check(r51b,r52b,r53b,r54b,white_protector,"r5b","k1w","w","b")

            King1b2=king1(k1b,"k1b","w","b")
            King1b2.check(k1b,"k1b","w","b")

            Pawn1b2=pawn1b(p1b,"p1b","w","b")
            Pawn1b2.check(p1b,"p1b","w","b")

            Pawn2b2=pawn1b(p2b,"p2b","w","b")
            Pawn2b2.check(p2b,"p2b","w","b")

            Pawn3b2=pawn1b(p3b,"p3b","w","b")
            Pawn3b2.check(p3b,"p3b","w","b")

            Pawn4b2=pawn1b(p4b,"p4b","w","b")
            Pawn4b2.check(p4b,"p4b","w","b")

            Pawn5b2=pawn1b(p5b,"p5b","w","b")
            Pawn5b2.check(p5b,"p5b","w","b")

            Pawn6b2=pawn1b(p6b,"p6b","w","b")
            Pawn6b2.check(p6b,"p6b","w","b")

            Pawn7b2=pawn1b(p7b,"p7b","w","b")
            Pawn7b2.check(p7b,"p7b","w","b")

            Pawn8b2=pawn1b(p8b,"p8b","w","b")
            Pawn8b2.check(p8b,"p8b","w","b")

            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
            xposition=60*xposition
            yposition=60*yposition
            attack=[]
            attack_positions=[]
            
            Rook11b_attack=attack_class_and_all_black("r1b",r11b,white_check,attack,attack_positions,all_black)
            Rook11b_attack.attack_class1("r1b",r11b,white_check,attack,attack_positions,all_black)
            Rook11b_attack.all_black_class1("r1b",r11b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook11b_attack.attack_positions
            attack=Rook11b_attack.attack
            
            Rook12b_attack=attack_class_and_all_black("r1b",r12b,white_check,attack,attack_positions,all_black)
            Rook12b_attack.attack_class1("r1b",r12b,white_check,attack,attack_positions,all_black)
            Rook12b_attack.all_black_class1("r1b",r12b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook12b_attack.attack_positions
            attack=Rook12b_attack.attack

            Rook13b_attack=attack_class_and_all_black("r1b",r13b,white_check,attack,attack_positions,all_black)
            Rook13b_attack.attack_class1("r1b",r13b,white_check,attack,attack_positions,all_black)
            Rook13b_attack.all_black_class1("r1b",r13b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook13b_attack.attack_positions
            attack=Rook13b_attack.attack
            
            Rook14b_attack=attack_class_and_all_black("r1b",r14b,white_check,attack,attack_positions,all_black)
            Rook14b_attack.attack_class1("r1b",r14b,white_check,attack,attack_positions,all_black)
            Rook14b_attack.all_black_class1("r1b",r14b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook14b_attack.attack_positions
            attack=Rook14b_attack.attack
                    
            Rook21b_attack=attack_class_and_all_black("r1b",r21b,white_check,attack,attack_positions,all_black)
            Rook21b_attack.attack_class1("r1b",r21b,white_check,attack,attack_positions,all_black)
            Rook21b_attack.all_black_class1("r1b",r21b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook21b_attack.attack_positions
            attack=Rook21b_attack.attack
            
            Rook22b_attack=attack_class_and_all_black("r1b",r22b,white_check,attack,attack_positions,all_black)
            Rook22b_attack.attack_class1("r1b",r22b,white_check,attack,attack_positions,all_black)
            Rook22b_attack.all_black_class1("r1b",r22b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook22b_attack.attack_positions
            attack=Rook22b_attack.attack

            Rook23b_attack=attack_class_and_all_black("r1b",r23b,white_check,attack,attack_positions,all_black)
            Rook23b_attack.attack_class1("r1b",r23b,white_check,attack,attack_positions,all_black)
            Rook23b_attack.all_black_class1("r1b",r23b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook23b_attack.attack_positions
            attack=Rook23b_attack.attack
            
            Rook24b_attack=attack_class_and_all_black("r1b",r24b,white_check,attack,attack_positions,all_black)
            Rook24b_attack.attack_class1("r1b",r24b,white_check,attack,attack_positions,all_black)
            Rook24b_attack.all_black_class1("r1b",r24b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook24b_attack.attack_positions
            attack=Rook24b_attack.attack

            Rook31b_attack=attack_class_and_all_black("r1b",r31b,white_check,attack,attack_positions,all_black)
            Rook31b_attack.attack_class1("r1b",r31b,white_check,attack,attack_positions,all_black)
            Rook31b_attack.all_black_class1("r1b",r31b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook31b_attack.attack_positions
            attack=Rook31b_attack.attack
            
            Rook32b_attack=attack_class_and_all_black("r1b",r32b,white_check,attack,attack_positions,all_black)
            Rook32b_attack.attack_class1("r1b",r32b,white_check,attack,attack_positions,all_black)
            Rook32b_attack.all_black_class1("r1b",r32b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook32b_attack.attack_positions
            attack=Rook32b_attack.attack

            Rook33b_attack=attack_class_and_all_black("r1b",r33b,white_check,attack,attack_positions,all_black)
            Rook33b_attack.attack_class1("r1b",r33b,white_check,attack,attack_positions,all_black)
            Rook33b_attack.all_black_class1("r1b",r33b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook33b_attack.attack_positions
            attack=Rook33b_attack.attack
            
            Rook34b_attack=attack_class_and_all_black("r1b",r34b,white_check,attack,attack_positions,all_black)
            Rook34b_attack.attack_class1("r1b",r34b,white_check,attack,attack_positions,all_black)
            Rook34b_attack.all_black_class1("r1b",r34b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook34b_attack.attack_positions
            attack=Rook34b_attack.attack
            
            Rook41b_attack=attack_class_and_all_black("r1b",r41b,white_check,attack,attack_positions,all_black)
            Rook41b_attack.attack_class1("r1b",r41b,white_check,attack,attack_positions,all_black)
            Rook41b_attack.all_black_class1("r1b",r41b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook41b_attack.attack_positions
            attack=Rook41b_attack.attack
            
            Rook42b_attack=attack_class_and_all_black("r1b",r42b,white_check,attack,attack_positions,all_black)
            Rook42b_attack.attack_class1("r1b",r42b,white_check,attack,attack_positions,all_black)
            Rook42b_attack.all_black_class1("r1b",r42b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook42b_attack.attack_positions
            attack=Rook42b_attack.attack

            Rook43b_attack=attack_class_and_all_black("r1b",r43b,white_check,attack,attack_positions,all_black)
            Rook43b_attack.attack_class1("r1b",r43b,white_check,attack,attack_positions,all_black)
            Rook43b_attack.all_black_class1("r1b",r43b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook43b_attack.attack_positions
            attack=Rook43b_attack.attack
            
            Rook44b_attack=attack_class_and_all_black("r1b",r44b,white_check,attack,attack_positions,all_black)
            Rook44b_attack.attack_class1("r1b",r44b,white_check,attack,attack_positions,all_black)
            Rook44b_attack.all_black_class1("r1b",r44b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook44b_attack.attack_positions
            attack=Rook44b_attack.attack

            Rook51b_attack=attack_class_and_all_black("r1b",r51b,white_check,attack,attack_positions,all_black)
            Rook51b_attack.attack_class1("r1b",r51b,white_check,attack,attack_positions,all_black)
            Rook51b_attack.all_black_class1("r1b",r51b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook51b_attack.attack_positions
            attack=Rook51b_attack.attack
            
            Rook52b_attack=attack_class_and_all_black("r1b",r52b,white_check,attack,attack_positions,all_black)
            Rook52b_attack.attack_class1("r1b",r52b,white_check,attack,attack_positions,all_black)
            Rook52b_attack.all_black_class1("r1b",r52b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook52b_attack.attack_positions
            attack=Rook52b_attack.attack

            Rook53b_attack=attack_class_and_all_black("r1b",r53b,white_check,attack,attack_positions,all_black)
            Rook53b_attack.attack_class1("r1b",r53b,white_check,attack,attack_positions,all_black)
            Rook53b_attack.all_black_class1("r1b",r53b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook53b_attack.attack_positions
            attack=Rook53b_attack.attack
            
            Rook54b_attack=attack_class_and_all_black("r1b",r54b,white_check,attack,attack_positions,all_black)
            Rook54b_attack.attack_class1("r1b",r54b,white_check,attack,attack_positions,all_black)
            Rook54b_attack.all_black_class1("r1b",r54b,white_check,attack,attack_positions,all_black)
            attack_positions=Rook54b_attack.attack_positions
            attack=Rook54b_attack.attack
                    
            Bishop11b_attack=attack_class_and_all_black("b1b",b11b,white_check,attack,attack_positions,all_black)
            Bishop11b_attack.attack_class1("b1b",b11b,white_check,attack,attack_positions,all_black)
            Bishop11b_attack.all_black_class1("b1b",b11b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop11b_attack.attack_positions
            attack=Bishop11b_attack.attack
            
            Bishop12b_attack=attack_class_and_all_black("b1b",b12b,white_check,attack,attack_positions,all_black)
            Bishop12b_attack.attack_class1("b1b",b12b,white_check,attack,attack_positions,all_black)
            Bishop12b_attack.all_black_class1("b1b",b12b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop12b_attack.attack_positions
            attack=Bishop12b_attack.attack

            Bishop13b_attack=attack_class_and_all_black("b1b",b13b,white_check,attack,attack_positions,all_black)
            Bishop13b_attack.attack_class1("b1b",b13b,white_check,attack,attack_positions,all_black)
            Bishop13b_attack.all_black_class1("b1b",b13b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop13b_attack.attack_positions
            attack=Bishop13b_attack.attack
            
            Bishop14b_attack=attack_class_and_all_black("b1b",b14b,white_check,attack,attack_positions,all_black)
            Bishop14b_attack.attack_class1("b1b",b14b,white_check,attack,attack_positions,all_black)
            Bishop14b_attack.all_black_class1("b1b",b14b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop14b_attack.attack_positions
            attack=Bishop14b_attack.attack
                    
            Bishop21b_attack=attack_class_and_all_black("b1b",b21b,white_check,attack,attack_positions,all_black)
            Bishop21b_attack.attack_class1("b1b",b21b,white_check,attack,attack_positions,all_black)
            Bishop21b_attack.all_black_class1("b1b",b21b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop21b_attack.attack_positions
            attack=Bishop21b_attack.attack
            
            Bishop22b_attack=attack_class_and_all_black("b1b",b22b,white_check,attack,attack_positions,all_black)
            Bishop22b_attack.attack_class1("b1b",b22b,white_check,attack,attack_positions,all_black)
            Bishop22b_attack.all_black_class1("b1b",b22b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop22b_attack.attack_positions
            attack=Bishop22b_attack.attack

            Bishop23b_attack=attack_class_and_all_black("b1b",b23b,white_check,attack,attack_positions,all_black)
            Bishop23b_attack.attack_class1("b1b",b23b,white_check,attack,attack_positions,all_black)
            Bishop23b_attack.all_black_class1("b1b",b23b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop23b_attack.attack_positions
            attack=Bishop23b_attack.attack
            
            Bishop24b_attack=attack_class_and_all_black("b1b",b24b,white_check,attack,attack_positions,all_black)
            Bishop24b_attack.attack_class1("b1b",b24b,white_check,attack,attack_positions,all_black)
            Bishop24b_attack.all_black_class1("b1b",b24b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop24b_attack.attack_positions
            attack=Bishop24b_attack.attack

            Bishop31b_attack=attack_class_and_all_black("b1b",b31b,white_check,attack,attack_positions,all_black)
            Bishop31b_attack.attack_class1("b1b",b31b,white_check,attack,attack_positions,all_black)
            Bishop31b_attack.all_black_class1("b1b",b31b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop31b_attack.attack_positions
            attack=Bishop31b_attack.attack
            
            Bishop32b_attack=attack_class_and_all_black("b1b",b32b,white_check,attack,attack_positions,all_black)
            Bishop32b_attack.attack_class1("b1b",b32b,white_check,attack,attack_positions,all_black)
            Bishop32b_attack.all_black_class1("b1b",b32b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop32b_attack.attack_positions
            attack=Bishop32b_attack.attack

            Bishop33b_attack=attack_class_and_all_black("b1b",b33b,white_check,attack,attack_positions,all_black)
            Bishop33b_attack.attack_class1("b1b",b33b,white_check,attack,attack_positions,all_black)
            Bishop33b_attack.all_black_class1("b1b",b33b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop33b_attack.attack_positions
            attack=Bishop33b_attack.attack
            
            Bishop34b_attack=attack_class_and_all_black("b1b",b34b,white_check,attack,attack_positions,all_black)
            Bishop34b_attack.attack_class1("b1b",b34b,white_check,attack,attack_positions,all_black)
            Bishop34b_attack.all_black_class1("b1b",b34b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop34b_attack.attack_positions
            attack=Bishop34b_attack.attack
            
            Bishop41b_attack=attack_class_and_all_black("b1b",b41b,white_check,attack,attack_positions,all_black)
            Bishop41b_attack.attack_class1("b1b",b41b,white_check,attack,attack_positions,all_black)
            Bishop41b_attack.all_black_class1("b1b",b41b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop41b_attack.attack_positions
            attack=Bishop41b_attack.attack
            
            Bishop42b_attack=attack_class_and_all_black("b1b",b42b,white_check,attack,attack_positions,all_black)
            Bishop42b_attack.attack_class1("b1b",b42b,white_check,attack,attack_positions,all_black)
            Bishop42b_attack.all_black_class1("b1b",b42b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop42b_attack.attack_positions
            attack=Bishop42b_attack.attack

            Bishop43b_attack=attack_class_and_all_black("b1b",b43b,white_check,attack,attack_positions,all_black)
            Bishop43b_attack.attack_class1("b1b",b43b,white_check,attack,attack_positions,all_black)
            Bishop43b_attack.all_black_class1("b1b",b43b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop43b_attack.attack_positions
            attack=Bishop43b_attack.attack
            
            Bishop44b_attack=attack_class_and_all_black("b1b",b44b,white_check,attack,attack_positions,all_black)
            Bishop44b_attack.attack_class1("b1b",b44b,white_check,attack,attack_positions,all_black)
            Bishop44b_attack.all_black_class1("b1b",b44b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop44b_attack.attack_positions
            attack=Bishop44b_attack.attack

            Bishop51b_attack=attack_class_and_all_black("b1b",b51b,white_check,attack,attack_positions,all_black)
            Bishop51b_attack.attack_class1("b1b",b51b,white_check,attack,attack_positions,all_black)
            Bishop51b_attack.all_black_class1("b1b",b51b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop51b_attack.attack_positions
            attack=Bishop51b_attack.attack
            
            Bishop52b_attack=attack_class_and_all_black("b1b",b52b,white_check,attack,attack_positions,all_black)
            Bishop52b_attack.attack_class1("b1b",b52b,white_check,attack,attack_positions,all_black)
            Bishop52b_attack.all_black_class1("b1b",b52b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop52b_attack.attack_positions
            attack=Bishop52b_attack.attack

            Bishop53b_attack=attack_class_and_all_black("b1b",b53b,white_check,attack,attack_positions,all_black)
            Bishop53b_attack.attack_class1("b1b",b53b,white_check,attack,attack_positions,all_black)
            Bishop53b_attack.all_black_class1("b1b",b53b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop53b_attack.attack_positions
            attack=Bishop53b_attack.attack
            
            Bishop54b_attack=attack_class_and_all_black("b1b",b54b,white_check,attack,attack_positions,all_black)
            Bishop54b_attack.attack_class1("b1b",b54b,white_check,attack,attack_positions,all_black)
            Bishop54b_attack.all_black_class1("b1b",b54b,white_check,attack,attack_positions,all_black)
            attack_positions=Bishop54b_attack.attack_positions
            attack=Bishop54b_attack.attack

            Queen11b_attack=attack_class_and_all_black("q1b",q11b,white_check,attack,attack_positions,all_black)
            Queen11b_attack.attack_class1("q1b",q11b,white_check,attack,attack_positions,all_black)
            Queen11b_attack.all_black_class1("q1b",q11b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen11b_attack.attack_positions
            attack=Queen11b_attack.attack
            
            Queen12b_attack=attack_class_and_all_black("q1b",q12b,white_check,attack,attack_positions,all_black)
            Queen12b_attack.attack_class1("q1b",q12b,white_check,attack,attack_positions,all_black)
            Queen12b_attack.all_black_class1("q1b",q12b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen12b_attack.attack_positions
            attack=Queen12b_attack.attack

            Queen13b_attack=attack_class_and_all_black("q1b",q13b,white_check,attack,attack_positions,all_black)
            Queen13b_attack.attack_class1("q1b",q13b,white_check,attack,attack_positions,all_black)
            Queen13b_attack.all_black_class1("q1b",q13b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen13b_attack.attack_positions
            attack=Queen13b_attack.attack
            
            Queen14b_attack=attack_class_and_all_black("q1b",q14b,white_check,attack,attack_positions,all_black)
            Queen14b_attack.attack_class1("q1b",q14b,white_check,attack,attack_positions,all_black)
            Queen14b_attack.all_black_class1("q1b",q14b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen14b_attack.attack_positions
            attack=Queen14b_attack.attack

            Queen15b_attack=attack_class_and_all_black("q1b",q15b,white_check,attack,attack_positions,all_black)
            Queen15b_attack.attack_class1("q1b",q15b,white_check,attack,attack_positions,all_black)
            Queen15b_attack.all_black_class1("q1b",q15b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen15b_attack.attack_positions
            attack=Queen15b_attack.attack
            
            Queen16b_attack=attack_class_and_all_black("q1b",q16b,white_check,attack,attack_positions,all_black)
            Queen16b_attack.attack_class1("q1b",q16b,white_check,attack,attack_positions,all_black)
            Queen16b_attack.all_black_class1("q1b",q16b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen16b_attack.attack_positions
            attack=Queen16b_attack.attack
            
            Queen17b_attack=attack_class_and_all_black("q1b",q17b,white_check,attack,attack_positions,all_black)
            Queen17b_attack.attack_class1("q1b",q17b,white_check,attack,attack_positions,all_black)
            Queen17b_attack.all_black_class1("q1b",q17b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen17b_attack.attack_positions
            attack=Queen17b_attack.attack
            
            Queen18b_attack=attack_class_and_all_black("q1b",q18b,white_check,attack,attack_positions,all_black)
            Queen18b_attack.attack_class1("q1b",q18b,white_check,attack,attack_positions,all_black)
            Queen18b_attack.all_black_class1("q1b",q18b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen18b_attack.attack_positions
            attack=Queen18b_attack.attack
            
            Queen21b_attack=attack_class_and_all_black("q1b",q21b,white_check,attack,attack_positions,all_black)
            Queen21b_attack.attack_class1("q1b",q21b,white_check,attack,attack_positions,all_black)
            Queen21b_attack.all_black_class1("q1b",q21b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen21b_attack.attack_positions
            attack=Queen21b_attack.attack
            
            Queen22b_attack=attack_class_and_all_black("q1b",q22b,white_check,attack,attack_positions,all_black)
            Queen22b_attack.attack_class1("q1b",q22b,white_check,attack,attack_positions,all_black)
            Queen22b_attack.all_black_class1("q1b",q22b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen22b_attack.attack_positions
            attack=Queen22b_attack.attack

            Queen23b_attack=attack_class_and_all_black("q1b",q23b,white_check,attack,attack_positions,all_black)
            Queen23b_attack.attack_class1("q1b",q23b,white_check,attack,attack_positions,all_black)
            Queen23b_attack.all_black_class1("q1b",q23b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen23b_attack.attack_positions
            attack=Queen23b_attack.attack
            
            Queen24b_attack=attack_class_and_all_black("q1b",q24b,white_check,attack,attack_positions,all_black)
            Queen24b_attack.attack_class1("q1b",q24b,white_check,attack,attack_positions,all_black)
            Queen24b_attack.all_black_class1("q1b",q24b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen24b_attack.attack_positions
            attack=Queen24b_attack.attack

            Queen25b_attack=attack_class_and_all_black("q1b",q25b,white_check,attack,attack_positions,all_black)
            Queen25b_attack.attack_class1("q1b",q25b,white_check,attack,attack_positions,all_black)
            Queen25b_attack.all_black_class1("q1b",q25b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen25b_attack.attack_positions
            attack=Queen25b_attack.attack
            
            Queen26b_attack=attack_class_and_all_black("q1b",q26b,white_check,attack,attack_positions,all_black)
            Queen26b_attack.attack_class1("q1b",q26b,white_check,attack,attack_positions,all_black)
            Queen26b_attack.all_black_class1("q1b",q26b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen26b_attack.attack_positions
            attack=Queen26b_attack.attack
            
            Queen27b_attack=attack_class_and_all_black("q1b",q27b,white_check,attack,attack_positions,all_black)
            Queen27b_attack.attack_class1("q1b",q27b,white_check,attack,attack_positions,all_black)
            Queen27b_attack.all_black_class1("q1b",q27b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen27b_attack.attack_positions
            attack=Queen27b_attack.attack
            
            Queen28b_attack=attack_class_and_all_black("q1b",q28b,white_check,attack,attack_positions,all_black)
            Queen28b_attack.attack_class1("q1b",q28b,white_check,attack,attack_positions,all_black)
            Queen28b_attack.all_black_class1("q1b",q28b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen28b_attack.attack_positions
            attack=Queen28b_attack.attack

            Queen31b_attack=attack_class_and_all_black("q1b",q31b,white_check,attack,attack_positions,all_black)
            Queen31b_attack.attack_class1("q1b",q31b,white_check,attack,attack_positions,all_black)
            Queen31b_attack.all_black_class1("q1b",q31b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen31b_attack.attack_positions
            attack=Queen31b_attack.attack
            
            Queen32b_attack=attack_class_and_all_black("q1b",q32b,white_check,attack,attack_positions,all_black)
            Queen32b_attack.attack_class1("q1b",q32b,white_check,attack,attack_positions,all_black)
            Queen32b_attack.all_black_class1("q1b",q32b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen32b_attack.attack_positions
            attack=Queen32b_attack.attack

            Queen33b_attack=attack_class_and_all_black("q1b",q33b,white_check,attack,attack_positions,all_black)
            Queen33b_attack.attack_class1("q1b",q33b,white_check,attack,attack_positions,all_black)
            Queen33b_attack.all_black_class1("q1b",q33b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen33b_attack.attack_positions
            attack=Queen33b_attack.attack
            
            Queen34b_attack=attack_class_and_all_black("q1b",q34b,white_check,attack,attack_positions,all_black)
            Queen34b_attack.attack_class1("q1b",q34b,white_check,attack,attack_positions,all_black)
            Queen34b_attack.all_black_class1("q1b",q34b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen34b_attack.attack_positions
            attack=Queen34b_attack.attack

            Queen35b_attack=attack_class_and_all_black("q1b",q35b,white_check,attack,attack_positions,all_black)
            Queen35b_attack.attack_class1("q1b",q35b,white_check,attack,attack_positions,all_black)
            Queen35b_attack.all_black_class1("q1b",q35b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen35b_attack.attack_positions
            attack=Queen35b_attack.attack
            
            Queen36b_attack=attack_class_and_all_black("q1b",q36b,white_check,attack,attack_positions,all_black)
            Queen36b_attack.attack_class1("q1b",q36b,white_check,attack,attack_positions,all_black)
            Queen36b_attack.all_black_class1("q1b",q36b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen36b_attack.attack_positions
            attack=Queen36b_attack.attack
            
            Queen37b_attack=attack_class_and_all_black("q1b",q37b,white_check,attack,attack_positions,all_black)
            Queen37b_attack.attack_class1("q1b",q37b,white_check,attack,attack_positions,all_black)
            Queen37b_attack.all_black_class1("q1b",q37b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen37b_attack.attack_positions
            attack=Queen37b_attack.attack
            
            Queen38b_attack=attack_class_and_all_black("q1b",q38b,white_check,attack,attack_positions,all_black)
            Queen38b_attack.attack_class1("q1b",q38b,white_check,attack,attack_positions,all_black)
            Queen38b_attack.all_black_class1("q1b",q38b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen38b_attack.attack_positions
            attack=Queen38b_attack.attack
            
            Queen41b_attack=attack_class_and_all_black("q1b",q41b,white_check,attack,attack_positions,all_black)
            Queen41b_attack.attack_class1("q1b",q41b,white_check,attack,attack_positions,all_black)
            Queen41b_attack.all_black_class1("q1b",q41b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen41b_attack.attack_positions
            attack=Queen41b_attack.attack
            
            Queen42b_attack=attack_class_and_all_black("q1b",q42b,white_check,attack,attack_positions,all_black)
            Queen42b_attack.attack_class1("q1b",q42b,white_check,attack,attack_positions,all_black)
            Queen42b_attack.all_black_class1("q1b",q42b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen42b_attack.attack_positions
            attack=Queen42b_attack.attack

            Queen43b_attack=attack_class_and_all_black("q1b",q43b,white_check,attack,attack_positions,all_black)
            Queen43b_attack.attack_class1("q1b",q43b,white_check,attack,attack_positions,all_black)
            Queen43b_attack.all_black_class1("q1b",q43b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen43b_attack.attack_positions
            attack=Queen43b_attack.attack
            
            Queen44b_attack=attack_class_and_all_black("q1b",q44b,white_check,attack,attack_positions,all_black)
            Queen44b_attack.attack_class1("q1b",q44b,white_check,attack,attack_positions,all_black)
            Queen44b_attack.all_black_class1("q1b",q44b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen44b_attack.attack_positions
            attack=Queen44b_attack.attack

            Queen45b_attack=attack_class_and_all_black("q1b",q45b,white_check,attack,attack_positions,all_black)
            Queen45b_attack.attack_class1("q1b",q45b,white_check,attack,attack_positions,all_black)
            Queen45b_attack.all_black_class1("q1b",q45b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen45b_attack.attack_positions
            attack=Queen45b_attack.attack
            
            Queen46b_attack=attack_class_and_all_black("q1b",q46b,white_check,attack,attack_positions,all_black)
            Queen46b_attack.attack_class1("q1b",q46b,white_check,attack,attack_positions,all_black)
            Queen46b_attack.all_black_class1("q1b",q46b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen46b_attack.attack_positions
            attack=Queen46b_attack.attack
            
            Queen47b_attack=attack_class_and_all_black("q1b",q47b,white_check,attack,attack_positions,all_black)
            Queen47b_attack.attack_class1("q1b",q47b,white_check,attack,attack_positions,all_black)
            Queen47b_attack.all_black_class1("q1b",q47b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen47b_attack.attack_positions
            attack=Queen47b_attack.attack
            
            Queen48b_attack=attack_class_and_all_black("q1b",q48b,white_check,attack,attack_positions,all_black)
            Queen48b_attack.attack_class1("q1b",q48b,white_check,attack,attack_positions,all_black)
            Queen48b_attack.all_black_class1("q1b",q48b,white_check,attack,attack_positions,all_black)
            attack_positions=Queen48b_attack.attack_positions
            attack=Queen48b_attack.attack
            
            for ju in range (0,len(kn1b)):
                if xposition==kn1b[ju][0] and yposition==kn1b[ju][1]:
                    attack.append(["kn1b"])
            for ju in range (0,len(kn2b)):
                if xposition==kn2b[ju][0] and yposition==kn2b[ju][1]:
                    attack.append(["kn2b"])
            for ju in range (0,len(kn3b)):
                if xposition==kn3b[ju][0] and yposition==kn3b[ju][1]:
                    attack.append(["kn3b"])
            for ju in range (0,len(kn4b)):
                if xposition==kn4b[ju][0] and yposition==kn4b[ju][1]:
                    attack.append(["kn4b"])
            for ju in range (0,len(kn5b)):
                if xposition==kn5b[ju][0] and yposition==kn5b[ju][1]:
                    attack.append(["kn5b"])
            for ju in range (0,len(p1b)):
                if xposition==p1b[ju][0] and yposition==p1b[ju][1]:
                    attack.append(["p1b"])
            for ju in range (0,len(p2b)):
                if xposition==p2b[ju][0] and yposition==p2b[ju][1]:
                    attack.append(["p2b"])
            for ju in range (0,len(p3b)):
                if xposition==p3b[ju][0] and yposition==p3b[ju][1]:
                    attack.append(["p3b"])
            for ju in range (0,len(p4b)):
                if xposition==p4b[ju][0] and yposition==p4b[ju][1]:
                    attack.append(["p4b"])
            for ju in range (0,len(p5b)):
                if xposition==p5b[ju][0] and yposition==p5b[ju][1]:
                    attack.append(["p5b"])
            for ju in range (0,len(p6b)):
                if xposition==p6b[ju][0] and yposition==p6b[ju][1]:
                    attack.append(["p6b"])
            for ju in range (0,len(p7b)):
                if xposition==p7b[ju][0] and yposition==p7b[ju][1]:
                    attack.append(["p7b"])
            for ju in range (0,len(p8b)):               
                if xposition==p8b[ju][0] and yposition==p8b[ju][1]:
                    attack.append(["p8b"])
                    
            if attack!=[]:
                white_check=True
                
            for i in range (0,len(kn1b)):
                if kn1b!=[]:
                    all_black.append(kn1b[i])
            for i in range (0,len(kn2b)):
                if kn2b!=[]:
                    all_black.append(kn2b[i])
            for i in range (0,len(kn3b)):
                if kn3b!=[]:
                    all_black.append(kn3b[i])
            for i in range (0,len(kn4b)):
                if kn4b!=[]:
                    all_black.append(kn4b[i])
            for i in range (0,len(kn5b)):
                if kn5b!=[]:
                    all_black.append(kn5b[i])
            for i in range (0,len(k1w)):
                if k1w!=[]:
                    all_black.append(k1w[i])
            for i in range (0,len(p1b)):
                if p1b!=[]:
                    all_black.append(p1b[i])
            for i in range (0,len(p2b)):
                if p2b!=[]:
                    all_black.append(p2b[i])
            for i in range (0,len(p3b)):
                if p3b!=[]:
                    all_black.append(p3b[i])
            for i in range (0,len(p4b)):
                if p4b!=[]:
                    all_black.append(p4b[i])
            for i in range (0,len(p5b)):
                if p5b!=[]:
                    all_black.append(p5b[i])
            for i in range (0,len(p6b)):
                if p6b!=[]:
                    all_black.append(p6b[i])
            for i in range (0,len(p7b)):
                if p7b!=[]:
                    all_black.append(p7b[i])
            for i in range (0,len(p8b)):
                if p8b!=[]:
                    all_black.append(p8b[i])
            hw=1
        white_stalemate=False
        white_checkmate=False
        coords_backup=coords
        coords_backup2=coords2
        if moves==0:
            yposition=list_searchy(Board,"k1w")
            xposition=list_searchx(Board,"k1w")
            xposition=60*xposition
            yposition=60*yposition
            coords=[]
            coords2=[]
            King1w2=king1(k1w,"k1w","b","w")
            King1w2.check(k1w,"k1w","b","w")
            vc="k1w"
            King1w=kingw(coords,coords2,kn1wmx,kn1wmy,"k1w","b")
            King1w.possible_moves(coords,coords2,"b")
            if white_check==False and all_white==k1w and coords==[]:
                white_stalemate=True
            if white_check==True and coords==[]:
                Bishop1w=bishopw(coords,coords2,b1wmx,b1wmy,"b1w","b")
                vc="b1w"
                Bishop1w.possible_moves(coords,coords2,"b")
                Bishop2w=bishopw(coords,coords2,b2wmx,b2wmy,"b2w","b")
                vc="b2w"
                Bishop2w.possible_moves(coords,coords2,"b")
                Bishop3w=bishopw(coords,coords2,b3wmx,b3wmy,"b3w","b")
                vc="b3w"
                Bishop3w.possible_moves(coords,coords2,"b")
                Bishop4w=bishopw(coords,coords2,b4wmx,b4wmy,"b4w","b")
                vc="b4w"
                Bishop4w.possible_moves(coords,coords2,"b")
                Bishop5w=bishopw(coords,coords2,b5wmx,b5wmy,"b5w","b")
                vc="b5w"
                Bishop5w.possible_moves(coords,coords2,"b")
                vc="r1w"
                Rook1w=rookw(coords,coords2,r1wmx,r1wmy,"r1w","b")
                Rook1w.possible_moves(coords,coords2,"b")
                vc="r2w"
                Rook2w=rookw(coords,coords2,r2wmx,r2wmy,"r2w","b")
                Rook2w.possible_moves(coords,coords2,"b")
                vc="r3w"
                Rook3w=rookw(coords,coords2,r3wmx,r3wmy,"r3w","b")
                Rook3w.possible_moves(coords,coords2,"b")
                vc="r4w"
                Rook4w=rookw(coords,coords2,r4wmx,r4wmy,"r4w","b")
                Rook4w.possible_moves(coords,coords2,"b")
                vc="r5w"
                Rook5w=rookw(coords,coords2,r5wmx,r5wmy,"r5w","b")
                Rook5w.possible_moves(coords,coords2,"b")
                vc="kn1w"
                Knight1w=knightw(coords,coords2,kn1wmx,kn1wmy,"kn1w","b")
                Knight1w.possible_moves(coords,coords2,"b")
                vc="kn2w"
                Knight2w=knightw(coords,coords2,kn2wmx,kn2wmy,"kn2w","b")
                Knight2w.possible_moves(coords,coords2,"b")
                vc="kn3w"
                Knight3w=knightw(coords,coords2,kn3wmx,kn3wmy,"kn3w","b")
                Knight3w.possible_moves(coords,coords2,"b")
                vc="kn4w"
                Knight4w=knightw(coords,coords2,kn4wmx,kn4wmy,"kn4w","b")
                Knight4w.possible_moves(coords,coords2,"b")
                vc="kn5w"
                Knight5w=knightw(coords,coords2,kn5wmx,kn5wmy,"kn5w","b")
                Knight5w.possible_moves(coords,coords2,"b")
                vc="q1w"
                Queen1w=queenw(coords,coords2,q1wmx,q1wmy,"q1w","b")
                Queen1w.possible_moves(coords,coords2,"b")
                vc="q2w"
                Queen2w=queenw(coords,coords2,q2wmx,q2wmy,"q2w","b")
                Queen2w.possible_moves(coords,coords2,"b")
                vc="q3w"
                Queen3w=queenw(coords,coords2,q3wmx,q3wmy,"q3w","b")
                Queen3w.possible_moves(coords,coords2,"b")
                vc="q4w"
                Queen4w=queenw(coords,coords2,q4wmx,q4wmy,"q4w","b")
                Queen4w.possible_moves(coords,coords2,"b")
                vc="p1w"
                pawn1w11=pawnw(coords,coords2,p1wmx,p1wmy,"p1w","b",moves21)
                pawn1w11.possible_moves(coords,coords2,"b",moves21)
                vc="p2w"
                pawn2w11=pawnw(coords,coords2,p2wmx,p2wmy,"p2w","b",moves22)
                pawn2w11.possible_moves(coords,coords2,"b",moves22)
                vc="p3w"
                pawn3w11=pawnw(coords,coords2,p3wmx,p3wmy,"p3w","b",moves23)
                pawn3w11.possible_moves(coords,coords2,"b",moves23)
                vc="p4w"
                pawn4w=pawnw(coords,coords2,p4wmx,p4wmy,"p4w","b",moves24)
                pawn4w.possible_moves(coords,coords2,"b",moves24)
                vc="p5w"
                pawn5w11=pawnw(coords,coords2,p5wmx,p5wmy,"p5w","b",moves25)
                pawn5w11.possible_moves(coords,coords2,"b",moves25)
                vc="p6w"
                pawn6w11=pawnw(coords,coords2,p6wmx,p6wmy,"p6w","b",moves26)
                pawn6w11.possible_moves(coords,coords2,"b",moves26)
                vc="p7w"
                pawn7w11=pawnw(coords,coords2,p7wmx,p7wmy,"p7w","b",moves27)
                pawn7w11.possible_moves(coords,coords2,"b",moves27)
                vc="p8w"
                Pawn8w11=pawnw(coords,coords2,p8wmx,p8wmy,"p8w","b",moves28)
                Pawn8w11.possible_moves(coords,coords2,"b",moves28)
                if coords==[]:
                    white_checkmate=True
            coords=[]
            coords2=[]
        num_of_pieces=0
        for i in range(0,8):
            for a in range(0,8):
                if Board[i][a][0]!="":
                    num_of_pieces=num_of_pieces+1
        if num_of_pieces==2:
            black_stalemate=True
        black_stalemate=False
        black_checkmate=False
        if moves==1:
            yposition=list_searchy(Board,"k1b")
            xposition=list_searchx(Board,"k1b")
            xposition=60*xposition
            yposition=60*yposition    
            coords=[]
            coords2=[]
            King1b2=king1(k1b,"k1b","w","b")
            King1b2.check(k1b,"k1b","w","b")
            vc="k1b"
            King1b=kingw(coords,coords2,kn1bmx,kn1bmy,"k1b","w")
            King1b.possible_moves(coords,coords2,"w")
            if black_check==False and all_black==k1b and coords==[]:
                black_stalemate=True
            if black_check==True and coords==[]:
                Bishop1b=bishopw(coords,coords2,b1bmx,b1bmy,"b1b","w")
                vc="b1b"
                Bishop1b.possible_moves(coords,coords2,"w")
                Bishop2b=bishopw(coords,coords2,b2bmx,b2bmy,"b2b","w")
                vc="b2b"
                Bishop2b.possible_moves(coords,coords2,"w")
                Bishop3b=bishopw(coords,coords2,b3bmx,b3bmy,"b3b","w")
                vc="b3b"
                Bishop3b.possible_moves(coords,coords2,"w")
                Bishop4b=bishopw(coords,coords2,b4bmx,b4bmy,"b4b","w")
                vc="b4b"
                Bishop4b.possible_moves(coords,coords2,"w")
                Bishop5b=bishopw(coords,coords2,b5bmx,b5bmy,"b5b","w")
                vc="b5b"
                Bishop5b.possible_moves(coords,coords2,"w")
                vc="r1b"
                Rook1b=rookw(coords,coords2,r1bmx,r1bmy,"r1b","w")
                Rook1b.possible_moves(coords,coords2,"w")
                vc="r2b"
                Rook2b=rookw(coords,coords2,r2bmx,r2bmy,"r2b","w")
                Rook2b.possible_moves(coords,coords2,"w")
                vc="r3b"
                Rook3b=rookw(coords,coords2,r3bmx,r3bmy,"r3b","w")
                Rook3b.possible_moves(coords,coords2,"w")
                vc="r4b"
                Rook4b=rookw(coords,coords2,r4bmx,r4bmy,"r4b","w")
                Rook4b.possible_moves(coords,coords2,"w")
                vc="r5b"
                Rook5b=rookw(coords,coords2,r5bmx,r5bmy,"r5b","w")
                Rook5b.possible_moves(coords,coords2,"w")
                vc="kn1b"
                Knight1b=knightw(coords,coords2,kn1bmx,kn1bmy,"kn1b","w")
                Knight1b.possible_moves(coords,coords2,"w")
                vc="kn2b"
                Knight2b=knightw(coords,coords2,kn2bmx,kn2bmy,"kn2b","w")
                Knight2b.possible_moves(coords,coords2,"w")
                vc="kn3b"
                Knight3b=knightw(coords,coords2,kn3bmx,kn3bmy,"kn3b","w")
                Knight3b.possible_moves(coords,coords2,"w")
                vc="kn4b"
                Knight4b=knightw(coords,coords2,kn4bmx,kn4bmy,"kn4b","w")
                Knight4b.possible_moves(coords,coords2,"w")
                vc="kn5b"
                Knight5b=knightw(coords,coords2,kn5bmx,kn5bmy,"kn5b","w")
                Knight5b.possible_moves(coords,coords2,"w")
                vc="q1b"
                Queen1b=queenw(coords,coords2,q1bmx,q1bmy,"q1b","w")
                Queen1b.possible_moves(coords,coords2,"w")
                vc="q2b"
                Queen2b=queenw(coords,coords2,q2bmx,q2bmy,"q2b","w")
                Queen2b.possible_moves(coords,coords2,"w")
                vc="q3b"
                Queen3b=queenw(coords,coords2,q3bmx,q3bmy,"q3b","w")
                Queen3b.possible_moves(coords,coords2,"w")
                vc="q4b"
                Queen4b=queenw(coords,coords2,q4bmx,q4bmy,"q4b","w")
                Queen4b.possible_moves(coords,coords2,"w")
                vc="p1b"
                pawn1b11=pawnb(coords,coords2,p1bmx,p1bmy,"p1b","w",moves21)
                pawn1b11.possible_moves(coords,coords2,"w",moves21)
                vc="p2b"
                pawn2b11=pawnb(coords,coords2,p2bmx,p2bmy,"p2b","w",moves22)
                pawn2b11.possible_moves(coords,coords2,"w",moves22)
                vc="p3b"
                pawn3b11=pawnb(coords,coords2,p3bmx,p3bmy,"p3b","w",moves23)
                pawn3b11.possible_moves(coords,coords2,"w",moves23)
                vc="p4b"
                pawn4b11=pawnb(coords,coords2,p4bmx,p4bmy,"p4b","w",moves24)
                pawn4b11.possible_moves(coords,coords2,"w",moves24)
                vc="p5b"
                pawn5b11=pawnb(coords,coords2,p5bmx,p5bmy,"p5b","w",moves25)
                pawn5b11.possible_moves(coords,coords2,"w",moves25)
                vc="p6b"
                pawn6b11=pawnb(coords,coords2,p6bmx,p6bmy,"p6b","w",moves26)
                pawn6b11.possible_moves(coords,coords2,"w",moves26)
                vc="p7b"
                pawn7b11=pawnb(coords,coords2,p7bmx,p7bmy,"p7b","w",moves27)
                pawn7b11.possible_moves(coords,coords2,"w",moves27)
                vc="p8b"
                pawn8b11=pawnb(coords,coords2,p8bmx,p8bmy,"p8b","w",moves28)
                pawn8b11.possible_moves(coords,coords2,"w",moves28)
                if coords==[]:
                    black_checkmate=True
            coords=[]
            coords2=[]
        coords=coords_backup
        coords2=coords_backup2
        if Check_screen==True:
            black_checkmate=False
            white_checkmate=False
            black_stalemate=False
            white_stalemate=False
        if black_checkmate==True or white_checkmate==True or black_stalemate==True or white_stalemate==True:
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
            if black_stalemate==True or white_stalemate==True:
                gameDisplay.blit(stalemate,(127,128))
            else:
                gameDisplay.blit(checkmate,(17,173))
            pygame.display.update()
            pygame.time.delay(1000)
            board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)                    
            pygame.display.update()
            pygame.time.delay(500)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    Check_screen==True
        if piece=="":
            if counter%2==1:
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                pygame.display.update()
                event3=wait2()
                counter=counter+1
                rfv=0
            elif counter%2!=1:
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                pygame.display.update()
                counter=counter+1
        moves=moves%2
        if moves==0:

    ######################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo1mx,bo1my=b1wmx,b1wmy
                    vc="b1w"
                    b1wmx,b1wmy=pygame.mouse.get_pos()
                    if b1wmx>list_searchx(Board,"b1w")*60 and b1wmx<list_searchx(Board,"b1w")*60+60 and b1wmy>list_searchy(Board,"b1w")*60 and b1wmy<list_searchy(Board,"b1w")*60+60:
                        piece="bishop1"
                        Bishop1w=bishopw(coords,coords2,b1wmx,b1wmy,"b1w","b")
                        Bishop1w.possible_moves(coords,coords2,"b")
                    else:
                        b1wmx,b1wmy=bo1mx,bo1my
                        
                    bo2mx,bo2my=b2wmx,b2wmy
                    vc="b2w"
                    b2wmx,b2wmy=pygame.mouse.get_pos()
                    if b2wmx>list_searchx(Board,"b2w")*60 and b2wmx<list_searchx(Board,"b2w")*60+60 and b2wmy>list_searchy(Board,"b2w")*60 and b2wmy<list_searchy(Board,"b2w")*60+60:
                        piece="bishop2"
                        Bishop2w=bishopw(coords,coords2,b2wmx,b2wmy,"b2w","b")
                        Bishop2w.possible_moves(coords,coords2,"b")
                    else:
                        b2wmx,b2wmy=bo2mx,bo2my
                        
            if piece=="bishop1":
                b1wmx,b1wmy=pygame.mouse.get_pos()
                tg=Bishop1w.position(coords,coords2,convertx(b1wmx),converty(b1wmy),"b1w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b1wmx,b1wmy=[],[],"",1,(list_searchx(Board,"b1w"))*60,(list_searchy(Board,"b1w"))*60
            if piece=="bishop2":
                b2wmx,b2wmy=pygame.mouse.get_pos()
                tg=Bishop2w.position(coords,coords2,convertx(b2wmx),converty(b2wmy),"b2w")                    
                if tg==2:
                    hb,white_check,moves=0,False,moves+1
                if tg==3 or tg==2 or tg==1:
                    coords,coords2,piece,rfv,b2wmx,b2wmy=[],[],"",1,(list_searchx(Board,"b2w"))*60,(list_searchy(Board,"b2w"))*60
#############################################################################
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo3mx=b3wmx
                    bo3my=b3wmy
                    vc="b3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    b3wmx,b3wmy=pygame.mouse.get_pos()
                    if b3wmx>xposition and b3wmx<xposition2 and b3wmy>yposition and b3wmy<yposition2:
                        piece="bishop3"
                        Bishop3w=bishopw(coords,coords2,b3wmx,b3wmy,"b3w","b")
                        Bishop3w.possible_moves(coords,coords2,"b")
                    else:
                        b3wmx=bo3mx
                        b3wmy=bo3my  
            if piece=="bishop3":
                b3wmx,b3wmy=pygame.mouse.get_pos()
                g="b3w"
                b3wmx,b3wmy=pygame.mouse.get_pos()
                bo3mx=b3wmx
                bo3my=b3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b3wmx=convertx(b3wmx)
                b3wmy=converty(b3wmy)
                tg=Bishop3w.position(coords,coords2,b3wmx,b3wmy,"b3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    hb=0
                    white_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b3wmy=(yposition)*60
                    b3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo4mx=b4wmx
                    bo4my=b4wmy
                    vc="b4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    b4wmx,b4wmy=pygame.mouse.get_pos()
                    if b4wmx>xposition and b4wmx<xposition2 and b4wmy>yposition and b4wmy<yposition2:
                        piece="bishop4"
                        Bishop4w=bishopw(coords,coords2,b4wmx,b4wmy,"b4w","b")
                        Bishop4w.possible_moves(coords,coords2,"b")
                    else:
                        b4wmx=bo4mx
                        b4wmy=bo4my  
            if piece=="bishop4":
                b4wmx,b4wmy=pygame.mouse.get_pos()
                g="b4w"
                b4wmx,b4wmy=pygame.mouse.get_pos()
                bo4mx=b4wmx
                bo4my=b4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b4wmx=convertx(b4wmx)
                b4wmy=converty(b4wmy)
                tg=Bishop4w.position(coords,coords2,b4wmx,b4wmy,"b4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    hb=0
                    white_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b4wmy=(yposition)*60
                    b4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo5mx=b5wmx
                    bo5my=b5wmy
                    vc="b5w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    b5wmx,b5wmy=pygame.mouse.get_pos()
                    if b5wmx>xposition and b5wmx<xposition2 and b5wmy>yposition and b5wmy<yposition2:
                        piece="bishop5"
                        Bishop5w=bishopw(coords,coords2,b5wmx,b5wmy,"b5w","b")
                        Bishop5w.possible_moves(coords,coords2,"b")
                    else:
                        b5wmx=bo5mx
                        b5wmy=bo5my  
            if piece=="bishop5":
                b5wmx,b5wmy=pygame.mouse.get_pos()
                g="b5w"
                b5wmx,b5wmy=pygame.mouse.get_pos()
                bo5mx=b5wmx
                bo5my=b5wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b5wmx=convertx(b5wmx)
                b5wmy=converty(b5wmy)
                tg=Bishop5w.position(coords,coords2,b5wmx,b5wmy,"b5w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    hb=0
                    white_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b5wmy=(yposition)*60
                    b5wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno1mx=kn1wmx
                    kno1my=kn1wmy
                    vc="kn1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn1wmx,kn1wmy=pygame.mouse.get_pos()
                    if kn1wmx>xposition and kn1wmx<xposition2 and kn1wmy>yposition and kn1wmy<yposition2:
                        piece="knight1"
                        Knight1w=knightw(coords,coords2,kn1wmx,kn1wmy,"kn1w","b")
                        Knight1w.possible_moves(coords,coords2,"b")
                    else:
                        kn1wmx=kno1mx
                        kn1wmy=kno1my  
            if piece=="knight1":
                kn1wmx,kn1wmy=pygame.mouse.get_pos()
                g="kn1w"
                kn1wmx,kn1wmy=pygame.mouse.get_pos()
                kno1mx=kn1wmx
                kno1my=kn1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn1wmx=convertx(kn1wmx)
                kn1wmy=converty(kn1wmy)
                tg=Knight1w.position(coords,coords2,kn1wmx,kn1wmy,"kn1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn1wmy=(yposition)*60
                    kn1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno2mx=kn2wmx
                    kno2my=kn2wmy
                    vc="kn2w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn2wmx,kn2wmy=pygame.mouse.get_pos()
                    if kn2wmx>xposition and kn2wmx<xposition2 and kn2wmy>yposition and kn2wmy<yposition2:
                        piece="knight2"
                        Knight2w=knightw(coords,coords2,kn2wmx,kn2wmy,"kn2w","b")
                        Knight2w.possible_moves(coords,coords2,"b")
                    else:
                        kn2wmx=kno2mx
                        kn2wmy=kno2my  
            if piece=="knight2":
                kn2wmx,kn2wmy=pygame.mouse.get_pos()
                g="kn2w"
                kn2wmx,kn2wmy=pygame.mouse.get_pos()
                kno2mx=kn2wmx
                kno2my=kn2wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn2wmx=convertx(kn2wmx)
                kn2wmy=converty(kn2wmy)
                tg=Knight2w.position(coords,coords2,kn2wmx,kn2wmy,"kn2w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn2wmy=(yposition)*60
                    kn2wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno3mx=kn3wmx
                    kno3my=kn3wmy
                    vc="kn3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn3wmx,kn3wmy=pygame.mouse.get_pos()
                    if kn3wmx>xposition and kn3wmx<xposition2 and kn3wmy>yposition and kn3wmy<yposition2:
                        piece="knight3"
                        Knight3w=knightw(coords,coords2,kn3wmx,kn3wmy,"kn3w","b")
                        Knight3w.possible_moves(coords,coords2,"b")
                    else:
                        kn3wmx=kno3mx
                        kn3wmy=kno3my  
            if piece=="knight3":
                kn3wmx,kn3wmy=pygame.mouse.get_pos()
                g="kn3w"
                kn3wmx,kn3wmy=pygame.mouse.get_pos()
                kno3mx=kn3wmx
                kno3my=kn3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn3wmx=convertx(kn3wmx)
                kn3wmy=converty(kn3wmy)
                tg=Knight3w.position(coords,coords2,kn3wmx,kn3wmy,"kn3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn3wmy=(yposition)*60
                    kn3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno4mx=kn4wmx
                    kno4my=kn4wmy
                    vc="kn4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn4wmx,kn4wmy=pygame.mouse.get_pos()
                    if kn4wmx>xposition and kn4wmx<xposition2 and kn4wmy>yposition and kn4wmy<yposition2:
                        piece="knight4"
                        Knight4w=knightw(coords,coords2,kn4wmx,kn4wmy,"kn4w","b")
                        Knight4w.possible_moves(coords,coords2,"b")
                    else:
                        kn4wmx=kno4mx
                        kn4wmy=kno4my  
            if piece=="knight4":
                kn4wmx,kn4wmy=pygame.mouse.get_pos()
                g="kn4w"
                kn4wmx,kn4wmy=pygame.mouse.get_pos()
                kno4mx=kn4wmx
                kno4my=kn4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn4wmx=convertx(kn4wmx)
                kn4wmy=converty(kn4wmy)
                tg=Knight4w.position(coords,coords2,kn4wmx,kn4wmy,"kn4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn4wmy=(yposition)*60
                    kn4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno5mx=kn5wmx
                    kno5my=kn5wmy
                    vc="kn5w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn5wmx,kn5wmy=pygame.mouse.get_pos()
                    if kn5wmx>xposition and kn5wmx<xposition2 and kn5wmy>yposition and kn5wmy<yposition2:
                        piece="knight5"
                        Knight5w=knightw(coords,coords2,kn5wmx,kn5wmy,"kn5w","b")
                        Knight5w.possible_moves(coords,coords2,"b")
                    else:
                        kn5wmx=kno5mx
                        kn5wmy=kno5my  
            if piece=="knight5":
                kn5wmx,kn5wmy=pygame.mouse.get_pos()
                g="kn5w"
                kn5wmx,kn5wmy=pygame.mouse.get_pos()
                kno5mx=kn5wmx
                kno5my=kn5wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn5wmx=convertx(kn5wmx)
                kn5wmy=converty(kn5wmy)
                tg=Knight5w.position(coords,coords2,kn5wmx,kn5wmy,"kn5w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn5wmy=(yposition)*60
                    kn5wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ko1mx=k1wmx
                    ko1my=k1wmy
                    vc="k1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    k1wmx,k1wmy=pygame.mouse.get_pos()
                    if k1wmx>xposition and k1wmx<xposition2 and k1wmy>yposition and k1wmy<yposition2:
                        piece="king1"
                        King1w=kingw(coords,coords2,kn1wmx,kn1wmy,"k1w","b")
                        King1w.possible_moves(coords,coords2,"b")
                    else:
                        k1wmx=ko1mx
                        k1wmy=ko1my  
            if piece=="king1":
                k1wmx,k1wmy=pygame.mouse.get_pos()
                g="k1w"
                k1wmx,k1wmy=pygame.mouse.get_pos()
                ko1mx=k1wmx
                ko1my=k1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                k1wmx=convertx(k1wmx)
                k1wmy=converty(k1wmy)
                tg=King1w.position(coords,coords2,k1wmx,k1wmy,"k1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves2kw=1
                    white_check=False
                    yposition=list_searchy(Board,"r1w")
                    xposition=list_searchx(Board,"r1w")
                    r1wmx=xposition*60
                    r1wmy=yposition*60
                    
                    yposition=list_searchy(Board,"r2w")
                    xposition=list_searchx(Board,"r2w")
                    r2wmx=xposition*60
                    r2wmy=yposition*60
                    hb=0
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    k1wmy=(yposition)*60
                    k1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro1mx=r1wmx
                    ro1my=r1wmy
                    vc="r1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    r1wmx,r1wmy=pygame.mouse.get_pos()
                    if r1wmx>xposition and r1wmx<xposition2 and r1wmy>yposition and r1wmy<yposition2:
                        piece="rook1"
                        Rook1w=rookw(coords,coords2,r1wmx,r1wmy,"r1w","b")
                        Rook1w.possible_moves(coords,coords2,"b")
                    else:
                        r1wmx=ro1mx
                        r1wmy=ro1my  
            if piece=="rook1":
                r1wmx,r1wmy=pygame.mouse.get_pos()
                g="r1w"
                r1wmx,r1wmy=pygame.mouse.get_pos()
                ro1mx=r1wmx
                ro1my=r1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r1wmx=convertx(r1wmx)
                r1wmy=converty(r1wmy)
                tg=Rook1w.position(coords,coords2,r1wmx,r1wmy,"r1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves2r1w=1
                    white_check=False
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r1wmy=(yposition)*60
                    r1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro2mx=r2wmx
                    ro2my=r2wmy
                    vc="r2w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    r2wmx,r2wmy=pygame.mouse.get_pos()
                    if r2wmx>xposition and r2wmx<xposition2 and r2wmy>yposition and r2wmy<yposition2:
                        piece="rook2"
                        Rook2w=rookw(coords,coords2,r2wmx,r2wmy,"r2w","b")
                        Rook2w.possible_moves(coords,coords2,"b")
                    else:
                        r2wmx=ro2mx
                        r2wmy=ro2my  
            if piece=="rook2":
                r2wmx,r2wmy=pygame.mouse.get_pos()
                g="r2w"
                r2wmx,r2wmy=pygame.mouse.get_pos()
                ro2mx=r2wmx
                ro2my=r2wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r2wmx=convertx(r2wmx)
                r2wmy=converty(r2wmy)
                tg=Rook2w.position(coords,coords2,r2wmx,r2wmy,"r2w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves2r2w=1
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r2wmy=(yposition)*60
                    r2wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro3mx=r3wmx
                    ro3my=r3wmy
                    vc="r3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    r3wmx,r3wmy=pygame.mouse.get_pos()
                    if r3wmx>xposition and r3wmx<xposition2 and r3wmy>yposition and r3wmy<yposition2:
                        piece="rook3"
                        Rook3w=rookw(coords,coords2,r3wmx,r3wmy,"r3w","b")
                        Rook3w.possible_moves(coords,coords2,"b")
                    else:
                        r3wmx=ro3mx
                        r3wmy=ro3my  
            if piece=="rook3":
                r3wmx,r3wmy=pygame.mouse.get_pos()
                g="r3w"
                r3wmx,r3wmy=pygame.mouse.get_pos()
                ro3mx=r3wmx
                ro3my=r3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r3wmx=convertx(r3wmx)
                r3wmy=converty(r3wmy)
                tg=Rook3w.position(coords,coords2,r3wmx,r3wmy,"r3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves2r3w=1
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r3wmy=(yposition)*60
                    r3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro4mx=r4wmx
                    ro4my=r4wmy
                    vc="r4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    r4wmx,r4wmy=pygame.mouse.get_pos()
                    if r4wmx>xposition and r4wmx<xposition2 and r4wmy>yposition and r4wmy<yposition2:
                        piece="rook4"
                        Rook4w=rookw(coords,coords2,r4wmx,r4wmy,"r4w","b")
                        Rook4w.possible_moves(coords,coords2,"b")
                    else:
                        r4wmx=ro4mx
                        r4wmy=ro4my  
            if piece=="rook4":
                r4wmx,r4wmy=pygame.mouse.get_pos()
                g="r4w"
                r4wmx,r4wmy=pygame.mouse.get_pos()
                ro4mx=r4wmx
                ro4my=r4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r4wmx=convertx(r4wmx)
                r4wmy=converty(r4wmy)
                tg=Rook4w.position(coords,coords2,r4wmx,r4wmy,"r4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves2r4w=1
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r4wmy=(yposition)*60
                    r4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro5mx=r5wmx
                    ro5my=r5wmy
                    vc="r5w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    r5wmx,r5wmy=pygame.mouse.get_pos()
                    if r5wmx>xposition and r5wmx<xposition2 and r5wmy>yposition and r5wmy<yposition2:
                        piece="rook5"
                        Rook5w=rookw(coords,coords2,r5wmx,r5wmy,"r5w","b")
                        Rook5w.possible_moves(coords,coords2,"b")
                    else:
                        r5wmx=ro5mx
                        r5wmy=ro5my  
            if piece=="rook5":
                r5wmx,r5wmy=pygame.mouse.get_pos()
                g="r5w"
                r5wmx,r5wmy=pygame.mouse.get_pos()
                ro5mx=r5wmx
                ro5my=r5wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r5wmx=convertx(r5wmx)
                r5wmy=converty(r5wmy)
                tg=Rook5w.position(coords,coords2,r5wmx,r5wmy,"r5w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves2r5w=1
                    hb=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r5wmy=(yposition)*60
                    r5wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo1mx=q1wmx
                    qo1my=q1wmy
                    vc="q1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    q1wmx,q1wmy=pygame.mouse.get_pos()
                    if q1wmx>xposition and q1wmx<xposition2 and q1wmy>yposition and q1wmy<yposition2:
                        piece="queen1"
                        Queen1w=queenw(coords,coords2,q1wmx,q1wmy,"q1w","b")
                        Queen1w.possible_moves(coords,coords2,"b")
                    else:
                        q1wmx=qo1mx
                        q1wmy=qo1my  
            if piece=="queen1":
                q1wmx,q1wmy=pygame.mouse.get_pos()
                g="q1w"
                q1wmx,q1wmy=pygame.mouse.get_pos()
                qo1mx=q1wmx
                qo1my=q1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q1wmx=convertx(q1wmx)
                q1wmy=converty(q1wmy)
                tg=Queen1w.position(coords,coords2,q1wmx,q1wmy,"q1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q1wmy=(yposition)*60
                    q1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo2mx=q2wmx
                    qo2my=q2wmy
                    vc="q2w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    q2wmx,q2wmy=pygame.mouse.get_pos()
                    if q2wmx>xposition and q2wmx<xposition2 and q2wmy>yposition and q2wmy<yposition2:
                        piece="queen2"
                        Queen2w=queenw(coords,coords2,q2wmx,q2wmy,"q2w","b")
                        Queen2w.possible_moves(coords,coords2,"b")
                    else:
                        q2wmx=qo2mx
                        q2wmy=qo2my  
            if piece=="queen2":
                q2wmx,q2wmy=pygame.mouse.get_pos()
                g="q2w"
                q2wmx,q2wmy=pygame.mouse.get_pos()
                qo2mx=q2wmx
                qo2my=q2wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q2wmx=convertx(q2wmx)
                q2wmy=converty(q2wmy)
                tg=Queen2w.position(coords,coords2,q2wmx,q2wmy,"q2w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q2wmy=(yposition)*60
                    q2wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy
)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo3mx=q3wmx
                    qo3my=q3wmy
                    vc="q3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    q3wmx,q3wmy=pygame.mouse.get_pos()
                    if q3wmx>xposition and q3wmx<xposition2 and q3wmy>yposition and q3wmy<yposition2:
                        piece="queen3"
                        Queen3w=queenw(coords,coords2,q3wmx,q3wmy,"q3w","b")
                        Queen3w.possible_moves(coords,coords2,"b")
                    else:
                        q3wmx=qo3mx
                        q3wmy=qo3my  
            if piece=="queen3":
                q3wmx,q3wmy=pygame.mouse.get_pos()
                g="q3w"
                q3wmx,q3wmy=pygame.mouse.get_pos()
                qo3mx=q3wmx
                qo3my=q3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q3wmx=convertx(q3wmx)
                q3wmy=converty(q3wmy)
                tg=Queen3w.position(coords,coords2,q3wmx,q3wmy,"q3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q3wmy=(yposition)*60
                    q3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo4mx=q4wmx
                    qo4my=q4wmy
                    vc="q4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q4wmx,q4wmy=pygame.mouse.get_pos()
                    if q4wmx>xposition and q4wmx<xposition2 and q4wmy>yposition and q4wmy<yposition2:
                        piece="queen4"
                        Queen4w=queenw(coords,coords2,q4wmx,q4wmy,"q4w","b")
                        Queen4w.possible_moves(coords,coords2,"b")
                    else:
                        q4wmx=qo4mx
                        q4wmy=qo4my  
            if piece=="queen4":
                q4wmx,q4wmy=pygame.mouse.get_pos()
                g="q4w"
                q4wmx,q4wmy=pygame.mouse.get_pos()
                qo4mx=q4wmx
                qo4my=q4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q4wmx=convertx(q4wmx)
                q4wmy=converty(q4wmy)
                tg=Queen4w.position(coords,coords2,q4wmx,q4wmy,"q4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q4wmy=(yposition)*60
                    q4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po1mx=p1wmx
                    po1my=p1wmy
                    vc="p1w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    p1wmx,p1wmy=pygame.mouse.get_pos()
                    if p1wmx>xposition and p1wmx<xposition2 and p1wmy>yposition and p1wmy<yposition2:
                        piece="pawn1"
                        Pawn1w=pawnw(coords,coords2,p1wmx,p1wmy,"p1w","b",moves21)
                        Pawn1w.possible_moves(coords,coords2,"b",moves21)
                    else:
                        p1wmx=po1mx
                        p1wmy=po1my  
            if piece=="pawn1":
                p1wmx,p1wmy=pygame.mouse.get_pos()
                g="p1w"
                p1wmx,p1wmy=pygame.mouse.get_pos()
                po1mx=p1wmx
                po1my=p1wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p1wmx=convertx(p1wmx)
                p1wmy=converty(p1wmy)
                tg=Pawn1w.position(coords,coords2,p1wmx,p1wmy,"p1w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves21=moves21+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p1wmy=(yposition)*60
                    p1wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po2mx=p2wmx
                    po2my=p2wmy
                    vc="p2w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p2wmx,p2wmy=pygame.mouse.get_pos()
                    if p2wmx>xposition and p2wmx<xposition2 and p2wmy>yposition and p2wmy<yposition2:
                        piece="pawn2"
                        Pawn2w=pawnw(coords,coords2,p2wmx,p2wmy,"p2w","b",moves22)
                        Pawn2w.possible_moves(coords,coords2,"b",moves22)
                    else:
                        p2wmx=po2mx
                        p2wmy=po2my  
            if piece=="pawn2":
                p2wmx,p2wmy=pygame.mouse.get_pos()
                g="p2w"


                p2wmx,p2wmy=pygame.mouse.get_pos()
                po2mx=p2wmx
                po2my=p2wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p2wmx=convertx(p2wmx)
                p2wmy=converty(p2wmy)
                tg=Pawn2w.position(coords,coords2,p2wmx,p2wmy,"p2w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    moves22=moves22+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p2wmy=(yposition)*60
                    p2wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po3mx=p3wmx
                    po3my=p3wmy
                    vc="p3w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p3wmx,p3wmy=pygame.mouse.get_pos()
                    if p3wmx>xposition and p3wmx<xposition2 and p3wmy>yposition and p3wmy<yposition2:
                        piece="pawn3"
                        Pawn3w=pawnw(coords,coords2,p3wmx,p3wmy,"p3w","b",moves23)
                        Pawn3w.possible_moves(coords,coords2,"b",moves23)
                    else:
                        p3wmx=po3mx
                        p3wmy=po3my  
            if piece=="pawn3":
                p3wmx,p3wmy=pygame.mouse.get_pos()
                g="p3w"
                p3wmx,p3wmy=pygame.mouse.get_pos()
                po3mx=p3wmx
                po3my=p3wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p3wmx=convertx(p3wmx)
                p3wmy=converty(p3wmy)
                tg=Pawn3w.position(coords,coords2,p3wmx,p3wmy,"p3w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves23=moves23+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p3wmy=(yposition)*60
                    p3wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po4mx=p4wmx
                    po4my=p4wmy
                    vc="p4w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p4wmx,p4wmy=pygame.mouse.get_pos()
                    if p4wmx>xposition and p4wmx<xposition2 and p4wmy>yposition and p4wmy<yposition2:
                        piece="pawn4"
                        Pawn4w=pawnw(coords,coords2,p4wmx,p4wmy,"p4w","b",moves24)
                        Pawn4w.possible_moves(coords,coords2,"b",moves24)
                    else:
                        p4wmx=po4mx
                        p4wmy=po4my  
            if piece=="pawn4":
                p4wmx,p4wmy=pygame.mouse.get_pos()
                g="p4w"
                p4wmx,p4wmy=pygame.mouse.get_pos()
                po4mx=p4wmx
                po4my=p4wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p4wmx=convertx(p4wmx)
                p4wmy=converty(p4wmy)
                tg=Pawn4w.position(coords,coords2,p4wmx,p4wmy,"p4w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves24=moves24+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p4wmy=(yposition)*60
                    p4wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po5mx=p5wmx
                    po5my=p5wmy
                    vc="p5w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    p5wmx,p5wmy=pygame.mouse.get_pos()
                    if p5wmx>xposition and p5wmx<xposition2 and p5wmy>yposition and p5wmy<yposition2:
                        piece="pawn5"
                        Pawn5w=pawnw(coords,coords2,p5wmx,p5wmy,"p5w","b",moves25)
                        Pawn5w.possible_moves(coords,coords2,"b",moves25)
                    else:
                        p5wmx=po5mx
                        p5wmy=po5my  
            if piece=="pawn5":
                p5wmx,p5wmy=pygame.mouse.get_pos()
                g="p5w"
                p5wmx,p5wmy=pygame.mouse.get_pos()
                po5mx=p5wmx
                po5my=p5wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p5wmx=convertx(p5wmx)
                p5wmy=converty(p5wmy)
                tg=Pawn5w.position(coords,coords2,p5wmx,p5wmy,"p5w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    white_check=False
                    hb=0
                    moves25=moves25+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p5wmy=(yposition)*60
                    p5wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po6mx=p6wmx
                    po6my=p6wmy
                    vc="p6w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    p6wmx,p6wmy=pygame.mouse.get_pos()
                    if p6wmx>xposition and p6wmx<xposition2 and p6wmy>yposition and p6wmy<yposition2:
                        piece="pawn6"
                        Pawn6w=pawnw(coords,coords2,p6wmx,p6wmy,"p6w","b",moves26)
                        Pawn6w.possible_moves(coords,coords2,"b",moves26)
                    else:
                        p6wmx=po6mx
                        p6wmy=po6my  
            if piece=="pawn6":
                p6wmx,p6wmy=pygame.mouse.get_pos()
                g="p6w"
                p6wmx,p6wmy=pygame.mouse.get_pos()
                po6mx=p6wmx
                po6my=p6wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p6wmx=convertx(p6wmx)
                p6wmy=converty(p6wmy)
                tg=Pawn6w.position(coords,coords2,p6wmx,p6wmy,"p6w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    moves26=moves26+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p6wmy=(yposition)*60
                    p6wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po7mx=p7wmx
                    po7my=p7wmy
                    vc="p7w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    p7wmx,p7wmy=pygame.mouse.get_pos()
                    if p7wmx>xposition and p7wmx<xposition2 and p7wmy>yposition and p7wmy<yposition2:
                        piece="pawn7"
                        Pawn7w=pawnw(coords,coords2,p7wmx,p7wmy,"p7w","b",moves27)
                        Pawn7w.possible_moves(coords,coords2,"b",moves27)
                    else:
                        p7wmx=po7mx
                        p7wmy=po7my  
            if piece=="pawn7":
                p7wmx,p7wmy=pygame.mouse.get_pos()
                g="p7w"
                p7wmx,p7wmy=pygame.mouse.get_pos()
                po7mx=p7wmx
                po7my=p7wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p7wmx=convertx(p7wmx)
                p7wmy=converty(p7wmy)
                tg=Pawn7w.position(coords,coords2,p7wmx,p7wmy,"p7w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves27=moves27+1
                    hb=0
                    white_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p7wmy=(yposition)*60
                    p7wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po8mx=p8wmx
                    po8my=p8wmy
                    vc="p8w"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p8wmx,p8wmy=pygame.mouse.get_pos()
                    if p8wmx>xposition and p8wmx<xposition2 and p8wmy>yposition and p8wmy<yposition2:
                        piece="pawn8"
                        Pawn8w=pawnw(coords,coords2,p8wmx,p8wmy,"p8w","b",moves28)
                        Pawn8w.possible_moves(coords,coords2,"b",moves28)
                    else:
                        p8wmx=po8mx
                        p8wmy=po8my  
            if piece=="pawn8":
                p8wmx,p8wmy=pygame.mouse.get_pos()
                g="p8w"
                p8wmx,p8wmy=pygame.mouse.get_pos()
                po8mx=p8wmx
                po8my=p8wmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p8wmx=convertx(p8wmx)
                p8wmy=converty(p8wmy)
                tg=Pawn8w.position(coords,coords2,p8wmx,p8wmy,"p8w")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hb=0
                    white_check=False
                    moves28=moves28+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p8wmy=(yposition)*60
                    p8wmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
        if moves==1:
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro2bmx=r2bmx
                    ro2bmy=r2bmy
                    vc="r2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r2bmx,r2bmy=pygame.mouse.get_pos()
                    if r2bmx>xposition and r2bmx<xposition2 and r2bmy>yposition and r2bmy<yposition2:
                        piece="rook2b"
                        Rook2b=rookw(coords,coords2,r2bmx,r2bmy,"r2b","w")
                        Rook2b.possible_moves(coords,coords2,"w")
                    else:
                        r2bmx=ro2bmx
                        r2bmy=ro2bmy  
            if piece=="rook2b":
                r2bmx,r2bmy=pygame.mouse.get_pos()
                g="r2b"
                r2bmx,r2bmy=pygame.mouse.get_pos()
                ro2bmx=r2bmx
                ro2bmy=r2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r2bmx=convertx(r2bmx)
                r2bmy=converty(r2bmy)
                tg=Rook2b.position(coords,coords2,r2bmx,r2bmy,"r2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves2r2b=1
                    hw=0
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r2bmy=(yposition)*60
                    r2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro3bmx=r3bmx
                    ro3bmy=r3bmy
                    vc="r3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    r3bmx,r3bmy=pygame.mouse.get_pos()
                    if r3bmx>xposition and r3bmx<xposition2 and r3bmy>yposition and r3bmy<yposition2:
                        piece="rook3b"
                        Rook3b=rookw(coords,coords2,r3bmx,r3bmy,"r3b","w")
                        Rook3b.possible_moves(coords,coords2,"w")
                    else:
                        r3bmx=ro3bmx
                        r3bmy=ro3bmy  
            if piece=="rook3b":
                r3bmx,r3bmy=pygame.mouse.get_pos()
                g="r3b"
                r3bmx,r3bmy=pygame.mouse.get_pos()
                ro3bmx=r3bmx
                ro3bmy=r3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r3bmx=convertx(r3bmx)
                r3bmy=converty(r3bmy)
                tg=Rook3b.position(coords,coords2,r3bmx,r3bmy,"r3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves2r3b=1
                    hw=0
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r3bmy=(yposition)*60
                    r3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro4bmx=r4bmx
                    ro4bmy=r4bmy
                    vc="r4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    r4bmx,r4bmy=pygame.mouse.get_pos()
                    if r4bmx>xposition and r4bmx<xposition2 and r4bmy>yposition and r4bmy<yposition2:
                        piece="rook4b"
                        Rook4b=rookw(coords,coords2,r4bmx,r4bmy,"r4b","w")
                        Rook4b.possible_moves(coords,coords2,"w")
                    else:
                        r4bmx=ro4bmx
                        r4bmy=ro4bmy  
            if piece=="rook4b":
                r4bmx,r4bmy=pygame.mouse.get_pos()
                g="r4b"
                r4bmx,r4bmy=pygame.mouse.get_pos()
                ro4bmx=r4bmx
                ro4bmy=r4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r4bmx=convertx(r4bmx)
                r4bmy=converty(r4bmy)
                tg=Rook4b.position(coords,coords2,r4bmx,r4bmy,"r4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves2r4b=1
                    hw=0
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r4bmy=(yposition)*60
                    r4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro5bmx=r5bmx
                    ro5bmy=r5bmy
                    vc="r5b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    r5bmx,r5bmy=pygame.mouse.get_pos()
                    if r5bmx>xposition and r5bmx<xposition2 and r5bmy>yposition and r5bmy<yposition2:
                        piece="rook5b"
                        Rook5b=rookw(coords,coords2,r5bmx,r5bmy,"r5b","w")
                        Rook5b.possible_moves(coords,coords2,"w")
                    else:
                        r5bmx=ro5bmx
                        r5bmy=ro5bmy  
            if piece=="rook5b":
                r5bmx,r5bmy=pygame.mouse.get_pos()
                g="r5b"
                r5bmx,r5bmy=pygame.mouse.get_pos()
                ro5bmx=r5bmx
                ro5bmy=r5bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r5bmx=convertx(r5bmx)
                r5bmy=converty(r5bmy)
                tg=Rook5b.position(coords,coords2,r5bmx,r5bmy,"r5b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves2r5b=1
                    hw=0
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r5bmy=(yposition)*60
                    r5bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""

########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno2bmx=kn2bmx
                    kno2bmy=kn2bmy
                    vc="kn2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn2bmx,kn2bmy=pygame.mouse.get_pos()
                    if kn2bmx>xposition and kn2bmx<xposition2 and kn2bmy>yposition and kn2bmy<yposition2:
                        piece="knight2b"
                        Knight2b=knightw(coords,coords2,kn2bmx,kn2bmy,"kn2b","w")
                        Knight2b.possible_moves(coords,coords2,"w")
                    else:
                        kn2bmx=kno2bmx
                        kn2bmy=kno2bmy  
            if piece=="knight2b":
                kn2bmx,kn2bmy=pygame.mouse.get_pos()
                g="kn2b"
                kn2bmx,kn2bmy=pygame.mouse.get_pos()
                kno2bmx=kn2bmx
                kno2bmy=kn2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn2bmx=convertx(kn2bmx)
                kn2bmy=converty(kn2bmy)
                tg=Knight2b.position(coords,coords2,kn2bmx,kn2bmy,"kn2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    hw=0
                    black_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn2bmy=(yposition)*60
                    kn2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno3bmx=kn3bmx
                    kno3bmy=kn3bmy
                    vc="kn3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn3bmx,kn3bmy=pygame.mouse.get_pos()
                    if kn3bmx>xposition and kn3bmx<xposition2 and kn3bmy>yposition and kn3bmy<yposition2:
                        piece="knight3b"
                        Knight3b=knightw(coords,coords2,kn3bmx,kn3bmy,"kn3b","w")
                        Knight3b.possible_moves(coords,coords2,"w")
                    else:
                        kn3bmx=kno3bmx
                        kn3bmy=kno3bmy  
            if piece=="knight3b":
                kn3bmx,kn3bmy=pygame.mouse.get_pos()
                g="kn3b"
                kn3bmx,kn3bmy=pygame.mouse.get_pos()
                kno3bmx=kn3bmx
                kno3bmy=kn3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn3bmx=convertx(kn3bmx)
                kn3bmy=converty(kn3bmy)
                tg=Knight3b.position(coords,coords2,kn3bmx,kn3bmy,"kn3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    hw=0
                    black_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn3bmy=(yposition)*60
                    kn3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno4bmx=kn4bmx
                    kno4bmy=kn4bmy
                    vc="kn4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn4bmx,kn4bmy=pygame.mouse.get_pos()
                    if kn4bmx>xposition and kn4bmx<xposition2 and kn4bmy>yposition and kn4bmy<yposition2:
                        piece="knight4b"
                        Knight4b=knightw(coords,coords2,kn4bmx,kn4bmy,"kn4b","w")
                        Knight4b.possible_moves(coords,coords2,"w")
                    else:
                        kn4bmx=kno4bmx
                        kn4bmy=kno4bmy  
            if piece=="knight4b":
                kn4bmx,kn4bmy=pygame.mouse.get_pos()
                g="kn4b"
                kn4bmx,kn4bmy=pygame.mouse.get_pos()
                kno4bmx=kn4bmx
                kno4bmy=kn4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn4bmx=convertx(kn4bmx)
                kn4bmy=converty(kn4bmy)
                tg=Knight4b.position(coords,coords2,kn4bmx,kn4bmy,"kn4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    hw=0
                    black_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn4bmy=(yposition)*60
                    kn4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno5bmx=kn5bmx
                    kno5bmy=kn5bmy
                    vc="kn5b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn5bmx,kn5bmy=pygame.mouse.get_pos()
                    if kn5bmx>xposition and kn5bmx<xposition2 and kn5bmy>yposition and kn5bmy<yposition2:
                        piece="knight5b"
                        Knight5b=knightw(coords,coords2,kn5bmx,kn5bmy,"kn5b","w")
                        Knight5b.possible_moves(coords,coords2,"w")
                    else:
                        kn5bmx=kno5bmx
                        kn5bmy=kno5bmy  
            if piece=="knight5b":
                kn5bmx,kn5bmy=pygame.mouse.get_pos()
                g="kn5b"
                kn5bmx,kn5bmy=pygame.mouse.get_pos()
                kno5bmx=kn5bmx
                kno5bmy=kn5bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn5bmx=convertx(kn5bmx)
                kn5bmy=converty(kn5bmy)
                tg=Knight5b.position(coords,coords2,kn5bmx,kn5bmy,"kn5b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    hw=0
                    black_check=False
                    moves=moves+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn5bmy=(yposition)*60
                    kn5bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    kno1bmx=kn1bmx
                    kno1bmy=kn1bmy
                    vc="kn1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    kn1bmx,kn1bmy=pygame.mouse.get_pos()
                    if kn1bmx>xposition and kn1bmx<xposition2 and kn1bmy>yposition and kn1bmy<yposition2:
                        piece="knight1b"
                        Knight1b=knightw(coords,coords2,kn1bmx,kn1bmy,"kn1b","w")
                        Knight1b.possible_moves(coords,coords2,"w")
                    else:
                        kn1bmx=kno1bmx
                        kn1bmy=kno1bmy  
            if piece=="knight1b":
                kn1bmx,kn1bmy=pygame.mouse.get_pos()
                g="kn1b"
                kn1bmx,kn1bmy=pygame.mouse.get_pos()
                kno1bmx=kn1bmx
                kno1bmy=kn1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                kn1bmx=convertx(kn1bmx)
                kn1bmy=converty(kn1bmy)
                tg=Knight1b.position(coords,coords2,kn1bmx,kn1bmy,"kn1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    kn1bmy=(yposition)*60
                    kn1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
########################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ro1bmx=r1bmx
                    ro1bmy=r1bmy
                    vc="r1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    r1bmx,r1bmy=pygame.mouse.get_pos()
                    if r1bmx>xposition and r1bmx<xposition2 and r1bmy>yposition and r1bmy<yposition2:
                        piece="rook1b"
                        Rook1b=rookw(coords,coords2,r1bmx,r1bmy,"r1b","w")
                        Rook1b.possible_moves(coords,coords2,"w")
                    else:
                        r1bmx=ro1bmx
                        r1bmy=ro1bmy  
            if piece=="rook1b":
                r1bmx,r1bmy=pygame.mouse.get_pos()
                g="r1b"
                r1bmx,r1bmy=pygame.mouse.get_pos()
                ro1bmx=r1bmx
                ro1bmy=r1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                r1bmx=convertx(r1bmx)
                r1bmy=converty(r1bmy)
                tg=Rook1b.position(coords,coords2,r1bmx,r1bmy,"r1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves2r1b=1
                    coords=[]
                    hw=0
                    black_check=False
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    r1bmy=(yposition)*60
                    r1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo2bmx=b2bmx
                    bo2bmy=b2bmy
                    vc="b2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    b2bmx,b2bmy=pygame.mouse.get_pos()
                    if b2bmx>xposition and b2bmx<xposition2 and b2bmy>yposition and b2bmy<yposition2:
                        piece="bishop2b"
                        Bishop2b=bishopw(coords,coords2,b2wmx,b2wmy,"b2b","w")
                        Bishop2b.possible_moves(coords,coords2,"w")
                    else:
                        b2bmx=bo2bmx
                        b2bmy=bo2bmy  
            if piece=="bishop2b":
                b2bmx,b2bmy=pygame.mouse.get_pos()
                g="b2b"
                b2bmx,b2bmy=pygame.mouse.get_pos()
                bo2bmx=b2bmx
                bo2bmy=b2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b2bmx=convertx(b2bmx)
                b2bmy=converty(b2bmy)
                tg=Bishop2b.position(coords,coords2,b2bmx,b2bmy,"b2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b2bmy=(yposition)*60
                    b2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#######################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo3bmx=b3bmx
                    bo3bmy=b3bmy
                    vc="b3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    b3bmx,b3bmy=pygame.mouse.get_pos()
                    if b3bmx>xposition and b3bmx<xposition2 and b3bmy>yposition and b3bmy<yposition2:
                        piece="bishop3b"
                        Bishop3b=bishopw(coords,coords2,b3wmx,b3wmy,"b3b","w")
                        Bishop3b.possible_moves(coords,coords2,"w")
                    else:
                        b3bmx=bo3bmx
                        b3bmy=bo3bmy  
            if piece=="bishop3b":
                b3bmx,b3bmy=pygame.mouse.get_pos()
                g="b3b"
                b3bmx,b3bmy=pygame.mouse.get_pos()
                bo3bmx=b3bmx
                bo3bmy=b3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b3bmx=convertx(b3bmx)
                b3bmy=converty(b3bmy)
                tg=Bishop3b.position(coords,coords2,b3bmx,b3bmy,"b3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b3bmy=(yposition)*60
                    b3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#######################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo4bmx=b4bmx
                    bo4bmy=b4bmy
                    vc="b4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b4bmx,b4bmy=pygame.mouse.get_pos()
                    if b4bmx>xposition and b4bmx<xposition2 and b4bmy>yposition and b4bmy<yposition2:
                        piece="bishop4b"
                        Bishop4b=bishopw(coords,coords2,b4wmx,b4wmy,"b4b","w")
                        Bishop4b.possible_moves(coords,coords2,"w")
                    else:
                        b4bmx=bo4bmx
                        b4bmy=bo4bmy  
            if piece=="bishop4b":
                b4bmx,b4bmy=pygame.mouse.get_pos()
                g="b4b"
                b4bmx,b4bmy=pygame.mouse.get_pos()
                bo4bmx=b4bmx
                bo4bmy=b4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b4bmx=convertx(b4bmx)
                b4bmy=converty(b4bmy)
                tg=Bishop4b.position(coords,coords2,b4bmx,b4bmy,"b4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b4bmy=(yposition)*60
                    b4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
###############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo5bmx=b5bmx
                    bo5bmy=b5bmy
                    vc="b5b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b5bmx,b5bmy=pygame.mouse.get_pos()
                    if b5bmx>xposition and b5bmx<xposition2 and b5bmy>yposition and b5bmy<yposition2:
                        piece="bishop5b"
                        Bishop5b=bishopw(coords,coords2,b5wmx,b5wmy,"b5b","w")
                        Bishop5b.possible_moves(coords,coords2,"w")
                    else:
                        b5bmx=bo5bmx
                        b5bmy=bo5bmy  
            if piece=="bishop5b":
                b5bmx,b5bmy=pygame.mouse.get_pos()
                g="b5b"
                b5bmx,b5bmy=pygame.mouse.get_pos()
                bo5bmx=b5bmx
                bo5bmy=b5bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b5bmx=convertx(b5bmx)
                b5bmy=converty(b5bmy)
                tg=Bishop5b.position(coords,coords2,b5bmx,b5bmy,"b5b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b5bmy=(yposition)*60
                    b5bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#######################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    bo1bmx=b1bmx
                    bo1bmy=b1bmy
                    vc="b1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    b1bmx,b1bmy=pygame.mouse.get_pos()
                    if b1bmx>xposition and b1bmx<xposition2 and b1bmy>yposition and b1bmy<yposition2:
                        piece="bishop1b"
                        Bishop1b=bishopw(coords,coords2,b1bmx,b1bmy,"b1b","w")
                        Bishop1b.possible_moves(coords,coords2,"w")
                    else:
                        b1bmx=bo1bmx
                        b1bmy=bo1bmy  
            if piece=="bishop1b":
                b1bmx,b1bmy=pygame.mouse.get_pos()
                g="b1b"
                b1bmx,b1bmy=pygame.mouse.get_pos()
                bo1bmx=b1bmx
                bo1bmy=b1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                b1bmx=convertx(b1bmx)
                b1bmy=converty(b1bmy)
                tg=Bishop1b.position(coords,coords2,b1bmx,b1bmy,"b1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    b1bmy=(yposition)*60
                    b1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo1bmx=q1bmx
                    qo1bmy=q1bmy
                    vc="q1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q1bmx,q1bmy=pygame.mouse.get_pos()
                    if q1bmx>xposition and q1bmx<xposition2 and q1bmy>yposition and q1bmy<yposition2:
                        piece="queen1b"
                        Queen1b=queenw(coords,coords2,q1bmx,q1bmy,"q1b","w")
                        Queen1b.possible_moves(coords,coords2,"w")
                    else:
                        q1bmx=qo1bmx
                        q1bmy=qo1bmy  
            if piece=="queen1b":
                q1bmx,q1bmy=pygame.mouse.get_pos()
                g="q1b"
                q1bmx,q1bmy=pygame.mouse.get_pos()
                qo1bmx=q1bmx
                qo1bmy=q1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q1bmx=convertx(q1bmx)
                q1bmy=converty(q1bmy)
                tg=Queen1b.position(coords,coords2,q1bmx,q1bmy,"q1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q1bmy=(yposition)*60
                    q1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo2bmx=q2bmx
                    qo2bmy=q2bmy
                    vc="q2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    q2bmx,q2bmy=pygame.mouse.get_pos()
                    if q2bmx>xposition and q2bmx<xposition2 and q2bmy>yposition and q2bmy<yposition2:
                        piece="queen2b"
                        Queen2b=queenw(coords,coords2,q2bmx,q2bmy,"q2b","w")
                        Queen2b.possible_moves(coords,coords2,"w")
                    else:
                        q2bmx=qo2bmx
                        q2bmy=qo2bmy  
            if piece=="queen2b":
                q2bmx,q2bmy=pygame.mouse.get_pos()
                g="q2b"
                q2bmx,q2bmy=pygame.mouse.get_pos()
                qo2bmx=q2bmx
                qo2bmy=q2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q2bmx=convertx(q2bmx)
                q2bmy=converty(q2bmy)
                tg=Queen2b.position(coords,coords2,q2bmx,q2bmy,"q2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q2bmy=(yposition)*60
                    q2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo3bmx=q3bmx
                    qo3bmy=q3bmy
                    vc="q3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    q3bmx,q3bmy=pygame.mouse.get_pos()
                    if q3bmx>xposition and q3bmx<xposition2 and q3bmy>yposition and q3bmy<yposition2:
                        piece="queen3b"
                        Queen3b=queenw(coords,coords2,q3bmx,q3bmy,"q3b","w")
                        Queen3b.possible_moves(coords,coords2,"w")
                    else:
                        q3bmx=qo3bmx
                        q3bmy=qo3bmy  
            if piece=="queen3b":
                q3bmx,q3bmy=pygame.mouse.get_pos()
                g="q3b"
                q3bmx,q3bmy=pygame.mouse.get_pos()
                qo3bmx=q3bmx
                qo3bmy=q3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q3bmx=convertx(q3bmx)
                q3bmy=converty(q3bmy)
                tg=Queen3b.position(coords,coords2,q3bmx,q3bmy,"q3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q3bmy=(yposition)*60
                    q3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    qo4bmx=q4bmx
                    qo4bmy=q4bmy
                    vc="q4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    q4bmx,q4bmy=pygame.mouse.get_pos()
                    if q4bmx>xposition and q4bmx<xposition2 and q4bmy>yposition and q4bmy<yposition2:
                        piece="queen4b"
                        Queen4b=queenw(coords,coords2,q4bmx,q4bmy,"q4b","w")
                        Queen4b.possible_moves(coords,coords2,"w")
                    else:
                        q4bmx=qo4bmx
                        q4bmy=qo4bmy  
            if piece=="queen4b":
                q4bmx,q4bmy=pygame.mouse.get_pos()
                g="q4b"
                q4bmx,q4bmy=pygame.mouse.get_pos()
                qo4bmx=q4bmx
                qo4bmy=q4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                q4bmx=convertx(q4bmx)
                q4bmy=converty(q4bmy)
                tg=Queen4b.position(coords,coords2,q4bmx,q4bmy,"q4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    q4bmy=(yposition)*60
                    q4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    ko1bmx=k1bmx
                    ko1bmy=k1bmy
                    vc="k1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    k1bmx,k1bmy=pygame.mouse.get_pos()
                    if k1bmx>xposition and k1bmx<xposition2 and k1bmy>yposition and k1bmy<yposition2:
                        piece="king1b"
                        King1b=kingw(coords,coords2,kn1wmx,kn1wmy,"k1b","w")
                        King1b.possible_moves(coords,coords2,"w")
                    else:
                        k1bmx=ko1bmx
                        k1bmy=ko1bmy  
            if piece=="king1b":
                k1bmx,k1bmy=pygame.mouse.get_pos()
                g="k1b"
                k1bmx,k1bmy=pygame.mouse.get_pos()
                ko1bmx=k1bmx
                ko1bmy=k1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                k1bmx=convertx(k1bmx)
                k1bmy=converty(k1bmy)
                tg=King1b.position(coords,coords2,k1bmx,k1bmy,"k1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves2kb=1
                    yposition=list_searchy(Board,"r1b")
                    xposition=list_searchx(Board,"r1b")
                    r1bmx=xposition*60
                    r1bmy=yposition*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    yposition=list_searchy(Board,"r2b")
                    xposition=list_searchx(Board,"r2b")
                    r2bmx=xposition*60
                    r2bmy=yposition*60
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    k1bmy=(yposition)*60
                    k1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
###################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po1bmx=p1bmx
                    po1bmy=p1bmy
                    vc="p1b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p1bmx,p1bmy=pygame.mouse.get_pos()
                    if p1bmx>xposition and p1bmx<xposition2 and p1bmy>yposition and p1bmy<yposition2:
                        piece="pawn1b"
                        Pawn1b=pawnb(coords,coords2,p1bmx,p1bmy,"p1b","w",moves21b)
                        Pawn1b.possible_moves(coords,coords2,"w",moves21b)
                    else:
                        p1bmx=po1bmx
                        p1bmy=po1bmy  
            if piece=="pawn1b":
                p1bmx,p1bmy=pygame.mouse.get_pos()
                g="p1b"
                p1bmx,p1bmy=pygame.mouse.get_pos()
                po1bmx=p1bmx
                po1bmy=p1bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p1bmx=convertx(p1bmx)
                p1bmy=converty(p1bmy)
                tg=Pawn1b.position(coords,coords2,p1bmx,p1bmy,"p1b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    black_check=False
                    hw=0
                    moves21b=moves21b+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p1bmy=(yposition)*60
                    p1bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#############################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po2bmx=p2bmx
                    po2bmy=p2bmy
                    vc="p2b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    p2bmx,p2bmy=pygame.mouse.get_pos()
                    if p2bmx>xposition and p2bmx<xposition2 and p2bmy>yposition and p2bmy<yposition2:
                        piece="pawn2b"
                        Pawn2b=pawnb(coords,coords2,p2bmx,p2bmy,"p2b","w",moves22b)
                        Pawn2b.possible_moves(coords,coords2,"w",moves22b)
                    else:
                        p2bmx=po2bmx
                        p2bmy=po2bmy  
            if piece=="pawn2b":
                p2bmx,p2bmy=pygame.mouse.get_pos()
                g="p2b"
                p2bmx,p2bmy=pygame.mouse.get_pos()
                po2bmx=p2bmx
                po2bmy=p2bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p2bmx=convertx(p2bmx)
                p2bmy=converty(p2bmy)
                tg=Pawn2b.position(coords,coords2,p1bmx,p1bmy,"p2b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    moves22b=moves22b+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p2bmy=(yposition)*60
                    p2bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
#####################################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po3bmx=p3bmx
                    po3bmy=p3bmy
                    vc="p3b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p3bmx,p3bmy=pygame.mouse.get_pos()
                    if p3bmx>xposition and p3bmx<xposition2 and p3bmy>yposition and p3bmy<yposition2:
                        piece="pawn3b"
                        Pawn3b=pawnb(coords,coords2,p3bmx,p3bmy,"p3b","w",moves23b)
                        Pawn3b.possible_moves(coords,coords2,"w",moves23b)
                    else:
                        p3bmx=po3bmx
                        p3bmy=po3bmy  
            if piece=="pawn3b":
                p3bmx,p3bmy=pygame.mouse.get_pos()
                g="p3b"
                p3bmx,p3bmy=pygame.mouse.get_pos()
                po3bmx=p3bmx
                po3bmy=p3bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p3bmx=convertx(p3bmx)
                p3bmy=converty(p3bmy)
                tg=Pawn3b.position(coords,coords2,p3bmx,p3bmy,"p3b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves23b=moves23b+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p3bmy=(yposition)*60
                    p3bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po4bmx=p4bmx
                    po4bmy=p4bmy
                    vc="p4b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60

                    p4bmx,p4bmy=pygame.mouse.get_pos()
                    if p4bmx>xposition and p4bmx<xposition2 and p4bmy>yposition and p4bmy<yposition2:
                        piece="pawn4b"
                        Pawn4b=pawnb(coords,coords2,p4bmx,p4bmy,"p4b","w",moves24b)
                        Pawn4b.possible_moves(coords,coords2,"w",moves24b)
                    else:
                        p4bmx=po4bmx
                        p4bmy=po4bmy  
            if piece=="pawn4b":
                p4bmx,p4bmy=pygame.mouse.get_pos()
                g="p4b"
                p4bmx,p4bmy=pygame.mouse.get_pos()
                po4bmx=p4bmx
                po4bmy=p4bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p4bmx=convertx(p4bmx)
                p4bmy=converty(p4bmy)
                tg=Pawn4b.position(coords,coords2,p4bmx,p4bmy,"p4b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    black_check=False
                    moves24b=moves24b+1
                    hw=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p4bmy=(yposition)*60
                    p4bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po5bmx=p5bmx
                    po5bmy=p5bmy
                    vc="p5b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    p5bmx,p5bmy=pygame.mouse.get_pos()
                    if p5bmx>xposition and p5bmx<xposition2 and p5bmy>yposition and p5bmy<yposition2:
                        piece="pawn5b"
                        Pawn5b=pawnb(coords,coords2,p5bmx,p5bmy,"p5b","w",moves25b)
                        Pawn5b.possible_moves(coords,coords2,"w",moves25b)
                    else:
                        p5bmx=po5bmx
                        p5bmy=po5bmy  
            if piece=="pawn5b":
                p5bmx,p5bmy=pygame.mouse.get_pos()
                g="p5b"
                p5bmx,p5bmy=pygame.mouse.get_pos()
                po5bmx=p5bmx
                po5bmy=p5bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p5bmx=convertx(p5bmx)
                p5bmy=converty(p5bmy)
                tg=Pawn5b.position(coords,coords2,p5bmx,p5bmy,"p5b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    moves25b=moves25b+1
                    coords=[]
                    black_check=False
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p5bmy=(yposition)*60
                    p5bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po6bmx=p6bmx
                    po6bmy=p6bmy
                    vc="p6b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    p6bmx,p6bmy=pygame.mouse.get_pos()
                    if p6bmx>xposition and p6bmx<xposition2 and p6bmy>yposition and p6bmy<yposition2:
                        piece="pawn6b"
                        Pawn6b=pawnb(coords,coords2,p6bmx,p6bmy,"p6b","w",moves26b)
                        Pawn6b.possible_moves(coords,coords2,"w",moves26b)
                    else:
                        p6bmx=po6bmx
                        p6bmy=po6bmy  
            if piece=="pawn6b":
                p6bmx,p6bmy=pygame.mouse.get_pos()
                g="p6b"
                p6bmx,p6bmy=pygame.mouse.get_pos()
                po6bmx=p6bmx
                po6bmy=p6bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p6bmx=convertx(p6bmx)
                p6bmy=converty(p6bmy)
                tg=Pawn6b.position(coords,coords2,p6bmx,p6bmy,"p6b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    moves26b=moves26b+1
                    hw=0
                    black_check=False
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p6bmy=(yposition)*60
                    p6bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po7bmx=p7bmx
                    po7bmy=p7bmy
                    vc="p7b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    p7bmx,p7bmy=pygame.mouse.get_pos()
                    if p7bmx>xposition and p7bmx<xposition2 and p7bmy>yposition and p7bmy<yposition2:
                        piece="pawn7b"
                        Pawn7b=pawnb(coords,coords2,p7bmx,p7bmy,"p7b","w",moves27b)
                        Pawn7b.possible_moves(coords,coords2,"w",moves27b)
                    else:
                        p7bmx=po7bmx
                        p7bmy=po7bmy  
            if piece=="pawn7b":
                p7bmx,p7bmy=pygame.mouse.get_pos()
                g="p7b"
                p7bmx,p7bmy=pygame.mouse.get_pos()
                po7bmx=p7bmx
                po7bmy=p7bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p7bmx=convertx(p7bmx)
                p7bmy=converty(p7bmy)
                tg=Pawn7b.position(coords,coords2,p7bmx,p7bmy,"p7b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    hw=0
                    black_check=False
                    moves27b=moves27b+1
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p7bmy=(yposition)*60
                    p7bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
            if event3.type==pygame.MOUSEBUTTONDOWN and rfv!=1:
                if piece=="":
                    po8bmx=p8bmx
                    po8bmy=p8bmy
                    vc="p8b"
                    yposition=list_searchy(Board,vc)
                    xposition=list_searchx(Board,vc)
                    yposition=(yposition+1)*60-60
                    xposition=(xposition+1)*60-60
                    yposition2=yposition+60
                    xposition2=xposition+60
                    p8bmx,p8bmy=pygame.mouse.get_pos()
                    if p8bmx>xposition and p8bmx<xposition2 and p8bmy>yposition and p8bmy<yposition2:
                        piece="pawn8b"
                        Pawn8b=pawnb(coords,coords2,p8bmx,p8bmy,"p8b","w",moves28b)
                        Pawn8b.possible_moves(coords,coords2,"w",moves28b)
                    else:
                        p8bmx=po8bmx
                        p8bmy=po8bmy  
            if piece=="pawn8b":
                p8bmx,p8bmy=pygame.mouse.get_pos()
                g="p8b"
                p8bmx,p8bmy=pygame.mouse.get_pos()
                po8bmx=p8bmx
                po8bmy=p8bmy
                board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                p8bmx=convertx(p8bmx)
                p8bmy=converty(p8bmy)
                tg=Pawn8b.position(coords,coords2,p8bmx,p8bmy,"p8b")
                if tg==1:
                    piece=""
                    coords=[]
                    coords2=[]
                    rfv=1
                elif tg==2:
                    piece=""
                    moves=moves+1
                    black_check=False
                    moves28b=moves28b+1
                    hw=0
                    coords=[]
                    coords2=[]
                elif tg==3:
                    yposition=list_searchy(Board,g)
                    xposition=list_searchx(Board,g)
                    p8bmy=(yposition)*60
                    p8bmx=(xposition)*60
                    board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)
                    coords=[]
                    coords2=[]
                    piece=""
####################################################################
        Pawn1b_status=Status("p1b",pawn_black1_status)
        Pawn1b_status.Status2("p1b",pawn_black1_status)
        pawn_black1_status=Pawn1b_status.pawn_black1_status

        Pawn2b_status=Status("p2b",pawn_black2_status)
        Pawn2b_status.Status2("p2b",pawn_black2_status)
        pawn_black2_status=Pawn2b_status.pawn_black1_status
        
        Pawn3b_status=Status("p3b",pawn_black3_status)
        Pawn3b_status.Status2("p3b",pawn_black3_status)
        pawn_black3_status=Pawn3b_status.pawn_black1_status

        Pawn4b_status=Status("p4b",pawn_black4_status)
        Pawn4b_status.Status2("p4b",pawn_black4_status)
        pawn_black4_status=Pawn4b_status.pawn_black1_status

        Pawn5b_status=Status("p5b",pawn_black5_status)
        Pawn5b_status.Status2("p5b",pawn_black5_status)
        pawn_black5_status=Pawn5b_status.pawn_black1_status

        Pawn6b_status=Status("p6b",pawn_black6_status)
        Pawn6b_status.Status2("p6b",pawn_black6_status)
        pawn_black6_status=Pawn6b_status.pawn_black1_status

        Pawn7b_status=Status("p7b",pawn_black7_status)
        Pawn7b_status.Status2("p7b",pawn_black7_status)
        pawn_black7_status=Pawn7b_status.pawn_black1_status

        Pawn8b_status=Status("p8b",pawn_black8_status)
        Pawn8b_status.Status2("p8b",pawn_black8_status)
        pawn_black8_status=Pawn8b_status.pawn_black1_status

        
        Pawn1w_status=Status("p1w",pawn_white1_status)
        Pawn1w_status.Status2("p1w",pawn_white1_status)
        pawn_white1_status=Pawn1w_status.pawn_black1_status

        Pawn2w_status=Status("p2w",pawn_white2_status)
        Pawn2w_status.Status2("p2w",pawn_white2_status)
        pawn_white2_status=Pawn2w_status.pawn_black1_status
        
        Pawn3w_status=Status("p3w",pawn_white3_status)
        Pawn3w_status.Status2("p3w",pawn_white3_status)
        pawn_white3_status=Pawn3w_status.pawn_black1_status

        Pawn4w_status=Status("p4w",pawn_white4_status)
        Pawn4w_status.Status2("p4w",pawn_white4_status)
        pawn_white4_status=Pawn4w_status.pawn_black1_status

        Pawn5w_status=Status("p5w",pawn_white5_status)
        Pawn5w_status.Status2("p5w",pawn_white5_status)
        pawn_white5_status=Pawn5w_status.pawn_black1_status

        Pawn6w_status=Status("p6w",pawn_white6_status)
        Pawn6w_status.Status2("p6w",pawn_white6_status)
        pawn_white6_status=Pawn6w_status.pawn_black1_status

        Pawn7w_status=Status("p7w",pawn_white7_status)
        Pawn7w_status.Status2("p7w",pawn_white7_status)
        pawn_white7_status=Pawn7w_status.pawn_black1_status

        Pawn8w_status=Status("p8w",pawn_white8_status)
        Pawn8w_status.Status2("p8w",pawn_white8_status)
        pawn_white8_status=Pawn8w_status.pawn_black1_status

        rook1w_status=Status("r1w",rook_white1_status)
        rook1w_status.Status2("r1w",rook_white1_status)
        rook_white1_status=rook1w_status.pawn_black1_status

        rook2w_status=Status("r2w",rook_white2_status)
        rook2w_status.Status2("r2w",rook_white2_status)
        rook_white2_status=rook2w_status.pawn_black1_status
        
        rook3w_status=Status("r3w",rook_white3_status)
        rook3w_status.Status2("r3w",rook_white3_status)
        rook_white3_status=rook3w_status.pawn_black1_status

        rook4w_status=Status("r4w",rook_white4_status)
        rook4w_status.Status2("r4w",rook_white4_status)
        rook_white4_status=rook4w_status.pawn_black1_status

        rook5w_status=Status("r5w",rook_white5_status)
        rook5w_status.Status2("r5w",rook_white5_status)
        rook_white5_status=rook5w_status.pawn_black1_status


        knight1w_status=Status("kn1w",knight_white1_status)
        knight1w_status.Status2("kn1w",knight_white1_status)
        knight_white1_status=knight1w_status.pawn_black1_status

        knight2w_status=Status("kn2w",knight_white2_status)
        knight2w_status.Status2("kn2w",knight_white2_status)
        knight_white2_status=knight2w_status.pawn_black1_status
        
        knight3w_status=Status("kn3w",knight_white3_status)
        knight3w_status.Status2("kn3w",knight_white3_status)
        knight_white3_status=knight3w_status.pawn_black1_status

        knight4w_status=Status("kn4w",knight_white4_status)
        knight4w_status.Status2("kn4w",knight_white4_status)
        knight_white4_status=knight4w_status.pawn_black1_status

        knight5w_status=Status("kn5w",knight_white5_status)
        knight5w_status.Status2("kn5w",knight_white5_status)
        knight_white5_status=knight5w_status.pawn_black1_status


        bishop1w_status=Status("b1w",bishop_white1_status)
        bishop1w_status.Status2("b1w",bishop_white1_status)
        bishop_white1_status=bishop1w_status.pawn_black1_status

        bishop2w_status=Status("b2w",bishop_white2_status)
        bishop2w_status.Status2("b2w",bishop_white2_status)
        bishop_white2_status=bishop2w_status.pawn_black1_status
        
        bishop3w_status=Status("b3w",bishop_white3_status)
        bishop3w_status.Status2("b3w",bishop_white3_status)
        bishop_white3_status=bishop3w_status.pawn_black1_status

        bishop4w_status=Status("b4w",bishop_white4_status)
        bishop4w_status.Status2("b4w",bishop_white4_status)
        bishop_white4_status=bishop4w_status.pawn_black1_status

        bishop5w_status=Status("b5w",bishop_white5_status)
        bishop5w_status.Status2("b5w",bishop_white5_status)
        bishop_white5_status=bishop5w_status.pawn_black1_status

        queen1w_status=Status("q1w",queen_white_status)
        queen1w_status.Status2("q1w",queen_white_status)
        queen_white_status=queen1w_status.pawn_black1_status

        queen2w_status=Status("q2w",queen_white2_status)
        queen2w_status.Status2("q2w",queen_white2_status)
        queen_white2_status=queen2w_status.pawn_black1_status

        queen3w_status=Status("q3w",queen_white3_status)
        queen3w_status.Status2("q3w",queen_white3_status)
        queen_white3_status=queen3w_status.pawn_black1_status

        queen4w_status=Status("q4w",queen_white4_status)
        queen4w_status.Status2("q4w",queen_white4_status)
        queen_white4_status=queen4w_status.pawn_black1_status


        rook1b_status=Status("r1b",rook_black1_status)
        rook1b_status.Status2("r1b",rook_black1_status)
        rook_black1_status=rook1b_status.pawn_black1_status

        rook2b_status=Status("r2b",rook_black2_status)
        rook2b_status.Status2("r2b",rook_black2_status)
        rook_black2_status=rook2b_status.pawn_black1_status
        
        rook3b_status=Status("r3b",rook_black3_status)
        rook3b_status.Status2("r3b",rook_black3_status)
        rook_black3_status=rook3b_status.pawn_black1_status

        rook4b_status=Status("r4b",rook_black4_status)
        rook4b_status.Status2("r4b",rook_black4_status)
        rook_black4_status=rook4b_status.pawn_black1_status

        rook5b_status=Status("r5b",rook_black5_status)
        rook5b_status.Status2("r5b",rook_black5_status)
        rook_black5_status=rook5b_status.pawn_black1_status


        knight1b_status=Status("kn1b",knight_black1_status)
        knight1b_status.Status2("kn1b",knight_black1_status)
        knight_black1_status=knight1b_status.pawn_black1_status

        knight2b_status=Status("kn2b",knight_black2_status)
        knight2b_status.Status2("kn2b",knight_black2_status)
        knight_black2_status=knight2b_status.pawn_black1_status
        
        knight3b_status=Status("kn3b",knight_black3_status)
        knight3b_status.Status2("kn3b",knight_black3_status)
        knight_black3_status=knight3b_status.pawn_black1_status

        knight4b_status=Status("kn4b",knight_black4_status)
        knight4b_status.Status2("kn4b",knight_black4_status)
        knight_black4_status=knight4b_status.pawn_black1_status

        knight5b_status=Status("kn5b",knight_black5_status)
        knight5b_status.Status2("kn5b",knight_black5_status)
        knight_black5_status=knight5b_status.pawn_black1_status


        bishop1b_status=Status("b1b",bishop_black1_status)
        bishop1b_status.Status2("b1b",bishop_black1_status)
        bishop_black1_status=bishop1b_status.pawn_black1_status

        bishop2b_status=Status("b2b",bishop_black2_status)
        bishop2b_status.Status2("b2b",bishop_black2_status)
        bishop_black2_status=bishop2b_status.pawn_black1_status
        
        bishop3b_status=Status("b3b",bishop_black3_status)
        bishop3b_status.Status2("b3b",bishop_black3_status)
        bishop_black3_status=bishop3b_status.pawn_black1_status

        bishop4b_status=Status("b4b",bishop_black4_status)
        bishop4b_status.Status2("b4b",bishop_black4_status)
        bishop_black4_status=bishop4b_status.pawn_black1_status

        bishop5b_status=Status("b5b",bishop_black5_status)
        bishop5b_status.Status2("b5b",bishop_black5_status)
        bishop_black5_status=bishop5b_status.pawn_black1_status


        queen1b_status=Status("q1b",queen_black_status)
        queen1b_status.Status2("q1b",queen_black_status)
        queen_black_status=queen1b_status.pawn_black1_status

        queen2b_status=Status("q2b",queen_black2_status)
        queen2b_status.Status2("q2b",queen_black2_status)
        queen_black2_status=queen2b_status.pawn_black1_status
        
        queen3b_status=Status("q3b",queen_black3_status)
        queen3b_status.Status2("q3b",queen_black3_status)
        queen_black3_status=queen3b_status.pawn_black1_status

        queen4b_status=Status("q4b",queen_black4_status)
        queen4b_status.Status2("q4b",queen_black4_status)
        queen_black4_status=queen4b_status.pawn_black1_status
    

        rook3w1_status=Status1("r3w",rook_white3_status,rook3w_spawn,r3wmx,r3wmy)
        rook3w1_status.Status21("r3w",rook_white3_status,rook3w_spawn,r3wmx,r3wmy)
        rook3w_spawn=rook3w1_status.queen4b_spawn
        rook_white3_status=rook3w1_status.queen_black4_status
        if rook3w_spawn==1:
            r3wmx=rook3w1_status.q4bmx 
            r3wmy=rook3w1_status.q4bmy
            rook3w_spawn=3
                
        rook4w1_status=Status1("r4w",rook_white4_status,rook4w_spawn,r4wmx,r4wmy)
        rook4w1_status.Status21("r4w",rook_white4_status,rook4w_spawn,r4wmx,r4wmy)
        rook4w_spawn=rook4w1_status.queen4b_spawn
        rook_white4_status=rook4w1_status.queen_black4_status
        if rook4w_spawn==1:
            r4wmx=rook4w1_status.q4bmx 
            r4wmy=rook4w1_status.q4bmy
            rook4w_spawn=4

        rook5w1_status=Status1("r5w",rook_white5_status,rook5w_spawn,r5wmx,r5wmy)
        rook5w1_status.Status21("r5w",rook_white5_status,rook5w_spawn,r5wmx,r5wmy)
        rook5w_spawn=rook5w1_status.queen4b_spawn
        rook_white5_status=rook5w1_status.queen_black4_status
        if rook5w_spawn==1:
            r5wmx=rook5w1_status.q4bmx 
            r5wmy=rook5w1_status.q4bmy
            rook5w_spawn=5
            
        knight3w1_status=Status1("kn3w",knight_white3_status,knight3w_spawn,kn3wmx,kn3wmy)
        knight3w1_status.Status21("kn3w",knight_white3_status,knight3w_spawn,kn3wmx,kn3wmy)
        knight3w_spawn=knight3w1_status.queen4b_spawn
        knight_white3_status=knight3w1_status.queen_black4_status
        if knight3w_spawn==1:
            kn3wmx=knight3w1_status.q4bmx 
            kn3wmy=knight3w1_status.q4bmy
            knight3w_spawn=3
                
        knight4w1_status=Status1("kn4w",knight_white4_status,knight4w_spawn,kn4wmx,kn4wmy)
        knight4w1_status.Status21("kn4w",knight_white4_status,knight4w_spawn,kn4wmx,kn4wmy)
        knight4w_spawn=knight4w1_status.queen4b_spawn
        knight_white4_status=knight4w1_status.queen_black4_status
        if knight4w_spawn==1:
            kn4wmx=knight4w1_status.q4bmx 
            kn4wmy=knight4w1_status.q4bmy
            knight4w_spawn=4

        knight5w1_status=Status1("kn5w",knight_white5_status,knight5w_spawn,kn5wmx,kn5wmy)
        knight5w1_status.Status21("kn5w",knight_white5_status,knight5w_spawn,kn5wmx,kn5wmy)
        knight5w_spawn=knight5w1_status.queen4b_spawn
        knight_white5_status=knight5w1_status.queen_black4_status
        if knight5w_spawn==1:
            kn5wmx=knight5w1_status.q4bmx 
            kn5wmy=knight5w1_status.q4bmy
            knight5w_spawn=5
                
        bishop3w1_status=Status1("b3w",bishop_white3_status,bishop3w_spawn,b3wmx,b3wmy)
        bishop3w1_status.Status21("b3w",bishop_white3_status,bishop3w_spawn,b3wmx,b3wmy)
        bishop3w_spawn=bishop3w1_status.queen4b_spawn
        bishop_white3_status=bishop3w1_status.queen_black4_status
        if bishop3w_spawn==1:
            b3wmx=bishop3w1_status.q4bmx 
            b3wmy=bishop3w1_status.q4bmy
            bishop3w_spawn=3
                
        bishop4w1_status=Status1("b4w",bishop_white4_status,bishop4w_spawn,b4wmx,b4wmy)
        bishop4w1_status.Status21("b4w",bishop_white4_status,bishop4w_spawn,b4wmx,b4wmy)
        bishop4w_spawn=bishop4w1_status.queen4b_spawn
        bishop_white4_status=bishop4w1_status.queen_black4_status
        if bishop4w_spawn==1:
            b4wmx=bishop4w1_status.q4bmx 
            b4wmy=bishop4w1_status.q4bmy
            bishop4w_spawn=4

        bishop5w1_status=Status1("b5w",bishop_white5_status,bishop5w_spawn,b5wmx,b5wmy)
        bishop5w1_status.Status21("b5w",bishop_white5_status,bishop5w_spawn,b5wmx,b5wmy)
        bishop5w_spawn=bishop5w1_status.queen4b_spawn
        bishop_white5_status=bishop5w1_status.queen_black4_status
        if bishop5w_spawn==1:
            b5wmx=bishop5w1_status.q4bmx 
            b5wmy=bishop5w1_status.q4bmy
            bishop5w_spawn=5
                
        queen2w1_status=Status1("q2w",queen_white2_status,queen2w_spawn,q2wmx,q2wmy)
        queen2w1_status.Status21("q2w",queen_white2_status,queen2w_spawn,q2wmx,q2wmy)
        queen2w_spawn=queen2w1_status.queen4b_spawn
        queen_white2_status=queen2w1_status.queen_black4_status
        if queen2w_spawn==1:
            q2wmx=queen2w1_status.q4bmx 
            q2wmy=queen2w1_status.q4bmy
            queen2w_spawn=2
            
        queen3w1_status=Status1("q3w",queen_white3_status,queen3w_spawn,q3wmx,q3wmy)
        queen3w1_status.Status21("q3w",queen_white3_status,queen3w_spawn,q3wmx,q3wmy)
        queen3w_spawn=queen3w1_status.queen4b_spawn
        queen_white3_status=queen3w1_status.queen_black4_status
        if queen3w_spawn==1:
            q3wmx=queen3w1_status.q4bmx 
            q3wmy=queen3w1_status.q4bmy
            queen3w_spawn=3
                
        queen4w1_status=Status1("q4w",queen_white4_status,queen4w_spawn,q4wmx,q4wmy)
        queen4w1_status.Status21("q4w",queen_white4_status,queen4w_spawn,q4wmx,q4wmy)
        queen4w_spawn=queen4w1_status.queen4b_spawn
        queen_white4_status=queen4w1_status.queen_black4_status
        if queen4w_spawn==1:
            q4wmx=queen4w1_status.q4bmx 
            q4wmy=queen4w1_status.q4bmy
            queen4w_spawn=4
            
        rook3b1_status=Status1("r3b",rook_black3_status,rook3b_spawn,r3bmx,r3bmy)
        rook3b1_status.Status21("r3b",rook_black3_status,rook3b_spawn,r3bmx,r3bmy)
        rook3b_spawn=rook3b1_status.queen4b_spawn
        rook_black3_status=rook3b1_status.queen_black4_status
        if rook3b_spawn==1:
            r3bmx=rook3b1_status.q4bmx 
            r3bmy=rook3b1_status.q4bmy
            rook3b_spawn=3
                
        rook4b1_status=Status1("r4b",rook_black4_status,rook4b_spawn,r4bmx,r4bmy)
        rook4b1_status.Status21("r4b",rook_black4_status,rook4b_spawn,r4bmx,r4bmy)
        rook4b_spawn=rook4b1_status.queen4b_spawn
        rook_black4_status=rook4b1_status.queen_black4_status
        if rook4b_spawn==1:
            r4bmx=rook4b1_status.q4bmx 
            r4bmy=rook4b1_status.q4bmy
            rook4b_spawn=4

        rook5b1_status=Status1("r5b",rook_black5_status,rook5b_spawn,r5bmx,r5bmy)
        rook5b1_status.Status21("r5b",rook_black5_status,rook5b_spawn,r5bmx,r5bmy)
        rook5b_spawn=rook5b1_status.queen4b_spawn
        rook_black5_status=rook5b1_status.queen_black4_status
        if rook5b_spawn==1:
            r5bmx=rook5b1_status.q4bmx 
            r5bmy=rook5b1_status.q4bmy
            rook5b_spawn=5
            
        knight3b1_status=Status1("kn3b",knight_black3_status,knight3b_spawn,kn3bmx,kn3bmy)
        knight3b1_status.Status21("kn3b",knight_black3_status,knight3b_spawn,kn3bmx,kn3bmy)
        knight3b_spawn=knight3b1_status.queen4b_spawn
        knight_black3_status=knight3b1_status.queen_black4_status
        if knight3b_spawn==1:
            kn3bmx=knight3b1_status.q4bmx 
            kn3bmy=knight3b1_status.q4bmy
            knight3b_spawn=3
                
        knight4b1_status=Status1("kn4b",knight_black4_status,knight4b_spawn,kn4bmx,kn4bmy)
        knight4b1_status.Status21("kn4b",knight_black4_status,knight4b_spawn,kn4bmx,kn4bmy)
        knight4b_spawn=knight4b1_status.queen4b_spawn
        knight_black4_status=knight4b1_status.queen_black4_status
        if knight4b_spawn==1:
            kn4bmx=knight4b1_status.q4bmx 
            kn4bmy=knight4b1_status.q4bmy
            knight4b_spawn=4

        knight5b1_status=Status1("kn5b",knight_black5_status,knight5b_spawn,kn5bmx,kn5bmy)
        knight5b1_status.Status21("kn5b",knight_black5_status,knight5b_spawn,kn5bmx,kn5bmy)
        knight5b_spawn=knight5b1_status.queen4b_spawn
        knight_black5_status=knight5b1_status.queen_black4_status
        if knight5b_spawn==1:
            kn5bmx=knight5b1_status.q4bmx 
            kn5bmy=knight5b1_status.q4bmy
            knight5b_spawn=5
                
        bishop3b1_status=Status1("b3b",bishop_black3_status,bishop3b_spawn,b3bmx,b3bmy)
        bishop3b1_status.Status21("b3b",bishop_black3_status,bishop3b_spawn,b3bmx,b3bmy)
        bishop3b_spawn=bishop3b1_status.queen4b_spawn
        bishop_black3_status=bishop3b1_status.queen_black4_status
        if bishop3b_spawn==1:
            b3bmx=bishop3b1_status.q4bmx 
            b3bmy=bishop3b1_status.q4bmy
            bishop3b_spawn=3
                
        bishop4b1_status=Status1("b4b",bishop_black4_status,bishop4b_spawn,b4bmx,b4bmy)
        bishop4b1_status.Status21("b4b",bishop_black4_status,bishop4b_spawn,b4bmx,b4bmy)
        bishop4b_spawn=bishop4b1_status.queen4b_spawn
        bishop_black4_status=bishop4b1_status.queen_black4_status
        if bishop4b_spawn==1:
            b4bmx=bishop4b1_status.q4bmx 
            b4bmy=bishop4b1_status.q4bmy
            bishop4b_spawn=4

        bishop5b1_status=Status1("b5b",bishop_black5_status,bishop5b_spawn,b5bmx,b5bmy)
        bishop5b1_status.Status21("b5b",bishop_black5_status,bishop5b_spawn,b5bmx,b5bmy)
        bishop5b_spawn=bishop5b1_status.queen4b_spawn
        bishop_black5_status=bishop5b1_status.queen_black4_status
        if bishop5b_spawn==1:
            b5bmx=bishop5b1_status.q4bmx 
            b5bmy=bishop5b1_status.q4bmy
            bishop5b_spawn=2
                
        queen2b1_status=Status1("q2b",queen_black2_status,queen2b_spawn,q2bmx,q2bmy)
        queen2b1_status.Status21("q2b",queen_black2_status,queen2b_spawn,q2bmx,q2bmy)
        queen2b_spawn=queen2b1_status.queen4b_spawn
        queen_black2_status=queen2b1_status.queen_black4_status
        if queen2b_spawn==1:
            q2bmx=queen2b1_status.q4bmx 
            q2bmy=queen2b1_status.q4bmy
            queen2b_spawn=2
            
        queen3b1_status=Status1("q3b",queen_black3_status,queen3b_spawn,q3bmx,q3bmy)
        queen3b1_status.Status21("q3b",queen_black3_status,queen3b_spawn,q3bmx,q3bmy)
        queen3b_spawn=queen3b1_status.queen4b_spawn
        queen_black3_status=queen3b1_status.queen_black4_status
        if queen3b_spawn==1:
            q3bmx=queen3b1_status.q4bmx 
            q3bmy=queen3b1_status.q4bmy
            queen3b_spawn=3
        
        queen4b1_status=Status1("q4b",queen_black4_status,queen4b_spawn,q4bmx,q4bmy)
        queen4b1_status.Status21("q4b",queen_black4_status,queen4b_spawn,q4bmx,q4bmy)
        queen4b_spawn=queen4b1_status.queen4b_spawn
        queen_black4_status=queen4b1_status.queen_black4_status
        if queen4b_spawn==1:
            q4bmx=queen4b1_status.q4bmx 
            q4bmy=queen4b1_status.q4bmy
            queen4b_spawn=4

        board(r1wmx,r1wmy,k1wmx,k1wmy,r2wmx,r2wmy,r2bmx,r2bmy,r1bmx,r1bmy,b1wmx,b1wmy,b2wmx,b2wmy,b1bmx,b1bmy,b2bmx,b2bmy,kn1wmx,kn1wmy,kn2wmx,kn2wmy,kn1bmx,kn1bmy,kn2bmx,kn2bmy,q1wmx,q1wmy,q1bmx,q1bmy,k1bmx,k1bmy,p8wmx,p8wmy,p7wmx,p7wmy,p6wmx,p6wmy,p5wmx,p5wmy,p4wmx,p4wmy,p3wmx,p3wmy,p2wmx,p2wmy,p1wmx,p1wmy,p5bmx,p5bmy,p1bmx,p1bmy,p2bmx,p2bmy,p3bmx,p3bmy,p4bmx,p4bmy,p6bmx,p6bmy,p7bmx,p7bmy,p8bmx,p8bmy,q2wmx,q2wmy,q2bmx,q2bmy,r3wmx,r3wmy,r4wmx,r4wmy,r5wmx,r5wmy,b3wmx,b3wmy,b4wmx,b4wmy,b5wmx,b5wmy,kn3wmx,kn3wmy,kn4wmx,kn4wmy,kn5wmx,kn5wmy,q3wmx,q3wmy,q4wmx,q4wmy,r3bmx,r3bmy,r4bmx,r4bmy,r5bmx,r5bmy,b3bmx,b3bmy,b4bmx,b4bmy,b5bmx,b5bmy,kn3bmx,kn3bmy,kn4bmx,kn4bmy,kn5bmx,kn5bmy,q3bmx,q3bmy,q4bmx,q4bmy)

        for er in range (0, len(coords2)):
            pygame.draw.circle(win,(255,0,0),(coords2[0][0],coords2[0][1]),15,0)
        for er in range (0, len(coords)):
            pygame.draw.circle(win,(50,205,50),(coords[er][0],coords[er][1]),15,0)
            
    pygame.display.update()
pygame.QUIT
