
class Empresa:

    def __init__(self, razonSocial, cuit, domicilio, localidad, emailEmpresa, telefono, actividad = None):
        self.__razonSocial = razonSocial
        self.__cuit = cuit
        self.__domicilio = domicilio
        self.__localidad = localidad
        self.__emailEmpresa = emailEmpresa
        self.__telefono = telefono
        self.__actividad = actividad


    def get_razonSocial(self):
        return self.__razonSocial
    def set_razonSocial(self, razonSocial):
        self.__razonSocial = razonSocial

    def get_cuit(self):
        return self.__cuit
    def set_cuit(self, cuit):
        self.__cuit = cuit

    def get_domicilio(self):
        return self.__domicilio
    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio

    def get_localidad(self):
        return self.__localidad
    def set_localidad(self, localiadad):
        self.__localidad = localiadad

    def get_emailEmpresa(self):
        return self.__emailEmpresa
    def set_emailEmpresa(self, emailEmpresa):
        self.__emailEmpresa = emailEmpresa

    def get_telefono(self):
        return self.__telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_actividad(self):
        return self.__actividad
    def set_actividad(self, actividad):
        self.__actividad = actividad
                      

    def __str__(self):
        return f"{self.__razonSocial}, {self.__cuit}, {self.__domicilio}, {self.__localidad}, {self.__emailEmpresa}, {self.__telefono}" 
