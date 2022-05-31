#!/usr/bin/env python3

import csv


def read_employees(csv_file_location):
    with open(csv_file_location) as fh:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        reader = csv.DictReader(fh, dialect='empDialect')
        employee_list = []
        for data in reader:
            employee_list.append(data)
    return employee_list

 
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(
            department_name)
    return department_data


def write_report(dictionary, report_file):
    with open(report_file, 'w+') as fh:
        for department in sorted(dictionary):
            fh.write(str(department)+':'+str(dictionary[department])+'\n')


employee_list = read_employees(
    '/home/student-00-968c908b7b55/data/employees.csv')
dictionary = process_data(employee_list)
write_report(dictionary, '/home/student-00-968c908b7b55/test_report.txt')
