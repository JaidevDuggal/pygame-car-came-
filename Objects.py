from pygame import *
import pygame
init()

screen=display.set_mode((0,0))

class Button() :
    def blit_image(self,i, center, length, width,align=1) :
            self.i=transform. scale(image. load(i),(length,width))
            if align == 1 :
                self.r=self.i. get_rect(center=center)
            else :
                self.r=self.i.get_rect(topleft=center)    
            screen. blit(self.i, self.r)
            return self. r
    def function(self,ev, length, width,c,d) :
            pos=mouse. get_pos()
            if self.r.collidepoint(pos) :                
                length=c-15
                width=d-15
                if ev. type==MOUSEBUTTONUP :
                    length=c
                    width=d
                    s=mixer. Sound('but.wav')
                    s.play()
                    return length, width , True
            elif ev. type==MOUSEBUTTONUP :
                 length=c
                 width=d
                 return length, width , False
            return length, width , False
            
class Music():
    def music(self,m,l):
        self. m=m 
        self. l=l
        self.p=mixer.Sound(self.m)
        self.p.play(self.l)  
    def s_music(self):
        self.p.stop()                    