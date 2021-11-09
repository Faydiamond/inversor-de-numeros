# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:38:34 2021

@author: FabiDiamanti
"""

import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self):
        self.title("Inversor de numeros")
#       self.geometry("600x200")
        self.resizable(0,0)
        #obtengo valores de las cajas
        self.pos0 = tk.IntVar()
        self.pos1 = tk.IntVar()
        self.pos2 = tk.IntVar()
        self.pos3 = tk.IntVar()
        self.pos4 = tk.IntVar()
        self.pos5 = tk.IntVar()
        self.pos6 = tk.IntVar()
        self.pos7 = tk.IntVar()
        self.pos8 = tk.IntVar()
        frm_izquierdo=tk.Frame(self,bg="#29bed4")
        frm_izquierdo.grid(row=0,column=0)
        frm_izquierdo.config(width=555,height=170)
        #ENTRADAS
        pos0 = tk.Entry(self, textvariable = self.pos0, bg='#b4dedf' ,fg='#234786')
        pos0.place(x= 10, y= 40,width='50')
        pos1 = tk.Entry(self, textvariable = self.pos1, bg='#b4dedf' ,fg='#234786')
        pos1.place(x= 70, y= 40,width='50')
        pos2= tk.Entry(self, textvariable = self.pos2, bg='#b4dedf' ,fg='#234786')
        pos2.place(x= 130, y= 40,width='50')
        pos3= tk.Entry(self, textvariable = self.pos3, bg='#b4dedf' ,fg='#234786')
        pos3.place(x= 190, y= 40,width='50')
        pos4= tk.Entry(self, textvariable = self.pos4, bg='#b4dedf' ,fg='#234786')
        pos4.place(x= 250, y= 40,width='50')
        pos5= tk.Entry(self, textvariable = self.pos5, bg='#b4dedf' ,fg='#234786')
        pos5.place(x= 310, y= 40,width='50')
        pos6= tk.Entry(self, textvariable = self.pos6, bg='#b4dedf' ,fg='#234786')
        pos6.place(x= 370, y= 40,width='50')
        pos7= tk.Entry(self, textvariable = self.pos7, bg='#b4dedf' ,fg='#234786')
        pos7.place(x= 430, y= 40,width='50')
        pos8= tk.Entry(self, textvariable = self.pos8, bg='#b4dedf' ,fg='#234786')
        pos8.place(x= 490, y= 40,width='50')
        #Etiquetas
      
        #BOTON
        calculate_btn = tk.Button(self ,text='Calcular Precio', command = self.calculate)
        calculate_btn.place(x = 215, y= 130)
       
    def calculate (self):
       self.list_numbers = []
       self.list_numbers.append(self.pos0.get())
       self.list_numbers.append(self.pos1.get())
       self.list_numbers.append(self.pos2.get())
       self.list_numbers.append(self.pos3.get())
       self.list_numbers.append(self.pos4.get())
       self.list_numbers.append(self.pos5.get())
       self.list_numbers.append(self.pos6.get())
       self.list_numbers.append(self.pos7.get())
       self.list_numbers.append(self.pos8.get())
       i = 0
       while (i < len(self.list_numbers)):
           #print(self.list_numbers[i],'          ')
           #print(self.list_numbers[i])
           ##print('############################')
           self.invert = str(self.list_numbers[i])[::-1]
           #print(self.invert)
           #cajas dinamicas:
           if(i == 0):
              print(self.invert)
              self.res = tk.Label(text="")
              self.co_x =10
              self.widthh =50
              self.res.place(x= self.co_x, y= 80, width = 30)
              self.res.config(text= self.invert )
           else:
              self.co_x = self.co_x +30
              self.widthh = self.widthh + 30
              print(self.invert)
              self.res = tk.Label(text="")
              self.res.place(x=  self.co_x , y= 80,width = 30 )
              self.res.config(text= self.invert )
           i+=1
           
def main():
    app=Window()
    app.mainloop()

if __name__ == '__main__':
    main()
    
