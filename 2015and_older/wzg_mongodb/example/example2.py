import sys
sys.path.insert(0, 'C:\\Users\\Administrator\\Desktop\\myCoding')

from wzg_mongodb import EasyModel, EmbeddedModel

if __name__ == '__main__':
    class Employee(EmbeddedModel):
        db='test'
        collection='company.staff'
        fields = ['name', 'salary', 'other_info']
    
        @classmethod
        def _init_instance(cls, pk):
            employee = cls()
            employee.pk = pk
            employee.name = ''
            employee.salary = 0
            employee.other_info = {
                'phone_number': '',
                'address': '',
            }

            return employee
    
        def raise_salary(self, amount):
            self.salary += amount
            self.save()


    class Company(EasyModel):
        db='test'
        collection='company'
        fields = ['pk', 'name', 'staff']

        @classmethod
        def _init_instance(cls, pk):
            company = cls()
            company.pk = pk
            company.name = ''
            company.staff = [
                {
                    'eid': 1,
                    'name': 'jimi',
                    'salary': 500,
                    'other_info': {
                        'phone_number': '',
                        'address': '',
                    }
                }
            ]
            company.save()
            return company

        def add_employee(self, employee):
            '''2 实现增加employee(内嵌文档的查)

            '''
            self.staff.append(employee)
            self.save()

        
        def get_employee(self, employee_name):
            '''1 先实现得到一个employee(内嵌文档的查)
            先用指定name来做
            '''
            pass


    #employee1 = Employee.get(10)
    company = Company.get(11)
    company.get_employee('jimi')
    print(company.staff)
    #company.add_employee(employee1) # 然后company的文档中多了一个employee的pk

