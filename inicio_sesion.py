import clases as pc
import FreeSimpleGUI as sg

"""
    Ventana para recuperar la clave de usuario.
    Por ahora no va a funcionar. Se va a reservar para el otro
    cuatrimestre.

    Entrega: Nada
"""
def RecuperarCuenta():
    layout = [
        [sg.T("Recuperar cuenta")],
        [sg.Text("DNI: ") ,sg.Input(key="in_userdni_rec")],
        [sg.Text("", key="tx_send_mail", text_color="#000000")],
        [sg.Button("Enviar a correo", key="btn_sendmail"), sg.Button("Volver")]
    ]

    window = sg.Window("Recuperar cuenta", layout=layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Volver':
            break

        if event == "btn_sendmail":
            window["tx_send_mail"].update("¡Correo enviado!")

    window.close()

"""
    Ventana que inicia sesion de usuario. Por ahora va a funcionar por solicitudes POST
    usando archivos json.

    Entrega: Si inicia sesion, un diccionario con los valores necesarios del usuario,
    sino None si se cierra la ventana.
"""
def VentanaInicioSesion() -> dict:
    layout = [
        [sg.T("SI.GE.AD.")],
        [sg.Text("DNI: ") ,sg.Input(key="in_userdni")],
        [sg.Text("Contraseña: ") ,sg.Input(key="in_passw", password_char="*")],
        [sg.Text("", key="tx_incorrectinp", text_color="#ff0000")],
        [sg.Text("Recuperar cuenta", key="tx_recover_acc", text_color="#0000ff", enable_events=True)],
        [sg.Button("Iniciar sesión"), sg.Button("Cerrar")]
    ]

    window = sg.Window("SIGEAD", layout=layout)
    user_info = None

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cerrar':
            break

        if event == "tx_recover_acc":
            RecuperarCuenta()
            continue

        if event == "Iniciar sesión":
            dni = values["in_userdni"]
            passw = values["in_passw"]

            usuario = pc.Usuario(dni, passw)
            usuario_json = usuario.autorizar_ingreso()

            if usuario_json:
                print("Hola {}. Tu DNI es {}.".format(usuario_json["name"], usuario_json["dni"]))
                user_info = usuario_json
                break
            else:
                print("El usuario no existe")
                window["tx_incorrectinp"].update("Usuario o contraseña incorrectos")
                continue

    window.close()
    return user_info