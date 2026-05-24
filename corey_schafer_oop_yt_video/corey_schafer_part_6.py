
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@example.com' #digantikan dengan method email di bawah, karena kita ingin email selalu update sesuai dengan nama depan dan belakang yang diubah

    @property  # decorator untuk membuat method menjadi property, sehingga bisa dipanggil seperti atribut biasa (tanpa tanda kurung)
    def email(self):
        return '{}.{}@example.com'.format(self.first, self.last)
        
    @property # sama seperti di atas, tapi untuk fullname
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter  # setter untuk fullname, sehingga kita bisa mengubah nama depan dan belakang sekaligus dengan mengubah fullname
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter  # deleter untuk fullname, sehingga kita bisa menghapus nama depan dan belakang sekaligus dengan menghapus fullname
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Corey', 'Schafer')

# emp_1.first = 'John'  # mengubah nama depan dari Corey menjadi John

emp_1.fullname = 'John Doe'  # mengubah nama depan dan belakang sekaligus dengan mengubah fullname

print(emp_1.first)  # Corey
print(emp_1.email)  # corey.schafer@example.com
print(emp_1.fullname)  # Corey Schafer

del emp_1.fullname  # menghapus nama depan dan belakang sekaligus dengan menghapus fullname

print(emp_1.fullname)  # None None