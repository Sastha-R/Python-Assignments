from pydantic import BaseModel
from datetime import date


class InvoiceCreate(BaseModel):
    
    invoice_number : str
    customer_name : str
    customer_email : str
    invoice_date : date
    product_name : str
    quantity : int
    unit_price : float


class InvoiceData(BaseModel):
    invoice_number : str
    customer_email : str
    invoice_date : date
    customer_name : str
    product_name : str
    quantity : int
    unit_price :float
    discount_percentage : float
    discount_amount : float
    tax_percentage : float
    tax_amount : float
    subtotal : float
    taxable_amount : float
    total_amount : float


class InvoicePatch(BaseModel):
    invoice_number : str | None = None
    customer_name : str | None = None
    customer_email : str | None = None
    invoice_date : date | None = None
    product_name : str | None = None
    quantity : int | None = None
    unit_price : float | None = None

    