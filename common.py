from PIL import Image, ImageTk
import pedidos as P
import ventana_principal as VP
import usuarios as U
import stock as S
import json

def GetUsers():
    f = open("usuarios/usuarios.json")
    usersjson = json.load(f)
    return usersjson

este_usuario = None

def EsSecretario():
    global este_usuario
    if este_usuario["rol"] == 2:
        return True
    else:
        return False
    
def EsDirectivo():
    global este_usuario
    if este_usuario["rol"] == 1:
        return True
    else:
        return False
    
def EsAdministrativo():
    global este_usuario
    if este_usuario["rol"] == 0:
        return True
    else:
        return False
    
def EsDeContabilidad():
    global este_usuario
    if este_usuario["area"] == 0:
        return True
    else:
        return False
    
def EsDeCompras():
    global este_usuario
    if este_usuario["area"] == 1:
        return True
    else:
        return False

def get_image(path, maxsize) -> ImageTk.PhotoImage:
    img = Image.open(path)
    img.thumbnail(maxsize)
    return ImageTk.PhotoImage(img)

def VentanaPrincipal():
    VP.VentanaPrincipal()

def NuevoPedido():
    P.CrearPedido()

def VerUsuarios():
    U.VerUsuarios()

def VerProductos():
    S.VerProductos()

def DevolverProductos():
    S.DevolverProductos()
