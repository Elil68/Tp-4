from Actividad import Actividad
Actividades = []
class RepositorioActividad:
    def GuardardAct(act):
        Actividades.append(act)
    def MostrarAct():
        for i in Actividades:
            print(i)
            
    def ExistenciaActividad(act):
        for j in Actividades:
            if act == Actividad.get_nombreActividad(j):
                return True
            
        
   