import PySimpleGUI as pg
pg.set_options(font=(None, 24))
layout = [
    [pg.Input(k="serch_word"), pg.Button("sarch", bind_return_key=True, k="serch")],
    [pg.Listbox(list(), k="cadidate")]
    ]
win = pg.Window("shizukani store", layout, finalize=True)
while True:
    e, v = win.read()
    if e == None: break
    print(e)
    win["candidate"].update(values=["dfsjklfsdkljdsfklsdfkldklfsdkfsdfkafkfjkrffnjkdg", "fdsjkaljieojfoeskevfm"])
win.close()