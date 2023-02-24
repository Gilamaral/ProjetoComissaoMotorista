from tkinter import *

class Grid( Frame ):
 
 def __init__(self):
  # Inicializando o frame 
  Frame.__init__(self)
  self.master.title("Grid")
  self.master.geometry( "80x80" )
  
  # Criando os labels e adicionando
  # com o método grid()
  for linha in range(3):
   for coluna in range(3):
    Label(self.master, text=str(linha)+','+str(coluna)).grid(row=linha,column=coluna)
  
  mainloop()