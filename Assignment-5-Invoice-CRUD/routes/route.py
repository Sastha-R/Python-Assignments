from schemas.schemas import InvoiceCreate
from fastapi import FastAPI,APIRouter
from services.services import Services


services = Services()
invoice_route = APIRouter()

@invoice_route.post("/invoices")
def create_invoices(invoices : InvoiceCreate):
    return services.create_invoice(invoices)
