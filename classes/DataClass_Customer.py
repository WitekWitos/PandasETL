from dataclasses import dataclass
@dataclass
class CustomerDC:
    name: str
    age: int
    sex: str
    type: str
    
def IsOver18(self):
        if isinstance(self.age,str) == True:
            return('Wrong value of your age')
        elif self.age >= 18:
            return('Yes I am over 18.')
        else:
            return('No, I am under 18.')
        
def IsImportantClient(self):
        if self.type == 'bussiness customer':
            answear = ('Let me call the manager please.')
        else:
            answear = ('So, how can I help you?')
        return answear
    
def ReviewOfService(x):
        x = input('Did you like you customer service? ')
        if x == 'yes' or x =='Yes' or x =='Tak' or x == 'YES':
            print('Thank you very much')
        elif x == 'no' or x == 'No' or x == 'NO':
            print('We are very sorry')
        else:
            print('Hm that is weird...')
def IsMale(self):
        return self.sex == 'Male'
    