from tkinter import *
import tkinter as tk
from tkinter import Button, Label, StringVar, ttk,messagebox
from prettytable import PrettyTable
root=Tk()
root.geometry('400x400')
root.configure(bg='#008080')
label = ttk.Label(text="    MINI PROJET SIMULATION")
label.pack(fill='x', padx=100, pady=25)
def AfficherTable():
    msg = value_radio.get()
    x = PrettyTable()
    if msg == '2':
        x.field_names = ["jours", "NCE", "NCP", "TFS",'TSmoy','TATmoy','TauC1','TauC2','Ratio1','Ratio2']
        TT = 9 
        import Simula2 as supe
    else:
        x.field_names = ["jours", "NCE", "NCP", "TFS",'TSmoy','TATmoy','TauC1','TauC2','TauC3','Ratio1','Ratio2']
        TT = 10 
        import SimulationC3 as  supe
    IX=e1.get()
    IY=e2.get()
    IZ=e3.get()
    if int(IX)> 29800 or int(IY)> 29800 or int(IZ)> 29800 or int(IX)<= 0 or int(IY)<= 0 or int(IZ)<= 0:
        messagebox.showinfo("Erreur", "Germe n'est pas dans l'intervalle ")
    else:
        K=supe.main(IX,IY,IZ,0)
        for j in range(41):
            for z in range(TT):
                    K[j][z+1] = round(K[j][z+1],4)
            x.add_row(K[j])  
        print(x) 

value_radio=StringVar()
radio_male=Radiobutton(root,text="2 caisses",value="2",variable=value_radio,indicatoron=0,width=10).pack(padx=15,pady=5,anchor=CENTER)
radio_female=Radiobutton(root,text="3 caisses",value="3",variable=value_radio,indicatoron=0,width=10).pack(padx=15,pady=5,anchor=CENTER)
tk.Label(root,text='Entrez IX',bg='#008080').pack(padx=15,pady=5,anchor=W)
e1=Entry(root,width=200)

e2=Entry(root,width=200)

e3=Entry(root,width=200)
e1.pack(padx=15,pady=5,anchor=W)
tk.Label(root,text='Entrez IY',bg='#008080').pack(padx=15,pady=5,anchor=W)
e2.pack(padx=15,pady=5,anchor=W)
tk.Label(root,text='Entrez IZ',bg='#008080').pack(padx=15,pady=5,anchor=W)
e3.pack(padx=15,pady=5,anchor=W)
Button(root, text="Afficher les reultats", command=AfficherTable).pack(padx=15,pady=5,anchor=CENTER)

def AfficherPlot():
    msg = value_radio.get()
    if msg == '2':
        import Simula2 as supe
    else:
        import SimulationC3 as  supe
    IX=e1.get()
    IY=e2.get()
    IZ=e3.get()
    if int(IX)> 29800 or int(IY)> 29800 or int(IZ)> 29800 or int(IX)<= 0 or int(IY)<= 0 or int(IZ)<= 0:
        messagebox.showinfo("Erreur", "Germe n'est pas dans l'intervalle ")
    else:
        K=supe.main(IX,IY,IZ,1)

Button(root, text="Plot", command=AfficherPlot).pack(padx=50,pady=5,anchor=CENTER)  
Button(root,text='Quitter',command=root.quit).pack(padx=46,pady=5,anchor=CENTER)

root.mainloop()