class ExtractProducts:
    """Extracts values from data frame 'products'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame products to every method."""
        self.row = row
        
    def get_product_id(self):
        """Takes in one row with product_id from df products and returns it."""
        return(self.row.productID)
    
    def get_product_name(self):
        """Takes in one row with product_name from df products and returns it."""
        return(self.row.productName)
    
    def get_supplier_id(self):
        """Takes in one row with supplier_id from df products and returns it."""
        return(self.row.supplierID)
    
    def get_category_id(self):
        """Takes in one row with category_id from df products and returns it."""
        return(self.row.categoryID)
    
    def get_quantityPerUnit(self):
        """Takes in one row with quantityPerUnit from df products and returns it."""
        return(self.row.quantityPerUnit)
    
    def get_unit_price(self):
        """Takes in one row with unit_price from df products and returns it."""
        return(self.row.unitPrice)
    
    def get_units_in_stock(self):
        """Takes in one row with units_in_stock from df products and returns it."""
        return(self.row.unitsInStock)
    
    def get_units_on_order(self):
        """Takes in one row with units_on_order from df products and returns it."""
        return(self.row.unitsOnOrder)
    
    def get_reorder_level(self):
        """Takes in one row with reorder_level from df products and returns it."""
        return(self.row.reorderLevel)
    
    def get_discontinued(self):
        """Takes in one row with discontinued from df products and returns it."""
        return(self.row.discontinued)
    