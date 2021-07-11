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
    
    def AutorizarFecha():
        for j in ListPersona:
            if Persona.get_FechaFin(j) >= FechaAhora:
                return True
            
    def AutorizarPersona(per):
        if RepositorioEmpresa.ComprobarAutorizacion(Persona.get_empresa(per)) == True:
            if RepositorioPersona.AutorizarFecha() == True:
                RepositorioPersona.AgregarPerAutorizada(per)
    
    def ComprobarAutorizados(dniPer):
        for i in ListPerAutorizado:
            print("\n----------------------------------------------------------------------------------------\n")
            if dniPer == Persona.get_dni(i):
                print("La persona esta autorizada")
            else:
                print("La persona no esta autorizada")

    def DarBaja(dniPer):
        for j in ListPerAutorizado:
            print("\n----------------------------------------------------------------------------------------\n")
            if dniPer == Persona.get_dni(j):
                ListPerAutorizado.remove(j)
                print("Persona fue dada de baja con exito.")
            else:
                print("Persona no existente.")

    
