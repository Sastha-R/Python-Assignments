from repository.repository import Repository
from schemas.schemas import InvoiceData

class Services:

    def __init__(self):
        self.repository = Repository()

    def create_invoice(self, invoice):

        subtotal = invoice.quantity * invoice.unit_price
        if subtotal < 10000:
            discount_percentage = 5
        elif subtotal <= 50000:
            discount_percentage = 10
        else:
            discount_percentage = 15

        discount_amount = subtotal * discount_percentage / 100

        taxable_amount = subtotal - discount_amount

        tax_percentage = 18

        tax_amount = taxable_amount * tax_percentage / 100

        total_amount = taxable_amount + tax_amount
        
        invoice_data = InvoiceData(
            invoice_number=invoice.invoice_number,
            customer_email=invoice.customer_email,
            invoice_date=invoice.invoice_date,
            customer_name=invoice.customer_name,
            product_name=invoice.product_name,
            quantity=invoice.quantity,
            unit_price=invoice.unit_price,
            discount_percentage=discount_percentage,
            discount_amount=discount_amount,
            tax_percentage=tax_percentage,
            tax_amount=tax_amount,
            subtotal=subtotal,
            taxable_amount=taxable_amount,
            total_amount=total_amount
        )

        return self.repository.create(
            invoice_data
        )