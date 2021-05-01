from Persona import Persona
from Actividad import Actividad

ListAct = []
ListPersona = []

#Actividades existentes.
act1 = Actividad('act1', 'autorizado')
ListAct.append(act1)
act2 = Actividad('act2', 'no autorizado')
ListAct.append(act2)
act3 = Actividad('act3', 'autorizado')
ListAct.append(act3)
act4 = Actividad('act4', 'autorizado')
ListAct.append(act4)
act5 = Actividad('act5', 'no autorizado')
ListAct.append(act5)
act6 = Actividad('act6', 'no autorizado')
ListAct.append(act6)

def RegistrarPersona():
    dni = input("DNI:")
    nombre = input("Nombre y Apellido:")
    dom  = input("Domicilio:")
    tel = input("Telefono:")
    em = input("Email:")
    persona = Persona(dni, nombre, dom, tel, em, 0)
    actRealiza = input("Actividad que realiza:")
    if actRealiza == 'act1':
        persona.set_act(act1)
    elif actRealiza == 'act2':
        persona.set_act(act2)
    elif actRealiza == 'act3':                          #Cambiar esto
        persona.set_act(act3)
    elif actRealiza == 'act4':
        persona.set_act(act4)
    elif actRealiza == 'act5':
        persona.set_act(act5)
    elif actRealiza == 'act6':
        persona.set_act(act6)
    ListPersona.append(persona)

def ComprobarAutorizacion():
    for i in ListPersona:
        i.comprobarPermiso(i.get_act())

menu = input("1. Registrarse. \n2. Comprobar Autorizacion \n3. Salir")
while menu != '3':
    if menu == '1':
        RegistrarPersona()
    elif menu == '2':
        ComprobarAutorizacion()
    else:
        print("Opcion no valida")
    menu = input("1. Registrarse. \n2. Comprobar Autorizacion \n3. Salir")





#Personas registradas
# persona1 = Persona('345123', 'Elias Colombo', '829347', '1324234', 'email1', act1)
# persona2 = Persona('89354', 'persona2', '73233', '12435', 'email2', act2)
# persona3 = Persona('89723', 'persona3', '89237', '4351', 'email3', act3)
# persona4 = Persona('892734', 'persona4', '892374', '12347', 'email4', act4)
# persona5 = Persona('12456', 'persona5', '90718', '908123', 'email5', act5)
# persona6 = Persona('907134', 'persona6', '13945', '908134', 'email6', act6)


# persona1.comprobarPermiso(act1)
# persona2.comprobarPermiso(act2)
# persona3.comprobarPermiso(act3)
# persona4.comprobarPermiso(act4)
# persona5.comprobarPermiso(act5)
# persona6.comprobarPermiso(act6)

