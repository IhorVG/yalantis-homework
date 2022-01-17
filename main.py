from decorators import timer, update_dict
from classes import Employee
from datetime import date
from decimal import Decimal

@timer
@update_dict(N=5)
def dict_const(**kwargs):
    # test function return dict constant
    return kwargs

def show_Employees(emp_list: list):
    """function call show methods from Emploee class

    """
    for empl in emp_list:
        empl.show_row()


def grow_rate(emp_list: list):
    """function increases the rate

    """
    for ind, empl in enumerate(emp_list):
        if (ind+1) % 2 == 1:
            empl.update_rate(Decimal(3.5))
        else:
            empl.update_rate(Decimal(1.5))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #test decorators
    d = {'a': 'x', 'b': 'y', 'c': 1, 'd': [1, 2, 3]}
    rezult = dict_const(**d)
    print( 'Result  act of decorators {} \n'.format(rezult))
    print('Tests for class Empoyee \n')


    Employees_list=[("Leonid",date(2020,1,1),date(2022,1,20),Decimal(95.00),15), ("Oleg", date(2021,10,1), date(2022,1,20), Decimal(90.00),10),
               ("Ihor", date(2022,1,1), date(2022,1,20), Decimal(99.00),10), ("Vlad",date(2021,7,1),date(2022,1,20), Decimal(80.00),10),
               ("Ira", date(2020,1,1), date(2022,1,20),Decimal(80.00),10), ("Viktoriia", date(2022,1,1), date(2022,1,20), Decimal(97.00),10),
               ("Maxsym", date(2021,12,1), date(2022,1,20), Decimal(90.50),10)]
    Employees_list_obj=[]
    for worker in Employees_list:
        Employees_list_obj.append(Employee(*worker))

    Employee.show_line()
    Employee.show_header()
    Employee.show_line()
    show_Employees(Employees_list_obj)
    Employee.show_line()

    print("\n After update rate the table is \n")
    grow_rate(Employees_list_obj)
    Employee.show_line()
    Employee.show_header()
    Employee.show_line()
    show_Employees(Employees_list_obj)
    Employee.show_line()








