import PySimpleGUI as pg
import json, glob, os, subprocess

pg.set_options(font=(None, 24))
apps = []
for a in glob.glob("apps/infos/*.json"):
    with open(a, mode="r", encoding="utf-8") as f:
        apps.append(json.loads(f.read()))
print(apps, os.getcwd())
apphomepath = os.path.abspath("apps")
layout = [[pg.Button(apps[i]["appname"], k=i) for i in range(len(apps))]]
win = pg.Window("mindows", layout=layout, finalize=True)
while True:
    e, v = win.read()
    if e == None:break
    for i in range(len(apps)):
        if e == i:
            exefilepath = "apps/" + apps[i]["exepath"]
            print(exefilepath)
            #os.startfile(exefilepath)
            print("cd " + os.path.dirname(exefilepath))
            subprocess.run("cd " + os.path.dirname(exefilepath), shell=True)
            print("start " + os.path.basename(os.path.abspath(apps[i]["exepath"])))
            subprocess.run("start " + os.path.abspath(exefilepath), shell=True)
win.close()
