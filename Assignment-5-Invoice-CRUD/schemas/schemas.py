from pydantic import BaseModel
from datetime import date


class InvoiceCreate(BaseModel):
    
    invoice_number : str
    customer_name : str
    customer_email : str
    invoice_date : date
    product_name : str
    quantity : int
    unit_price :int


class InvoiceData(BaseModel):
    invoice_number : str
    customer_email : str
    invoice_date : date
    customer_name : str
    product_name : str
    quantity : int
    unit_price :int
    discount_percentage : int
    discount_amount : int
    tax_percentage : int
    tax_amount : int
    subtotal : int
    taxable_amount : int
    total_amount : int

