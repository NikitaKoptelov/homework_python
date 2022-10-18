from ast import Global
import os



def console_vive(dannie_t, vid, nach_spiska, kon_spiska):
    os.system('cls' if os.name == 'nt' else 'clear')
    if(vid==0):
        print('-'*120)
        print('|'+' '*3+'ID'+' '*3+'|'+' '*10+'Фамилия'+' '*10+'|'+' '*10+'Имя'+' '*10+'|'+' '*10+'Отчество'+' '*10+'|'+' '*10+'Телефон'+' '*10+'|')
        print('-'*120)
        for i in range(nach_spiska, kon_spiska):
            n = i
            if(i<len(dannie_t)):
                print ('|'+' '*2, i, ' '*3+'|'+' '*6, dannie_t[n]['фамилия'], 
                        ' '*9+'|'+' '*9, dannie_t[n]['имя'], 
                        ' '*9+'|'+' '*9, dannie_t[n]['отчество'], 
                        ' '*9+'|'+' '*9, dannie_t[n]['телефон'], ' '*9+'|')
                print('-'*120)
                n+=1
            elif(i>=len(dannie_t)):
                print ('|'+' '*2, i, ' '*3+'|'+' '*9, ' ', ' '*9+'|'+' '*9, ' ', ' '*9+'|'+' '*9, ' ', ' '*9+'|'+' '*9, ' ', ' '*9+'|')
                print('-'*120)
    elif(vid==1):
        print('-'*70)
        print('|'+' '*3+'ID'+' '*3+'|'+' '*10+'Фамилия И О'+' '*10+'|'+' '*10+'Телефон'+' '*10+'|')
        print('-'*70)
        for i in range(nach_spiska, kon_spiska):
            n = i
            if(i<len(dannie_t)):
                print ('|'+' '*2, i, ' '*3+'|'+' '*6, dannie_t[n]['фамилия'], 
                            (dannie_t[n]['имя']).strip()[0], 
                            (dannie_t[n]['отчество']).strip()[0], 
                            ' '*9+'|'+' '*9, dannie_t[n]['телефон'], ' '*9+'|')
                print('-'*70)
                n+=1
            elif(i>=len(dannie_t)):
                print ('|'+' '*2, i, ' '*3+'|'+' '*15, ' ', ' '*15+'|'+' '*13, ' ', ' '*13+'|')
                print('-'*70)
    print('всего записаных строк - ', len(dannie_t))

def consol_comand_user():
    consol_comanda = input('введите команду - ')
    return consol_comanda

def dobav_zapis_book():
    dobav_zapis = int(input('введите номер ID для создания записи - '))
    return dobav_zapis

def zapis_tel_book():
    zapis_tel = input('введите ФИО и № телефона через пробел - ')
    return zapis_tel