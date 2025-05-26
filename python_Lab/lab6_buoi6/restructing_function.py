"""
Restructuring the company data:
 Suppose you have a dictionary that contains information about employees at a company. Each employee is identified by an ID number, and their information
 includes their name, department, and salary. You want to create a nested dictionary that groups employees by department so that you can easily see the
 names and salaries of all employees in each department.

 Write a Python program that when given a dictionary, employees, outputs a nested dictionary, dept_employees, which groups employees by department.
"""

def ex(employees):
    dept_employees = {}
    for emp_id, emp_info in employees.items():
        dept = emp_info['department']
        if dept not in dept_employees:
            dept_employees[dept] = {}
        dept_employees[dept][emp_id] = {
            'name': emp_info['name'],
            'salary': emp_info['salary']
        }
    return dept_employees

if __name__ == '__main__':
    employees = {
        101: {'name': 'John', 'department': 'Sales', 'salary': 50000},
        102: {'name': 'Jane', 'department': 'IT', 'salary': 60000},
        103: {'name': 'Bob', 'department': 'Sales', 'salary': 55000},
    }
    result = ex(employees)
    print(result)