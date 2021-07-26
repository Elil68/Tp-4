
class Persona:
    def  __init__(self, dni, nombreApellido, domicilio, telefono, email, FechaIn = None, FechaFin = None, empresa = None, codigoQr = None):
      self.__dni = dni
      self.__nombreApellido = nombreApellido
      self.__domicilio = domicilio
      self.__telefono = telefono
      self.__email = email
      self.__FechaIn = FechaIn
      self.__FechaFin = FechaFin
      self.__empresa = empresa
      self.__codigoQr = codigoQr
      
    

    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni = dni

    def get_nombreApellido(self):
        return self.__nombreApellido
    def set_nombreApellido(self, nombreApellido):
        self.__nombreApellido = nombreApellido
  
    def get_domicilio(self):
        return self.__domicilio
    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio

    def get_telefono(self):
        return self.__telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_FechaIn(self):
        return self.__FechaIn
    def set_FechaIn(self, FechaIn):
        self.__FechaIn = FechaIn

    def get_FechaFin(self):
        return self.__FechaFin
    def set_FechaFin(self, FechaFin):
        self.__FechaFin = FechaFin

    def get_empresa(self):
        return self.__empresa
    def set_empresa(self, empresa):
        self.__empresa = empresa

    def get_codigoQr(self):
        return self.__codigoQr
    def set_codigoQr(self, codigoQr):
        self.__codigoQr = codigoQr

    def __str__(self):
        return f"{self.__dni}, {self.__nombreApellido}, {self.__domicilio}, {self.__telefono}, {self.__email}, {self.__FechaIn}, {self.__FechaFin}, {self.__empresa}, {self.__codigoQr}"
        