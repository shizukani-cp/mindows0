import PySimpleGUI as pg
layout = [[pg.Text("this is test app.")]]
win = pg.Window("test app", layout)
while True:
    e, v = win.read()
    if e == None: break
win.close()