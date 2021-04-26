from Persona import Persona
from Actividad import Actividad

#Actividades existentes.
act1 = Actividad('act1', 'autorizado')
act2 = Actividad('act2', 'no autorizado')
act3 = Actividad('act3', 'autorizado')
act4 = Actividad('act4', 'autorizado')
act5 = Actividad('act5', 'no autorizado')
act6 = Actividad('act6', 'no autorizado')

#Personas registradas
persona1 = Persona('345123', 'Elias Colombo', '829347', '1324234', 'email1', act1)
persona2 = Persona('89354', 'persona2', '73233', '12435', 'email2', act2)
persona3 = Persona('89723', 'persona3', '89237', '4351', 'email3', act3)
persona4 = Persona('892734', 'persona4', '892374', '12347', 'email4', act4)
persona5 = Persona('12456', 'persona5', '90718', '908123', 'email5', act5)
persona6 = Persona('907134', 'persona6', '13945', '908134', 'email6', act6)


persona1.comprobarPermiso(act1)
persona2.comprobarPermiso(act2)
persona3.comprobarPermiso(act3)
persona4.comprobarPermiso(act4)
persona5.comprobarPermiso(act5)
persona6.comprobarPermiso(act6)

