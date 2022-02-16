# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

IT = 1
EL = 2

class MyError(Exception):
    def __init__(self, text):
        self.txt = text

class Warehouse:
    def __init__(self, name):
        self.name = name
        self.eq_it = {}
        self.eq_el = {}
        #print('Склад ' + self.name)

    def add_equipment(self, eq, department, num = 1):
        try:
            if not isinstance(num, int):
                raise MyError("Количество д.б. числом. " + eq.name + " не добавлен.")
        except ValueError:
            print("Err")
        except MyError as err:
            print(err)
        else:
            num_int = int(num)
            if department == IT:
                s_eq = self.eq_it
            else:
                s_eq = self.eq_el

            if not eq in s_eq.keys():
                s_eq[eq]= 1
            else:
                curr_n = s_eq.get(eq)
                s_eq.update({eq: curr_n + num_int})
            #print('добавлен ' + eq.name + ' на склад ' + self.name)


    def show(self):
        print("СКЛАД IT:")
        for key, val in self.eq_it.items():
            print(key.name + ' - ' + str(val))
        print("СКЛАД ЭЛЕКТРИКОВ:")
        for key, val in self.eq_el.items():
            print(key.name + ' - ' + str(val))


class Equipment:
    def __init__(self, id, name, nom_number, price):
        self.id = id
        self.name = name
        self.nom_number = nom_number
        self.price = price


class Scaner(Equipment):
    def __init__(self, id, name, nom_number, price, scanning_speed):
        super().__init__(id, name, nom_number, price)
        self.scanning_speed = scanning_speed
        #print('Сканер ' + self.name)


class Printer(Equipment):
    def __init__(self,id,  name, nom_number, price, printer_type):
        super().__init__(id, name, nom_number, price)
        self.printer_type = printer_type
        #print('Принтер ' + name)


class Xerox(Equipment):
    def __init__(self,id,  name, nom_number, price, xerox_addr):
        super().__init__(id, name, nom_number, price)
        self.xerox_addr = xerox_addr
        #print('Ксерокс ' + name)


store = Warehouse("Склад#1")
new_scanner = Scaner(1,"SDJ1", "150-20", 151, 151)
new_printer = Printer(2,"TGBR", "1150-88", 800, "a")
new_xerox = Xerox(3, "HHB", "1511", 70, '150-55-55')
store.add_equipment(new_scanner, IT)
store.add_equipment(new_scanner, IT)
store.add_equipment(new_printer, EL)
store.add_equipment(new_xerox, EL)
store.add_equipment(new_xerox, EL, 2)
store.add_equipment(new_xerox, EL, "dd")
store.show()

