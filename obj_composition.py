class salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = salary(self.pay)

    def annual_salary(self):
        return f"Total: {self.obj_salary.get_total() + self.bonus}"


obj_emp = employee(600, 500)
print(obj_emp.annual_salary())
