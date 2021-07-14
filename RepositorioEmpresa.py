from Empresa import Empresa

ListEmpresa = [] 
ListEmpresasAutorizadas = []

class RepositorioEmpresa():
    def GuardarEmpresa(empre):
        ListEmpresa.append(empre)

    def GuardadEmpreA(empreA):
        ListEmpresasAutorizadas.append(empreA)

    def ExistenciaEmpre(empre):
        for i in ListEmpresa:
            if Empresa.get_razonSocial(i) == empre:
                return True
            else:
                return False
    def ObtenerEmpresa(empre):
        for i in ListEmpresa:
            if Empresa.get_razonSocial(i) == empre:
                return i

    def ObtnerEmpresaA(empreA):
        for i in ListEmpresasAutorizadas:
            if Empresa.get_razonSocial(i) == empreA:
                return i
    
    def ComprobarAutorizacion(empre):
        for i in ListEmpresasAutorizadas:
            if Empresa.get_razonSocial(i) == empre:
                return True
            else:
                return False
                
            