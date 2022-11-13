category_features = ['categoryName', 'categoryID', 'description', 'picture']
customer_features = ['region', 'postalCode', 'country', 'phone','fax']
employee_territories_features = ['employeeID', 'territoryID']
employees_features = ['employeeID', 'listName', 'firstName', 'title', 
                      'titleOfCourtesy','birthDate', 'hireDate', 'adress', 
                      'city', 'region', 'postalCode', 'country','homePhone', 
                      'extension', 'photo', 'notes', 'reportsTo', 'photoPath']
order_details_features = ['orderID', 'productID', 'unitPrice', 'quantity', 'discount']
orders_features = ['orderID', 'customerID', 'employeeID', 'orderDate', 'requiredDate',
                   'shippedDate', 'shipVia', 'freight', 'shipName', 'shipAddress', 
                   'shipCity','shipRegion', 'shipPostalCode', 'shipCountry']
products_features = ['productID', 'productName', 'supplierID', 'categoryID', 'quantityPerUnit',
                    'unitPrice', 'unitsInStock', 'unitsOnOrder', 'reorderLevel', 'getDictontinued']
region_features = ['regionID', 'regionDescription']
shippers_features = ['shipperID', 'companyName', 'phone']
suppliers_features = ['supplierID', 'companyName', 'contactName', 'contactTitle', 'address',
                      'city', 'region', 'postalCode', 'country', 'phone', 'fax', 'homePage']
territories_features = ['territoryID', 'territoryDescription', 'regionID']
