from fastapi import FastAPI , HTTPException
from routes.route import invoice_route


from schemas.schemas import InvoiceCreate
from database.database import get_connection

app = FastAPI()
app.include_router(router = invoice_route)

# @app.get("/")
# def home():
#     return{"message" : "InvoiceAPI is working"}




# @app.get("/invoices")
# def get_invoices():
#     connection = get_connection()
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM invoices")

#     result = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return result

