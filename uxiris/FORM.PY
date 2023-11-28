import PySimpleGUI as sg

dropDown = ["USA", "Germany", "Nigeria", "Brazil"]

menu =[["sss", ["aaiaia", "aiaiaia","shvhwj"]], ["ggg", ["sksksk", "isisis"]], ["gggg", ["jusss","uuaaia"]], ["ltp", ["ususus", "usisis", "isisis"]], ["kske", ["jdsjjs", "siisis", "jsjsjs"]], ["hrhrh"], ["ururu"]]

layout = [ 
    [sg.Menu(menu, size = (30,4)) ],
    [sg.Text("My First Gui App")],
    [sg.InputText()],
    [sg.Combo(dropDown, readonly = True, key = "_dropDown", default_value = dropDown[0])],
    [sg.Button("Done", key = "_done"), sg.Button("Enter", key = "_enter")],
    [sg.Listbox(dropDown, size = (20,5))],
    [sg.Multiline(size = (100,20), key = "_editor")]
]

window = sg.Window("GUI", layout, resizable = True,  size = (800, 600), icon= 'favicon.ico')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
      break

    if event == "_enter":
      print(values)

window.close()