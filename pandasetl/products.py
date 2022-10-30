class Products:
    def __init__(self,row):
        self.row = row
        
    def get_product_id(self):
        return(self.row.productID)
    
    def get_product_name(self):
        return(self.row.productName)
    
    def get_supplier_id(self):
        return(self.row.supplierID)
    
    def get_category_id(self):
        return(self.row.categoryID)
    
    def get_quantityPerUnit(self):
        return(self.row.quantityPerUnit)
    
    def get_unit_price(self):
        return(self.row.unitPrice)
    
    def get_units_in_stock(self):
        return(self.row.unitsInStock)
    
    def get_units_on_order(self):
        return(self.row.unitsOnOrder)
    
    def get_reorder_level(self):
        return(self.row.reorderLevel)
    
    def get_discontinued(self):
        return(self.row.discontinued)
    