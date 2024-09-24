                            # GENERADOR DE TIKETS!!!
# Usuario : Monto/ dinero.  
# Usuario : Producto. 
from datetime import datetime
from tkinter import *


def Mostrar():
    screen = Tk();
    screen.config(bg='#ecebe6')
    screen.geometry('300x200')
    screen.title('Ticket')

    h_actual = datetime.now().strftime("%d/%m/%Y %H:%M") 
    mostrarHora = f'FECHA: {h_actual}'

    Label1 = Label(screen,text='   ',font='18px') #Name - Empresa
    Label1.pack()

    Label1 = Label(screen,text='******* MACROCOMPRA *******',font='18px') #Name - Empresa
    Label1.pack()

    Label1 = Label(screen,text=mostrarHora,font='18px')
    Label1.pack()

    Label1 = Label(screen,text=x,font='18px')
    Label1.pack()
    Label1 = Label(screen,text='***************************',font='20px')
    Label1.pack()
    Label1 = Label(screen,text=xx,font='20px')
    Label1.pack()


    screen.mainloop()


userProduct0 = input('Ingresa Producto 1: ')
usertPrecio0 = float(input('Ingresa Precio producto 1: '))

userProduct1 = input('Ingresa Producto 2: ')
usertPrecio1 = float(input('Ingresa Precio producto 2: '))

userProduct2 = input('Ingresa Producto 2: ')
usertPrecio2 = float(input('Ingresa Precio producto 2: '))


total = usertPrecio0 + usertPrecio1 + usertPrecio2;

redondeado = round(total,2)

x  = (f'Producto: {userProduct0}: S/.{usertPrecio0}\nProducto: {userProduct1}: S/.{usertPrecio1}\nProducto: {userProduct2}: S/.{usertPrecio2}' )
xx = (f'Total: S/.{redondeado}')

Mostrar()

