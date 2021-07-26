from Ingreso import Ingreso
from Persona import Persona
from datetime import date
from RepositorioEmpresa import RepositorioEmpresa

FechaAhora = date.today()
ListPersona = []
ListPerAutorizado = []

class RepositorioPersona:
    def GuardarPersona(per):
        ListPersona.append(per)
    def AgregarPerAutorizada(perA):
        ListPerAutorizado.append(perA)
    def MostrarPersona():
        for i in ListPersona:
            print(i)
    def MostrarPersonaA():
        for i in ListPerAutorizado:
            print(i)
    
            
    def AutorizarPersona(per, empre):
        if RepositorioEmpresa.ComprobarAutorizacion(empre) == True:
            if Persona.get_FechaFin(per) >= FechaAhora:
                RepositorioPersona.AgregarPerAutorizada(per)
            else:
                print("Fecha de ingreso vencida.")
        else:
            print("Empresa no autorizada.")
            
    
    def ComprobarAutorizados(dniPer):
        for i in ListPerAutorizado:
            if Persona.get_dni(i) == dniPer:
                return True

    def DarBaja(dniPer):
        for j in ListPerAutorizado:
            print("\n----------------------------------------------------------------------------------------\n")
            if dniPer == Persona.get_dni(j):
                ListPerAutorizado.remove(j)
                print("Persona fue dada de baja con exito.")
            else:
                print("Persona no existente.")
    
    def ObtenerPer(dni):
        for i in ListPerAutorizado:
            if Persona.get_dni(i) == dni:
                return i

    def ObtenerNom(dni):
        for i in ListPersona:
            if Persona.get_dni(i) == dni:
                return Persona.get_nombreApellido
    
    def ExistenciaPer(dni):
        for j in ListPerAutorizado:
            if Persona.get_dni(j) == dni:
                return True