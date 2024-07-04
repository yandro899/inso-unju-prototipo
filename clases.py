import time
from common import GetUsers

class Seguimiento:
    
    def __init__(self, cod : str, estado : int) -> None:
        self.codigo = cod
        self.estado = estado
        self.fecha_generacion = time.time()

class PedidoAdquisicion:

    def __init__(self, cod : str) -> None:
        self.codigo = cod
        self.estado = 0
        self.fecha_generacion = time.time()
        self.concepto = ""
        
class Producto:

    def __init__(self, cod : str, nombre : str, precio : float, cantidad : int) -> None:
        self.codigo = cod
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Usuario:
    
    def __init__(self, dni : str, passw : str) -> None:
        self.dni = dni
        self.passw = passw
        self.name = ""
        self.rol = 0
        self.area = 0
        self.legajo = ""
        self.mail = ""

    def autorizar_ingreso(self) -> dict:
        
        users = GetUsers()
        for user in users:
            if user["dni"] == self.dni and user["pass"] == self.passw:
                reguser = {
                    "name" : user["name"],
                    "dni" : user["dni"],
                    "pass" : "",
                    "rol" : int(user["rol"]),
                    "area" : int(user["area"]),
                    "legajo" : user["legajo"],
                    "mail" : user["mail"]
                }

                return reguser
            
        return None

