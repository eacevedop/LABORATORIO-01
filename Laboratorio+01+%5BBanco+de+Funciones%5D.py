
# coding: utf-8

# In[ ]:

#Librerías Usadas#
#-----------------------#
import numpy as np # --> para cómputo numérico
import matplotlib.pyplot as plt # --> realizar gráficas

#Funciones básicas para el desarrollo de las graficas en los bancos de funciones#
#-------------------------------------------------------------------------------#
def graficar(x, y, nombre):    
        plt.figure()
        plt.grid()
        plt.plot(x,y)
        plt.axis([np.min(x), np.max(x), np.min(y), 1.1*np.max(y)])
        plt.title(str(nombre))
        plt.show()
        label = str(nombre) + ".pdf"
        plt.savefig(label)

#Funciones Básicas Desarrolladas en el Banco de Funciones#
#--------------------------------------------------------#

def escalon(t_inf, t_sup, N_ptos, despl, ampl):
    if(despl < t_inf):
        print('Error, valor de desplzamiento muy pequeño')
    elif(despl > t_sup):
        print('Error, valor de desplzamiento muy grande')
    t = np.linspace(t_inf, t_sup, N_ptos)
    y = np.zeros([1, np.size(t, 0)])
    y[0, np.where(t > despl)[0]] = ampl
    return [t, y[0,:]]
    """
    escalon(t_inf, t_sup, N_ptos, despl, ampl) desarrolla la función escalón unitario:
    t_inf := inicio función.
    t_sup := finalización función.
    N_ptos := Cantidad de puntos a graficar en la función.
    despl := valor de desplazamiento.
    ampl := Amplitud de la señal.
        """
def func_seno(t_inf, t_sup, N_ptos, ampl, freq, phase):
    t = np.linspace(t_inf, t_sup, N_ptos)
    y = np.sin(2*np.pi*freq*t + phase)
    return [t, y]
    """
    seno(t_inf, t_sup, N_ptos, ampl, freq, phase) desarrolla la función seno:
    t_inf := inicio función.
    t_sup := finalización función.
    N_ptos := Cantidad de puntos a graficar en la función.
    freq := frecuencia de la señal.
    ampl := Amplitud de la señal.
    phase := Fase da la señal.
        """
def func_coseno(t_inf, t_sup, N_ptos, ampl, freq, phase):
    t = np.linspace(t_inf, t_sup, N_ptos)
    y = np.cos(2*np.pi*freq*t + phase)
    return [t, y]
    """
    coseno(t_inf, t_sup, N_ptos, ampl, freq, phase) desarrolla la función coseno:
    t_inf := inicio función.
    t_sup := finalización función.
    N_ptos := Cantidad de puntos a graficar en la función.
    freq := frecuencia de la señal.
    ampl := Amplitud de la señal.
    phase := Fase da la señal.
        """
def func_Exponencial(t_inf, t_sup, N_ptos):
    t = np.linspace(t_inf, t_sup, N_ptos)
    y = np.exp(t)
    return [t, y]
    """
    Exponencial(t_inf, t_sup, N_ptos) desarrolla la función exponencial:
    t_inf := inicio función.
    t_sup := finalización función.
    N_ptos := Cantidad de puntos a graficar en la función.
        """
def func_Cuadratica(t_inf, t_sup, N_ptos,a,b,c):
    t = np.linspace(t_inf, t_sup, N_ptos)
    y = ((a*t*t)+(b*t)+c)
    return [t, y]
    """
    Cuadratica(t_inf, t_sup, N_ptos,a,b,c) desarrolla la función cuadratica:
    a := constante a.
    b := constante b.
    c := constante c.
    t_inf := inicio función.
    t_sup := finalización función.
    N_ptos := Cantidad de puntos a graficar en la función.
        """        
#Menú Principal de opciones y llamado de funciones#
#----------------------------------- #
while(1): #Bucle para menú opciones#
    print ("1.Función Escalon")
    print ("2.Función Seno")
    print ("3.Función Coseno")
    print ("4.Función Exponencial")
    print ("5.Función Cuadrática")
    F= input("Ingresa una opcion:")
    print ("La funcion es:",F)
    print("Elegir Parametros")
    
    if(F==1):
        t_inf=input("t_inferior:")
        t_sup=input("t_superior:")
        ampl= input ("Amplitud:")
        despl= input ("Desplazamiento:")
        N_ptos=input("Numero de puntos a graficar:")
        if(F==1):
            [t, x] = escalon(t_inf, t_sup, N_ptos, despl, ampl) #Llamado funcion Graficar con valores de funcion escalon#
            graficar(t,x, "Figura_1(Escalon)")

    elif(F==2):
        t_inf=input("t_inferior:")
        t_sup=input("t_superior:")
        ampl=input("Amplitud:")
        freq=input("Frecuencia:")
        phase=input("Fase:")
        N_ptos=input("Numero de puntos a graficar:")
        if(F==2):
            [t1, x1] = func_seno(t_inf, t_sup, N_ptos, ampl, freq, phase)#Llamado funcion Graficar con valores de funcion escalon#
            graficar(t1,x1, "Figura_2(Seno)")

    elif(F==3):
        t_inf=input("t_inferior:")
        t_sup=input("t_superior:")
        ampl=input("Amplitud:")
        freq=input("Frecuencia:")
        phase=input("Fase:")
        N_ptos=input("Numero de puntos a graficar:")
        if(F==3):
            [t2, x2] = func_coseno(t_inf, t_sup, N_ptos, ampl, freq, phase)#Llamado funcion Graficar con valores de funcion escalon#
            graficar(t2,x2, "Figura_3(Coseno)")
    elif(F==4):
        t_inf=input("t_inferior:")
        t_sup=input("t_superior:")
        N_ptos=input("Numero de puntos a graficar:")
        if(F==4):
            [t3, x3] = func_Exponencial(t_inf, t_sup, N_ptos)#Llamado funcion Graficar con valores de funcion escalon#
            graficar(t3,x3, "Figura_4(Exponencial)")  
    elif(F==5):
        print("Insertar a,b,c(at^2+bt+c)")
        a=input("a:")
        b=input("b:")
        c=input("c:")
        t_inf=input("t_inferior:")
        t_sup=input("t_superior:")
        N_ptos=input("Numero de puntos a graficar:")
        if(F==5):
            [t5, x5] = func_Cuadratica(t_inf, t_sup, N_ptos,a,b,c)#Llamado funcion Graficar con valores de funcion escalon#
            graficar(t5,x5, "Figura_5(Cuadratica)")  

