import PySimpleGUI as pg
layout = [[pg.Text("this is test ap copy.")]]
win = pg.Window("test ap copy", layout)
while True:
    e, v = win.read()
    if e == None: break
win.close()