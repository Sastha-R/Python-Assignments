from schemas.schemas import InvoiceCreate
from database.database import get_connection


class Repository:

    def create(self,invoice):
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

    def getall(self):
        connection = get_connection()

        try:

            with connection.cursor() as cursor:
                cursor.execute("""select
                    invoice_number,
                    customer_email ,
                    invoice_date,
                    customer_name,
                    product_name ,
                    quantity ,
                    unit_price,
                    discount_percentage ,
                    discount_amount ,
                    tax_percentage ,
                    tax_amount ,
                    subtotal ,
                    taxable_amount
                    total_amount
                    from invoices""")
                result = cursor.fetchall()
                return result
            
        finally:
            connection.close()


    def get_by_id(self,invoice_id : str):

        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                               select
                                invoice_number,
                                customer_email ,
                                invoice_date,
                                customer_name,
                                product_name ,
                                quantity ,
                                unit_price,
                                discount_percentage ,
                                discount_amount ,
                                tax_percentage ,
                                tax_amount ,
                                subtotal ,
                                taxable_amount
                                total_amount
                                from invoices WHERE invoice_number = %s
                                """,(invoice_id,))
                return  cursor.fetchone()   
        finally:
            connection.close()

    def update(self,invoice_id : int,invoice):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                                UPDATE invoices SET
                                invoice_number = %s,
                                customer_name = %s,
                                customer_email = %s ,
                                invoice_date = %s,
                                product_name = %s ,
                                quantity = %s ,
                                unit_price = %s,
                                discount_percentage = %s ,
                                discount_amount = %s ,
                                tax_percentage = %s ,
                                tax_amount = %s ,
                                subtotal = %s ,
                                taxable_amount = %s,
                                total_amount = %s WHERE id = %s
                                """,( invoice.invoice_number,
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
                                    invoice.total_amount,
                                    invoice_id))

                if cursor.rowcount == 0 :
                    return None
                
                connection.commit()

                return {"msg" : f"invoice : {invoice_id} updated"}
            
        finally:
            connection.close()


    def delete(self , invoice_id : int):
        connection = get_connection()
        try:

            with connection.cursor() as cursor:
                cursor.execute("""
                                DELETE FROM invoices WHERE id = %s
                                """,(invoice_id,))

                if cursor.rowcount == 0:
                    return None
                
                connection.commit()

                return {"msg" : f"deleted the row id {invoice_id}"}
            
        finally:
            connection.close()
