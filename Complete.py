

# global variables
count = 0
employees = []

# function to add employees
def Export_Employees_To_File(employees, filename):
    with open(filename, 'w')as file:
        for employee in employees:
            file.write(','.join(employee)+'\n')
        print('Employees\information exported sucessfully to', filename)


def Import_Employees_From_File(employees, filename):
   with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            employee = line.strip().split(',')
            employees.append(employee)
            print('Employees\'info imported successfully from', filename)



def Add_Employee():
    employeeName = input("\nEnter employee name: ")
    employeeSSN = input("Enter employee SSN: ")
    employeePhone = input("Enter employee Phone: ")
    employeeEmail = input("Enter employee Email: ")
    employeeSalary = input("Enter employee Salary: ")


    employee = []


    employee.append(employeeName)
    employee.append(employeeSSN)
    employee.append(employeePhone)
    employee.append(employeeEmail)
    employee.append(employeeSalary)


    return employee


def View_All_Employees(employees):
    for employee in employees:
        print('--------------', employee[0], '------------')
        print('SSN:', employee[1])
        print('Phone:', employee[2])
        print('Email:', employee[3])
        print('Salary: $' + employee[4])
        print('-------------------------------------------')


def Search_Employee_By_SSN(SSN):
    for employee in employees:
        if employee[1] == SSN:
            print('---------------', employee[0], '------------')
            print('SSN:', employee[1])
            print('Phone:', employee[2])
            print('Email:', employee[3])
            print('Salary: $' + employee[4])
            print('-------------------------------------------')

            return employee
        


def Edit_Employee_Info():
    SSN = input('\n Enter SSN to search for employee to edit: ')
    employee = Search_Employee_By_SSN(SSN)

    if employee:
        employee[0] = input('Enter employee name: ')
        employee[2] = input('Enter employee phone number: ')
        employee[3] = input('Enter employee Email: ')
        employee[4] = input('Enter employee Salary: ')






def main():
            count = 0

            while True:
                print('--------Employee Management------------\n')
                print('Enter -1 to exit')
                print('------------------------------------------')
                print('Add New employee press 1\n')
                print('View all employees press 2\n')
                print('Search employee by SSN press 3\n')
                print('Edit employee info press 4\n')
                print('Export employees\'info to text file press 5\n')
                print('Import employees\'info to text file press 6\n')
                print('---------------------------------------------')

                print('choose option nunber:', end='')
                choice = int(input())
                if choice == -1:
                    break
                elif choice == 1:
                    employee = Add_Employee()
                    employees.append(employee)
                    count += 1

                elif choice == 2:
                    View_All_Employees(employees)
                    print()

                elif choice == 3:
                    SSN = input('\nEnter employee SSN to search: ')
                    Search_Employee_By_SSN(SSN)
                    print()

                elif choice == 4: 
                 Edit_Employee_Info()
                 print()


                elif choice == 5:
                    filename = input('\nEnter name of file to export employee info to:')
                    Export_Employees_To_File(employees, filename)
                    print()

                elif choice == 6:
                    filename = input('\nEnter the name of file to import employess info from: ')
                    Import_Employees_From_File(employees, filename)
                    employeeCount = len(employees)
                    print('Number of Employees: {employeeCount}')
                print('\n next')

        # if __name__ == '__main__':
main()
input("Press Enter to exit")








































