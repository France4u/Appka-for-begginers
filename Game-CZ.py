#Datum poslední úpravy: 23.03.2021

import PySimpleGUI as sg

sg.change_look_and_feel("Topanga")

#okno - menu hry (v tomto okně se budou zobrazovat i výsledné věty)

layout1 = [( sg.Text ("Zadej množství hráčů. (Minimálně 2 a maximálně 10):"), sg. Input(key = "players")),
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT1')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT2')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT3')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT4')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT5')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT6')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT7')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT8')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT9')],
            [sg.Text(("**************************************************************************************************************************************************************************************************************"), key = 'OUTPUT10')],
            [sg. Button("Pokračovat"), sg.Button("Opustit")]]

window1 = sg.Window('Slovní hra', layout1)

window2_active = False
while True:
    event1, values1 = window1.read(timeout=100)

    if event1 == sg.WIN_CLOSED or event1 == 'Opustit':
        break

        #Otevření okna prvního hráče (Sem si zadá, kdy, kde, kdo, atd.. a počítač to v poslení fázi rozhází)
    if not window2_active and event1 == 'Pokračovat':
        window2_active = True

        i = 0 #proměnná ,,i" v programu počítá, kolikrát se okno, kam hráč může zadat větu, otevřelo

        players = int(values1["players"])
        if ((players >= 2) and (players <= 10)):
            if i < players :
                pismeno = "abcdefghijklm"[i]
                layout2 = [
                            ( sg.Text ("Zadej kdy:"), sg. Input(key = "kdy")),
                            ( sg.Text ("Zadej kde:"), sg. Input(key = "kde")),
                            ( sg.Text ("Zadej kdo:"), sg. Input(key = "kdo")),
                            ( sg.Text ("Zadej s kým:"), sg. Input(key = "s_kým")),
                            ( sg.Text ("Zadej co dělali:"), sg. Input(key = "dělali")),
                            ( sg.Text ("Zadej věc/člověka:"), sg. Input(key = "co")),
                            [sg. Button("Ok")]]

                window2 = sg.Window('Věta', layout2)
                i = i + 1
    if window2_active:
        event2, values2 = window2.read(timeout=100)
        if event2 == sg.WIN_CLOSED:
            window2_active  = False
            window2.close()


        #uložení zadaných údajů (věty)
        if event2 == "Ok" :
            kdy = values2["kdy"]
            kde = values2["kde"]
            kdo = values2["kdo"]
            s_kým = values2["s_kým"]
            dělali = values2["dělali"]
            co = values2["co"]

            if i == 1 :
                kdy_a = kdy + pismeno
                kde_a = kde + pismeno
                kdo_a = kdo + pismeno
                s_kým_a = s_kým + pismeno
                dělali_a = dělali + pismeno
                co_a = co + pismeno
            elif i == 2 :
                kdy_b = kdy + pismeno
                kde_b = kde + pismeno
                kdo_b = kdo + pismeno
                s_kým_b = s_kým + pismeno
                dělali_b = dělali + pismeno
                co_b = co + pismeno
            elif i == 3 :
                kdy_c = kdy + pismeno
                kde_c = kde + pismeno
                kdo_c = kdo + pismeno
                s_kým_c = s_kým + pismeno
                dělali_c = dělali + pismeno
                co_c = co + pismeno
            elif i == 4 :
                kdy_d = kdy + pismeno
                kde_d= kde + pismeno
                kdo_d = kdo + pismeno
                s_kým_d = s_kým + pismeno
                dělali_d = dělali + pismeno
                co_d = co + pismeno
            elif i == 5 :
                kdy_e = kdy + pismeno
                kde_e = kde + pismeno
                kdo_e = kdo + pismeno
                s_kým_e = s_kým + pismeno
                dělali_e = dělali + pismeno
                co_e = co + pismeno
            elif i == 6 :
                kdy_f = kdy + pismeno
                kde_f = kde + pismeno
                kdo_f = kdo + pismeno
                s_kým_f = s_kým + pismeno
                dělali_f = dělali + pismeno
                co_f = co + pismeno
            elif i == 7 :
                kdy_g = kdy + pismeno
                kde_g = kde + pismeno
                kdo_g = kdo + pismeno
                s_kým_g = s_kým + pismeno
                dělali_g = dělali + pismeno
                co_g = co + pismeno
            elif i == 8 :
                kdy_h = kdy + pismeno
                kde_h = kde + pismeno
                kdo_h = kdo + pismeno
                s_kým_h = s_kým + pismeno
                dělali_h = dělali + pismeno
                co_h = co + pismeno
            elif i == 9:
                kdy_i = kdy + pismeno
                kde_i = kde + pismeno
                kdo_i = kdo + pismeno
                s_kým_i = s_kým + pismeno
                dělali_i = dělali + pismeno
                co_i = co + pismeno
            elif i == 10 :
                kdy_j = kdy + pismeno
                kde_j = kde + pismeno
                kdo_j = kdo + pismeno
                s_kým_j = s_kým + pismeno
                dělali_j = dělali + pismeno
                co_j = co + pismeno

            window2_active  = False
            window2.close()

            #postupné otevírání dalších oken, dokud proměná ,,i" není rovno hráčům
            if i < players :
                window2_active = True
                pismeno = "abcdefghijklm"[i]
                layout2 = [
                            ( sg.Text ("Zadej kdy:"), sg. Input(key = "kdy")),
                            ( sg.Text ("Zadej kde:"), sg. Input(key = "kde")),
                            ( sg.Text ("Zadej kdo:"), sg. Input(key = "kdo")),
                            ( sg.Text ("Zadej s kým:"), sg. Input(key = "s_kým")),
                            ( sg.Text ("Zadej co dělali:"), sg. Input(key = "dělali")),
                            ( sg.Text ("Zadej věc/člověka:"), sg. Input(key = "co")),
                            [sg. Button("Ok")]]

                window2 = sg.Window('Věta', layout2)
                i = i + 1

            #zbytek kódu je jen systém, jakým program rozhazuje slova (Chtěl bych v budoucnu to naprogramovat tak, aby slova počítač rozhazoval zcela náhodně)
            else:
                if players == 2 :
                    vysledek1 = '{0} '.format(kdy_a[0:-1]) + '{0} '.format(kde_b[0:-1]) + '{0} '.format(kdo_a[0:-1]) + '{0} '.format(s_kým_b[0:-1]) + '{0} '.format(dělali_a[0:-1]) + '{0} '.format(co_b[0:-1])
                    vysledek2 = '{0} '.format (kdy_b[0:-1]) + '{0} '.format(kde_a[0:-1]) + '{0} '.format(kdo_b[0:-1]) + '{0} '.format(s_kým_a[0:-1]) + '{0} '.format(dělali_b[0:-1]) + '{0} '.format(co_a[0:-1])

                    window1['OUTPUT1'].update(vysledek1)
                    window1['OUTPUT2'].update(vysledek2)
                elif players == 3 :
                    vysledek1 = '{0} '.format(kdy_a[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_b[0:-1])+ '{0} '.format(s_kým_a[0:-1])+ '{0} '.format(dělali_c[0:-1])+ '{0} '.format(co_b[0:-1])
                    vysledek2 = '{0} '.format(kdy_b[0:-1]) + '{0} '.format(kde_a[0:-1])+ '{0} '.format(kdo_c[0:-1])+ '{0} '.format(s_kým_b[0:-1])+ '{0} '.format(dělali_a[0:-1])+ '{0} '.format(co_c[0:-1])
                    vysledek3 = '{0} '.format(kdy_c[0:-1]) + '{0} '.format(kde_b[0:-1])+ '{0} '.format(kdo_a[0:-1])+ '{0} '.format(s_kým_c[0:-1])+ '{0} '.format(dělali_b[0:-1])+ '{0} '.format(co_a[0:-1])

                    window1['OUTPUT1'].update(vysledek1)
                    window1['OUTPUT2'].update(vysledek2)
                    window1['OUTPUT3'].update(vysledek3)
                elif players == 4 :
                    vysledek1 = '{0} '.format(kdy_a[0:-1]) + '{0} '.format(kde_d[0:-1])+ '{0} '.format(kdo_c[0:-1])+ '{0} '.format(s_kým_b[0:-1])+ '{0} '.format(dělali_a[0:-1])+ '{0} '.format(co_a[0:-1])
                    vysledek2 = '{0} '.format(kdy_b[0:-1]) + '{0} '.format(kde_a[0:-1])+ '{0} '.format(kdo_d[0:-1])+ '{0} '.format(s_kým_c[0:-1])+ '{0} '.format(dělali_c[0:-1])+ '{0} '.format(co_d[0:-1])
                    vysledek3 = '{0} '.format(kdy_c[0:-1]) + '{0} '.format(kde_b[0:-1])+ '{0} '.format(kdo_a[0:-1])+ '{0} '.format(s_kým_d[0:-1])+ '{0} '.format(dělali_b[0:-1])+ '{0} '.format(co_b[0:-1])
                    vysledek4 = '{0} '.format(kdy_d[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_b[0:-1])+ '{0} '.format(s_kým_a[0:-1])+ '{0} '.format(dělali_d[0:-1])+ '{0} '.format(co_c[0:-1])

                    window1['OUTPUT1'].update(vysledek1)
                    window1['OUTPUT2'].update(vysledek2)
                    window1['OUTPUT3'].update(vysledek3)
                    window1['OUTPUT4'].update(vysledek4)
                elif players == 5 :
                    vysledek1 = '{0} '.format(kdy_b[0:-1]) + '{0} '.format(kde_e[0:-1])+ '{0} '.format(kdo_c[0:-1])+ '{0} '.format(s_kým_a[0:-1])+ '{0} '.format(dělali_d[0:-1])+ '{0} '.format(co_a[0:-1])
                    vysledek2 = '{0} '.format(kdy_d[0:-1]) + '{0} '.format(kde_b[0:-1])+ '{0} '.format(kdo_b[0:-1])+ '{0} '.format(s_kým_c[0:-1])+ '{0} '.format(dělali_c[0:-1])+ '{0} '.format(co_d[0:-1])
                    vysledek3 = '{0} '.format(kdy_a[0:-1]) + '{0} '.format(kde_a[0:-1])+ '{0} '.format(kdo_d[0:-1])+ '{0} '.format(s_kým_e[0:-1])+ '{0} '.format(dělali_b[0:-1])+ '{0} '.format(co_e[0:-1])
                    vysledek4 = '{0} '.format(kdy_c[0:-1]) + '{0} '.format(kde_d[0:-1])+ '{0} '.format(kdo_a[0:-1])+ '{0} '.format(s_kým_b[0:-1])+ '{0} '.format(dělali_e[0:-1])+ '{0} '.format(co_c[0:-1])
                    vysledek5 = '{0} '.format(kdy_e[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_e[0:-1])+ '{0} '.format(s_kým_d[0:-1])+ '{0} '.format(dělali_a[0:-1])+ '{0} '.format(co_b[0:-1])

                    window1['OUTPUT1'].update(vysledek1)
                    window1['OUTPUT2'].update(vysledek2)
                    window1['OUTPUT3'].update(vysledek3)
                    window1['OUTPUT4'].update(vysledek4)
                    window1['OUTPUT5'].update(vysledek5)
                elif players == 6 :
                    vysledek1 = '{0} '.format(kdy_a[0:-1]) + '{0} '.format(kde_b[0:-1])+ '{0} '.format(kdo_c[0:-1])+ '{0} '.format(s_kým_d[0:-1])+ '{0} '.format(dělali_e[0:-1])+ '{0} '.format(co_f[0:-1])
                    vysledek2 = '{0} '.format(kdy_b[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_d[0:-1])+ '{0} '.format(s_kým_e[0:-1])+ '{0} '.format(dělali_f[0:-1])+ '{0} '.format(co_a[0:-1])
                    vysledek3 = '{0} '.format(kdy_f[0:-1]) + '{0} '.format(kde_a[0:-1])+ '{0} '.format(kdo_b[0:-1])+ '{0} '.format(s_kým_c[0:-1])+ '{0} '.format(dělali_d[0:-1])+ '{0} '.format(co_e[0:-1])
                    vysledek4 = '{0} '.format(kdy_e[0:-1]) + '{0} '.format(kde_f[0:-1])+ '{0} '.format(kdo_a[0:-1])+ '{0} '.format(s_kým_b[0:-1])+ '{0} '.format(dělali_c[0:-1])+ '{0} '.format(co_d[0:-1])
                    vysledek5 = '{0} '.format(kdy_d[0:-1]) + '{0} '.format(kde_e[0:-1])+ '{0} '.format(kdo_f[0:-1])+ '{0} '.format(s_kým_a[0:-1])+ '{0} '.format(dělali_b[0:-1])+ '{0} '.format(co_c[0:-1])
                    vysledek6 = '{0} '.format(kdy_c[0:-1]) + '{0} '.format(kde_d[0:-1])+ '{0} '.format(kdo_e[0:-1])+ '{0} '.format(s_kým_f[0:-1])+ '{0} '.format(dělali_a[0:-1])+ '{0} '.format(co_b[0:-1])

                    window1['OUTPUT1'].update(vysledek1)
                    window1['OUTPUT2'].update(vysledek2)
                    window1['OUTPUT3'].update(vysledek3)
                    window1['OUTPUT4'].update(vysledek4)
                    window1['OUTPUT5'].update(vysledek5)
                    window1['OUTPUT6'].update(vysledek6)
                elif players == 7 :
                    vysledek1 = '{0} '.format(kdy_a[0:-1]) + '{0} '.format(kde_b[0:-1])+ '{0} '.format(kdo_c[0:-1])+ '{0} '.format(s_kým_d[0:-1])+ '{0} '.format(dělali_e[0:-1])+ '{0} '.format(co_f[0:-1])
                    vysledek2 = '{0} '.format(kdy_g[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_d[0:-1])+ '{0} '.format(s_kým_e[0:-1])+ '{0} '.format(dělali_f[0:-1])+ '{0} '.format(co_a[0:-1])
                    vysledek3 = '{0} '.format(kdy_f[0:-1]) + '{0} '.format(kde_a[0:-1])+ '{0} '.format(kdo_b[0:-1])+ '{0} '.format(s_kým_c[0:-1])+ '{0} '.format(dělali_d[0:-1])+ '{0} '.format(co_e[0:-1])
                    vysledek4 = '{0} '.format(kdy_e[0:-1]) + '{0} '.format(kde_f[0:-1])+ '{0} '.format(kdo_g[0:-1])+ '{0} '.format(s_kým_b[0:-1])+ '{0} '.format(dělali_g[0:-1])+ '{0} '.format(co_g[0:-1])
                    vysledek5 = '{0} '.format(kdy_d[0:-1]) + '{0} '.format(kde_e[0:-1])+ '{0} '.format(kdo_f[0:-1])+ '{0} '.format(s_kým_a[0:-1])+ '{0} '.format(dělali_b[0:-1])+ '{0} '.format(co_c[0:-1])
                    vysledek6 = '{0} '.format(kdy_c[0:-1]) + '{0} '.format(kde_d[0:-1])+ '{0} '.format(kdo_e[0:-1])+ '{0} '.format(s_kým_g[0:-1])+ '{0} '.format(dělali_a[0:-1])+ '{0} '.format(co_b[0:-1])
                    vysledek7 = '{0} '.format(kdy_b[0:-1]) + '{0} '.format(kde_g[0:-1])+ '{0} '.format(kdo_a[0:-1])+ '{0} '.format(s_kým_f[0:-1])+ '{0} '.format(dělali_c[0:-1])+ '{0} '.format(co_d[0:-1])

                    window1['OUTPUT1'].update(vysledek1)
                    window1['OUTPUT2'].update(vysledek2)
                    window1['OUTPUT3'].update(vysledek3)
                    window1['OUTPUT4'].update(vysledek4)
                    window1['OUTPUT5'].update(vysledek5)
                    window1['OUTPUT6'].update(vysledek6)
                    window1['OUTPUT7'].update(vysledek7)
                elif players == 8 :
                    vysledek1 = '{0} '.format(kdy_a[0:-1]) + '{0} '.format(kde_b[0:-1])+ '{0} '.format(kdo_c[0:-1])+ '{0} '.format(s_kým_d[0:-1])+ '{0} '.format(dělali_e[0:-1])+ '{0} '.format(co_h[0:-1])
                    vysledek2 = '{0} '.format(kdy_g[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_d[0:-1])+ '{0} '.format(s_kým_e[0:-1])+ '{0} '.format(dělali_f[0:-1])+ '{0} '.format(co_a[0:-1])
                    vysledek3 = '{0} '.format(kdy_f[0:-1]) + '{0} '.format(kde_a[0:-1])+ '{0} '.format(kdo_b[0:-1])+ '{0} '.format(s_kým_c[0:-1])+ '{0} '.format(dělali_h[0:-1])+ '{0} '.format(co_e[0:-1])
                    vysledek4 = '{0} '.format(kdy_e[0:-1]) + '{0} '.format(kde_f[0:-1])+ '{0} '.format(kdo_g[0:-1])+ '{0} '.format(s_kým_b[0:-1])+ '{0} '.format(dělali_g[0:-1])+ '{0} '.format(co_g[0:-1])
                    vysledek5 = '{0} '.format(kdy_d[0:-1]) + '{0} '.format(kde_e[0:-1])+ '{0} '.format(kdo_f[0:-1])+ '{0} '.format(s_kým_h[0:-1])+ '{0} '.format(dělali_b[0:-1])+ '{0} '.format(co_c[0:-1])
                    vysledek6 = '{0} '.format(kdy_c[0:-1]) + '{0} '.format(kde_d[0:-1])+ '{0} '.format(kdo_h[0:-1])+ '{0} '.format(s_kým_g[0:-1])+ '{0} '.format(dělali_a[0:-1])+ '{0} '.format(co_b[0:-1])
                    vysledek7 = '{0} '.format(kdy_b[0:-1]) + '{0} '.format(kde_h[0:-1])+ '{0} '.format(kdo_a[0:-1])+ '{0} '.format(s_kým_f[0:-1])+'{0} '.format (dělali_c[0:-1])+ '{0} '.format(co_d[0:-1])
                    vysledek8 = '{0} '.format(kdy_h[0:-1]) + '{0} '.format(kde_g[0:-1])+ '{0} '.format(kdo_e[0:-1])+ '{0} '.format(s_kým_a[0:-1])+ '{0} '.format(dělali_d[0:-1])+ '{0} '.format(co_f[0:-1])

                    window1['OUTPUT1'].update(vysledek1)
                    window1['OUTPUT2'].update(vysledek2)
                    window1['OUTPUT3'].update(vysledek3)
                    window1['OUTPUT4'].update(vysledek4)
                    window1['OUTPUT5'].update(vysledek5)
                    window1['OUTPUT6'].update(vysledek6)
                    window1['OUTPUT7'].update(vysledek7)
                    window1['OUTPUT8'].update(vysledek8)
                elif players == 9 :
                    vysledek1 = '{0} '.format(kdy_a[0:-1]) + '{0} '.format(kde_b[0:-1])+ '{0} '.format(kdo_c[0:-1])+ '{0} '.format(s_kým_d[0:-1])+ '{0} '.format(dělali_e[0:-1])+ '{0} '.format(co_g[0:-1])
                    vysledek2 = '{0} '.format(kdy_g[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_d[0:-1])+ '{0} '.format(s_kým_e[0:-1])+ '{0} '.format(dělali_f[0:-1])+ '{0} '.format(co_a[0:-1])
                    vysledek3 = '{0} '.format(kdy_f[0:-1]) + '{0} '.format(kde_a[0:-1])+ '{0} '.format(kdo_b[0:-1])+ '{0} '.format(s_kým_c[0:-1])+ '{0} '.format(dělali_h[0:-1])+ '{0} '.format(co_e[0:-1])
                    vysledek4 = '{0} '.format(kdy_e[0:-1]) + '{0} '.format(kde_f[0:-1])+ '{0} '.format(kdo_g[0:-1])+ '{0} '.format(s_kým_b[0:-1])+ '{0} '.format(dělali_g[0:-1])+ '{0} '.format(co_i[0:-1])
                    vysledek5 = '{0} '.format(kdy_d[0:-1]) + '{0} '.format(kde_e[0:-1])+ '{0} '.format(kdo_f[0:-1])+ '{0} '.format(s_kým_h[0:-1])+ '{0} '.format(dělali_i[0:-1])+ '{0} '.format(co_c[0:-1])
                    vysledek6 = '{0} '.format(kdy_c[0:-1]) + '{0} '.format(kde_d[0:-1])+ '{0} '.format(kdo_h[0:-1])+ '{0} '.format(s_kým_i[0:-1])+ '{0} '.format(dělali_a[0:-1])+ '{0} '.format(co_b[0:-1])
                    vysledek7 = '{0} '.format(kdy_b[0:-1]) + '{0} '.format(kde_h[0:-1])+ '{0} '.format(kdo_i[0:-1])+ '{0} '.format(s_kým_f[0:-1])+ '{0} '.format(dělali_c[0:-1])+ '{0} '.format(co_d[0:-1])
                    vysledek8 = '{0} '.format(kdy_h[0:-1]) + '{0} '.format(kde_i[0:-1])+ '{0} '.format(kdo_e[0:-1])+ '{0} '.format(s_kým_a[0:-1])+ '{0} '.format(dělali_d[0:-1])+ '{0} '.format(co_f[0:-1])
                    vysledek9 = '{0} '.format(kdy_i[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_a[0:-1])+ '{0} '.format(s_kým_g[0:-1])+ '{0} '.format(dělali_b[0:-1])+ '{0} '.format(co_h[0:-1])

                    window1['OUTPUT1'].update(vysledek1)
                    window1['OUTPUT2'].update(vysledek2)
                    window1['OUTPUT3'].update(vysledek3)
                    window1['OUTPUT4'].update(vysledek4)
                    window1['OUTPUT5'].update(vysledek5)
                    window1['OUTPUT6'].update(vysledek6)
                    window1['OUTPUT7'].update(vysledek7)
                    window1['OUTPUT8'].update(vysledek8)
                    window1['OUTPUT9'].update(vysledek9)
                elif players == 10 :
                    vysledek1 = '{0} '.format(kdy_a[0:-1]) + '{0} '.format(kde_b[0:-1])+ '{0} '.format(kdo_c[0:-1])+ '{0} '.format(s_kým_d[0:-1])+ '{0} '.format(dělali_e[0:-1])+ '{0} '.format(co_g[0:-1])
                    vysledek2 = '{0} '.format(kdy_g[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_d[0:-1])+ '{0} '.format(s_kým_e[0:-1])+ '{0} '.format(dělali_f[0:-1])+ '{0} '.format(co_a[0:-1])
                    vysledek3 = '{0} '.format(kdy_f[0:-1]) + '{0} '.format(kde_a[0:-1])+ '{0} '.format(kdo_b[0:-1])+ '{0} '.format(s_kým_c[0:-1])+ '{0} '.format(dělali_h[0:-1])+ '{0} '.format(co_j[0:-1])
                    vysledek4 = '{0} '.format(kdy_e[0:-1]) + '{0} '.format(kde_f[0:-1])+ '{0} '.format(kdo_j[0:-1])+ '{0} '.format(s_kým_b[0:-1])+ '{0} '.format(dělali_g[0:-1])+ '{0} '.format(co_i[0:-1])
                    vysledek5 = '{0} '.format(kdy_d[0:-1]) + '{0} '.format(kde_e[0:-1])+ '{0} '.format(kdo_f[0:-1])+ '{0} '.format(s_kým_g[0:-1])+ '{0} '.format(dělali_j[0:-1])+ '{0} '.format(co_c[0:-1])
                    vysledek6 = '{0} '.format(kdy_c[0:-1]) + '{0} '.format(kde_d[0:-1])+ '{0} '.format(kdo_h[0:-1])+ '{0} '.format(s_kým_i[0:-1])+ '{0} '.format(dělali_a[0:-1])+ '{0} '.format(co_b[0:-1])
                    vysledek7 = '{0} '.format(kdy_b[0:-1]) + '{0} '.format(kde_h[0:-1])+ '{0} '.format(kdo_i[0:-1])+ '{0} '.format(s_kým_f[0:-1])+ '{0} '.format(dělali_c[0:-1])+ '{0} '.format(co_d[0:-1])
                    vysledek8 = '{0} '.format(kdy_h[0:-1]) + '{0} '.format(kde_i[0:-1])+ '{0} '.format(kdo_e[0:-1])+ '{0} '.format(s_kým_a[0:-1])+ '{0} '.format(dělali_d[0:-1])+ '{0} '.format(co_f[0:-1])
                    vysledek9 = '{0} '.format(kdy_i[0:-1]) + '{0} '.format(kde_j[0:-1])+ '{0} '.format(kdo_a[0:-1])+ '{0} '.format(s_kým_c[0:-1])+ '{0} '.format(dělali_b[0:-1])+ '{0} '.format(co_h[0:-1])
                    vysledek10 = '{0} '.format(kdy_j[0:-1]) + '{0} '.format(kde_c[0:-1])+ '{0} '.format(kdo_g[0:-1])+ '{0} '.format(s_kým_h[0:-1])+ '{0} '.format(dělali_i[0:-1])+ '{0} '.format(co_e[0:-1])

                    window1['OUTPUT1'].update(vysledek1)
                    window1['OUTPUT2'].update(vysledek2)
                    window1['OUTPUT3'].update(vysledek3)
                    window1['OUTPUT4'].update(vysledek4)
                    window1['OUTPUT5'].update(vysledek5)
                    window1['OUTPUT6'].update(vysledek6)
                    window1['OUTPUT7'].update(vysledek7)
                    window1['OUTPUT8'].update(vysledek8)
                    window1['OUTPUT9'].update(vysledek9)
                    window1['OUTPUT10'].update(vysledek10)
