import os
import time

import Leer
import COVIDModelodeDatos

try:
    COVIDDATOS = COVIDModelodeDatos.CovidDatos()
except:
    print("Ocurrio un error")


def IngresarDatosBD(pais,nombre):
    COVIDDataApi=Leer.obtenerapi(pais)
    pais=COVIDDataApi["country"]
    idpais=COVIDDataApi["code"]
    casosconfirmados=COVIDDataApi["confirmed"]
    casoscriticos=COVIDDataApi["critical"]
    muertes=COVIDDataApi["deaths"]

    COVIDDATOS.agregarCovidInfo(nombre,idpais,casosconfirmados,casoscriticos,muertes)
    time.sleep(1)


def CargarDatosdeApi():
    IngresarDatosBD("Spain", "España")
    IngresarDatosBD("Honduras", "Honduras")
    IngresarDatosBD("Italy", "Italia")
    IngresarDatosBD("USA", "Estados Unidos")
    IngresarDatosBD("El Salvador", "El Salvador")


opcion=0
while(opcion!=4):
    print("-----------------Menu------------")
    print("1.Cargar Datos a la Base de Datos")
    print("2.Mostrar todos los datos")
    print("3.Mostrar los datos de un pais especifico")
    print("4.Salir")
    opcion=int(input("Ingrese que accion desea realizar: "))

    if(opcion==1):
        CargarDatosdeApi()
    if(opcion==2):
        COVIDDATOS.MostrarTodalaInformacion()
    if(opcion==3):
        opcion1=0
        while opcion1!=6:
            print("1.España")
            print("2.Honduras")
            print("3.Italia")
            print("4.Estados Unidos")
            print("5.El Salvador")
            print("6.Salir")
            opcion1=int(input("Elija el pais a mostrar informacion: "))
            if(opcion1==1):
                COVIDDATOS.Mostrarinformaciondepais("España")
            if(opcion1==2):
                COVIDDATOS.Mostrarinformaciondepais("Honduras")
            if(opcion1==3):
                COVIDDATOS.Mostrarinformaciondepais("Italia")
            if(opcion1==4):
                COVIDDATOS.Mostrarinformaciondepais("Estados Unidos")
            if(opcion1==5):
                COVIDDATOS.Mostrarinformaciondepais("El Salvador")
            else:
                print("Ingrese un comando valido")






