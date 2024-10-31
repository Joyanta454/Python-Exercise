class Teacher:
    def teachers_action(self):
        print('I can teach')
class Engineer:
    def engineers_action(self):
        print('I can code')
class Youtubers:
    def youtubers_action(self):
        print('I can teach and code')
    
class Person(Teacher, Engineer, Youtubers):
    pass

coder = Person()
coder.teachers_action()
coder.engineers_action()
coder.youtubers_action()

def next_square():
    i = 1
    while True:
        yield i*i
        i += 1

for n in next_square():
    if n > 25:
        break
    print(n)