from RepositorioActividad import RepositorioActividad
from RepositorioEmpresa import RepositorioEmpresa
from RepositorioPersona import RepositorioPersona 
from RepositorioIngreso import RepositorioIngreso
from Persona import Persona
from Actividad import Actividad
from Empresa import Empresa                         
from Ingreso import Ingreso        
from datetime import date
from datetime import datetime  
import sys
from PIL import Image
import qrcode

FechaAhora = date.today()
FHActual = datetime.today()

#Actividades autorizadas registradas.
def RegistrarAct():
        
    act1 = Actividad('act1')
    RepositorioActividad.GuardardAct(act1)

    act2 = Actividad('act2')
    RepositorioActividad.GuardardAct(act2)

    act3 = Actividad('act3')
    RepositorioActividad.GuardardAct(act3)

    act4 = Actividad('act4')
    RepositorioActividad.GuardardAct(act4)

    act5 = Actividad('act5')
    RepositorioActividad.GuardardAct(act5)

    act6 = Actividad('act6')
    RepositorioActividad.GuardardAct(act6)

#Registrar Empresas
def RegistrarEmpresa():
    rs = input("Razon Social:")
    cuit = input("Cuit:")
    dom = input("Domicilio:")
    loc = input("Localidad:")
    emE = input("Email de la empresa:")
    tel = input("Telefono:")
    empresa = Empresa(rs, cuit, dom, loc, emE, tel)

    act = input("Ingrese actividad de la empresa: ")
    if RepositorioActividad.ExistenciaActividad(act) == True:
        empresa.set_actividad(act)
        RepositorioEmpresa.GuardadEmpreA(empresa)
    else:
        print("Actividad no autorizada")
        
    RepositorioEmpresa.GuardarEmpresa(empresa)
    print("\n----------------------------------------------------------------------------------------\n")
    print("Empresa registrada correctamente.")

def RegistrarEmpresaNoRegistrada(per):
    print("\n----------------------------------------------------------------------------------------\n")
    razon = input("Razon Social:")
    Cuit = input("Cuit:")
    domi = input("Domicilio:")
    loca = input("Localidad:")
    emailE = input("Email de la empresa:")
    tele = input("Telefono:")
    empresaN = Empresa(razon, Cuit, domi, loca, emailE, tele)

    act = input("Ingrese actividad de la empresa: ")
    if RepositorioActividad.ExistenciaActividad(act) == True:
        empresaN.set_actividad(act)
        RepositorioEmpresa.GuardadEmpreA(empresaN)
    else:
        print("Actividad no autorizada")
        
    RepositorioEmpresa.GuardarEmpresa(empresaN)
    per.set_empresa(empresaN)
    RepositorioPersona.AutorizarPersona(per, empresaN)
    print("\n----------------------------------------------------------------------------------------\n")
    print("Empresa registrada correctamente.")

#Registrar Personas
def RegistrarPersona():
    dni = input("DNI: ")
    nomA = input("Nombre y Apellido: ")
    dom = input("Domicilio: ")
    tel = input("Telefono: ")
    email = input("Email: ")
    print("Ingrese fecha inicio de autorizacion: ")
    dI = int(input("Dia: "))
    mI = int(input("Mes: "))
    aI = int(input("Anio: "))
    fechaI = date(aI, mI, dI)
    print("Ingrese fecha fin de autorizacion: ")
    dF = int(input("Dia: "))
    mF = int(input("Mes: "))
    aF = int(input("Anio: "))
    fechaF = date(aF, mF, dF)
    persona = Persona(dni, nomA, dom, tel, email, fechaI, fechaF)

    empre = input("Ingrese nombre de la empresa en la que trabaja: ")
    if RepositorioEmpresa.ExistenciaEmpre(empre) == True:
        persona.set_empresa(RepositorioEmpresa.ObtenerEmpresa(empre))
    else:
        print("Empresa no existente.")
        print("Desea registrar una nueva empresa?")
        op = input("1. Si \n2. No")
        if op == '1':
            RegistrarEmpresaNoRegistrada(persona)
    data = str(dni + nomA)
    qr = qrcode.make(data)
    qr.save(nomA + '.png') 

    
    persona.set_codigoQr(qr)
    
    RepositorioPersona.GuardarPersona(persona)
    RepositorioPersona.AutorizarPersona(persona, empre)
    print("\n----------------------------------------------------------------------------------------\n")
    print("Persona registrada con exito")

#Regitrar ingresos
def RegistrarIngreso():
    print("Registro de ingresos.")
    print("\n----------------------------------------------------------------------------------------\n")
    dniIngreso = input("Ingrese DNI de la persona: ")
    namPerson = RepositorioPersona.ObtenerNom(dniIngreso + ".png")
    imgQr = Image.open(namPerson)
    imgQr.show()
    fechaAI = FHActual
    temp = input("Temperatura registrada: ")
    destino = input("Lugar de destino: ")
    
    ingreso = Ingreso(fechaAI, temp, destino)
    RepositorioIngreso.GuardarIngreso(ingreso)
    x = input("Ingreso con algun vehiculo?\n1. Si \n2. No")
    if x == '1':
        pat = input("Patente: ")
        ingreso.set_patente(pat)

    RepositorioIngreso.AsignarEstado(ingreso, dniIngreso)

    if RepositorioPersona.ExistenciaPer(dniIngreso) == True:
        ingreso.set_persona(RepositorioPersona.ObtenerPer(dniIngreso))
    else:
        print("\n----------------------------------------------------------------------------------------\n")
        print("Persona no registrado o no autorizada.")
    

def RegistrarSalida():
    print("Registro de Salida.")
    print("\n----------------------------------------------------------------------------------------\n")
    dniSalida = input("Ingrese dni de la persona: ")
    ing = RepositorioIngreso.ObtenerIngresoPer(dniSalida)
    ing.set_fechaEg(FHActual)
    

RegistrarAct()

#interfaz 
menu1 = input("1. Registrar Persona. \n2. Registrar Empresa. \n3. Comprobar Personas Autorizadas \n4. Dar de baja una persona \n5. Registrar ingresos \n6. Registrar salida \n0. Salir")
while menu1 != '0':
    print("\n----------------------------------------------------------------------------------------\n")
    if menu1 == '1':
        RegistrarPersona()
    elif menu1 == '2':
        RegistrarEmpresa()
    elif menu1 == '3':
        ComPer = input("Ingresar DNI de la persona: ")
        print("\n----------------------------------------------------------------------------------------\n")
        if RepositorioPersona.ComprobarAutorizados(ComPer) == True:
            print("Persona autorizada.")
        else:
            print("Persona no autorizada.")
    elif menu1 == '4':
        PerBaja = input("Ingrese DNI de la persona a dar de baja: ")
        RepositorioPersona.DarBaja(PerBaja)
    elif menu1 == '5':
        RegistrarIngreso()
    elif menu1 == '6':
        RegistrarSalida()
    else:
        
        print("Opcion no valida")
    print("\n----------------------------------------------------------------------------------------\n")    
    menu1 = input("1. Registrar Persona. \n2. Registrar Empresa. \n3. Comprobar Personas Autorizadas \n4. Dar de baja una persona \n5. Registrar ingresos \n6. Registrar salida \n0. Salir")












