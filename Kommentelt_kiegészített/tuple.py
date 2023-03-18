from collections import namedtuple

# tuple az egy olyan lista ami nem ehet megváltoztatni??

Student = namedtuple('Student', ['name', 'age', 'DOB'])
S = Student('Nandini', '19', '2541997')

print("Index is :", S[0])