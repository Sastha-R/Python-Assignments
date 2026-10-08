from schemas.schemas import InvoiceCreate
from fastapi import FastAPI,APIRouter,HTTPException
from services.services import Services


services = Services()
invoice_route = APIRouter()

@invoice_route.post("/invoices")
def create_invoices(invoices : InvoiceCreate):
    return services.create_invoice(invoices)

@invoice_route.get("/invoices")
def get_invoices():
    return services.get_invoices()

@invoice_route.get("/invoices/{invoice_number}")
def get_invoice_id(invoice_number : str):
    try:
        return services.get_invoice_by_id(invoice_number)
    except ValueError as error:
        raise HTTPException(status_code=404,detail=str(error))

@invoice_route.put("/invoices/{invoice_id}")
def update_invoice(invoice_id : int,invoices : InvoiceCreate):
    try:
        return services.update_invoice(invoice_id,invoices)
    except ValueError as error:
        raise HTTPException(status_code = 404, detail=str(error))



# @invoice_route.patch("/invoices/{invoice_id}")
# def patch_invoice(invoice_id : int,invoices : InvoiceCreate):
#     try:
#         return services.patch_invoice(invoice_id,invoices)
#     except ValueError as error:
#             raise HTTPException(status_code = 404, detail=str(error))



@invoice_route.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id : int):
    try:

        return services.delete_invoice(invoice_id)
    
    except ValueError as error:
        raise HTTPException(status_code = 404, detail = str(error))


