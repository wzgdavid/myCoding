import sys
sys.path.insert(0, 'C:\\Users\\Administrator\\Desktop\\myCoding')

from wzg_mongodb import EasyModel

if __name__ == '__main__':

    class Person(EasyModel):
        db='test'
        collection='person'
        fields = ['pk', 'name', 'age', 'other_info']
    
        @classmethod
        def _init_instance(cls, pk):
            person = cls()
            person.pk = pk
            person.name = ''
            person.age = 0
            person.other_info = {
                'phone_number': '',
                'address': '',
            }
            person.save()
            return person
    
        def grow_up(self):
            self.age += 1
            self.save()
    
        def change_name(self, name):
            self.name = name
            self.save()

    m = Person.get(2)
    print(m.name, m.age)
    m.grow_up()
    m.change_name('yy')