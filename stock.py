import PySimpleGUI as sg
import common as C
import defs as D

def RegistrarProducto():
    layout = [
        [sg.Text("Detalle*:"), sg.Input(key="in_detalle")],
        [sg.Text("Precio*:"), sg.Input(key="in_precio")],
        [sg.Text("Codigo*:"), sg.Input(key="in_codigo")],
        [sg.Text("Stock actual*:"), sg.Input(key="in_sactual")],
        [sg.Text("Stock minimo*:"), sg.Input(key="in_sminimo")],
        [sg.Text("Proveedor*:"), sg.Input(key="in_proveedor")],
        [sg.Button("Registrar producto"), sg.Button("Registrar proveedor"), sg.Button("Cancelar")]
    ]

    window = sg.Window("Registrar producto", layout=layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "btn_cancelar":
            break

    window.close()

def ModificarProducto(prod):
    layout = [
        [sg.Text("Detalle*:"), sg.Input(key="in_detalle", default_text=prod[0])],
        [sg.Text("Precio*:"), sg.Input(key="in_precio", default_text=str(prod[5]))],
        [sg.Text("Codigo*:"), sg.Input(key="in_codigo", disabled=True, default_text=prod[3])],
        [sg.Text("Stock actual*:"), sg.Input(key="in_sactual", default_text=str(prod[1]))],
        [sg.Text("Stock minimo*:"), sg.Input(key="in_sminimo", default_text=str(prod[2]))],
        [sg.Text("Proveedor*:"), sg.Input(key="in_proveedor", default_text=prod[4])],
        [sg.Button("Modificar producto"), sg.Button("Registrar proveedor"), sg.Button("Cancelar", k="btn_cancelar")]
    ]

    window = sg.Window("Modificar producto", layout=layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "btn_cancelar":
            break

    window.close()

def DevolverProductos():
    layout_01 = [
        [sg.Text("Datos del solicitante*:"), sg.Input(key="in_username")],
        [sg.Text("Motivo*:")],
        [sg.Multiline(key="in_motivo", s=(None, 10))],
        [sg.Text("Observaciones:")],
        [sg.Multiline(key="in_observaciones", s=(None, 10))]
    ]

    layout_02 = [
        [sg.Button("Devolver productos", key="btn_devolver")],
        [sg.Text("Lista de productos a devolver*:")],
        [sg.Input(key="in_c1", s=10), sg.Input(key="in_p1", s=40)],
        [sg.Input(key="in_c2", s=10), sg.Input(key="in_p2", s=40)],
        [sg.Input(key="in_c3", s=10), sg.Input(key="in_p3", s=40)],
        [sg.Input(key="in_c4", s=10), sg.Input(key="in_p4", s=40)],
        [sg.Input(key="in_c5", s=10), sg.Input(key="in_p5", s=40)],
    ]
    
    layout = [
        [sg.Menu([["Inicio", ["Menu Principal", "Cerrar sesión", "Salir"]], ["Pedidos de adquisición", ["Crear nuevo pedido", "Revisar pedidos"]], ["Usuarios", ["Ver usuarios"]]])],
        [sg.T("Devolucion de productos")],
        [sg.Column(layout_01, p=0, vertical_alignment="top"), sg.VerticalSeparator(), sg.Column(layout_02, p=0, vertical_alignment="top")]
    ]

    window = sg.Window("Devolucion de productos", layout=layout)

    new_window = ""

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Salir':
            break

        if event == "Menu Principal":
            
            new_window = "vp"
            break

    window.close()

    if new_window == "vp":
        C.VentanaPrincipal()

def VerProductos():
    import json

    contenido = []
    f = open("productos/productos.json")
    productos = json.load(f)

    for prod in productos:
        contenido.append(
            [prod["nombre"], prod["stock_actual"], prod["stock_minimo"], prod["cod"], prod["proveedor"], "$ {}".format(prod["precio"])]
        )
    
    layout = [
        [sg.Menu(D.GetUserMenuBar())],
        [
            sg.Button("Nuevo", key="btn_nuevopedido"), 
            sg.Button("Buscar", key="btn_buscarpedido"), 
            sg.Button("Resetear busqueda", key="btn_newbusqueda"),
            sg.Frame("Cod. Producto", [[sg.Input(key="in_busqnro", s=10)]]),
            sg.Frame("Detalle", [[sg.Input(key="in_busqnombre", s=25)]]),
            sg.Frame("Proveedor", [[sg.Input(key="in_busqest", s=10)]])
        ],
        [sg.Table(contenido, ['Detalle', 'Stock actual', 'Stock minimo', 'Código','Proveedor','Precio'], num_rows=20, key="table_productos", enable_events=True)]
    ]

    window = sg.Window("Ver productos", layout=layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Salir':
            break

        if event in ["Menu Principal"]:
            new_window = event
            break

        if event == "btn_nuevopedido":
            RegistrarProducto()

        if event == "table_productos":
            selected_row_index = values['table_productos'][0]
            cod = contenido[selected_row_index]
            ModificarProducto(cod)

    window.close()

    if new_window == "Menu Principal":
        C.VentanaPrincipal()