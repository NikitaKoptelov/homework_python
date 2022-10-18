import tel_book
import vive

def pusk_prog():
    comanda_cs = vive.consol_comand_user()
    tel_book.init(comanda_cs)
    vive.console_vive(tel_book.dannue_tel_book, tel_book.vid_otobragen, tel_book.n_nach_cpiska, tel_book.n_konc_spiska)
    
        

