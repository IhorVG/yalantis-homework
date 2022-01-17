#!venv/bin/python
from datetime import date
from decimal import Decimal

class Employee:
    """class Employee for calculate salary and taxes

    Note: Taxes are fix  and don't change
    """

    def __init__(self,name: str, start: date, end: date, rate: Decimal, taxes: int):
        try:
            if not (20 >= len(name) > 2) or not (99 >= taxes > 1) or not (end > start) or not(100 > rate > 10):
                raise ValueError
            self.name: str = name
            self._start: date = start
            self._end: date = end
            self._rate: Decimal = rate
            self._taxes: int = taxes
        except ValueError:
            print("Your parameters don\'t satisfy necessary the conditions. Please check the parameters!")


    def _balance(self) -> Decimal:
        """Balance of funds"""
        return  self.recalculate_balance()

    def how_long(self) -> str:
        """ The method returns the number of days the employee worked """
        days_working = (self._end - self._start).days
        return f"{self.name} works {days_working} day(s)"

    def recalculate_balance(self):
        """The method return recalculate_balance """
        return self._rate*(self._end - self._start).days

    def update_rate(self, coeficient_rate: Decimal):
        self._rate = coeficient_rate*self._rate
        self.recalculate_balance()

    @classmethod
    def show_header(cls):
        print("{} {:<27} {} {:<10} {} {:<10} {} {:<10}".format('| ', 'Name', '|',  'Balance', '|', 'Taxes Pay', '|', 'Salary'))

    @staticmethod
    def show_line():
        print("_" * 67)

    def show_row(self):
        print("{} {:<27} {} {:<10} {} {:<10} {} {:<10}".format('| ',self.how_long(), '|',self._balance(), '|', self._taxes, "|", self._balance()-self._taxes))

if __name__ == '__main__':
    t=date(2022,1,2)
    tt=date(2022,1,7)
    print(t<tt)
    A=Employee('Andriy',t,tt,Decimal(90.50),10)
    print(A.recalculate_balance())
    Employee.show_line()
    Employee.show_header()
    Employee.show_line()
    A.show_row()


