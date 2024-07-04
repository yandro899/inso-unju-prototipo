def GetUserMenuBar() -> list: 
    import common as C
    return [
        ["Inicio", ["Menu Principal", "Cerrar sesión", "Salir"]], 
        ["Pedidos de adquisición", ["Crear nuevo pedido", "Revisar pedidos"]], 
        ["Usuarios", ["Ver usuarios"]],
        [C.este_usuario["name"], ["DNI {}".format(C.este_usuario["dni"])]]
        ]

def GetEstadoStr(cod):
    import json

    f = open("defs/estados.json")
    estados = json.load(f)

    return estados[cod]