from RepositorioActividad import RepositorioActividad
from RepositorioEmpresa import RepositorioEmpresa
from Persona import Persona
from Actividad import Actividad
from Empresa import Empresa                         
from RepositorioPersona import RepositorioPersona               
from datetime import date                           

FechaAhora = date.today()

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
        persona.set_empresa(empre)
    else:
        print("Empresa no existente.")
        print("Desea registrar una nueva empresa?")
        op = input("1. Si \n2. No")
        if op == '1':
            empreN = RegistrarEmpresa()
            persona.set_empresa(empreN)
    RepositorioPersona.GuardarPersona(persona)
    RepositorioPersona.AutorizarPersona(persona)
    print("Persona registrada con exito")
RegistrarAct()

#interfaz 
menu1 = input("1. Registrar Persona. \n2. Registrar Empresa. \n3. Comprobar Personas Autorizadas \n4. Dar de baja una persona \n0. Salir")
while menu1 != '0':
    print("\n----------------------------------------------------------------------------------------\n")
    if menu1 == '1':
        RegistrarPersona()
    elif menu1 == '2':
        RegistrarEmpresa()
    elif menu1 == '3':
        ComPer = input("Ingresar DNI de la persona: ")
        RepositorioPersona.ComprobarAutorizados(ComPer)
    elif menu1 == '4':
        PerBaja = input("Ingrese DNI de la persona a dar de baja: ")
        RepositorioPersona.DarBaja(PerBaja)
    else:
        print("Opcion no valida")
    print("\n----------------------------------------------------------------------------------------\n")    
    menu1 = input("1. Registrar Persona. \n2. Registrar Empresa. \n3. Comprobar Personas Autorizadas \n4. Dar de baja una persona \n0. Salir")

    










