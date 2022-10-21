from classes.customer import Customer


customer1 = Customer('John',25,'Male','private customer')
customer2 = Customer('Sara',46,'female','bussiness customer')
customer3 = Customer('Anna',15,'female','private customer')
customer4 = Customer('Seb','Eight','Male','bussiness client')

print(f'My name is {customer1.name} and I am {customer1.age} I am {customer1.sex} and my type is {customer1.type} Are you an adult? {customer1.IsOver18()}')
print(f'My name is {customer2.name} and I am {customer2.age} I am {customer2.sex} and my type is {customer2.type} Are you and adult? {customer2.IsOver18()} {customer2.IsImportantClient()}')
print(f'My name is {customer3.name} and I am {customer3.age} I am {customer3.sex} and my type is {customer3.type} Are you an adult? {customer3.IsOver18()}')
print(customer4.name,customer4.IsOver18())


print(customer1.IsMale())
print(customer3.IsOver18())
customer1.ReviewOfService()




