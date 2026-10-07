from schemas.schemas import InvoiceCreate
from database.database import get_connection


class Repository:

    def create(
        self,
        invoice
    ):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:

                cursor.execute(
                    """INSERT INTO invoices(
                    invoice_number,
                    customer_name,
                    customer_email,
                    invoice_date,
                    product_name,
                    quantity,
                    unit_price,
                    discount_percentage,
                    discount_amount,
                    tax_percentage,
                    tax_amount,
                    subtotal,
                    taxable_amount,
                    total_amount
                    )
                    VALUES( %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)""",
                    (
                    invoice.invoice_number,
                    invoice.customer_name,
                    invoice.customer_email,
                    invoice.invoice_date,
                    invoice.product_name,
                    invoice.quantity,
                    invoice.unit_price,
                    invoice.discount_percentage,
                    invoice.discount_amount,
                    invoice.tax_percentage,
                    invoice.tax_amount,
                    invoice.subtotal,
                    invoice.taxable_amount,
                    invoice.total_amount)
                )
                connection.commit()

                return {"message": "Invoice inserted successfully"}

        finally:
            connection.close()