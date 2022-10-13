from DataClass_Customer import CustomerDC

client1 = CustomerDC('John',25,'Male','private customer')
client2 = CustomerDC('Sara',46,'female','bussiness customer')
client3 = CustomerDC('Anna',15,'female','private customer')
client4 = CustomerDC('Seb','Eight','Male','bussiness client')

print(f'My name is {client1.name} and I am {client1.age} I am {client1.sex} and my type is {client1.type} Are you an adult? {client1.IsOver18()}')
print(f'My name is {client2.name} and I am {client2.age} I am {client2.sex} and my type is {client2.type} Are you and adult? {client2.IsOver18()} {client2.IsImportantClient()}')
print(f'My name is {client3.name} and I am {client3.age} I am {client3.sex} and my type is {client3.type} Are you an adult? {client3.IsOver18()}')
print(client4.name,client4.IsOver18())

client1.ReviewOfService()




