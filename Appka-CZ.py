#Datum poslední úpravy: 23.03.2021

import os
import subprocess

import PySimpleGUI as sg

sg.change_look_and_feel("Topanga")

#okno - menu aplikace
layout = [[sg.Text ("Co chceš zapnout?"),],
        [sg.Text(("***************************************************************"), key = 'OUTPUT')],
        [sg.Button("Slovní hru"),sg.Button("Něco mi nakresli"), sg.Button("Info"), sg.Button("Opustit")]]

window = sg.Window("Menu Appky", layout)
window1_active = False
window2_active = False
while True:
    event, values = window.read(timeout=100)

    if event == sg.WIN_CLOSED or event == 'Opustit':
        break

    #otevření slovní hry
    if event == "Slovní hru" :

        answer = "Slovní hra spuštěna!"

        window['OUTPUT'].update(answer)

        command = "Game-CZ"

        subprocess.Popen (command)

    #okno - info
    if not window1_active and event == 'Info':
        window1_active = True
        answer = "Pro více info kontaktuj autora na tom.ferdan@seznamcz"

        window['OUTPUT'].update(answer)




        layout1 = [[sg.Text ("Autor: Tomáš Ferdan | Datum vydání: 17:06 CET 23.03.2021 | Verze: 1.13 | Creative Commons")],
                   [sg.Button('Opustit')]]


        window1 = sg.Window("Info", layout1)



    if window1_active:
        event1, values1 = window1.read(timeout=100)

        if event1 == sg.WIN_CLOSED or event1 == 'Opustit':
            window1_active  = False
            window1.close()

    #okno - menu krelení
    if not window2_active and event == 'Něco mi nakresli':
        window2_active = True

        layout2 = [[sg.Text ("Co chceš nakreslit?")],
                    [sg.Text(("***************************************************"), key = 'OUTPUT2')],
                   [sg.Button('Srdce'), sg.Button("Opustit")]]


        window2 = sg.Window("Kreslení", layout2)



    if window2_active:
        event2, values2 = window2.read(timeout=100)

        if event2 == sg.WIN_CLOSED or event2 == 'Opustit':
            window2_active  = False
            window2.close()

        #otevření souboru kreslení
        if event2 == "Srdce" :

            answer2 = "Kreslení spuštěno, měj trpělivost."

            window2['OUTPUT2'].update(answer2)

            command = "Hearth-CZ"

            subprocess.Popen (command)
