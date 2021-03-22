#Datum vydání: 12:40 CET  22.03.2021
#Verze: 1.11

import os
import subprocess

import PySimpleGUI as sg

sg.change_look_and_feel("Topanga")

layout = [[sg.Text ("Co chceš zapnout?"),],
        [sg.Text(("*********************************************************"), key = 'OUTPUT')],
        [sg.Button("Slovní hru"),sg.Button("Info"), sg.Button("Opustit")]]

window = sg.Window("Tomova appka", layout)
window1_active = False

while True:
    event, values = window.read(timeout=100)

    if event == sg.WIN_CLOSED or event == 'Opustit':
        break

    if event == "Slovní hru" :

        answer = "Slovní hra spuštěna!"

        window['OUTPUT'].update(answer)

        command = "game"

        subprocess.Popen(command)

    if not window1_active and event == 'Info':
        window1_active = True
        answer = "Pro více info kontaktuj 'tom.ferdan@seznamcz'"

        window['OUTPUT'].update(answer)




        layout1 = [[sg.Text ("Autor: Tomáš Ferdan | Datum vydání: 20:08 CET 22.03.2021 | Verze: 1.11 | Creative Commons")],
                   [sg.Button('Opustit')]]


        window1 = sg.Window("Info", layout1)



    if window1_active:
        event1, values1 = window1.read(timeout=100)

        if event1 == sg.WIN_CLOSED or event1 == 'Opustit':
            window1_active  = False
            window1.close()
            window.close()
            break
