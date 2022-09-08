import os
try :
    sco=open('name.txt','x')
    sco. write('0')
    sco. close()
    sco = open('name.txt')
    read=int(sco. read())
except :
    sco=open('name.txt')
    read=int(sco.read())
from pygame import *
import pygame 
from random import *
import random
from Objects import *

init()
screen=display.set_mode((9,16))
clock=time.Clock()
        
Main_music=Music()  
End_music=Music()
Score_music=Music()
easy_button=Button()
hard_button=Button()
normal_button=Button()
back_button=Button()

def button(img,x,y):       
    i=image.load(img).convert_alpha()
    screen.blit(i,(x,y))
    
def massage(massage,style, size, color, x,y):
    f=font.SysFont(style,size)    
    m=f. render(massage, True,color)
    screen. blit(m,(x,y))    
    
def display_1():
    screen=display. set_mode((0,0))    
    Main_music.music('bm.mp3',-1)       
    easy_button_length , easy_button_width = 400 , 185
    hard_button_length , hard_button_width = 400 , 185
    normal_button_length , normal_button_width = 550 , 185
    back_button_length , back_button_width = 125 , 125
    
    tr=True    
    while tr :       
        button('bi.jpg',0,-90)
        #
        easy_button. blit_image('easy.png',(280,900), easy_button_length, easy_button_width)
        hard_button. blit_image('hard.png',(800,900), hard_button_length, hard_button_width)
        normal_button. blit_image('normal.png',(540,1200), normal_button_length , normal_button_width)
        back_button. blit_image('bb.png',(70,2000),back_button_length , back_button_width)
        for Event in event. get():     
            ev=Event

            easy_button_length , easy_button_width , easy_condition = easy_button. function(ev, easy_button_length, easy_button_width,400,185)
            hard_button_length , hard_button_width , hard_condition = hard_button. function(ev, hard_button_length, hard_button_width, 400,185)
            normal_button_length , normal_button_width , normal_condition = normal_button. function(ev , normal_button_length , normal_button_width , 550 , 185 )
            back_button_length , back_button_width , back_condition = back_button. function(ev , back_button_length , back_button_width , 125 , 125)
            pos=mouse.get_pos()
            i=pos[0]
            j=pos[1]
            #easy
            if easy_condition :
                play(10)
                tr=False
            #hard            
            if hard_condition :
                play(27)   
                tr=False
            #n8rkormal
            if normal_condition :
                play(20)
                tr=False
            if back_condition :                  
                tr=False     
        display. update()
col=('red','green','blue','pink','orange','black','gold','yellow')
def game_over(score,hs):
                    print(score , hs)
                    Score_music.music('go.wav',0)
                    End_music. music('end.mp3',-1)
                    screen=display. set_mode((0,0))
                    mouse.set_pos([0,0])
                    Main_music.s_music()                    
                    b=True                     
                    while b :  
                        button('bi.jpg',0,-90)  
                        button('go.png',330,1150)      
                        button('bb.png',0,300)              
                        massage('Score : '+str(score),'a.ttf',150,'blue',310,800)
                        massage('High Score : '+hs,'a.ttf',150,'red',50,1000)   
                        massage('New ' ,' ',150,'blue',50,800)
                        p=mouse. get_pos() 
                        ii=p[0]
                        jj=p[1]
                        if 0<ii<122 and 300<jj<424 :   
                            End_music.s_music()                             
                            mouse. set_pos((0,0))                            
                            display_1()
                            b=False
                        mouse. set_pos((0,0))
                        display. update()                                                            
def play(speed):            
    car=Button()     
    x=480
    s=speed
    y=2100
    t=True
    tu=(90,270,450,630,810,990,1170)
    xe=choice(tu)
    xe1=choice(tu)
    xe2=choice(tu)
    xe3=choice(tu)
    xe4=choice(tu)
    xe5=choice(tu)
    xe6=choice(tu)
    xe7=choice(tu)
    ca1=choice(tu)
    ca2=choice(tu)
    ca3=choice(tu)
    ca4=choice(tu)
    ca5=choice(tu)
    a,b,c,d,e,f=0,-500,-700,-1200,-1700,-2200
    a1 , b1 =-2700 , -3300 
    cb1 , cb2 , cb3 , cb4 , cb5 , cb6=1800 , 900 , 600 , 100 , -500 , -1000
            
    enemy_1 = Button()
    enemy_2 = Button()
    enemy_3 = Button()
    enemy_4 = Button()
    enemy_5 = Button()
    enemy_6 = Button()
    enemy_7 = Button()
    enemy_8 = Button()
    cash_1 = Button()
    cash_2 = Button()
    cash_3 = Button()
    cash_4 = Button()
    cash_5 = Button()        
    score=0  
    cl=choice(col) 
    colour=choice(col)
    while t :            
        screen.fill('#30302A')        
        line_position = 180
        for line in range(5) :
               draw. line(screen, colour ,(line_position,0),(line_position,2409),5)
               line_position += 180
        draw. line(screen, choice(col),(0,0),(0,2409),5)
        draw. line(screen, choice(col),(1080,0),(1080,2409),5)
                
        car_rect=car. blit_image('my_car.png',(x,y),130,250)        
        pos=mouse.get_pos()      
        i=pos[0]
        j=pos[1]
        x=i    
        #stop on side 
        if x<55 :
            x=55
        if x>1025 :
            x=1025    
        
        enemy_1_rect=enemy_1. blit_image('red_car.png',(xe,a),130,250)
        enemy_2_rect=enemy_2. blit_image('blue_car.png',(xe1,b),130,250)
        enemy_3_rect=enemy_3. blit_image('green_car.png',(xe2,c),130,250)
        enemy_4_rect=enemy_4. blit_image('blue_truck.png',(xe3,d),150,300)
        enemy_5_rect=enemy_5. blit_image('yellow_car.png',(xe4,e),130,250)
        enemy_6_rect=enemy_6. blit_image('orange_car.png',(xe5,f),130,250)
        enemy_7_rect=enemy_7. blit_image('red_truck.png',(xe6,a1),170,330)
        enemy_8_rect=enemy_8. blit_image('white_car.png',(xe7,b1),130,250) 
        enemy_rect_list=[enemy_1_rect,enemy_2_rect,enemy_3_rect,enemy_4_rect,enemy_5_rect,enemy_6_rect,enemy_7_rect,enemy_8_rect]      
        cash_1_rect=cash_1.blit_image('bcash.jpg',(ca1,cb1),120,80)
        cash_2_rect=cash_1.blit_image('ycash.jpg',(ca2,cb2),120,80)
        cash_3_rect=cash_1.blit_image('gcash.jpg',(ca3,cb3),120,80)
        cash_4_rect=cash_1.blit_image('vcash.jpg',(ca4,cb4),120,80)
        cash_5_rect=cash_1.blit_image('bcash.jpg',(ca5,cb5),120,80)                     
        a+=s+10
        b+=s+15
        c+=s+20
        d+=s+10
        e+=s+15
        f+=s+15
        a1+=s+5
        b1+=s+20
        cb1+=s
        cb2+=s+15
        cb3+=s+10
        cb4+=s+20
        cb5+=s-10
        if a>2500 :
            xe=choice(tu)
            score+=1
            a=-200
        if b>2500 :       
            xe1=choice(tu)
            score+=1
            b=-200
        if c>2500 :
            xe2=choice(tu)
            score+=1
            c=-200
        if d>2500 :
            xe3=choice(tu)
            score+=1
            d=-200
        if e>2500 :
            xe4=choice(tu)
            score+=1
            e=-200
        if f>2500 :
            xe5=choice(tu)
            score+=1
            f=-200                       
        if a1>2500 :
            xe6=choice(tu)          
            score+=1
            a1=-200
        if b1>2500 :             
            xe7=choice(tu)         
            score+=1
            b1=-200
        if cb1>2500 :
            ca1=choice(tu)   
            cb1=-200
        if cb2>2500 :
            ca2=choice(tu)   
            cb2=-200
        if cb3>2500 :
            ca3=choice(tu)   
            cb3=-200
        if cb4>2500 :
            ca4=choice(tu)   
            cb4=-200
        if cb5>2500 :
            ca5=choice(tu)   
            cb5=-200
        if cb6>2500 :
            ca6=choice(tu)   
            cb6=-200
        sc=470
        if score>10 :
            sc-=50
        if score>99:
            sc-=50
        if score>999:
            sc-=50
        if score>9999:
            sc-=50       
        massage(str(score),'a4.ttf',300,cl,sc,20)        
        #out with first car   
        sco=open('name.txt')
        read=int(sco.read()) 
        if score>read :
                    os.remove('name.txt')
                    sco=open('name.txt','x')
                    sco.write(str(score))
                    sco. close()
                    sco=open('name.txt')
                    read=int(sco.read())  
                    sco. close()    
                    
        
        # Game Over 
        for enemy in enemy_rect_list :              
            if car_rect.colliderect(enemy) :
                t=False
                game_over(score,str(read))                                                                                                                                                
        
        if car_rect.colliderect(cash_1_rect) :
            ca1=choice(tu)
            cb1=-80
            Score_music.music('sc.mp3',0)
            cl=choice(col)
            colour=choice(col)
            score+=50
        if car_rect.colliderect(cash_2_rect) :
            ca2=choice(tu)
            cb2=-80
            Score_music.music('sc.mp3',0)
            cl=choice(col)
            colour=choice(col)
            score+=50    
        if car_rect.colliderect(cash_3_rect) :
            ca3=choice(tu)
            cb3=-80
            Score_music.music('sc.mp3',0)
            cl=choice(col)
            colour=choice(col)
            score+=50    
        if car_rect.colliderect(cash_4_rect) :
            ca4=choice(tu)
            cb4=-80
            Score_music.music('sc.mp3',0)
            cl=choice(col)
            colour=choice(col)
            score+=50 
        if car_rect.colliderect(cash_5_rect) :
            ca5=choice(tu)
            cb5=-80
            Score_music.music('sc.mp3',0)
            cl=choice(col)
            colour=choice(col)
            score+=50                                                                                                                                                                                                                                   
        display.update()       
        #clock.tick(60)             
display_1()        