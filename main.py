import inicio_sesion as IS
import ventana_principal as VP
import common as C

C.este_usuario = IS.VentanaInicioSesion()

if C.este_usuario:
    print("se inicio sesion")
    VP.VentanaPrincipal()
else:
    print("no")