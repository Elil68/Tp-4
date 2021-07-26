from Persona import Persona


class Ingreso:
    def __init__(self, fechaIn, temperatura, lugarDestino, persona = None, patente = None, estado = None, fechaEg = None):
        self.__fechaIn = fechaIn
        self.__fechaEg = fechaEg
        self.__temeperatura = temperatura
        self.__patente = patente
        self.__lugarDestino = lugarDestino
        self.__estado = estado
        self.__persona = persona

    def get_fechaIn(self):
        return self.__fechaIn
    def set_fechaIn (self, fechaIn):
        self.__fechaIn = fechaIn

    def get_fechaEg(self):
        return self.__fechaEg
    def set_fechaEg(self, fechaEg):
        self.__fechaEg = fechaEg
    
    def get_temperatura(self):
        return self.__temeperatura
    def set_temperatura(self, temperatura):
        self.__temeperatura = temperatura

    def get_patente(self):
        return self.__patente
    def set_patente(self, patente):
        self.__patente = patente
    
    def get_lugarDestino(self):
        return self.__lugarDestino
    def set_lugarDirige(self, lugarDestino):
        self.__lugarDestino = lugarDestino

    def get_estado(self):
        return self.__estado
    def set_estado(self, estado):
        self.__estado = estado

    def get_persona(self):
        return self.__persona
    def set_persona(self, persona):
        self.__persona = persona

    def __str__(self):
        return f"{self.__fechaIn}, {self.__fechaEg}, {self.__temeperatura}, {self.__patente}, {self.__lugarDestino}, {self.__estado}, {self.__persona}"

    
