class Actividad:
    def __init__(self, nombreActividad, estado):
        self.__nombreActividad = nombreActividad
        self.__estado = estado

    def get_nombreActividad(self):
        return self.__nombreApellido
    def set_nombreActividad(self, nombreActividad):
        self.__nombreActivida = nombreActividad

    def get_estado(self):
        return self.__estado
    def set_estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return self.__nombreActivida+ "," +self.__estado
