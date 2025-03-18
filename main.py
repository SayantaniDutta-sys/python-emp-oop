# Main file

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 10:48:31 2025

@author: 91912
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name, department):
        self._employee_id = employee_id
        self._name = name
        self._department = department
    
    @abstractmethod
    def calculate_salary(self):
        pass
    
    def display_details(self):
        print("--- Employee Details ---")
        print(f"Employee ID: {self._employee_id}")
        print(f"Name: {self._name}")
        print(f"Department: {self._department}")

class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, department, basic_salary, bonus):
        super().__init__(employee_id, name, department)
        self.__basic_salary = basic_salary
        self.__bonus = bonus
    
    def calculate_salary(self):
        return self.__basic_salary + self.__bonus
    
    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self.__basic_salary:.2f}")
        print(f"Bonus: ${self.__bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class ContractEmployee(Employee):
    def __init__(self, employee_id, name, department, hourly_rate, hours_worked):
        super().__init__(employee_id, name, department)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked
    
    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self.__hourly_rate:.2f}")
        print(f"Hours Worked: {self.__hours_worked}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class Intern(Employee):
    def __init__(self, employee_id, name, department, stipend):
        super().__init__(employee_id, name, department)
        self.__stipend = stipend
    
    def calculate_salary(self):
        return self.__stipend
    
    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self.__stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

e1 = PermanentEmployee("P123", "Priya Sharma", "IT", 60000, 5000)
e2 = ContractEmployee("C456", "Raj Verma", "HR", 50, 160)
e3 = Intern("I789", "Ananya Iyer", "Finance", 1500)

e1.display_details()
e2.display_details()
e3.display_details()
