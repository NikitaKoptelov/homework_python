import npyscreen
import datetime
import threading
from time import sleep
import rabota_s_xls
rabota_s_xls.init
rabota_s_xls.tast_zapisi


class StartovauStranica(npyscreen.ActionForm, npyscreen.FormWithMenus):                                         #  форма в нутри приложений
    def create(self):
        # self.stroka_vvoda_1 = self.add(npyscreen.TitleText, name="название ввода строки текста")
        self.date = self.add(npyscreen.TitleText, value = str(datetime.datetime.now()), editable=False, name='Дата и Время')
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
        
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class schit_tab_Филиалы(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    
    def create(self):
        # self.parentApp.dat_tamer = False
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")
        self.tablet= self.add(npyscreen.GridColTitles,)
        self.tablet.values=rabota_s_xls.schit_tab_Филиалы()
        

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
        self.rabota_s_xls.tast_zapisi = 'schit_tab_Филиалы'
        self.rabota_s_xls.wread_fail()
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class schit_tab_Товары(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")
        self.tablet= self.add(npyscreen.GridColTitles,)
        self.tablet.values=rabota_s_xls.schit_tab_Товары()

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class schit_tab_Производители_товаров(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")
        self.tablet= self.add(npyscreen.GridColTitles,)
        self.tablet.values=rabota_s_xls.schit_tab_Производители_товаров()

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class schit_tab_Поставки(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")
        self.tablet= self.add(npyscreen.GridColTitles,)
        self.tablet.values=rabota_s_xls.schit_tab_Поставки()

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class schit_tab_Покупки(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")
        self.tablet= self.add(npyscreen.GridColTitles,)
        self.tablet.values=rabota_s_xls.schit_tab_Покупки()

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class schit_tab_Клиенты(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")
        self.tablet= self.add(npyscreen.GridColTitles,)
        self.tablet.values=rabota_s_xls.schit_tab_Клиенты()

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class schit_tab_Категории(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")
        self.tablet= self.add(npyscreen.GridColTitles,)
        self.tablet.values=rabota_s_xls.schit_tab_Категории()

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class schit_tab_Изменение_цены_на_товары(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")
        self.tablet= self.add(npyscreen.GridColTitles,)
        self.tablet.values=rabota_s_xls.schit_tab_Изменение_цены_на_товары()

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class schit_tab_Запись_в_счете(npyscreen.ActionForm, npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):
        self.menu = self.new_menu(name="новое глвное меню", shortcut='m')
        self.menu.addItem("1 Главное окно", self.press_1, "1")
        self.menu.addItem("2 Таблица - Филиалы", self.press_2, "2")
        self.menu.addItem("3 Таблица - Товары", self.press_3, "3")
        self.menu.addItem("4 Таблица - Производители товаров", self.press_4, "4")
        self.menu.addItem("5 Таблица - Поставки", self.press_5, "5")
        self.menu.addItem("6 Таблица - Покупки", self.press_6, "6")
        self.menu.addItem("7 Таблица - Клиенты", self.press_7, "7")
        self.menu.addItem("8 Таблица - Категории", self.press_8, "8")
        self.menu.addItem("9 Таблица - Изменение цены на товары", self.press_9, "9")
        self.menu.addItem("10 Таблица - Запись в счете", self.press_10, "10")
        self.menu.addItem("выход из программы", self.exit_form, "^X")
        self.tablet= self.add(npyscreen.GridColTitles,)
        self.tablet.values=rabota_s_xls.schit_tab_Запись_в_счете()

    def press_1(self):
        npyscreen.notify_confirm("выбрано Главное окно")
        self.parentApp.change_form('MAIN')
        
    def press_2(self):
        npyscreen.notify_confirm("выбрана Таблица - Филиалы")
        self.parentApp.change_form('FORMA2')
    
    def press_3(self):
        npyscreen.notify_confirm("выбрана Таблица - Товары")
        self.parentApp.change_form('FORMA3')

    def press_4(self):
        npyscreen.notify_confirm("выбрана Таблица - Производители товаров")
        self.parentApp.change_form('FORMA4')
    
    def press_5(self):
        npyscreen.notify_confirm("выбрана Таблица - Поставки")
        self.parentApp.change_form('FORMA5')

    def press_6(self):
        npyscreen.notify_confirm("выбрана Таблица - Покупки")
        self.parentApp.change_form('FORMA6')

    def press_7(self):
        npyscreen.notify_confirm("выбрана Таблица - Клиенты")
        self.parentApp.change_form('FORMA7')

    def press_8(self):
        npyscreen.notify_confirm("выбрана Таблица - Категории")
        self.parentApp.change_form('FORMA8')

    def press_9(self):
        npyscreen.notify_confirm("выбрана Таблица - Изменение цены на товары")
        self.parentApp.change_form('FORMA9')

    def press_10(self):
        npyscreen.notify_confirm("выбрана Таблица - Запись в счете")
        self.parentApp.change_form('FORMA10')

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("OK button")

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("выход из программы")
        if(exiting):
            npyscreen.notify_confirm("да, выход. НЕТ, остаться")
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("продолжим работу")

class App(npyscreen.NPSAppManaged):                                           #   приложение для запуска нескольких форм
    
    # rabota_s_xls.init
    # tast_zapisi_progi = 'f'
    rabota_s_xls.tast_zapisi
    rabota_s_xls.wread_fail()
    # dat_tamer = True

    def onStart(self):
        self.addForm('MAIN', StartovauStranica, name= "Главное окно")
        # self.textual = StartovauStranica()
        # self.registerForm("MAIN", self.textual)

        # thread_time = threading.Thread(target=self.update_time,args=())
        # if(self.dat_tamer == True):
        #     thread_time.daemon = True
        #     thread_time.start()
        

        self.addForm('FORMA2', schit_tab_Филиалы, name= "Таблица - Филиалы")
        self.addForm('FORMA3', schit_tab_Товары, name= "Таблица - Товары")
        self.addForm('FORMA4', schit_tab_Производители_товаров, name= "Таблица - Производители товаров")
        self.addForm('FORMA5', schit_tab_Поставки, name= "Таблица - Поставки")
        self.addForm('FORMA6', schit_tab_Покупки, name= "Таблица - Покупки")
        self.addForm('FORMA7', schit_tab_Клиенты, name= "Таблица - Клиенты")
        self.addForm('FORMA8', schit_tab_Категории, name= "Таблица - Категории")
        self.addForm('FORMA9', schit_tab_Изменение_цены_на_товары, name= "Таблица - Изменение цены на товары")
        self.addForm('FORMA10', schit_tab_Запись_в_счете, name= "Таблица - Запись в счете")
    def change_form(self, name):
        self.switchForm(name)
        self.resetHistory()

    def update_time(self):
        while True:
            self.textual.date.value = str(datetime.datetime.now())
            self.textual.display()
            sleep(1)

if(__name__=="__main__"):
    app=App().run()



