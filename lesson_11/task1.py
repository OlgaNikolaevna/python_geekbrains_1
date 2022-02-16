#
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import datetime as DT

class DataClass:
    date_val = None
    def __init__(self, data_str):
        self.date_val = DT.datetime.strptime(data_str, '%d-%m-%Y').date()
        #print(self.date_val)

    def getdate(self):
        return self.date_val

    @classmethod
    def get_date_month_year(cls, date):
        return date.day, date.month, date.year

   # @staticmethod
    def checkdate(self):
        day, month, year = self.get_date_month_year(self.date_val)
        if day>=5 and day<=10 and month>=1 and month<=6:
            return "ок"
        else:
            return "не ок"


thdate = DataClass('05-3-2202')
print(thdate.get_date_month_year(thdate.getdate()))
print(thdate.checkdate())