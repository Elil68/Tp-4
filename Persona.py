class Persona:
    def  __init__(self, dni, nombreApellido, domicilio, telefono, email, act):
      self.__dni = dni
      self.__nombreApellido = nombreApellido
      self.__domicilio = domicilio
      self.__telefono = telefono
      self.__act = act

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

    def get_act(self):
        return self.__act
    def set_act(self, act):
        self.__act = act

    def comprobarPermiso(self, actividad):
        self.actividad = actividad
        if self.actividad.get_estado() == 'autorizado':
            print('Esta autorizado')
        else:
            print('No esta autorizado')

    def __str__(self):
        return self.__dni+ "," +self.__nombreApellido+ "," +self.__domicilio+ "," +self.__telefono+ "," +self.__email+ "," +self.__act