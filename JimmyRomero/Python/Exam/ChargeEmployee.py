from Python.Exam.Employee_commercial import EmployeeCommercial
from Python.Exam.Employee_production import ProductionEmployee
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('Test_Log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def insert_amount_of_employees():
    while True:
        print("Insert the amount of employees: ")
        amount = input()
        try:
            amount = int(amount)
            if 2 < amount < 16:
                return amount
            print("Insert a number between 3 and 15")
        except ValueError:
            print("Insert a valid number.")


def read_name(i):
    print("Enter the {} employee name:".format(i))
    name = input()
    return name


def read_piece(i):
    while True:
        print("Insert the {} pieces:".format(i))
        amount_of_pieces = input()
        try:
            amount_of_pieces = int(amount_of_pieces)
            if amount_of_pieces >= 0:
                return amount_of_pieces
            print("Insert a number between 3 and 15")
        except ValueError:
            print("Insert a valid number.")


def read_defective_piece(i):
    while True:
        print("Insert the {} defective pieces: ".format(i))
        amount_of_defective_pieces = input()
        try:
            amount_of_defective_pieces = int(amount_of_defective_pieces)
            if amount_of_defective_pieces >= 0:
                return amount_of_defective_pieces
            print("Insert a number between 3 and 15")
        except ValueError:
            print("Insert a valid number.")


def insert_department(i):
    print("Insert the {} departament i.e.(Commercial or Production) ".format(i))
    dep = input()
    if dep == "Commercial":
        return "Commercial"
    return "Production"


list_of_employees = []


def charge_employee():
    logger.info('Start reading amount of employees')
    amount_of_employees = insert_amount_of_employees()
    for i in range(1, amount_of_employees + 1):
        employee_name = read_name(i)
        logger.debug(employee_name)
        employee_department = insert_department(i)
        logger.debug(employee_department)

        if employee_department == "Commercial":
            employee_price = read_piece(i)
            logger.debug(employee_price)
            employee = EmployeeCommercial(employee_name, employee_price, employee_department, i)
        else:
            employee_price = read_piece(i)
            logger.debug(employee_price)
            price2 = read_defective_piece(i)
            employee = ProductionEmployee(employee_name, employee_price, price2, employee_department, i)

        list_of_employees.append(employee)


def display_list():
    print(f"List of the Employee {len(list_of_employees)}")
    for i in range(0, len(list_of_employees)):
        print(list_of_employees[i].get_employee())


charge_employee()
display_list()
