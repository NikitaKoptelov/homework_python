import json
import vive


consol_comanda = ''
dannue_tel_book = ''
id_zapisi = 0
slovar_zapisi = {}
vid_otobragen = 0
n_nach_cpiska = 0
n_konc_spiska = 0

def init(comanda):
    global consol_comanda
    global dannue_tel_book
    global id_zapisi
    global slovar_zapisi
    global vid_otobragen
    global n_nach_cpiska
    global n_konc_spiska
    consol_comanda = comanda
    if(consol_comanda=='пуск'):
        dannue_tel_book = read_fail()
        n_konc_spiska = len(dannue_tel_book)
        consol_comanda = ''
    elif(consol_comanda.split()[0] =='строк'):
        n_nach_cpiska=0
        n_konc_spiska = int(consol_comanda.split()[1])
        consol_comanda = ''
    elif((consol_comanda.split()[0]+' '+consol_comanda.split()[1])=='показать строку'):
        n_nach_cpiska=(int(consol_comanda.split()[2]))
        n_konc_spiska=(int(consol_comanda.split()[2]))+1
        consol_comanda = ''
    elif((consol_comanda.split()[0]+' '+consol_comanda.split()[1])=='показать строки'):
        n_nach_cpiska=(int(consol_comanda.split()[2]))
        n_konc_spiska=(int(consol_comanda.split()[3]))+1
        consol_comanda = ''
    elif(consol_comanda=='показать все строки'):
        n_nach_cpiska=0
        n_konc_spiska=len(dannue_tel_book)
        consol_comanda = ''
    elif(consol_comanda=='обновить'):
        dannue_tel_book = read_fail()
        consol_comanda = ''
    elif(consol_comanda=='сохранить'):
        wread_fail()
        consol_comanda = ''
    elif(consol_comanda=='добавить запись'):
        id_zapisi = vive.dobav_zapis_book()
        vvedenna_zapis=vive.zapis_tel_book()
        if(0<=id_zapisi<=len(dannue_tel_book)):
            slovar_zapisi = {'фамилия': vvedenna_zapis.split()[0] , 
                            'имя': vvedenna_zapis.split()[1], 
                            'отчество': vvedenna_zapis.split()[2], 
                            'телефон': vvedenna_zapis.split()[3]}
            dannue_tel_book.insert(id_zapisi, slovar_zapisi)
        if(id_zapisi>len(dannue_tel_book)):
            slovar_zapisi = {'фамилия': vvedenna_zapis.split()[0] , 
                            'имя': vvedenna_zapis.split()[1], 
                            'отчество': vvedenna_zapis.split()[2], 
                            'телефон': vvedenna_zapis.split()[3]}
            dannue_tel_book.append(slovar_zapisi)
        consol_comanda = ''
    elif(consol_comanda=='упращенный вид'):
        vid_otobragen = 1
        consol_comanda = ''
    elif(consol_comanda=='полный вид'):
        vid_otobragen = 0
        consol_comanda = ''
    elif((consol_comanda.split()[0]+' '+consol_comanda.split()[1])=='удалить запись'):
        del_index = int(consol_comanda.split()[2])
        if(del_index<=len(dannue_tel_book)):
            dannue_tel_book.pop(del_index)
        consol_comanda = ''

def read_fail():
    baza_dannix = ''
    with open("/media/nik/Disk_2/lesson_Python/homework_python/homework_007/data.json", "r") as read_file: 
        baza_dannix = json.load(read_file)
    return baza_dannix

def wread_fail():
    baza_dannix = ''
    with open("/media/nik/Disk_2/lesson_Python/homework_python/homework_007/data.json", "w") as write_file:
        json.dump(dannue_tel_book, write_file)
    return baza_dannix
