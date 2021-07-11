class Actividad:
    def __init__(self, nombreActividad):
        self.__nombreActividad = str(nombreActividad)
        

    def get_nombreActividad(self):
        return self.__nombreActividad
    def set_nombreActividad(self, nombreActividad):
        self.__nombreActividad = nombreActividad

    def __str__(self):
        return f"{self.__nombreActividad}"
