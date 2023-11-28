import PySimpleGUI as sg
import io
import os


scriptPath = os.path.dirname(__file__)
currentSize = 11
currentFont = "Arial"
firstSave = 1
filename = scriptPath

def about():
    sg.popup("About this application, Version 1.01 TREMETA, UXIRIS-TEXT-EDITOR COPYRIGHT 2023", title="MADE BY TREMICK")

def save(data):
    if filename != '':
        with io.open(filename , "w", encoding = "utf-8") as f:
            f.write(data)

def saveas(data):
    global filename
    filename = sg.tk.filedialog.asksaveasfilename(
        defaultextension = 'txt', filetypes = (("ALL TXT FILES,", "*.txt"), ("All Files", "*.*")), initialdir= scriptPath, title = "Save as")
    if filename != '':
        with io.open(filename, "w", encoding = "utf-8") as f:
             f.write(data)

def openFile():
    fileOpen = sg.popup_get_file('file to open', no_window= True)
    if fileOpen != '':
        with open(fileopen, "rt", encoding = "utf-8") as f:
            text = f.read()
        window['_text_'].update(value = text)
        window.TKroot.title(fileOpen)


menu = [["File", ["Open", "Save", "Save as", "Close"]],
       ["Edit", ["Font",["Arial", "Courier","Cooper", "Elephant"], "Size", ["8", "11", "15", "18", "20"] ]],
       ["About", ["Version"]]
]

layout = [
    [sg.Menu(menu)],
    [sg.Multiline( size = (600,400), font= ("Arial", 11), key= "_text_")]
]

window = sg.Window("XIRIS-Text-Editor", layout, resizable = True, size =(600,400), icon='favicon.ico' )

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break

    if event == "Courier":
        currentFont = "Courier"
        window['_text_'].update(font = ("Courier", currentSize))

    
   
    if event == "Arial":
        currentFont == "Arial"
        window['_text_'].update(font = ("Arial", currentSize))

    if event == "8":
        currentSize = "8"
        window['_text_'].update(font = (currentFont, "8"))

    if event == "11":
        currentSize = "11"
        window['_text_'].update(font = (currentFont, "11"))

    if event == "15":
        currentSize = "15"
        window['_text_'].update(font = (currentFont, "15"))

    if event == "18":
        currentSize = "18"
        window['_text_'].update(font = (currentFont, "18"))

    if event == "20":
        currentSize = "20"
        window['_text_'].update(font = (currentFont, "20"))

    if event == "Version":
        about()
    
    if event == "Save":
        if firstSave == 0:
            save(value['_text_'])
        else:
            saveas(value['_text_'])
            fisrtSave = 0


    if event == "Save as":
        saveas(value['_text_'])

    if event == 'Open':
        openFile()




    
window.close()
