class Customer:
    def __init__(self,name,age,sex,type,):
        self.name = name
        self.age = age
        self.sex = sex
        self.type = type
    def IsOver18(self):
        if self.age >= 18:
            print(self.name,'is an adult.')
        elif self.age <=18:
            print(self.name,'is not an adult.')
        else:
            print('We cannot verify your age.')
            
        
