from Ingreso import Ingreso
from RepositorioPersona import RepositorioPersona
ListIngresos = []

class RepositorioIngreso:
    def GuardarIngreso(ingre):
        ListIngresos.append(ingre)

    def ObtenerIngresoPer(dni):
         for i in ListIngresos:
            if Ingreso.get_persona(i) == RepositorioPersona.ObtenerPer(dni):
                 return i
            
                
    def MostrarIngresos():
        for j in ListIngresos:
            print(j)
    
    def AsignarEstado(ingreso, dni):
        if RepositorioPersona.ComprobarAutorizados(dni) == True:
            if ingreso.get_temperatura() < '37':
                ingreso.set_estado('Ingreso Permitido.')
            else:
                ingreso.set_estado('Ingreso no permitido.')